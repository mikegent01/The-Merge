document.addEventListener('DOMContentLoaded', function() {
    const commandInput = document.getElementById('command-input');
    const commandOutput = document.getElementById('command-output');
    const normalOutput = document.getElementById('normal-output');
    const scpScreen = document.getElementById('scp-screen');
    const normalScreen = document.getElementById('normal-screen');
    let connectedToInternet = false;
    let specialCommandEntered = false;
    let currentDirectory = '/'; 
    let hasEnteredPassword = false;
    const maxLines = 14; 

    const fileSystem = {
        '/': {
            type: 'directory',
            contents: {
                'home': {
                    type: 'directory',
                    contents: {
                        'guestpc008': {
                            type: 'directory',
                            contents: {
                                'documents': {
                                    type: 'directory',
                                    contents: {
                                        'memo002.txt': { type: 'file', locked: true },
                                        'notes_on_anomoly312.doc': { type: 'file', locked: true },
                                        'research_notes.txt': { type: 'file', locked: false }
                                    }
                                },
                                'downloads': {
                                    type: 'directory',
                                    contents: {
                                        'iexpolorer.exe': { type: 'file', locked: true },
                                        'research008_20410012.png': { type: 'file', locked: true }
                                    }
                                },
                                'pictures': {
                                    type: 'directory',
                                    contents: {
                                        'research008_20410012.png': { type: 'file', locked: true },
                                        'project_varan.jpg': { type: 'file', locked: true }
                                    }
                                }
                            }
                        }
                    }
                },
                'Recycle Bin': {
                    type: 'directory',
                    contents: {
                        'deleted_file.txt': { type: 'file', locked: false },
                        'old_project.doc': { type: 'file', locked: false }
                    }
                },
                'etc': {
                    type: 'directory',
                    contents: {
                        'config.ini': { type: 'file', locked: true },
                        'hosts': { type: 'file', locked: false }
                    }
                },
                'var': {
                    type: 'directory',
                    contents: {
                        'log': {
                            type: 'directory',
                            contents: {
                                'system.log': { type: 'file', locked: false }
                            }
                        }
                    }
                }
            }
        }
    };

    function resolvePath(path) {
        let parts = path.split('/').filter(Boolean);
        if (!parts.length) return fileSystem['/'];

        let node = fileSystem['/'];
        for (let part of parts) {
            if (node.contents && node.contents[part]) {
                node = node.contents[part];
            } else {
                return null; 
            }
        }
        return node;
    }

    function listDirectoryContents(path) {
        const dir = resolvePath(path);
        if (dir && dir.type === 'directory') {
            return Object.keys(dir.contents).join('\n');
        } else {
            return 'Not a directory';
        }
    }

    function normalizePath(currentDir, newDir) {
        if (newDir === '/') return '/';
        const stack = currentDir.split('/').filter(Boolean);

        newDir.split('/').forEach(part => {
            if (part === '..') {
                if (stack.length > 0) stack.pop();
            } else if (part !== '.' && part !== '') {
                stack.push(part);
            }
        });

        return '/' + stack.join('/');
    }

    function processNormalCommand(command) {
        const [cmd, ...args] = command.trim().split(/\s+/);
        const address = args.join(' ');

        switch (cmd.toLowerCase()) {
            case 'help':
                return 'Available commands:\n- help: Show available commands\n- tree: Show folder structure\n- cd <path>: Change directory\n- clear: Clear the terminal\n- connect: Connect to the internet\n- ls: List directory contents\n- open <file>: Open a file \n password <password>: Enter a protected file \n(LowerCase Only)';
            case 'tree':
                return `
    .
    ├── home
    │   ├── guestpc008
    │   │   ├── documents
    │   │   ├── downloads
    │   │   └── pictures
    ├── Recycle Bin
    ├── etc
    └── var
        └── log`;
        case 'connect':
              const ipAddress = '136.228.116.222';
              if (args[0] === ipAddress) {
                connectedToInternet = true;
                normalScreen.style.display = 'none'; 
                scpScreen.style.display = 'block';  
                return `Internet connected to ${ipAddress}. SCP screen activated.`;
              } else {
                return 'Invalid or Unknown IP address.';
              }                          
        case 'cd':
                const newDir = normalizePath(currentDirectory, address);
                const dir = resolvePath(newDir);
                if (dir && dir.type === 'directory') {
                    currentDirectory = newDir;
                    return `Changed directory to ${currentDirectory}`;
                } else {
                    return 'Directory not found.';
                }
            case 'ls':
                return listDirectoryContents(currentDirectory);
            case 'open':
                const file = resolvePath(`${currentDirectory}/${address}`);
                if (file && file.type === 'file') {
                    if (address === 'research008_20410012.png') {
                        if (!hasEnteredPassword) {
                            return 'Enter password to open this file.';
                        } else {
                            return `Output saved to https://i.ibb.co/XkH8gVw/house.png...`;
                        }
                    }
                    return file.locked ? 'File is locked.' : `Opening ${address}...`;
                } else {
                    return 'File not found.';
                }
            case 'clear':
                commandOutput.textContent = ''; 
                return '';  
            case 'password':
                if (args[0] === '51856') {
                    hasEnteredPassword = true;
                    return 'Password accepted. You can now open research008_20410012.png.';
                } else {
                    return 'Incorrect password.';
                }
            default:
                return `Command not recognized: ${command}`;
        }
    }

    function handleNormalCommand(event) {
        if (event.key === 'Enter') {
            const command = commandInput.value.trim();
            if (command) {
                const result = processNormalCommand(command); 
                if (result) {
                    const lines = commandOutput.textContent.split('\n').length;
                    if (lines >= maxLines) {
                        commandOutput.textContent = '';  
                    }
                    commandOutput.textContent += `\n> ${command}\n${result}`;
                }
                commandInput.value = ''; 
            }
        }
    }

    commandInput.addEventListener('keypress', handleNormalCommand);
});
