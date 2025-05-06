import { Window } from './window.js';

export class SCPDatabaseApp {
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
    windowElement.id = 'scp-database-window';
    windowElement.classList.add('window');
    windowElement.style.width = '700px';
    windowElement.style.height = '550px';
    windowElement.style.top = '100px';
    windowElement.style.left = '100px';

    const header = document.createElement('div');
    header.classList.add('window-header');
    header.innerHTML = `
      <div class="window-title">SCP Database - Classified Access</div>
      <div class="window-controls">
        <button class="close-button">X</button>
      </div>
    `;

    const content = document.createElement('div');
    content.classList.add('window-content');
    // Updated content based on previous request
    content.innerHTML = `
      <div class="scp-interface">
        <div class="scp-header">
          <div class="scp-warning">CLASSIFIED LEVEL 3 - AUTHORIZED PERSONNEL ONLY</div>
          <div class="scp-identifier">SCP-██████████ - [REDACTED]</div>
        </div>

        <div class="scp-classification">
          <div class="classification-box">
            <span class="label">Item #:</span>
            <span class="value">SCP-██████████</span>
          </div>
          <div class="classification-box">
            <span class="label">Object Class:</span>
            <span class="value euclid">EUCLID</span>
          </div>
          <div class="classification-box">
            <span class="label">Containment:</span>
            <span class="value provisional">PROVISIONAL</span>
          </div>
        </div>

        <div class="scp-content">
          <div class="content-section">
            <h3>Special Containment Procedures:</h3>
            <p>SCP-██████████ is to be contained within a reinforced humanoid containment cell at Research Sector-██. Cell is to be equipped with constant surveillance. Any changes in behavior or vocalizations are to be immediately reported to the on-site security director.</p>
          </div>

          <div class="content-section">
            <h3>Description:</h3>
            <p>SCP-██████████ is a humanoid entinty that currently resides in <span class="redacted">████████████</span>. The entity has gained notoriety on the internet and displayed the power to see other <span class="redacted">████████████</span> throughout the universe. A holding site located in the North Atlantic Ocean (Latitude: 37.02806, Longitude: -30.54940, Distortion: 1.57) was prepared on <span class="redacted">████████████</span> to contain the entity. Currently the site is abandoned after a earthquake due to a seismic shifts damaged the holding equipment, although new containment procedures are currently being made they are not expected to finish until 2042. Most of the anomalous properties of SCP-██████████ do not effect others however, the possibility of a Great Convergence K-Class Scenario remains possible.</p>

            <p>SCP-██████████ has expressed insists that <span class="redacted">████████████ ████████████ ████████████</span> similar to a Great Convergence K-Class Scenario will occur. The entity is not hostile to most humans however it will retaliate if <span class="redacted">██████████████ ██████████████████ ██████████████ ████████████████</span></p>

            <p><span class="redacted">██████████ ██████████████████████████████████████████████████ ██████████████████████████████ ████████████████████ ████████████████████ ████████████████████ ████████████████████ ██████████</span></p>
          </div>
        </div>

        <div class="scp-footer">
          <div class="footer-warning">INFORMATION SECURITY NOTICE: Unauthorized access to this file will result in immediate administration of Class-B amnestics and review by the Ethics Committee.</div>
        </div>
      </div>
    `;

    windowElement.appendChild(header);
    windowElement.appendChild(content);

    const style = document.createElement('style');
    style.textContent = `
      .scp-interface {
        font-family: monospace;
        color: #0ff;
      }

      .scp-header {
        margin-bottom: 15px;
        border-bottom: 2px solid #0ff;
        padding-bottom: 10px;
      }

      .scp-warning {
        color: #f00;
        font-weight: bold;
        margin-bottom: 5px;
      }

      .scp-identifier {
        font-size: 1.4em;
        font-weight: bold;
      }

      .scp-classification {
        display: flex;
        gap: 15px;
        margin-bottom: 20px;
      }

      .classification-box {
        background: #111;
        border: 1px solid #0ff;
        padding: 5px 10px;
        display: flex;
        flex-direction: column;
        width: 30%;
      }

      .classification-box .label {
        font-size: 0.8em;
        color: #aaa;
      }

      .classification-box .value {
        font-size: 1.1em;
        font-weight: bold;
      }

      .euclid { /* Changed from keter */
        color: #f00; /* Still using red for Euclid, adjust if needed */
      }

      .provisional { /* Changed from uncontained */
        color: #f80;
      }

      .scp-content {
        background: #111;
        border: 1px solid #333;
        padding: 15px;
        margin-bottom: 15px;
        height: 300px; /* Adjust height as needed */
        overflow-y: auto;
      }

      .content-section {
        margin-bottom: 20px;
      }

      .content-section h3 {
        color: #0ff;
        margin-top: 0;
        border-bottom: 1px solid #333;
        padding-bottom: 5px;
      }

      .redacted {
        background-color: #000;
        color: #000;
        user-select: none; /* Prevent selection */
      }

      .scp-footer {
        font-size: 0.8em;
        text-align: center;
        color: #f00;
      }
    `;
    windowElement.appendChild(style);

    const closeButton = header.querySelector('.close-button');
    closeButton.addEventListener('click', () => {
      this.windowManager.closeWindow(windowElement);
      this.windowInstance = null;
    });

    return new Window(windowElement, this.windowManager);
  }
}
