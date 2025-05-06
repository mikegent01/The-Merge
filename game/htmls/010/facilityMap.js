import { Window } from './window.js';

export class FacilityMapApp {
  constructor(windowManager) {
    this.windowManager = windowManager;
    this.windowInstance = null;
    this.currentView = 'floor1'; // options: 'floor1', 'floor2', 'aerial'
  }

  open() {
    if (!this.windowInstance) {
      this.windowInstance = this.createWindow();
    }
    this.windowManager.openWindow(this.windowInstance);
    this.renderMap();
  }

  createWindow() {
    const windowElement = document.createElement('div');
    windowElement.id = 'facility-map-window';
    windowElement.classList.add('window');
    windowElement.style.width = '1000px';
    windowElement.style.height = '700px';
    windowElement.style.top = '80px';
    windowElement.style.left = '150px';

    const header = document.createElement('div');
    header.classList.add('window-header');
    header.innerHTML = `
      <div class="window-title">Facility Map - Fort Belvoir, Virginia</div>
      <div class="window-controls">
        <button class="close-button">X</button>
      </div>
    `;
    windowElement.appendChild(header);

    const content = document.createElement('div');
    content.classList.add('window-content');
    content.style.position = 'relative';
    content.style.overflow = 'auto';
    content.style.padding = '10px';

    // View Switch Controls
    const controls = document.createElement('div');
    controls.id = 'map-controls';
    controls.style.textAlign = 'center';
    controls.style.marginBottom = '10px';
    controls.innerHTML = `
      <button id="floor1-btn" class="control-button">Floor 1</button>
      <button id="floor2-btn" class="control-button">Floor 2</button>
      <button id="aerial-btn" class="control-button">Aerial View</button>
    `;
    content.appendChild(controls);

    // Map Container
    this.mapContainer = document.createElement('div');
    this.mapContainer.id = 'map-container';
    this.mapContainer.style.border = '2px solid #0ff';
    this.mapContainer.style.backgroundColor = '#000';
    this.mapContainer.style.borderRadius = '8px';
    this.mapContainer.style.margin = '0 auto';
    this.mapContainer.style.width = '90%';
    this.mapContainer.style.height = '500px';
    content.appendChild(this.mapContainer);

    // Room Info Panel
    this.roomInfo = document.createElement('div');
    this.roomInfo.id = 'room-info';
    this.roomInfo.style.marginTop = '10px';
    this.roomInfo.style.padding = '8px';
    this.roomInfo.style.backgroundColor = '#222';
    this.roomInfo.style.border = '1px solid #0ff';
    this.roomInfo.style.borderRadius = '4px';
    this.roomInfo.style.fontSize = '0.9em';
    this.roomInfo.textContent = 'Click on a room for details.';
    content.appendChild(this.roomInfo);

    windowElement.appendChild(content);

    // Close Button functionality
    const closeButton = header.querySelector('.close-button');
    closeButton.addEventListener('click', () => {
      this.windowManager.closeWindow(windowElement);
      this.windowInstance = null;
    });

    // Setup view switch events
    content.querySelector('#floor1-btn').addEventListener('click', () => {
      this.currentView = 'floor1';
      this.renderMap();
    });
    content.querySelector('#floor2-btn').addEventListener('click', () => {
      this.currentView = 'floor2';
      this.renderMap();
    });
    content.querySelector('#aerial-btn').addEventListener('click', () => {
      this.currentView = 'aerial';
      this.renderMap();
    });

    return new Window(windowElement, this.windowManager);
  }

  renderMap() {
    // Clear previous map content
    this.mapContainer.innerHTML = '';
    const svgNS = 'http://www.w3.org/2000/svg';
    const svg = document.createElementNS(svgNS, 'svg');
    svg.setAttribute('width', '100%');
    svg.setAttribute('height', '100%');
    svg.style.background = 'linear-gradient(135deg, #0a0a0a, #111)';

    if (this.currentView === 'floor1') {
      this.renderFloor1(svg);
    }
    else if (this.currentView === 'floor2') {
      this.renderFloor2(svg);
    }
    else if (this.currentView === 'aerial') {
      this.renderAerial(svg);
    }

    this.mapContainer.appendChild(svg);
  }

  renderFloor1(svg) {
    const svgNS = 'http://www.w3.org/2000/svg';

    // Define gradient for futuristic look
    const gradientDef = document.createElementNS(svgNS, 'defs');
    const mainGradient = document.createElementNS(svgNS, 'linearGradient');
    mainGradient.setAttribute('id', 'room-gradient');
    mainGradient.setAttribute('x1', '0%');
    mainGradient.setAttribute('y1', '0%');
    mainGradient.setAttribute('x2', '100%');
    mainGradient.setAttribute('y2', '100%');
    
    const stop1 = document.createElementNS(svgNS, 'stop');
    stop1.setAttribute('offset', '0%');
    stop1.setAttribute('stop-color', '#013');
    const stop2 = document.createElementNS(svgNS, 'stop');
    stop2.setAttribute('offset', '100%');
    stop2.setAttribute('stop-color', '#024');
    
    mainGradient.appendChild(stop1);
    mainGradient.appendChild(stop2);
    gradientDef.appendChild(mainGradient);
    svg.appendChild(gradientDef);

    // Main building outline
    const buildingOutline = document.createElementNS(svgNS, 'path');
    buildingOutline.setAttribute('d', 'M50,50 L850,50 L850,550 L50,550 Z');
    buildingOutline.setAttribute('fill', 'none');
    buildingOutline.setAttribute('stroke', '#0ff');
    buildingOutline.setAttribute('stroke-width', '3');
    buildingOutline.setAttribute('stroke-dasharray', '5,5');
    svg.appendChild(buildingOutline);

    // Command Center - hexagonal shape
    const commandCenter = document.createElementNS(svgNS, 'polygon');
    commandCenter.setAttribute('points', '150,150 250,100 350,150 350,250 250,300 150,250');
    commandCenter.setAttribute('fill', 'url(#room-gradient)');
    commandCenter.setAttribute('stroke', '#0ff');
    commandCenter.setAttribute('stroke-width', '2');
    commandCenter.style.cursor = 'pointer';
    commandCenter.addEventListener('click', () => {
      this.updateRoomInfo('Command Center', 'Primary operations control with holographic displays and advanced tactical systems.');
    });
    svg.appendChild(commandCenter);

    // Secure Server Room - with pulsing effect
    const serverRoom = document.createElementNS(svgNS, 'rect');
    serverRoom.setAttribute('x', '450');
    serverRoom.setAttribute('y', '100');
    serverRoom.setAttribute('width', '150');
    serverRoom.setAttribute('height', '150');
    serverRoom.setAttribute('fill', 'url(#room-gradient)');
    serverRoom.setAttribute('stroke', '#f0f');
    serverRoom.setAttribute('stroke-width', '2');
    serverRoom.classList.add('pulse-element');
    serverRoom.style.cursor = 'pointer';
    serverRoom.addEventListener('click', () => {
      this.updateRoomInfo('Secure Server Room', 'Houses quantum computers and classified data storage. Advanced cooling systems maintain optimal conditions.');
    });
    svg.appendChild(serverRoom);

    // Research Lab - circular shape
    const researchLab = document.createElementNS(svgNS, 'circle');
    researchLab.setAttribute('cx', '700');
    researchLab.setAttribute('cy', '175');
    researchLab.setAttribute('r', '75');
    researchLab.setAttribute('fill', 'url(#room-gradient)');
    researchLab.setAttribute('stroke', '#0f0');
    researchLab.setAttribute('stroke-width', '2');
    researchLab.style.cursor = 'pointer';
    researchLab.addEventListener('click', () => {
      this.updateRoomInfo('Research Laboratory', 'State-of-the-art facility for classified research projects and experimental technologies.');
    });
    svg.appendChild(researchLab);

    // Armory
    const armory = document.createElementNS(svgNS, 'rect');
    armory.setAttribute('x', '150');
    armory.setAttribute('y', '350');
    armory.setAttribute('width', '200');
    armory.setAttribute('height', '150');
    armory.setAttribute('fill', 'url(#room-gradient)');
    armory.setAttribute('stroke', '#f00');
    armory.setAttribute('stroke-width', '2');
    armory.style.cursor = 'pointer';
    armory.addEventListener('click', () => {
      this.updateRoomInfo('Armory', 'High-security weapons storage with biometric access controls and automated inventory systems.');
    });
    svg.appendChild(armory);

    // Communications Hub
    const commsHub = document.createElementNS(svgNS, 'polygon');
    commsHub.setAttribute('points', '450,350 600,350 550,500 400,500');
    commsHub.setAttribute('fill', 'url(#room-gradient)');
    commsHub.setAttribute('stroke', '#ff0');
    commsHub.setAttribute('stroke-width', '2');
    commsHub.style.cursor = 'pointer';
    commsHub.addEventListener('click', () => {
      this.updateRoomInfo('Communications Hub', 'Satellite and quantum-encrypted communications center with global reach capabilities.');
    });
    svg.appendChild(commsHub);

    // Medical Bay
    const medicalBay = document.createElementNS(svgNS, 'rect');
    medicalBay.setAttribute('x', '650');
    medicalBay.setAttribute('y', '350');
    medicalBay.setAttribute('width', '150');
    medicalBay.setAttribute('height', '150');
    medicalBay.setAttribute('rx', '20');
    medicalBay.setAttribute('ry', '20');
    medicalBay.setAttribute('fill', 'url(#room-gradient)');
    medicalBay.setAttribute('stroke', '#0ff');
    medicalBay.setAttribute('stroke-width', '2');
    medicalBay.style.cursor = 'pointer';
    medicalBay.addEventListener('click', () => {
      this.updateRoomInfo('Medical Bay', 'Advanced treatment facility with regenerative medicine capabilities and automated diagnostic systems.');
    });
    svg.appendChild(medicalBay);

    // Add some decorative elements
    for (let i = 0; i < 5; i++) {
      const decorCircle = document.createElementNS(svgNS, 'circle');
      decorCircle.setAttribute('cx', 50 + (i * 200));
      decorCircle.setAttribute('cy', 50);
      decorCircle.setAttribute('r', '5');
      decorCircle.setAttribute('fill', '#0ff');
      svg.appendChild(decorCircle);
    }

    // Add corridors
    const corridors = document.createElementNS(svgNS, 'path');
    corridors.setAttribute('d', 'M250,250 L450,250 M550,250 L700,250 M250,350 L450,350 M550,350 L650,350');
    corridors.setAttribute('stroke', '#0ff');
    corridors.setAttribute('stroke-width', '10');
    corridors.setAttribute('fill', 'none');
    corridors.setAttribute('stroke-linecap', 'round');
    svg.appendChild(corridors);
  }

  renderFloor2(svg) {
    const svgNS = 'http://www.w3.org/2000/svg';

    // Define gradient for futuristic look
    const gradientDef = document.createElementNS(svgNS, 'defs');
    const mainGradient = document.createElementNS(svgNS, 'linearGradient');
    mainGradient.setAttribute('id', 'room-gradient-f2');
    mainGradient.setAttribute('x1', '0%');
    mainGradient.setAttribute('y1', '0%');
    mainGradient.setAttribute('x2', '100%');
    mainGradient.setAttribute('y2', '100%');
    
    const stop1 = document.createElementNS(svgNS, 'stop');
    stop1.setAttribute('offset', '0%');
    stop1.setAttribute('stop-color', '#103');
    const stop2 = document.createElementNS(svgNS, 'stop');
    stop2.setAttribute('offset', '100%');
    stop2.setAttribute('stop-color', '#204');
    
    mainGradient.appendChild(stop1);
    mainGradient.appendChild(stop2);
    gradientDef.appendChild(mainGradient);
    svg.appendChild(gradientDef);

    // Main building outline
    const buildingOutline = document.createElementNS(svgNS, 'path');
    buildingOutline.setAttribute('d', 'M50,50 L850,50 L850,550 L50,550 Z');
    buildingOutline.setAttribute('fill', 'none');
    buildingOutline.setAttribute('stroke', '#0ff');
    buildingOutline.setAttribute('stroke-width', '3');
    buildingOutline.setAttribute('stroke-dasharray', '5,5');
    svg.appendChild(buildingOutline);

    // Briefing Room
    const briefingRoom = document.createElementNS(svgNS, 'rect');
    briefingRoom.setAttribute('x', '100');
    briefingRoom.setAttribute('y', '100');
    briefingRoom.setAttribute('width', '250');
    briefingRoom.setAttribute('height', '150');
    briefingRoom.setAttribute('rx', '15');
    briefingRoom.setAttribute('ry', '15');
    briefingRoom.setAttribute('fill', 'url(#room-gradient-f2)');
    briefingRoom.setAttribute('stroke', '#0ff');
    briefingRoom.setAttribute('stroke-width', '2');
    briefingRoom.style.cursor = 'pointer';
    briefingRoom.addEventListener('click', () => {
      this.updateRoomInfo('Briefing Room', 'Tactical planning center with 3D holographic terrain rendering and secure communications.');
    });
    svg.appendChild(briefingRoom);

    // Executive Offices
    const execOffices = document.createElementNS(svgNS, 'polygon');
    execOffices.setAttribute('points', '450,100 700,100 700,250 600,250 600,200 450,200');
    execOffices.setAttribute('fill', 'url(#room-gradient-f2)');
    execOffices.setAttribute('stroke', '#f80');
    execOffices.setAttribute('stroke-width', '2');
    execOffices.style.cursor = 'pointer';
    execOffices.addEventListener('click', () => {
      this.updateRoomInfo('Executive Offices', 'Command staff offices with enhanced security and private communications systems.');
    });
    svg.appendChild(execOffices);

    // Simulation Chamber
    const simChamber = document.createElementNS(svgNS, 'circle');
    simChamber.setAttribute('cx', '200');
    simChamber.setAttribute('cy', '350');
    simChamber.setAttribute('r', '100');
    simChamber.setAttribute('fill', 'url(#room-gradient-f2)');
    simChamber.setAttribute('stroke', '#f0f');
    simChamber.setAttribute('stroke-width', '2');
    simChamber.style.cursor = 'pointer';
    simChamber.addEventListener('click', () => {
      this.updateRoomInfo('Simulation Chamber', 'Virtual reality training facility with haptic feedback systems and combat scenario generation.');
    });
    svg.appendChild(simChamber);

    // Surveillance Center
    const survCenter = document.createElementNS(svgNS, 'rect');
    survCenter.setAttribute('x', '450');
    survCenter.setAttribute('y', '300');
    survCenter.setAttribute('width', '200');
    survCenter.setAttribute('height', '150');
    survCenter.setAttribute('fill', 'url(#room-gradient-f2)');
    survCenter.setAttribute('stroke', '#0f0');
    survCenter.setAttribute('stroke-width', '2');
    survCenter.style.cursor = 'pointer';
    survCenter.addEventListener('click', () => {
      this.updateRoomInfo('Surveillance Center', 'Advanced monitoring systems with AI-powered threat detection and facial recognition.');
    });
    svg.appendChild(survCenter);

    // Living Quarters
    const livingQuarters = document.createElementNS(svgNS, 'rect');
    livingQuarters.setAttribute('x', '700');
    livingQuarters.setAttribute('y', '300');
    livingQuarters.setAttribute('width', '100');
    livingQuarters.setAttribute('height', '200');
    livingQuarters.setAttribute('fill', 'url(#room-gradient-f2)');
    livingQuarters.setAttribute('stroke', '#ff0');
    livingQuarters.setAttribute('stroke-width', '2');
    livingQuarters.style.cursor = 'pointer';
    livingQuarters.addEventListener('click', () => {
      this.updateRoomInfo('Living Quarters', 'Residential area for on-site personnel with smart environmental controls and emergency protocols.');
    });
    svg.appendChild(livingQuarters);

    // Rec Area
    const recArea = document.createElementNS(svgNS, 'polygon');
    recArea.setAttribute('points', '400,500 650,500 650,450 550,450 500,400 400,400');
    recArea.setAttribute('fill', 'url(#room-gradient-f2)');
    recArea.setAttribute('stroke', '#0ff');
    recArea.setAttribute('stroke-width', '2');
    recArea.style.cursor = 'pointer';
    recArea.addEventListener('click', () => {
      this.updateRoomInfo('Recreation Area', 'Personnel relaxation zone with virtual environments and fitness monitoring systems.');
    });
    svg.appendChild(recArea);

    // Add corridors
    const corridors = document.createElementNS(svgNS, 'path');
    corridors.setAttribute('d', 'M350,175 L450,175 M350,350 L450,350 M650,350 L700,350');
    corridors.setAttribute('stroke', '#0ff');
    corridors.setAttribute('stroke-width', '10');
    corridors.setAttribute('fill', 'none');
    corridors.setAttribute('stroke-linecap', 'round');
    svg.appendChild(corridors);

    // Add some decorative elements
    for (let i = 0; i < 5; i++) {
      const decorCircle = document.createElementNS(svgNS, 'circle');
      decorCircle.setAttribute('cx', 50 + (i * 200));
      decorCircle.setAttribute('cy', 550);
      decorCircle.setAttribute('r', '5');
      decorCircle.setAttribute('fill', '#0ff');
      svg.appendChild(decorCircle);
    }
  }

  renderAerial(svg) {
    const svgNS = 'http://www.w3.org/2000/svg';

    // Define gradient for the base
    const gradientDef = document.createElementNS(svgNS, 'defs');
    
    const baseGradient = document.createElementNS(svgNS, 'radialGradient');
    baseGradient.setAttribute('id', 'base-gradient');
    baseGradient.setAttribute('cx', '50%');
    baseGradient.setAttribute('cy', '50%');
    baseGradient.setAttribute('r', '50%');
    
    const stop1 = document.createElementNS(svgNS, 'stop');
    stop1.setAttribute('offset', '0%');
    stop1.setAttribute('stop-color', '#024');
    const stop2 = document.createElementNS(svgNS, 'stop');
    stop2.setAttribute('offset', '100%');
    stop2.setAttribute('stop-color', '#002');
    
    baseGradient.appendChild(stop1);
    baseGradient.appendChild(stop2);
    gradientDef.appendChild(baseGradient);
    svg.appendChild(gradientDef);

    // Base perimeter - irregular shape for a military compound
    const basePerimeter = document.createElementNS(svgNS, 'path');
    basePerimeter.setAttribute('d', 'M100,100 L700,50 L800,300 L750,500 L400,550 L150,450 Z');
    basePerimeter.setAttribute('fill', 'url(#base-gradient)');
    basePerimeter.setAttribute('stroke', '#0ff');
    basePerimeter.setAttribute('stroke-width', '3');
    svg.appendChild(basePerimeter);

    // Main facility building
    const mainBuilding = document.createElementNS(svgNS, 'rect');
    mainBuilding.setAttribute('x', '300');
    mainBuilding.setAttribute('y', '200');
    mainBuilding.setAttribute('width', '200');
    mainBuilding.setAttribute('height', '150');
    mainBuilding.setAttribute('fill', '#036');
    mainBuilding.setAttribute('stroke', '#0ff');
    mainBuilding.setAttribute('stroke-width', '2');
    svg.appendChild(mainBuilding);

    // Secondary buildings
    const buildings = [
      {x: 200, y: 150, w: 80, h: 80},
      {x: 520, y: 200, w: 100, h: 80},
      {x: 350, y: 380, w: 120, h: 60},
      {x: 200, y: 350, w: 70, h: 70}
    ];
    
    buildings.forEach(b => {
      const building = document.createElementNS(svgNS, 'rect');
      building.setAttribute('x', b.x);
      building.setAttribute('y', b.y);
      building.setAttribute('width', b.w);
      building.setAttribute('height', b.h);
      building.setAttribute('fill', '#025');
      building.setAttribute('stroke', '#0ff');
      building.setAttribute('stroke-width', '1');
      svg.appendChild(building);
    });

    // Helicopter landing pads
    const helipad1 = document.createElementNS(svgNS, 'circle');
    helipad1.setAttribute('cx', '150');
    helipad1.setAttribute('cy', '250');
    helipad1.setAttribute('r', '30');
    helipad1.setAttribute('fill', '#111');
    helipad1.setAttribute('stroke', '#ff0');
    helipad1.setAttribute('stroke-width', '2');
    svg.appendChild(helipad1);
    
    const helipad2 = document.createElementNS(svgNS, 'circle');
    helipad2.setAttribute('cx', '600');
    helipad2.setAttribute('cy', '350');
    helipad2.setAttribute('r', '30');
    helipad2.setAttribute('fill', '#111');
    helipad2.setAttribute('stroke', '#ff0');
    helipad2.setAttribute('stroke-width', '2');
    svg.appendChild(helipad2);

    // Antenna/communications tower
    const antenna = document.createElementNS(svgNS, 'polygon');
    antenna.setAttribute('points', '650,150 670,150 660,50');
    antenna.setAttribute('fill', 'none');
    antenna.setAttribute('stroke', '#f0f');
    antenna.setAttribute('stroke-width', '2');
    svg.appendChild(antenna);
    
    const antennaBase = document.createElementNS(svgNS, 'rect');
    antennaBase.setAttribute('x', '645');
    antennaBase.setAttribute('y', '150');
    antennaBase.setAttribute('width', '30');
    antennaBase.setAttribute('height', '30');
    antennaBase.setAttribute('fill', '#025');
    antennaBase.setAttribute('stroke', '#f0f');
    antennaBase.setAttribute('stroke-width', '1');
    svg.appendChild(antennaBase);

    // Roads
    const roads = document.createElementNS(svgNS, 'path');
    roads.setAttribute('d', 'M100,300 L200,250 L300,250 L400,275 L500,275 L600,350 L750,500 M300,250 L200,350 L400,450');
    roads.setAttribute('fill', 'none');
    roads.setAttribute('stroke', '#333');
    roads.setAttribute('stroke-width', '15');
    roads.setAttribute('stroke-linecap', 'round');
    roads.setAttribute('stroke-linejoin', 'round');
    svg.appendChild(roads);

    // Perimeter fence indicators
    for (let i = 0; i < 20; i++) {
      const angle = (i / 20) * Math.PI * 2;
      const radius = 260 + Math.sin(i * 5) * 20;
      const x = 450 + Math.cos(angle) * radius;
      const y = 300 + Math.sin(angle) * radius;
      
      const fencePost = document.createElementNS(svgNS, 'circle');
      fencePost.setAttribute('cx', x);
      fencePost.setAttribute('cy', y);
      fencePost.setAttribute('r', '2');
      fencePost.setAttribute('fill', '#f00');
      svg.appendChild(fencePost);
    }

    // Map title
    const mapTitle = document.createElementNS(svgNS, 'text');
    mapTitle.setAttribute('x', '450');
    mapTitle.setAttribute('y', '80');
    mapTitle.setAttribute('text-anchor', 'middle');
    mapTitle.setAttribute('fill', '#0ff');
    mapTitle.setAttribute('font-size', '24');
    mapTitle.setAttribute('font-family', 'monospace');
    mapTitle.textContent = 'FORT BELVOIR - VIRGINIA';
    svg.appendChild(mapTitle);

    // North indicator
    const northArrow = document.createElementNS(svgNS, 'polygon');
    northArrow.setAttribute('points', '750,100 770,130 750,120 730,130');
    northArrow.setAttribute('fill', '#0ff');
    svg.appendChild(northArrow);
    
    const northLabel = document.createElementNS(svgNS, 'text');
    northLabel.setAttribute('x', '750');
    northLabel.setAttribute('y', '150');
    northLabel.setAttribute('text-anchor', 'middle');
    northLabel.setAttribute('fill', '#0ff');
    northLabel.setAttribute('font-size', '18');
    northLabel.setAttribute('font-family', 'monospace');
    northLabel.textContent = 'N';
    svg.appendChild(northLabel);
  }

  updateRoomInfo(name, description) {
    if (this.roomInfo) {
      this.roomInfo.innerHTML = `<strong>${name}:</strong> ${description}`;
    }
  }
}