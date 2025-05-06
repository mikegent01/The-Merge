import { Window } from './window.js';

export class MissileInventoryApp {
  constructor(windowManager) {
    this.windowManager = windowManager;
    this.windowInstance = null;
    this.missileData = { 
      'AIM-120 AMRAAM': { status: 'Ready for Launch', location: 'Silo A' },
      'AGM-158 JASSM': { status: 'Maintenance Required', location: 'Bunker C' },
      'RIM-174 ERAM': { status: 'Ready for Launch', location: 'Silo B' },
      'BGM-109 Tomahawk': { status: 'Ready for Launch', location: 'Launch Bay D' }
    };
  }

  open() {
    if (!this.windowInstance) {
      this.windowInstance = this.createWindow();
    }
    this.windowManager.openWindow(this.windowInstance);
    this.updateInventoryDisplay(); 
  }

  updateMissileStatus(missileName, newStatus) {
    if (this.missileData[missileName]) {
      this.missileData[missileName].status = newStatus;
      this.updateInventoryDisplay(); 
    }
  }

  updateInventoryDisplay() {
    if (!this.windowInstance) return; 
    const content = this.windowInstance.windowElement.querySelector('.window-content');
    if (!content) return; 

    let missileGridHTML = '<div class="missile-grid">';
    for (const missileName in this.missileData) {
      const missileInfo = this.missileData[missileName];
      let statusClass = '';
      let statusText = missileInfo.status;
      if (missileInfo.status === 'Ready for Launch') {
        statusClass = 'ready';
      } else if (missileInfo.status === 'Maintenance Required') {
        statusClass = 'maintenance';
      } else if (missileInfo.status === 'No Fuel') {
        statusClass = 'no-fuel';
      } else if (missileInfo.status === 'Launched') {
        statusClass = 'launched'; 
        statusText = 'Launched'; 
      }

      missileGridHTML += `
        <div class="missile-card">
          <div class="missile-visual">
            <svg viewBox="0 0 50 200" style="width:30px; height:60px;" class="missile-svg">
              <path d="M25,0 L35,40 L35,160 L25,200 L15,160 L15,40 Z" class="missile-body"/>
              <path d="M15,160 L35,160 L30,180 L20,180 Z" class="missile-fins"/>
              <circle cx="25" cy="90" r="8" class="missile-detail"/>
            </svg>
            <div class="missile-status ${statusClass}"></div>
          </div>
          <div class="missile-info">
            <h4>${missileName}</h4>
            <p>Status: ${statusText}</p>
            <p>Type: Tactical Ballistic</p>
            <p>Range: Classified</p>
            <p>Warhead: Classified</p>
            <p>Location: ${missileInfo.location}</p>
          </div>
        </div>
      `;
    }
    missileGridHTML += '</div>';
    content.querySelector('.missile-inventory').innerHTML = missileGridHTML;
  }

  createWindow() {
    const windowElement = document.createElement('div');
    windowElement.id = 'missile-inventory-window';
    windowElement.classList.add('window');
    windowElement.style.width = '600px';
    windowElement.style.height = '500px';
    windowElement.style.top = '70px';
    windowElement.style.left = '220px';

    const header = document.createElement('div');
    header.classList.add('window-header');
    header.innerHTML = `
      <div class="window-title">Missile Inventory</div>
      <div class="window-controls">
        <button class="close-button">X</button>
      </div>
    `;

    const content = document.createElement('div');
    content.classList.add('window-content');
    content.innerHTML = `
      <h3>Missile Inventory</h3>
      <div class="missile-inventory"></div>
    `;

    windowElement.appendChild(header);
    windowElement.appendChild(content);

    const closeButton = header.querySelector('.close-button');
    closeButton.addEventListener('click', () => {
      this.windowManager.closeWindow(windowElement);
      this.windowInstance = null;
    });

    return new Window(windowElement, this.windowManager);
  }
}