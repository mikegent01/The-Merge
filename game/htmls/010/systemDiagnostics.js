import { Window } from './window.js';

export class SystemDiagnosticsApp {
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
    windowElement.id = 'system-diagnostics-window';
    windowElement.classList.add('window');
    windowElement.style.width = '400px';
    windowElement.style.height = '300px';
    windowElement.style.top = '150px';
    windowElement.style.left = '150px';

    const header = document.createElement('div');
    header.classList.add('window-header');
    header.innerHTML = `
      <div class="window-title">System Diagnostics</div>
      <div class="window-controls">
        <button class="close-button">X</button>
      </div>
    `;

    const content = document.createElement('div');
    content.classList.add('window-content');
    content.innerHTML = `
      <h3>System Status: <span id="system-status">Nominal</span></h3>
      <p><strong>CPU Load:</strong> <span id="cpu-load">12%</span></p>
      <p><strong>Memory Usage:</strong> <span id="memory-usage">28%</span></p>
      <p><strong>Network Latency:</strong> <span id="network-latency">12ms</span></p>
    `;

    windowElement.appendChild(header);
    windowElement.appendChild(content);

    const closeButton = header.querySelector('.close-button');
    closeButton.addEventListener('click', () => {
      this.windowManager.closeWindow(windowElement);
      this.windowInstance = null;
    });

    // Simulate system diagnostics update with more stable numbers
    setInterval(() => {
      const cpuBase = 12;
      const memBase = 28;
      const variation = 2;

      const cpuLoad = cpuBase + (Math.random() * variation);
      const memoryUsage = memBase + (Math.random() * variation);
      const networkLatency = Math.floor(10 + (Math.random() * 4));

      content.querySelector('#cpu-load').textContent = `${cpuLoad.toFixed(1)}%`;
      content.querySelector('#memory-usage').textContent = `${memoryUsage.toFixed(1)}%`;
      content.querySelector('#network-latency').textContent = `${networkLatency}ms`;

      content.querySelector('#system-status').textContent = 'Nominal';
      content.querySelector('#system-status').style.color = 'green';
    }, 2000);

    return new Window(windowElement, this.windowManager);
  }
}