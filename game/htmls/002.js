document.addEventListener('DOMContentLoaded', () => {
  const windows = new Set();
  let activeWindow = null;

  // Update clock
  const updateClock = () => {
    const timeElement = document.getElementById('time');
    timeElement.textContent = moment().format('HH:mm:ss');
  };

  setInterval(updateClock, 1000);
  updateClock();

  function createWindow(title, content, width = 500) {
    const windowEl = document.createElement('div');
    windowEl.className = 'window';
    windowEl.style.width = `${width}px`;

    const windowHTML = `
      <div class="title-bar">
        <div class="title-bar-text">${title}</div>
        <div class="title-bar-controls">
          <button class="minimize">_</button>
          <button class="maximize">□</button>
          <button class="close">×</button>
        </div>
      </div>
      <div class="window-content">${content}</div>
    `;

    windowEl.innerHTML = windowHTML;
    document.body.appendChild(windowEl);
    windows.add(windowEl);

    makeWindowDraggable(windowEl);
    setupWindowControls(windowEl);
    activateWindow(windowEl);
    updateTaskbar();

    return windowEl;
  }

  function makeWindowDraggable(windowEl) {
    const titleBar = windowEl.querySelector('.title-bar');
    let isDragging = false;
    let currentX, currentY, initialX, initialY, xOffset = 0, yOffset = 0;

    titleBar.addEventListener('mousedown', e => {
      if (e.target === titleBar) {
        isDragging = true;
        initialX = e.clientX - xOffset;
        initialY = e.clientY - yOffset;
        activateWindow(windowEl);
      }
    });

    document.addEventListener('mousemove', e => {
      if (isDragging) {
        e.preventDefault();
        currentX = e.clientX - initialX;
        currentY = e.clientY - initialY;
        xOffset = currentX;
        yOffset = currentY;
        windowEl.style.transform = `translate(${currentX}px, ${currentY}px)`;
      }
    });

    document.addEventListener('mouseup', () => {
      isDragging = false;
    });
  }

  function setupWindowControls(windowEl) {
    const closeBtn = windowEl.querySelector('.close');
    closeBtn.addEventListener('click', () => {
      windowEl.remove();
      windows.delete(windowEl);
      if (activeWindow === windowEl) {
        activeWindow = null;
      }
      updateTaskbar();
    });
  }

  function activateWindow(windowEl) {
    if (activeWindow) {
      activeWindow.classList.remove('active');
      activeWindow.querySelector('.title-bar').classList.add('inactive');
    }
    windowEl.classList.add('active');
    windowEl.querySelector('.title-bar').classList.remove('inactive');
    activeWindow = windowEl;
    updateTaskbar();
  }

  function updateTaskbar() {
    const taskbarItems = document.querySelector('.taskbar-items');
    taskbarItems.innerHTML = '';

    windows.forEach(window => {
      const title = window.querySelector('.title-bar-text').textContent;
      const item = document.createElement('div');
      item.className = `taskbar-item ${window === activeWindow ? 'active' : ''}`;
      item.textContent = title;
      item.addEventListener('click', () => {
        if (window === activeWindow) {
          window.style.display = window.style.display === 'none' ? 'block' : 'none';
        } else {
          window.style.display = 'block';
          activateWindow(window);
        }
      });
      taskbarItems.appendChild(item);
    });
  }

  // Program handlers
  const programs = {
    'my-computer': () => {
      const driveContent = {
        'c-drive': (callback) => {
          setTimeout(() => {
            callback(`
              <div class="folder-content">
                <div class="error-message">
                  ACCESS DENIED: This drive has been locked by system administrator.
                  <br><br>
                  Error code: 0x80070005
                  <br>
                  Contact your system administrator for access.
                </div>
              </div>
            `);
          }, 1500); // Loading delay
        },
        'd-drive': (callback) => {
          const isConnected = document.querySelector('.network-status')?.textContent.includes('Connected');
          
          setTimeout(() => {
            if (isConnected) {
              callback(`
                <div class="folder-content">
                  <div class="error-message">
                    NETWORK DRIVE CONTENTS INACCESSIBLE
                    <br><br>
                    Error code: 0x80070035
                    <br>
                    Access denied due to insufficient permissions.
                    <br>
                    Please contact network administrator.
                  </div>
                </div>
              `);
            } else {
              callback(`
                <div class="folder-content">
                  <div class="error-message">
                    NETWORK ERROR: Unable to establish connection to network drive.
                    <br><br>
                    Error code: 0x80070035
                    <br>
                    Check your network connection and try again.
                  </div>
                </div>
              `);
            }
          }, 2000);
        },
        'internet': (callback) => {
          setTimeout(() => {
            callback(`
              <div class="folder-content">
                <div class="error-message">
                  This application has been deprecated.
                  <br><br>
                  Please use the Internet Explorer icon on the desktop.
                </div>
              </div>
            `);
          }, 2000);
        },
        'reports': (callback) => {
          setTimeout(() => {
            callback(`
              <div class="folder-content">
                <div class="error-message">
                  FOLDER EMPTY
                  <br><br>
                  No documents found in this location.
                </div>
              </div>
            `);
          }, 2000);
        },
        'system32': (callback) => {
          setTimeout(() => {
            callback(`
              <div class="folder-content">
                <div class="error-message">
                  CRITICAL SYSTEM FILES
                  <br><br>
                  Access to this folder has been restricted by DoD Directive 8500.1
                  <br>
                  Unauthorized access attempts will be logged and reported.
                </div>
              </div>
            `);
          }, 2000);
        },
        'threshold': (callback) => {
          setTimeout(() => {
            callback(`
              <div class="threshold-viewer">
                <div class="threshold-header">
                  <h3>PROJECT THRESHOLD v2.3.1</h3>
                  <p class="warning">CLASSIFIED - LEVEL 5 CLEARANCE REQUIRED</p>
                </div>
                <div class="threshold-content">
                  <div class="threshold-visualization">
                    <svg viewBox="0 0 500 300" class="threshold-diagram">
                      <defs>
                        <pattern id="glitch" patternUnits="userSpaceOnUse" width="50" height="50">
                          <path d="M0 0h50v50H0z" fill="none" stroke="#0f0" stroke-width="0.5"/>
                          <path d="M25 0v50M0 25h50" stroke="#0f0" stroke-width="0.5" opacity="0.5"/>
                        </pattern>
                      </defs>
                      <rect width="500" height="300" fill="#001"/>
                      <path d="M100 50h300v200H100z" fill="url(#glitch)" stroke="#0f0"/>
                      <rect x="150" y="100" width="200" height="100" fill="#300" opacity="0.5"/>
                      <path d="M150 150h200" stroke="#f00" stroke-width="2" stroke-dasharray="5,5"/>
                      <text x="250" y="140" fill="#0f0" text-anchor="middle">THRESHOLD ZONE</text>
                      <g class="measurement-points">
                        ${Array.from({length: 8}, (_, i) => `
                          <circle cx="${150 + i * 28}" cy="150" r="2" fill="#f00"/>
                          <line x1="${150 + i * 28}" y1="150" x2="${150 + i * 28}" y2="160" 
                            stroke="#f00" stroke-width="1"/>
                        `).join('')}
                      </g>
                    </svg>
                  </div>
                  <div class="threshold-parameters">
                    <div class="parameter">
                      <label>Quantum Threshold:</label>
                      <div class="meter">
                        <div class="bar" style="width: ${Math.random() * 30}%"></div>
                      </div>
                      <span>${(Math.random() * 1000).toFixed(2)} μV</span>
                    </div>
                    <div class="parameter">
                      <label>Reality Anchor:</label>
                      <div class="meter">
                        <div class="bar" style="width: ${Math.random() * 30}%"></div>
                      </div>
                      <span>${(Math.random() * 30).toFixed(2)}%</span>
                    </div>
                    <div class="parameter">
                      <label>Dimensional Stability:</label>
                      <div class="meter">
                        <div class="bar" style="width: ${Math.random() * 30}%"></div>
                      </div>
                    </div>
                    <div class="parameter">
                      <label>Noclip Probability:</label>
                      <div class="meter critical">
                        <div class="bar" style="width: ${Math.random() * 2}%"></div>
                      </div>
                    </div>
                    <div class="threshold-warning">
                      WARNING: Values exceeding safety threshold. 
                      Automatic System Stabilization Activated.
                    </div>
                  </div>
                </div>
              </div>
            `);

            // Animate parameters
            setInterval(() => {
              document.querySelectorAll('.threshold-parameters .bar').forEach(bar => {
                bar.style.width = `${Math.random() * 100}%`;
              });
              document.querySelectorAll('.threshold-parameters span').forEach(span => {
                span.textContent = `${(Math.random() * 100).toFixed(2)}${span.textContent.slice(-1)}`;
              });
            }, 1000);
          }, 1500);
        }
      };

      const mainWindow = createWindow('My Computer', `
        <div class="folder-content">
          <div class="loading-indicator">Loading...</div>
        </div>
      `);

      setTimeout(() => {
        mainWindow.querySelector('.folder-content').innerHTML = `
          <div class="folder-item" data-folder="c-drive">
            <svg class="folder-item-icon" viewBox="0 0 24 24">
              <rect x="2" y="4" width="20" height="16" fill="#FFD700"/>
            </svg>
            <span>Local Disk (C:)</span>
          </div>
          <div class="folder-item" data-folder="d-drive">
            <svg class="folder-item-icon" viewBox="0 0 24 24">
              <rect x="2" y="4" width="20" height="16" fill="#A0A0A0"/>
            </svg>
            <span>Network Drive (D:)</span>
          </div>
          <div class="folder-item" data-folder="internet">
            <svg class="folder-item-icon" viewBox="0 0 24 24">
              <path d="M4 4h16v16H4z" fill="#4169E1"/>
            </svg>
            <span>Internet Explorer</span>
          </div>
          <div class="folder-item" data-folder="reports">
            <svg class="folder-item-icon" viewBox="0 0 24 24">
              <path d="M4 4h16v16H4z" fill="#008000"/>
              <text x="12" y="14" text-anchor="middle" fill="white" font-size="10">DOC</text>
            </svg>
            <span>Reports</span>
          </div>
          <div class="folder-item" data-folder="system32">
            <svg class="folder-item-icon" viewBox="0 0 24 24">
              <path d="M4 4h16v16H4z" fill="#800000"/>
              <text x="12" y="14" text-anchor="middle" fill="white" font-size="10">SYS</text>
            </svg>
            <span>System32</span>
          </div>
          <div class="folder-item" data-folder="threshold">
            <svg class="folder-item-icon" viewBox="0 0 24 24">
              <rect x="2" y="4" width="20" height="16" fill="#666"/>
            </svg>
            <span>Threshold</span>
          </div>
        `;

        mainWindow.querySelector('.folder-content').addEventListener('click', (e) => {
          const item = e.target.closest('.folder-item');
          if (!item) return;

          const folderId = item.dataset.folder;
          if (driveContent[folderId]) {
            const window = createWindow(item.querySelector('span').textContent, `
              <div class="loading-indicator">
                <div class="spinner"></div>
                Loading...
              </div>
            `);
            
            driveContent[folderId]((content) => {
              window.querySelector('.window-content').innerHTML = content;
            });
          }
        });
      }, 1000);
    },
    'internet': () => {
      const win = createWindow('Internet Explorer', `
        <div class="browser">
          <div class="browser-toolbar">
            <button>←</button>
            <button>→</button>
            <button>⟳</button>
            <input type="text" value="http://www.google.com" class="address-bar">
          </div>
          <div class="browser-content">
            <div class="loading-indicator">
              <div class="spinner"></div>
              Connecting to www.google.com...
            </div>
          </div>
        </div>
      `, 800);

      setTimeout(() => {
        win.querySelector('.browser-content').innerHTML = `
          <div class="google-page">
            Google
            <div class="connection-error">
              <h3>⚠️ No Internet Connection</h3>
              <p>Check your network cables, modem, and router</p>
              <p>ERR_INTERNET_DISCONNECTED</p>
            </div>
          </div>
        `;
      }, 2500);
    },
    'scp': () => {
      createWindow('SCP Foundation Database', `
        <div class="scp-database">
          <div class="scp-header">
            <h2>SCP Foundation</h2>
            <p>Secure. Contain. Protect.</p>
          </div>
          <div class="scp-list">
            <div class="scp-item">
              <h3>Space Pipes</h3>
              <p>Pipes of Space</p>
            </div>
           <div class="scp-item">
              <h3>SCP-████</h3>
              <p>The "████ ████"</p>
            </div>
            <div class="scp-item" data-scp="682">
              <h3>SCP-████</h3>
              <p>Hard-to-Destroy Reptile</p>
            </div>
            <div class="scp-item" data-scp="049">
              <h3>SCP-████</h3>
              <p>Plague Doctor</p>
            </div>
          </div>
        </div>
      `);

      const triggerLockdown = () => {
        const lockdownWindow = document.createElement('div');
        lockdownWindow.className = 'lockdown-screen';
        lockdownWindow.innerHTML = `
          <div class="lockdown-content">
            <div class="warning-symbol">⚠</div>
            <h1>SECURITY BREACH DETECTED</h1>
            <p>Unauthorized access to classified SCP Foundation files.</p>
            <p>System lockdown initiated.</p>
            <p>Process code: 78391</p>
            <p>Please wait for administrator assistance.</p>
            <div class="lockdown-footer">
              Site-████ SECURITY PROTOCOL ACTIVATED
            </div>
          </div>
        `;
        document.body.appendChild(lockdownWindow);
      };

      const scpData = {
        '173': {
          title: 'Space Pipes',
          class: 'Euclid',
          description: `Object Class: Euclid

Special Containment Procedures:
Space pipes can be stopped by drying out the general area they are located in. Once the space pipie is completedly dry it can be safely removed from the area. If you have come in contact with space pipes it is advisable to go through a full de-contamination process to assure you will not spread any of the particles onto other pipes.
Description:
Space pipes are dangerous and you should avoid making contact or breathing in the particles near the affected pipes. Space pipes while not hostile on their own inhibit a dangerous property. When interacted with space pipes will explode and spread there particles onto other pipes creating more space pipes. Breathing in the particles emitted by the pipes is also harmful to human health and can lead to drowsiness and shortness of breath. Falling asleep on uncontrolled pipes can also cause drowsiness and shortness of breath. Falling asleep next to a space pipe can lead to death by suffocation.
Space pipes can be stopped by drying out the general area they are located in. Once the space pipie is completedly dry it can be safely removed from the area. If you have come in contact with space pipes it is advisable to go through a full de-contamination process to assure you will not spread any of the particles onto other pipes.`

},
        '096': {
          title: 'SCP-096',
          class: 'Euclid',
          description: `Object Class: Euclid

Special Containment Procedures:
SCP-096 is to be contained in its cell, a 5m x 5m x 5m airtight steel cube, at all times. Weekly checks for any cracks or holes are mandatory. There are to be absolutely no video surveillance or optical tools of any kind inside SCP-096's cell. Security personnel will use pre-installed pressure sensors and laser detectors to ensure SCP-096's presence inside the cell.

Description:
SCP-096 is a humanoid creature measuring approximately 2.38 meters in height. Subject shows very little muscle mass, with preliminary analysis of body mass suggesting mild malnutrition. Arms are grossly out of proportion with the rest of the subject's body, with an approximate length of 1.5 meters each. Skin is mostly devoid of pigmentation, with no sign of any body hair.`
        }
      };

      document.querySelector('.scp-list').addEventListener('click', (e) => {
        const item = e.target.closest('.scp-item');
        if (!item) return;

        const scpId = item.dataset.scp;
        if (scpData[scpId]) {
          const detailWindow = createWindow(scpData[scpId].title, `
            <div class="scp-details">
              <div class="scp-warning">WARNING: LEVEL 4 CLEARANCE REQUIRED</div>
              <div class="scp-content">
                <h3>${scpData[scpId].title}</h3>
                <p class="scp-class">Object Class: ${scpData[scpId].class}</p>
                <div class="scp-description">
                  ${scpData[scpId].description}
                </div>
              </div>
            </div>
          `);

          // Trigger lockdown after random delay
          setTimeout(triggerLockdown, (Math.random() * 4000 + 1000));
        }
      });
    },
    'network': () => {
      createWindow('Network Connections', `
        <div class="network-interface">
          <div class="network-header">
            <h3>Available Networks</h3>
          </div>
          <div class="network-list">
            <div class="network-item">
              <div class="network-info">
                <div class="network-name">[Site-████-SECURE]</div>
                <div class="network-type">Secured [Read Only]</div>
                <div class="network-strength">Signal Strength: Strong</div>
              </div>
              <button class="connect-btn" disabled>Access Denied</button>
            </div>
            <div class="network-item">
              <div class="network-info">
                <div class="network-name">BRnet</div>
                <div class="network-type">Unknown Protocol</div>
                <div class="network-strength">Signal Strength: ??????????</div>
              </div>
              <button class="connect-btn" disabled>ERROR</button>
            </div>
            <div class="network-item">
              <div class="network-info">
                <div class="network-name">Public_sands</div>
                <div class="network-type">Unsecured</div>
                <div class="network-strength">Signal Strength: Weak</div>
              </div>
              <button class="connect-btn">Connect</button>
            </div>
            <div class="network-item">
              <div class="network-info">
                <div class="network-name">████-Guest</div>
                <div class="network-type">Secured</div>
                <div class="network-strength">Signal Strength: Medium</div>
              </div>
              <button class="connect-btn">Connect</button>
            </div>
          </div>
          <div class="network-status">
            <p>Current Connection: None</p>
            <p>Status: Searching for networks...</p>
            <p class="error-message">Warning: Anomalous signals detected</p>
          </div>
        </div>
      `);

      document.querySelectorAll('.connect-btn').forEach(btn => {
        if (!btn.disabled) {
          btn.addEventListener('click', () => {
            const networkName = btn.closest('.network-item').querySelector('.network-name').textContent;
            document.querySelector('.network-status').innerHTML = `
              <p>Current Connection: ${networkName}</p>
              <p>Status: Connected</p>
              <p class="warning">Notice: Network access restricted</p>
            `;
            
            document.querySelectorAll('.browser').forEach(browser => {
              const content = browser.querySelector('.browser-content');
              content.innerHTML = `
                <div class="google-page">
                  Google
                  <div class="search-box">
                    <input type="text" placeholder="Enter password to access internet...">
                    <button>Login</button>
                  </div>
                  <div class="error-message">
                    ERROR: Access to internet resources is restricted to authorized personnel only.
                    <br>Please contact your system administrator for access credentials.
                    <br>Error code: AUTH_403
                  </div>
                </div>
              `;
            });
          });
        }
      });
    },
    'timetable': () => {
      createWindow('Backrooms Transit Authority', `
        <div class="transit-timetable">
          <div class="timetable-header">
            <h2>INTERDIMENSIONAL TRANSIT SCHEDULE</h2>
            <p class="warning">※ Schedule subject to non-euclidean distortions and includes trains that are not safe by M.E.G standards</p>
          </div>
          <div class="timetable-content">
            ${Array.from({ length: 6590 }, (_, i) => `
              <div class="timetable-row">
                <div class="time">${moment().add(Math.random() * 60, 'minutes').format('HH:mm')}</div>
                <div class="route">Route ${['A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'][Math.floor(Math.random() * 26)]}-${Math.floor(Math.random() * 999)}</div>
                <div class="destination">Level ${Math.floor(Math.random() * 1000)}</div>
                <div class="status">${['On Time', 'Delayed', 'Unknown', 'Out of Service', 'Cancelled','In Transit', 'Anomaly Danger','Off-Track'][Math.floor(Math.random() * 7)]}</div>
              </div>
            `).join('')}
          </div>
        </div>
      `, 600);
    },
    'classified': () => {
      const win = createWindow('CLASSIFIED FILES', `
        <div class="password-prompt">
          <p>ENTER SECURITY CLEARANCE CODE:</p>
          <input type="password" class="password-input">
          <button class="submit-password">SUBMIT</button>
        </div>
        <div class="files" style="display: none;">
          <div class="file" data-file="scp">
            <h3>SCP-████████.doc</h3>
            <p>Pending name and classifications</p>
          </div>
          <div class="file" data-file="backrooms">
            <h3>BACKROOMS-INCIDENT-LOG.txt</h3>
            <p>Level 0 Breach Report - Security Level 5</p>
          </div>
          <div class="file" data-file="threshold">
            <h3>PROJECT-THRESHOLD.log</h3>
            <p>Noclip Investigation Tool - Security Level 6</p>
          </div>
          <div class="file" data-file="trainmap">
            <h3>BACKROOMS-TRAIN-SYSTEM.svg</h3>
            <p>Interdimensional Rail Network - Security Level 5</p>
          </div>
        </div>
      `);

      const input = win.querySelector('.password-input');
      const submit = win.querySelector('.submit-password');
      const files = win.querySelector('.files');

      submit.addEventListener('click', () => {
        if (input.value === 'wspg') {
          win.querySelector('.password-prompt').style.display = 'none';
          files.style.display = 'block';
        } else {
          alert('ACCESS DENIED - SECURITY VIOLATION LOGGED');
        }
      });

      files.addEventListener('click', (e) => {
        const file = e.target.closest('.file');
        if (!file) return;

        const fileContents = {
          'scp': `SCP-████████████
OBJECT CLASS: Pending

SPECIAL CONTAINMENT PROCEDURES:
Unable to contain at this time. Current Status is to observe all actions of ████████████ and report any changes or abnormalities in behavior. 

DESCRIPTION:
SCP-██████████ is a humanoid entinty that currently resides in ████████████ . The entity has gained notoriety on the internet and displayed the power to see other ████████████ throughout the universe. A holding site located in the North Atlantic Ocean (Latitude: 37.02806, Longitude: -30.54940, Distortion: 1.57) was prepared on ████████████ to contain the entity. Currently the site is abandoned after a earthquake due to a seismic shifts damaged the holding equipment, although new containment procedures are currently being made they are not expected to finish until 2042. Most of the anomalous properties of SCP-██████████ do not effect others however, the possibility of a Great Convergence K-Class Scenario remains possible.`,
          'backrooms': `BACKROOMS INCIDENT LOG - 05/23/20██

0300 hrs: First reports of wall phasing incident outside of testing room █████ at Site-████.
0317 hrs: Multiple personnel reported missing.
0330 hrs: Recovery team shota-A assembled and deployed to Site-████.
0345 hrs: Recovery team reports breach at Site-████.
0350 hrs: Remaning personnel evacuated and recovery team deployed to backrooms.
0355 hrs: Pending incident report from recovery team.`,
          'threshold': `PROJECT THRESHOLD
STATUS: MAINTENANCE
CLEARANCE: LEVEL 6

Warning: This program is currently in autonomus mode actions will be taken by the system.
Any system readings currently displayed are not accurate. The pulse of the program is to monitor the quantum fluctuations of object ████████ at site ████████. If there is any value above the safety threshold please  consult the system administrator at 612-861-3421`,
          'trainmap': () => {
            createWindow('BACKROOMS TRAIN SYSTEM', `
              <div class="map-viewer">
                <p>This file has been moved to the Network Monitor.</p>
                <p>Please use the Network application to view train system status.</p>
              </div>
            `);
          }
        };

        if (typeof fileContents[file.dataset.file] === 'function') {
          fileContents[file.dataset.file]();
        } else {
          const win = createWindow(file.querySelector('h3').textContent, `
            <div class="${file.dataset.file === 'trainmap' ? 'map-viewer' : 'text-viewer'}">
              ${fileContents[file.dataset.file]}
            </div>
          `, file.dataset.file === 'trainmap' ? 800 : 500);
        }
      });
    },
    'recycle-bin': () => {
      createWindow('Recycle Bin', `
        <div class="folder-content">
          <p style="padding: 20px;">Recycle Bin is empty</p>
        </div>
      `);
    },
    'metro': () => {
      const trainData = {
        locations: [
          { id: 'pi', name: 'Level π', x: 150, y: 100 },
          { id: '0', name: 'Level 0', x: 300, y: 100 },
          { id: '9', name: 'Level 9', x: 450, y: 150 },
          { id: '36b', name: 'Level 36-B', x: 600, y: 200 },
          { id: '11', name: 'Level 11?', x: 450, y: 300 },
          { id: '990', name: 'Level 990', x: 300, y: 300 },
          { id: 'dark', name: 'Dark Metro', x: 150, y: 300 },
          { id: '6.1', name: 'Level 6.1', x: 150, y: 200 },
          { id: 'end', name: 'The End', x: 400, y: 400 },
          { id: '1883', name: 'Level 1883', x: 500, y: 400 },
          { id: '188', name: 'Level 188', x: 600, y: 400 },
          { id: '14', name: 'Level 14', x: 700, y: 350 },
          { id: 'airport', name: 'Level 36', x: 750, y: 250 },
          { id: '10', name: 'Level 10', x: 700, y: 150 },
          { id: '4', name: 'Level 4', x: 650, y: 50 },
          { id: 'hub', name: 'The Hub', x: 500, y: 50 },
          { id: '-33', name: 'Level -33', x: 350, y: 50 },
          { id: '3', name: 'Level 3', x: 200, y: 50 }
        ],
        connections: [
          ['pi', '0'],
          ['0', '9'],
          ['9', '36b'],
          ['36b', '11'],
          ['11', '990'],
          ['990', 'dark'],
          ['dark', '6.1'],
          ['6.1', 'pi']
        ],
        trains: [
          {
            id: 'A1',
            type: 'a',
            route: ['pi', '0', '9', '36b', '11', 'hub'],
            speed: 0.001,
            position: 0,
            progress: 0,
            waiting: 0
          },
          {
            id: 'B1',
            type: 'b',
            route: ['36b', '11', '990', 'dark', '6.1', 'hub'],
            speed: 0.001,
            position: 0,
            progress: 0,
            waiting: 0
          },
          {
            id: 'STEAM1',
            type: 'steam',
            route: ['hub', '-33', '3', 'pi', 'hub'],
            speed: 0.0015, 
            position: 0,
            progress: 0,
            waiting: 0
          }
        ]
      };

      const win = createWindow('Metro Network Monitor', `
        <div class="network-monitor">
          <div class="monitor-split">
            <div class="map-container">
              <div class="map-controls">
                <button class="zoom-in">+</button>
                <button class="zoom-out">-</button>
                <button class="pan-reset">R</button>
              </div>
              <div class="map-viewport">
                <svg viewBox="0 0 800 500" class="network-map">
                  <defs>
                    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5"
                      markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                      <path d="M 0 0 L 10 5 L 0 10 z" fill="#00ff00"/>
                    </marker>
                  </defs>
                  <g class="connections"></g>
                  <g class="stations"></g>
                  <g class="trains"></g>
                </svg>
              </div>
            </div>
            <div class="info-panel">
              <div class="system-status">
                <h3>SYSTEM STATUS</h3>
                <div class="status-details">
                  <p>Active Trains: <span class="train-count">3</span></p>
                  <p>System Status: <span class="system-status">OPERATIONAL</span></p>
                  <p>Next Maintenance: <span class="next-maintenance">12:00</span></p>
                  <p>Visible: <span class="next-maintenance">Safe Trains</span></p>                  
                </div>
              </div>
              <div class="train-list">
                <h3>ACTIVE TRAINS</h3>
                <div class="train-details"></div>
              </div>
            </div>
          </div>
        </div>
      `, 900);

      const svg = win.querySelector('.network-map');
      let scale = 1;
      let panX = 0;
      let panY = 0;
      
      const updateTransform = () => {
        const g = svg.querySelector('g.connections').parentElement;
        g.style.transform = `scale(${scale}) translate(${panX}px, ${panY}px)`;
      };

      win.querySelector('.zoom-in').addEventListener('click', () => {
        scale = Math.min(scale * 1.2, 2);
        updateTransform();
      });

      win.querySelector('.zoom-out').addEventListener('click', () => {
        scale = Math.max(scale / 1.2, 0.5);
        updateTransform();
      });

      win.querySelector('.pan-reset').addEventListener('click', () => {
        scale = 1;
        panX = 0;
        panY = 0;
        updateTransform();
      });

      let isDragging = false;
      let startX, startY;

      svg.addEventListener('mousedown', (e) => {
        isDragging = true;
        startX = e.clientX - panX;
        startY = e.clientY - panY;
      });

      window.addEventListener('mousemove', (e) => {
        if (isDragging) {
          panX = e.clientX - startX;
          panY = e.clientY - startY;
          updateTransform();
        }
      });

      window.addEventListener('mouseup', () => {
        isDragging = false;
      });

      const drawNetwork = () => {
        const stations = win.querySelector('.stations');
        const connections = win.querySelector('.connections');
        const trains = win.querySelector('.trains');
        
        connections.innerHTML = trainData.connections.map(([from, to]) => {
          const fromStation = trainData.locations.find(l => l.id === from);
          const toStation = trainData.locations.find(l => l.id === to);
          return `<path 
            d="M ${fromStation.x} ${fromStation.y} L ${toStation.x} ${toStation.y}"
            class="track"
            data-from="${from}"
            data-to="${to}"
          />`;
        }).join('');

        stations.innerHTML = trainData.locations.map(loc => `
          <g class="station" data-id="${loc.id}" onclick="showStationInfo('${loc.id}')">
            <circle cx="${loc.x}" cy="${loc.y}" r="10" />
            <text x="${loc.x}" y="${loc.y + 25}" text-anchor="middle">${loc.name}</text>
          </g>
        `).join('');

        trainData.trains.forEach(train => {
          const fromStation = trainData.locations.find(l => l.id === train.route[train.position]);
          const toStation = trainData.locations.find(l => l.id === train.route[(train.position + 1) % train.route.length]);
          
          const x = fromStation.x + (toStation.x - fromStation.x) * train.progress;
          const y = fromStation.y + (toStation.y - fromStation.y) * train.progress;

          const trainEl = trains.querySelector(`[data-id="${train.id}"]`) || document.createElementNS("http://www.w3.org/2000/svg", "g");
          trainEl.setAttribute('class', `train ${train.type}`);
          trainEl.setAttribute('data-id', train.id);
          trainEl.innerHTML = `<circle cx="${x}" cy="${y}" r="5" class="train-marker"/>`;
          
          if (!trainEl.parentElement) {
            trains.appendChild(trainEl);
          }
        });
      };

      const updateTrains = () => {
        trainData.trains.forEach(train => {
          if (train.waiting > 0) {
            train.waiting -= 1;
            return;
          }
          
          train.progress += train.speed;
          if (train.progress >= 1) {
            train.progress = 0;
            train.position = (train.position + 1) % train.route.length;
            train.waiting = 200; 
          }
        });
        drawNetwork();
      };

      const animationInterval = setInterval(updateTrains, 100);

      win.addEventListener('remove', () => {
        clearInterval(animationInterval);
      });

      drawNetwork();

      window.showStationInfo = (stationId) => {
        const station = trainData.locations.find(l => l.id === stationId);
        const info = win.querySelector('.station-info') || document.createElement('div');
        info.className = 'station-info';
        info.innerHTML = `
          <h4>${station.name}</h4>
          <p>Status: OPERATIONAL</p>
          <p>Security Level: UNKNOWN</p>
          <p>Current Occupancy: --</p>
          <p>Next Arrival: ${moment().add(Math.floor(Math.random() * 10), 'minutes').format('HH:mm')}</p>
          <p style="color: #666">Note: Further information unavailable due to ERROR CODE 451</p>
        `;
        win.querySelector('.info-panel').appendChild(info);
      };

      const updateTrainInfo = () => {
        const trainDetails = win.querySelector('.train-details');
        trainDetails.innerHTML = trainData.trains.map(train => {
          const currentStation = trainData.locations.find(l => l.id === train.route[train.position]);
          const nextStation = trainData.locations.find(l => l.id === train.route[(train.position + 1) % train.route.length]);
          const status = train.waiting > 0 ? 'STOPPED' : 'IN TRANSIT';
          return `
            <div class="train-info ${train.type}">
              <h4>Train ${train.id}</h4>
              <p>Type: ${train.type.toUpperCase()}</p>
              <p>Status: ${status}</p>
              <p>Current: ${currentStation.name}</p>
              <p>Next: ${nextStation.name}</p>
              <p>Progress: ${Math.round(train.waiting > 0 ? 100 : train.progress * 100)}%</p>
            </div>
          `;
        }).join('');

        let schedule = document.querySelector('.schedule');
        if (!schedule) {
          schedule = document.createElement('div');
          schedule.className = 'schedule';
          schedule.innerHTML = '<h3>TIMETABLE</h3><div class="schedule-content"></div>';
          win.querySelector('.network-monitor').appendChild(schedule);
        }

        const scheduleContent = schedule.querySelector('.schedule-content');
        scheduleContent.innerHTML = trainData.trains.map(train => {
          const currentStation = trainData.locations.find(l => l.id === train.route[train.position]);
          const time = moment().add(Math.round((1 - train.progress) * 5), 'minutes').format('HH:mm');
          return `
            <div class="schedule-entry ${train.type}">
              <span>${train.id}</span>
              <span>${time}</span>
              <span>${currentStation.name}</span>
            </div>
          `;
        }).join('');
      };

      setInterval(updateTrainInfo, 1000);
      updateTrainInfo();
    }
  };

  const startMenu = {
    init() {
      const startButton = document.querySelector('.start-button');
      const menu = document.createElement('div');
      menu.className = 'start-menu';
      menu.innerHTML = `
        <div class="start-menu-header">
          <div class="user-info">
            <svg viewBox="0 0 32 32" class="user-icon">
              <circle cx="16" cy="16" r="16" fill="#008080"/>
              <text x="16" y="20" text-anchor="middle" fill="white" font-size="12">U</text>
            </svg>
            <span>USDOD-USER</span>
          </div>
        </div>
        <div class="start-menu-items">
          <div class="start-item" data-program="my-computer">
            <svg viewBox="0 0 24 24" class="start-icon">
              <rect x="4" y="4" width="16" height="12" fill="#ccc"/>
              <rect x="7" y="16" width="10" height="4" fill="#999"/>
            </svg>
            My Computer
          </div>
          <div class="start-item" data-program="internet">
            <svg viewBox="0 0 24 24" class="start-icon">
              <circle cx="12" cy="12" r="10" fill="#0078D7"/>
              <text x="12" y="16" text-anchor="middle" fill="white" font-size="12">e</text>
            </svg>
            Internet
          </div>
          <div class="start-item" data-program="network">
            <svg viewBox="0 0 24 24" class="start-icon">
              <circle cx="12" cy="12" r="8" fill="#4169E1"/>
              <path d="M8 12h8M12 8v8" stroke="white" stroke-width="2"/>
            </svg>
            Network
          </div>
          <div class="start-menu-separator"></div>
          <div class="start-item" data-program="classified">
            <svg viewBox="0 0 24 24" class="start-icon">
              <path d="M4 4h16v16H4z" fill="#fc0"/>
              <text x="12" y="14" text-anchor="middle" font-size="8" fill="black">TOP</text>
              <text x="12" y="20" text-anchor="middle" font-size="8" fill="black">SECRET</text>
            </svg>
            Classified Files
          </div>
          <div class="start-item" data-program="scp">
            <svg viewBox="0 0 24 24" class="start-icon">
              <rect x="2" y="2" width="20" height="20" fill="#000"/>
              <text x="12" y="14" text-anchor="middle" fill="#f00" font-size="8">SCP</text>
              <text x="12" y="20" text-anchor="middle" fill="#f00" font-size="6">DATABASE</text>
            </svg>
            SCP Database
          </div>
          <div class="start-menu-separator"></div>
          <div class="start-item shutdown">
            <svg viewBox="0 0 24 24" class="start-icon">
              <circle cx="12" cy="12" r="10" fill="#ff0000"/>
              <path d="M8 12h8M12 8v8" stroke="white" stroke-width="2"/>
            </svg>
            Shut Down...
          </div>
        </div>
      `;
      
      document.body.appendChild(menu);
      
      let isMenuOpen = false;
      
      startButton.addEventListener('click', (e) => {
        e.stopPropagation();
        isMenuOpen = !isMenuOpen;
        menu.style.display = isMenuOpen ? 'block' : 'none';
        startButton.classList.toggle('active', isMenuOpen);
      });
      
      menu.addEventListener('click', (e) => {
        const item = e.target.closest('.start-item');
        if (!item) return;
        
        if (item.classList.contains('shutdown')) {
          alert('ACCESS DENIED: System shutdown requires ADMIN clearance.');
          return;
        }
        
        const program = item.dataset.program;
        if (programs[program]) {
          programs[program]();
        }
        
        isMenuOpen = false;
        menu.style.display = 'none';
        startButton.classList.remove('active');
      });
      
      document.addEventListener('click', (e) => {
        if (!menu.contains(e.target) && !startButton.contains(e.target)) {
          isMenuOpen = false;
          menu.style.display = 'none';
          startButton.classList.remove('active');
        }
      });
    }
  };

  startMenu.init();

  document.querySelectorAll('.icon').forEach(icon => {
    icon.addEventListener('click', () => {
      const program = icon.dataset.program;
      if (programs[program]) {
        programs[program]();
      }
    });
  });
});