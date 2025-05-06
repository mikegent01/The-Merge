import { Window } from './window.js';

export class LaunchControlApp {
  constructor(windowManager, missileInventoryApp) {
    this.windowManager = windowManager;
    this.missileInventoryApp = missileInventoryApp; 
    this.windowInstance = null;
    this.launchCode = '786312';  
    this.launchedMissile = 'AIM-120 AMRAAM'; 
  }

  open() {
    if (!this.windowInstance) {
      this.windowInstance = this.createWindow();
    }
    this.windowManager.openWindow(this.windowInstance);
  }

  createTrajectoryAnimation() {
    const container = document.createElement('div');
    container.className = 'trajectory-container';

    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('viewBox', '0 0 1000 500');
    svg.classList.add('missile-trajectory');

    const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    const d = `M 50,450 Q 500,50 950,450`;
    path.setAttribute('d', d);
    path.classList.add('trajectory-path');

    svg.appendChild(path);

    const missile = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    missile.setAttribute('r', '10');
    missile.setAttribute('fill', '#f80');

    const animateMotion = document.createElementNS('http://www.w3.org/2000/svg', 'animateMotion');
    animateMotion.setAttribute('dur', '20s');
    animateMotion.setAttribute('fill', 'freeze');
    animateMotion.setAttribute('path', d);
    missile.appendChild(animateMotion);

    svg.appendChild(missile);
    container.appendChild(svg);
    return container;
  }

  createLaunchGraph() {
    const container = document.createElement('div');
    container.className = 'launch-graph-container';
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.classList.add('launch-graph');
    svg.setAttribute('viewBox', '0 0 400 150');

    const axes = document.createElementNS('http://www.w3.org/2000/svg', 'g');

    const xAxis = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    xAxis.setAttribute('x1', '50');
    xAxis.setAttribute('y1', '130');
    xAxis.setAttribute('x2', '350');
    xAxis.setAttribute('y2', '130');
    xAxis.setAttribute('stroke', '#888');
    xAxis.setAttribute('stroke-width', '2');
    axes.appendChild(xAxis);

    const yAxis = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    yAxis.setAttribute('x1', '50');
    yAxis.setAttribute('y1', '10');
    yAxis.setAttribute('x2', '50');
    yAxis.setAttribute('y2', '130');
    yAxis.setAttribute('stroke', '#888');
    yAxis.setAttribute('stroke-width', '2');
    axes.appendChild(yAxis);

    svg.appendChild(axes);

    const polyline = document.createElementNS('http://www.w3.org/2000/svg', 'polyline');
    polyline.setAttribute('points', '50,130 200,10 350,130');
    polyline.setAttribute('fill', 'none');
    polyline.setAttribute('stroke', '#f00');
    polyline.setAttribute('stroke-width', '2');
    polyline.setAttribute('stroke-dasharray', '400');
    polyline.setAttribute('stroke-dashoffset', '400');
    polyline.style.transition = 'stroke-dashoffset 5s ease-in-out';

    setTimeout(() => {
      polyline.setAttribute('stroke-dashoffset', '0');
    }, 500);

    svg.appendChild(polyline);
    container.appendChild(svg);
    return container;
  }

  simulateLaunch(content) {
    const launchStatus = content.querySelector('.launch-status');
    const trajectoryContainer = this.createTrajectoryAnimation();
    const launchGraph = this.createLaunchGraph();

    const launchControls = content.querySelector('.launch-controls');
    launchControls.appendChild(trajectoryContainer);
    launchControls.appendChild(launchGraph);

    setTimeout(() => {
      trajectoryContainer.querySelector('.missile-trajectory').classList.add('active');
      launchStatus.textContent = 'Missile launched successfully. Tracking trajectory...';
      if (this.missileInventoryApp) {
        this.missileInventoryApp.updateMissileStatus(this.launchedMissile, 'Launched'); 
      }
    }, 500);
  }

  createWindow() {
    const windowElement = document.createElement('div');
    windowElement.id = 'launch-control-window';
    windowElement.classList.add('window');
    windowElement.style.width = '600px';
    windowElement.style.height = '500px';
    windowElement.style.top = '80px';
    windowElement.style.left = '240px';

    const header = document.createElement('div');
    header.classList.add('window-header');
    header.innerHTML = `
      <div class="window-title">Launch Control System</div>
      <div class="window-controls">
        <button class="close-button">X</button>
      </div>
    `;

    const content = document.createElement('div');
    content.classList.add('window-content');
    content.innerHTML = `
      <h3>Launch Control System</h3>
      <div class="launch-controls">
        <div class="launch-status">System Ready</div>
        <input type="password" class="launch-code-input" placeholder="Enter launch code">
        <button class="launch-button">Initiate Launch</button>
      </div>
    `;

    windowElement.appendChild(header);
    windowElement.appendChild(content);

    const closeButton = header.querySelector('.close-button');
    closeButton.addEventListener('click', () => {
      this.windowManager.closeWindow(windowElement);
      this.windowInstance = null;
    });

    const launchButton = content.querySelector('.launch-button');
    const codeInput = content.querySelector('.launch-code-input');

    launchButton.addEventListener('click', () => {
      if (codeInput.value === this.launchCode) {
        if (confirm('WARNING: Missile launch sequence initiated. Confirm launch?')) {
          this.simulateLaunch(content);
        }
      } else {
        alert('Invalid launch code. Access denied.');
      }
    });

    return new Window(windowElement, this.windowManager);
  }
}