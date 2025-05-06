import { Window } from './window.js';

export class WifiSystemApp {
  constructor(windowManager) {
    this.windowManager = windowManager;
    this.windowInstance = null;
    this.isConnected = false;
    this.wifiPassword = "136.228.116.222";
    this.networks = [
      { name: "MILITARY-SECURED-NETWORK", strength: 95, secured: true, connected: false },
      { name: "GUEST-ACCESS", strength: 87, secured: true, connected: false },
      { name: "FIELD-OPS-BACKUP", strength: 72, secured: true, connected: false },
      { name: "EMERGENCY-COMMS", strength: 45, secured: true, connected: false }
    ];
  }

  open() {
    if (!this.windowInstance) {
      this.windowInstance = this.createWindow();
    }
    this.windowManager.openWindow(this.windowInstance);
  }

  createWindow() {
    const windowElement = document.createElement('div');
    windowElement.id = 'wifi-system-window';
    windowElement.classList.add('window');
    windowElement.style.width = '500px';
    windowElement.style.height = '400px';
    windowElement.style.top = '120px';
    windowElement.style.left = '250px';

    const header = document.createElement('div');
    header.classList.add('window-header');
    header.innerHTML = `
      <div class="window-title">WiFi System</div>
      <div class="window-controls">
        <button class="close-button">X</button>
      </div>
    `;

    const content = document.createElement('div');
    content.classList.add('window-content');
    content.innerHTML = `
      <h3>Network Connections</h3>
      <div class="wifi-status ${this.isConnected ? 'connected' : 'disconnected'}">
        Status: ${this.isConnected ? 'Connected' : 'Disconnected'}
      </div>
      <div class="network-list">
        ${this.networks.map(network => `
          <div class="network-item" data-name="${network.name}">
            <div class="network-info">
              <div class="network-name">${network.name}</div>
              <div class="network-strength" title="${network.strength}% Signal Strength">
                ${this.generateSignalBars(network.strength)}
              </div>
              ${network.secured ? '<div class="network-secured">🔒</div>' : ''}
            </div>
            <button class="connect-button">${network.connected ? 'Disconnect' : 'Connect'}</button>
          </div>
        `).join('')}
      </div>
      <div class="password-prompt" style="display: none;">
        <h4>Enter Network Password</h4>
        <input type="password" class="network-password" placeholder="Password">
        <div class="password-buttons">
          <button class="cancel-password">Cancel</button>
          <button class="submit-password">Connect</button>
        </div>
      </div>
    `;

    windowElement.appendChild(header);
    windowElement.appendChild(content);

    // Event listeners
    const closeButton = header.querySelector('.close-button');
    closeButton.addEventListener('click', () => {
      this.windowManager.closeWindow(windowElement);
      this.windowInstance = null;
    });

    // Add connect button functionality
    const connectButtons = content.querySelectorAll('.connect-button');
    connectButtons.forEach(button => {
      button.addEventListener('click', (e) => {
        const networkItem = e.target.closest('.network-item');
        const networkName = networkItem.dataset.name;
        
        if (this.isConnected) {
          this.disconnectNetwork();
          return;
        }
        
        const passwordPrompt = content.querySelector('.password-prompt');
        passwordPrompt.style.display = 'block';
        
        // Store the selected network name for connection attempt
        passwordPrompt.dataset.network = networkName;
      });
    });
    
    // Password handling
    const submitPassword = content.querySelector('.submit-password');
    submitPassword.addEventListener('click', () => {
      const passwordInput = content.querySelector('.network-password');
      const password = passwordInput.value;
      const networkName = content.querySelector('.password-prompt').dataset.network;
      
      if (password === this.wifiPassword) {
        this.connectNetwork(networkName);
        content.querySelector('.password-prompt').style.display = 'none';
        passwordInput.value = '';
      } else {
        alert('Incorrect password. Access denied.');
      }
    });
    
    const cancelPassword = content.querySelector('.cancel-password');
    cancelPassword.addEventListener('click', () => {
      content.querySelector('.password-prompt').style.display = 'none';
      content.querySelector('.network-password').value = '';
    });

    return new Window(windowElement, this.windowManager);
  }
  
  generateSignalBars(strength) {
    const bars = Math.ceil(strength / 20); // 0-5 bars based on strength
    let barsHTML = '';
    for (let i = 0; i < 5; i++) {
      if (i < bars) {
        barsHTML += '<span class="signal-bar active"></span>';
      } else {
        barsHTML += '<span class="signal-bar"></span>';
      }
    }
    return `<div class="signal-bars">${barsHTML}</div>`;
  }
  
  connectNetwork(networkName) {
    // Only allow connection to GUEST-ACCESS network
    if (networkName !== "GUEST-ACCESS") {
      alert("Connection to this network requires administrative privileges.");
      return;
    }
    
    this.isConnected = true;
    
    // Update networks list
    this.networks.forEach(network => {
      network.connected = (network.name === networkName);
    });
    
    // Update UI if window is open
    if (this.windowInstance) {
      const content = this.windowInstance.windowElement.querySelector('.window-content');
      
      // Update status
      const statusElement = content.querySelector('.wifi-status');
      statusElement.textContent = 'Status: Connected';
      statusElement.classList.remove('disconnected');
      statusElement.classList.add('connected');
      
      // Update network list
      const networkItems = content.querySelectorAll('.network-item');
      networkItems.forEach(item => {
        const name = item.dataset.name;
        const connectButton = item.querySelector('.connect-button');
        
        if (name === networkName) {
          connectButton.textContent = 'Disconnect';
        } else {
          connectButton.textContent = 'Connect';
        }
      });
    }
  }
  
  disconnectNetwork() {
    this.isConnected = false;
    
    // Update networks list
    this.networks.forEach(network => {
      network.connected = false;
    });
    
    // Update UI if window is open
    if (this.windowInstance) {
      const content = this.windowInstance.windowElement.querySelector('.window-content');
      
      // Update status
      const statusElement = content.querySelector('.wifi-status');
      statusElement.textContent = 'Status: Disconnected';
      statusElement.classList.remove('connected');
      statusElement.classList.add('disconnected');
      
      // Update network list
      const connectButtons = content.querySelectorAll('.connect-button');
      connectButtons.forEach(button => {
        button.textContent = 'Connect';
      });
    }
  }
}