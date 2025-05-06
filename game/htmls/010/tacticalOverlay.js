import { Window } from './window.js';

export class TacticalOverlayApp {
  constructor(windowManager) {
    this.windowManager = windowManager;
    this.windowInstance = null;
    this.mapSvg = null;
    // Updated unit names for consistency with DT9 and Nu-7 lore
    this.units = [
      { id: 'alpha_dt9', name: 'Alpha Squad (DT9)', type: 'infantry', position: { x: 650, y: 400 }, status: 'standby' }, // Near hangar
      { id: 'bravo_dt9', name: 'Bravo Squad (DT9)', type: 'infantry', position: { x: 680, y: 420 }, status: 'standby' }, // Near hangar 1
      { id: 'charlie_dt9', name: 'Charlie Squad (DT9)', type: 'infantry', position: { x: 150, y: 400 }, status: 'standby' }, // Near hangar 2
      { id: 'delta_dt9', name: 'Delta Squad (DT9)', type: 'infantry', position: { x: 710, y: 400 }, status: 'standby' }, // Near hangar 1
      { id: 'osprey_player', name: 'Osprey (Transport)', type: 'air', position: { x: 400, y: 250 }, status: 'landed' }, // On taxiway/apron
      { id: 'osprey_support', name: 'Osprey (Support)', type: 'air', position: { x: 480, y: 280 }, status: 'landed' }, // On apron
      { id: 'humvee_1', name: 'Humvee', type: 'vehicle', position: { x: 180, y: 160 }, status: 'standby' }, // Near control tower/JTF
      { id: 'echo_dt9', name: 'Echo Squad (DT9)', type: 'infantry', position: { x: 420, y: 320 }, status: 'standby' }, // Near apron
      { id: 'foxtrot_dt9', name: 'Foxtrot Squad (DT9)', type: 'infantry', position: { x: 450, y: 320 }, status: 'standby' }, // Near apron
      { id: 'logistics_truck', name: 'Logistics Truck', type: 'vehicle', position: { x: 620, y: 370 }, status: 'standby' }, // Near hangar 1
      { id: 'jtf_cmd', name: 'Nu-7 Command', type: 'command', position: { x: 150, y: 150 }, status: 'standby' } // Near control tower
    ];
  }

  open() {
    if (!this.windowInstance) {
      this.windowInstance = this.createWindow();
    }
    this.windowManager.openWindow(this.windowInstance);

    // Initialize the tactical map after the window opens
    setTimeout(() => {
      this.initializeMap();
      this.changeMapView('thermal'); // Default to thermal view
    }, 100);
  }

  createWindow() {
    const windowElement = document.createElement('div');
    windowElement.id = 'tactical-overlay-window';
    windowElement.classList.add('window');
    windowElement.style.width = '800px';
    windowElement.style.height = '600px';
    windowElement.style.top = '50px';
    windowElement.style.left = '200px';

    const header = document.createElement('div');
    header.classList.add('window-header');
    header.innerHTML = `
      <div class="window-title">Tactical Overlay - Fort Belvoir</div>
      <div class="window-controls">
        <button class="close-button">X</button>
      </div>
    `;

    const content = document.createElement('div');
    content.classList.add('window-content');
    content.innerHTML = `
      <div class="tactical-controls">
        <div class="map-filters">
          <button class="filter-button active" data-filter="all">All Units</button>
          <button class="filter-button" data-filter="infantry">Infantry</button>
          <button class="filter-button" data-filter="air">Air Support</button>
          <button class="filter-button" data-filter="command">Command</button>
          <button class="filter-button" data-filter="vehicle">Vehicles</button>
        </div>
        <div class="view-controls">
          <button class="view-button" data-view="satellite">Satellite (NV)</button>
          <button class="view-button" data-view="terrain">Terrain (NV)</button>
          <button class="view-button active" data-view="thermal">Thermal</button>
        </div>
      </div>

      <div class="tactical-map-container">
        <svg id="tactical-map" width="100%" height="100%"></svg>
      </div>

      <div class="unit-details-panel">
        <h4>Unit Details</h4>
        <div class="unit-details">
          <p>Select a unit to view details</p>
        </div>
      </div>
    `;

    windowElement.appendChild(header);
    windowElement.appendChild(content);

    // Close button functionality
    const closeButton = header.querySelector('.close-button');
    closeButton.addEventListener('click', () => {
      this.windowManager.closeWindow(windowElement);
      this.windowInstance = null;
    });

    // Filter buttons functionality
    const filterButtons = content.querySelectorAll('.filter-button');
    filterButtons.forEach(button => {
      button.addEventListener('click', (e) => {
        // Update active state
        filterButtons.forEach(btn => btn.classList.remove('active'));
        e.target.classList.add('active');

        // Apply filter
        const filter = e.target.dataset.filter;
        this.filterUnits(filter);
      });
    });

    // View buttons functionality
    const viewButtons = content.querySelectorAll('.view-button');
    viewButtons.forEach(button => {
      button.addEventListener('click', (e) => {
        // Update active state
        viewButtons.forEach(btn => btn.classList.remove('active'));
        e.target.classList.add('active');

        // Apply view change
        const view = e.target.dataset.view;
        this.changeMapView(view);
      });
    });

    return new Window(windowElement, this.windowManager);
  }

  initializeMap() {
    if (!this.windowInstance) return;

    const svg = this.windowInstance.windowElement.querySelector('#tactical-map');
    if (!svg) return;

    this.mapSvg = svg;

    // Clear any existing content
    svg.innerHTML = '';

    // Set SVG namespace
    const svgNS = 'http://www.w3.org/2000/svg';

    // Create terrain background
    const background = document.createElementNS(svgNS, 'rect');
    background.setAttribute('width', '100%');
    background.setAttribute('height', '100%');
    background.setAttribute('fill', '#282828'); // Dark grey tarmac color for night airfield
    svg.appendChild(background);

    // Create terrain features
    this.createTerrainFeatures(svg, svgNS);

    // Create grid lines
    this.createGridLines(svg, svgNS);

    // Add units to the map
    this.units.forEach(unit => {
      this.addUnitToMap(unit, svg, svgNS);
    });

    // Add event listener for unit selection
    svg.addEventListener('click', (e) => {
      const unitElement = e.target.closest('.unit-icon');
      if (unitElement) {
        const unitId = unitElement.dataset.unitId;
        const unit = this.units.find(u => u.id === unitId);
        if (unit) {
          this.showUnitDetails(unit);
        }
      }
    });
  }

  createTerrainFeatures(svg, svgNS) { // Replaced forest with airfield elements
    // Main Runway
    const runway = document.createElementNS(svgNS, 'rect');
    runway.setAttribute('x', '50');
    runway.setAttribute('y', '200');
    runway.setAttribute('width', '700');
    runway.setAttribute('height', '80');
    runway.setAttribute('fill', '#383838'); // Slightly lighter grey for runway
    runway.setAttribute('stroke', '#aaa');
    runway.setAttribute('stroke-width', '1');
    svg.appendChild(runway);

    // Runway Markings (Centerline)
    const centerline = document.createElementNS(svgNS, 'line');
    centerline.setAttribute('x1', '70');
    centerline.setAttribute('y1', '240');
    centerline.setAttribute('x2', '730');
    centerline.setAttribute('y2', '240');
    centerline.setAttribute('stroke', '#eee');
    centerline.setAttribute('stroke-width', '3');
    centerline.setAttribute('stroke-dasharray', '20, 15'); // Dashed line
    svg.appendChild(centerline);

    // Taxiways
    const taxiway1 = document.createElementNS(svgNS, 'rect');
    taxiway1.setAttribute('x', '350');
    taxiway1.setAttribute('y', '150');
    taxiway1.setAttribute('width', '50');
    taxiway1.setAttribute('height', '200'); // Connects runway to apron/hangars
    taxiway1.setAttribute('fill', '#303030');
    svg.appendChild(taxiway1);

    const taxiway2 = document.createElementNS(svgNS, 'rect');
    taxiway2.setAttribute('x', '550');
    taxiway2.setAttribute('y', '280'); // Connects runway to lower area
    taxiway2.setAttribute('width', '50');
    taxiway2.setAttribute('height', '100');
    taxiway2.setAttribute('fill', '#303030');
    svg.appendChild(taxiway2);

    // Hangars / Buildings
    const hangars = [
      { x: 600, y: 350, width: 150, height: 100 },
      { x: 100, y: 350, width: 120, height: 80 },
      { x: 450, y: 80, width: 100, height: 70 }
    ];

    hangars.forEach(h => {
      const hangar = document.createElementNS(svgNS, 'rect');
      hangar.setAttribute('x', h.x);
      hangar.setAttribute('y', h.y);
      hangar.setAttribute('width', h.width);
      hangar.setAttribute('height', h.height);
      hangar.setAttribute('fill', '#1a1a1a'); // Very dark grey for buildings
      hangar.setAttribute('stroke', '#555');
      hangar.setAttribute('stroke-width', '1');
      svg.appendChild(hangar);
    });

    // Control Tower
    const towerBase = document.createElementNS(svgNS, 'rect');
    towerBase.setAttribute('x', '140');
    towerBase.setAttribute('y', '140');
    towerBase.setAttribute('width', '30');
    towerBase.setAttribute('height', '30');
    towerBase.setAttribute('fill', '#1a1a1a');
    towerBase.setAttribute('stroke', '#555');
    svg.appendChild(towerBase);
    const towerTop = document.createElementNS(svgNS, 'circle');
    towerTop.setAttribute('cx', '155');
    towerTop.setAttribute('cy', '130'); // Slightly above base
    towerTop.setAttribute('r', '10');
    towerTop.setAttribute('fill', '#cc5'); // Command color for visual cue
    svg.appendChild(towerTop);

    // Apron Area (Parking/Staging)
    const apron = document.createElementNS(svgNS, 'rect');
    apron.setAttribute('x', '400'); // Connects to taxiway1
    apron.setAttribute('y', '150');
    apron.setAttribute('width', '200');
    apron.setAttribute('height', '200');
    apron.setAttribute('fill', '#2f2f2f'); // Slightly different grey
    svg.appendChild(apron);

    // Perimeter lights (optional decoration)
    for(let i = 0; i < 10; i++) {
        const light = document.createElementNS(svgNS, 'circle');
        light.setAttribute('cx', 50 + i * 75);
        light.setAttribute('cy', '40');
        light.setAttribute('r', '3');
        light.setAttribute('fill', '#ff0'); // Yellow lights
        light.setAttribute('opacity', '0.7');
        svg.appendChild(light);
        const light2 = document.createElementNS(svgNS, 'circle');
        light2.setAttribute('cx', 50 + i * 75);
        light2.setAttribute('cy', '560');
        light2.setAttribute('r', '3');
        light2.setAttribute('fill', '#ff0');
        light2.setAttribute('opacity', '0.7');
        svg.appendChild(light2);
    }
  }

  createGridLines(svg, svgNS) {
    const width = svg.clientWidth || 800;
    const height = svg.clientHeight || 600;
    const gridSize = 50;

    // Create grid group
    const gridGroup = document.createElementNS(svgNS, 'g');
    gridGroup.classList.add('grid-lines');

    // Horizontal lines
    for (let y = 0; y <= height; y += gridSize) {
      const line = document.createElementNS(svgNS, 'line');
      line.setAttribute('x1', '0');
      line.setAttribute('y1', y);
      line.setAttribute('x2', width);
      line.setAttribute('y2', y);
      line.setAttribute('stroke', 'rgba(100, 255, 100, 0.1)'); // Lighter green grid for night vision feel
      line.setAttribute('stroke-width', '1');
      gridGroup.appendChild(line);
    }

    // Vertical lines
    for (let x = 0; x <= width; x += gridSize) {
      const line = document.createElementNS(svgNS, 'line');
      line.setAttribute('x1', x);
      line.setAttribute('y1', '0');
      line.setAttribute('x2', x);
      line.setAttribute('y2', height);
      line.setAttribute('stroke', 'rgba(100, 255, 100, 0.1)'); // Lighter green grid
      line.setAttribute('stroke-width', '1');
      gridGroup.appendChild(line);
    }

    svg.appendChild(gridGroup);
  }

  addUnitToMap(unit, svg, svgNS) {
    const unitGroup = document.createElementNS(svgNS, 'g');
    unitGroup.classList.add('unit-icon');
    unitGroup.dataset.unitId = unit.id;
    unitGroup.dataset.unitType = unit.type;

    // Define colors for night view
    const infantryColor = '#3f3'; // Brighter green
    const airColor = '#5cc'; // Cyan
    const commandColor = '#cc5'; // Orange/Yellow
    const vehicleColor = '#aaa'; // Grey for vehicles
    const strokeColor = '#ccc'; // Light grey stroke

    // Different shapes/icons for different unit types
    if (unit.type === 'infantry') {
      const infantry = document.createElementNS(svgNS, 'rect');
      infantry.setAttribute('x', unit.position.x - 8);
      infantry.setAttribute('y', unit.position.y - 8);
      infantry.setAttribute('width', '16');
      infantry.setAttribute('height', '16');
      infantry.setAttribute('fill', infantryColor);
      infantry.setAttribute('stroke', strokeColor);
      infantry.setAttribute('stroke-width', '2');
      unitGroup.appendChild(infantry);
    } else if (unit.type === 'air') {
      const air = document.createElementNS(svgNS, 'polygon');
      air.setAttribute('points', `${unit.position.x},${unit.position.y - 10} ${unit.position.x + 10},${unit.position.y + 10} ${unit.position.x - 10},${unit.position.y + 10}`);
      air.setAttribute('fill', airColor);
      air.setAttribute('stroke', strokeColor);
      air.setAttribute('stroke-width', '2');
      unitGroup.appendChild(air);
    } else if (unit.type === 'command') {
      // Diamond shape for command units
      const command = document.createElementNS(svgNS, 'polygon');
      command.setAttribute('points', `
        ${unit.position.x},${unit.position.y - 12}
        ${unit.position.x + 12},${unit.position.y}
        ${unit.position.x},${unit.position.y + 12}
        ${unit.position.x - 12},${unit.position.y}`);
      command.setAttribute('fill', commandColor);
      command.setAttribute('stroke', strokeColor);
      command.setAttribute('stroke-width', '2');
      unitGroup.appendChild(command);
    } else if (unit.type === 'vehicle') {
      // Simple rectangle for ground vehicles
      const vehicle = document.createElementNS(svgNS, 'rect');
      vehicle.setAttribute('x', unit.position.x - 12);
      vehicle.setAttribute('y', unit.position.y - 6);
      vehicle.setAttribute('width', '24');
      vehicle.setAttribute('height', '12');
      vehicle.setAttribute('fill', vehicleColor);
      vehicle.setAttribute('stroke', strokeColor);
      vehicle.setAttribute('stroke-width', '1');
      unitGroup.appendChild(vehicle);
    }

    // Add unit name label
    const nameLabel = document.createElementNS(svgNS, 'text');
    nameLabel.setAttribute('x', unit.position.x);
    nameLabel.setAttribute('y', unit.position.y + 25);
    nameLabel.setAttribute('text-anchor', 'middle');
    nameLabel.setAttribute('fill', '#fff');
    nameLabel.setAttribute('font-size', '10'); // Slightly smaller font
    nameLabel.textContent = unit.name;
    unitGroup.appendChild(nameLabel);

    // Add status indicator
    let statusColor = '#ff0'; // Default yellow for standby
    if (unit.status === 'engaged') statusColor = '#f00'; // Red for engaged
    if (unit.status === 'moving') statusColor = '#0ff'; // Cyan for moving
    if (unit.status === 'landed') statusColor = '#aaa'; // Grey for landed
    if (unit.status === 'active') statusColor = '#0f0'; // Green for active (if needed later)

    const statusIndicator = document.createElementNS(svgNS, 'circle');
    statusIndicator.setAttribute('cx', unit.position.x + 15);
    statusIndicator.setAttribute('cy', unit.position.y - 15);
    statusIndicator.setAttribute('r', '5');
    statusIndicator.setAttribute('fill', statusColor);
    unitGroup.appendChild(statusIndicator);

    svg.appendChild(unitGroup);
  }

  showUnitDetails(unit) {
    if (!this.windowInstance) return;

    const detailsPanel = this.windowInstance.windowElement.querySelector('.unit-details');
    if (!detailsPanel) return;

    // Define status text and color
    let statusText, statusColor;
    switch(unit.status) {
      case 'active':
        statusText = 'Active';
        statusColor = '#0f0';
        break;
      case 'engaged':
        statusText = 'Engaged in Combat';
        statusColor = '#f00';
        break;
      case 'landed':
        statusText = 'Landed - Staging Area';
        statusColor = '#aaa';
        break;
      case 'standby':
        statusText = 'Standby - Awaiting Orders';
        statusColor = '#ff0';
        break;
      case 'moving':
        statusText = 'Moving';
        statusColor = '#0ff';
        break;
      default:
        statusText = unit.status;
        statusColor = '#fff';
    }

    detailsPanel.innerHTML = `
      <h3>${unit.name}</h3>
      <p><strong>Type:</strong> ${unit.type.charAt(0).toUpperCase() + unit.type.slice(1)}</p>
      <p><strong>Status:</strong> <span style="color: ${statusColor}">${statusText}</span></p>
      <p><strong>Position:</strong> ${unit.position.x}, ${unit.position.y}</p>
      <p>--- No Direct Control Available ---</p>
    `;
  }

  filterUnits(filter) {
    if (!this.mapSvg) return;

    const unitElements = this.mapSvg.querySelectorAll('.unit-icon');
    unitElements.forEach(unit => {
      if (filter === 'all' || unit.dataset.unitType === filter) {
        unit.style.display = '';
      } else {
        unit.style.display = 'none';
      }
    });
  }

  changeMapView(view) {
    if (!this.mapSvg) return;

    const background = this.mapSvg.querySelector('rect');
    if (!background) return;

    // Reset unit colors first
    const allUnitElements = this.mapSvg.querySelectorAll('.unit-icon');
    allUnitElements.forEach(unit => {
        const shape = unit.firstElementChild;
        if (shape) {
            // Use the night colors defined earlier
            let color = '#3f3'; // infantry
            if (unit.dataset.unitType === 'air') color = '#5cc';
            if (unit.dataset.unitType === 'command') color = '#cc5';
            if (unit.dataset.unitType === 'vehicle') color = '#aaa';

            shape.setAttribute('fill', color);
            shape.setAttribute('opacity', '1');
        }
    });


    switch(view) {
      case 'satellite':
        background.setAttribute('fill', '#111'); // Darker for satellite night view
        break; // Keep airfield structures visible
      case 'terrain':
        background.setAttribute('fill', '#282828'); // Dark grey tarmac for night terrain
        break; // Keep airfield structures visible
      case 'thermal':
        background.setAttribute('fill', '#001a33'); // Dark blue thermal background

        // Make units appear as heat signatures in thermal view
        const unitElementsThermal = this.mapSvg.querySelectorAll('.unit-icon');
        unitElementsThermal.forEach(unit => {
          const shape = unit.firstElementChild;
          if (shape) {
            let heatColor = '#f80'; // Default orange/yellow heat
            if (unit.dataset.unitType === 'infantry') heatColor = '#ff0'; // Yellow for infantry
            if (unit.dataset.unitType === 'air') heatColor = '#f40'; // Red/Orange for air (engines)
            if (unit.dataset.unitType === 'command') heatColor = '#fff'; // White hot for command?
            if (unit.dataset.unitType === 'vehicle') heatColor = '#f60'; // Orange for vehicles (engine heat)

            shape.setAttribute('fill', heatColor);
            shape.setAttribute('opacity', '0.9');
          }
        });
        break; // No need for early return now
    }
  }
}
