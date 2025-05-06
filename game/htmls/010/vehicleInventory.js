import { Window } from './window.js';

export class VehicleInventoryApp {
  constructor(windowManager) {
    this.windowManager = windowManager;
    this.windowInstance = null;
  }

  open() {
    if (!this.windowInstance) {
      this.windowInstance = this.createWindow();
    }
    this.windowManager.openWindow(this.windowInstance);
  }

  createWindow() {
    const windowElement = document.createElement('div');
    windowElement.id = 'vehicle-inventory-window';
    windowElement.classList.add('window');
    windowElement.style.width = '600px';
    windowElement.style.height = '400px';
    windowElement.style.top = '50px';
    windowElement.style.left = '200px';

    const header = document.createElement('div');
    header.classList.add('window-header');
    header.innerHTML = `
      <div class="window-title">Vehicle Inventory - Fort Belvoir</div>
      <div class="window-controls">
        <button class="close-button">X</button>
      </div>
    `;

    const content = document.createElement('div');
    content.classList.add('window-content');
    content.innerHTML = `
      <h3>Available Military Vehicles</h3>
      <div class="vehicle-inventory">
        <div class="vehicle-item">
          <div class="vehicle-image">
            <svg viewBox="0 0 100 60" width="80" height="50">
              <rect x="20" y="30" width="60" height="20" rx="5" fill="#333" stroke="#0ff" stroke-width="1"/>
              <rect x="10" y="40" width="80" height="10" rx="2" fill="#444" stroke="#0ff" stroke-width="1"/>
              <circle cx="25" cy="50" r="8" fill="#222" stroke="#0ff" stroke-width="1"/>
              <circle cx="75" cy="50" r="8" fill="#222" stroke="#0ff" stroke-width="1"/>
              <rect x="30" y="20" width="40" height="10" rx="5" fill="#333" stroke="#0ff" stroke-width="1"/>
            </svg>
          </div>
          <div>
            <h4>M1126 Stryker</h4>
            <p>Type: Infantry Carrier Vehicle</p>
            <p>Status: Operational</p>
          </div>
          <div>
            <p>Storage Capacity: 2,340kg</p>
            <p>Personnel Capacity: 9 + 2 crew</p>
            <p>Fuel Status: 92%</p>
          </div>
          <div>
            <p>Maintenance Required: No</p>
            <p>Last Service: 36 hours ago</p>
            <p>Location: Vehicle Bay A</p>
          </div>
        </div>

        <div class="vehicle-item">
          <div class="vehicle-image">
            <svg viewBox="0 0 100 60" width="80" height="50">
              <path d="M10,40 L30,25 L70,25 L90,40 L90,50 L10,50 Z" fill="#333" stroke="#0ff" stroke-width="1"/>
              <circle cx="25" cy="50" r="8" fill="#222" stroke="#0ff" stroke-width="1"/>
              <circle cx="75" cy="50" r="8" fill="#222" stroke="#0ff" stroke-width="1"/>
              <rect x="40" y="15" width="20" height="10" fill="#333" stroke="#0ff" stroke-width="1"/>
            </svg>
          </div>
          <div>
            <h4>UH-60 Black Hawk</h4>
            <p>Type: Utility Helicopter</p>
            <p>Status: Ready for Deployment</p>
          </div>
          <div>
            <p>Storage Capacity: 9,000 lbs</p>
            <p>Personnel Capacity: 11 + 3 crew</p>
            <p>Fuel Status: 100%</p>
          </div>
          <div>
            <p>Maintenance Required: No</p>
            <p>Last Service: 8 hours ago</p>
            <p>Location: Hangar C</p>
          </div>
        </div>

        <div class="vehicle-item">
          <div class="vehicle-image">
            <svg viewBox="0 0 100 60" width="80" height="50">
              <rect x="20" y="35" width="60" height="15" rx="2" fill="#444" stroke="#0ff" stroke-width="1"/>
              <rect x="10" y="30" width="80" height="10" fill="#333" stroke="#0ff" stroke-width="1"/>
              <rect x="35" y="15" width="30" height="15" fill="#333" stroke="#0ff" stroke-width="1"/>
              <circle cx="25" cy="50" r="8" fill="#222" stroke="#0ff" stroke-width="1"/>
              <circle cx="75" cy="50" r="8" fill="#222" stroke="#0ff" stroke-width="1"/>
              <rect x="45" y="10" width="10" height="5" fill="#333" stroke="#0ff" stroke-width="1"/>
            </svg>
          </div>
          <div>
            <h4>MRAP MaxxPro</h4>
            <p>Type: Mine-Resistant Vehicle</p>
            <p>Status: Under Maintenance</p>
          </div>
          <div>
            <p>Storage Capacity: 4,000kg</p>
            <p>Personnel Capacity: 7</p>
            <p>Fuel Status: 65%</p>
          </div>
          <div>
            <p>Maintenance Required: Yes</p>
            <p>ETA: 4 hours</p>
            <p>Location: Maintenance Bay</p>
          </div>
        </div>
        
        <div class="vehicle-item">
          <div class="vehicle-image">
            <svg viewBox="0 0 100 60" width="80" height="50">
              <rect x="15" y="40" width="70" height="10" fill="#444" stroke="#0ff" stroke-width="1"/>
              <rect x="25" y="20" width="50" height="20" fill="#333" stroke="#0ff" stroke-width="1"/>
              <rect x="35" y="10" width="30" height="10" fill="#333" stroke="#0ff" stroke-width="1"/>
              <circle cx="25" cy="50" r="6" fill="#222" stroke="#0ff" stroke-width="1"/>
              <circle cx="40" cy="50" r="6" fill="#222" stroke="#0ff" stroke-width="1"/>
              <circle cx="60" cy="50" r="6" fill="#222" stroke="#0ff" stroke-width="1"/>
              <circle cx="75" cy="50" r="6" fill="#222" stroke="#0ff" stroke-width="1"/>
            </svg>
          </div>
          <div>
            <h4>M1A2 Abrams</h4>
            <p>Type: Main Battle Tank</p>
            <p>Status: Ready</p>
          </div>
          <div>
            <p>Ammo Capacity: 100%</p>
            <p>Personnel Capacity: 4 crew</p>
            <p>Fuel Status: 88%</p>
          </div>
          <div>
            <p>Maintenance Required: No</p>
            <p>Last Service: 48 hours ago</p>
            <p>Location: Armored Division</p>
          </div>
        </div>
      </div>
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

