import { Window } from './window.js';

export class PersonnelDatabaseApp {
  constructor(windowManager) {
    this.windowManager = windowManager;
    this.windowInstance = null;
    // Updated personnel list
    this.personnel = [
      // Division 1 DT9
      {
        id: 'DT9-001',
        name: 'Lt. Harry',
        rank: 'Lieutenant',
        division: 'Tactical (DT9 Command)',
        clearance: 'Beta',
        status: 'Active',
        specialty: 'Field Command',
        //photo: '👨‍✈️'
      },
      {
        id: 'DT9-002',
        name: 'Drill Sgt. J.J. R. Jones',
        rank: 'Drill Sergeant',
        division: 'Tactical (DT9 Training)',
        clearance: 'Beta',
        status: 'Active',
        specialty: 'Personnel Training',
        //photo: '👮‍♂️'
      },
      {
        id: 'DT9-003',
        name: 'Eric', // Was 3rd in importance
        rank: 'Sergeant',
        division: 'Tactical (DT9)',
        clearance: 'Gamma',
        status: 'Active',
        specialty: 'Field Operations',
        //photo: '👩‍✈️'
      },
      {
        id: 'DT9-004',
        name: '"Bagman" (Joe Curtus)', // Was 4th
        rank: 'Corporal',
        division: 'Tactical (DT9)',
        clearance: 'Gamma',
        status: 'Active',
        specialty: 'The keyholder',
        //photo: '❓'
      },
      {
        id: 'DT9-005',
        name: 'Benjamin', // Was 5th 
        rank: 'Private First Class',
        division: 'Tactical (DT9)',
        clearance: 'Gamma',
        status: 'Active',
        specialty: 'Artillery Specialist',
        //photo: '👨‍✈️'
      },
      {
        id: 'DT9-006',
        name: 'David', // Was 6th
        rank: 'Private',
        division: 'Tactical (DT9)',
        clearance: 'Gamma',
        status: 'Active',
        specialty: 'Artillery Support',
        //photo: '👨‍✈️'
      },
      {
        id: 'DT9-007',
        name: 'Emma S. (Researcher)',
        rank: 'Researcher',
        division: 'Research (Deceased)',
        clearance: 'Beta',
        status: 'Deceased',
        specialty: 'Expermintal Weapons Studies',
        //photo: '👤'
      },
      {
        id: 'DT9-008',
        name: 'Emma S.', // Placeholder name
        rank: 'Civilian', // Assuming
        division: 'Civilian', // Assuming
        clearance: 'None',
        status: 'Active',
        specialty: 'Handling of anomalous materials',
        //photo: '👩'
      },
      // Division 2 DT10
      {
        id: 'DT10-001',
        name: 'Lt. Barry',
        rank: 'Lieutenant',
        division: 'Tactical (DT10 Command)',
        clearance: 'Beta',
        status: 'Active',
        specialty: 'Field Command',
        //photo: '👨‍✈️'
      },
      {
        id: 'DT10-002',
        name: 'Samuel', // Was 2nd in importance for DT10
        rank: 'Sergeant',
        division: 'Tactical (DT10)',
        clearance: 'Gamma',
        status: 'Active',
        specialty: 'Demolition Expert',
        //photo: '👨‍✈️'
      },
      {
        id: 'DT10-003',
        name: 'Garrad', // Was 3rd
        rank: 'Corporal',
        division: 'Tactical (DT10)',
        clearance: 'Gamma',
        status: 'Active',
        specialty: 'Engineer',
        //photo: '👨‍✈️'
      },
      {
        id: 'DT10-004',
        name: 'Poe', // Was 4th
        rank: 'Private First Class',
        division: 'Tactical (DT10)',
        clearance: 'Gamma',
        status: 'Active',
        specialty: 'Marksman',
        //photo: '👨‍✈️'
      },
      {
        id: 'DT10-005',
        name: 'Lian', // Was 5th
        rank: 'Private',
        division: 'Tactical (DT10)',
        clearance: 'Gamma',
        status: 'Active',
        specialty: 'Field Operations',
        //photo: '👩‍✈️'
      },
      // Civil Personnel
      { id: 'CIV-001', name: 'Dan', rank: 'Civilian', division: 'Civilian', clearance: 'None', status: 'Active', specialty: 'N/A'},
      { id: 'CIV-002', name: 'John', rank: 'Civilian', division: 'Civilian', clearance: 'None', status: 'Active', specialty: 'N/A'},
      { id: 'CIV-003', name: 'Cranton', rank: 'Civilian', division: 'Civilian', clearance: 'None', status: 'Active', specialty: 'N/A'},
      { id: 'CIV-004', name: 'Liam', rank: 'Civilian', division: 'Civilian', clearance: 'None', status: 'Active', specialty: 'N/A'},
      { id: 'CIV-005', name: 'Rick', rank: 'Civilian', division: 'Civilian', clearance: 'None', status: 'Active', specialty: 'N/A'},
      { id: 'CIV-006', name: 'Joseph', rank: 'Civilian', division: 'Civilian', clearance: 'None', status: 'Active', specialty: 'N/A'},
      { id: 'CIV-007', name: 'Sayo', rank: 'Civilian', division: 'Civilian', clearance: 'None', status: 'Active', specialty: 'N/A'}
    ];
    this.selectedPerson = null;
  }

  open() {
    if (!this.windowInstance) {
      this.windowInstance = this.createWindow();
    }
    this.windowManager.openWindow(this.windowInstance);
  }

  createWindow() {
    const windowElement = document.createElement('div');
    windowElement.id = 'personnel-database-window';
    windowElement.classList.add('window');
    windowElement.style.width = '800px';
    windowElement.style.height = '600px';
    windowElement.style.top = '80px';
    windowElement.style.left = '250px';

    const header = document.createElement('div');
    header.classList.add('window-header');
    header.innerHTML = `
      <div class="window-title">Personnel Database</div>
      <div class="window-controls">
        <button class="close-button">X</button>
      </div>
    `;

    const content = document.createElement('div');
    content.classList.add('window-content');
    content.style.display = 'flex';
    content.style.flexDirection = 'column';
    content.innerHTML = `
      <div class="search-bar">
        <input type="text" placeholder="Search personnel..." class="personnel-search">
        <button class="search-button">Search</button>
        <div class="filter-dropdown">
          <select class="division-filter">
            <option value="all">All Divisions</option>
            <option value="Command">Command</option>
            <option value="Tactical">Tactical</option>
            <option value="Research">Research</option>
            <option value="Security">Security</option>
            <option value="Training Command">Training</option>
            <option value="Civilian">Civilian</option> 
          </select>
        </div>
      </div>
      
      <div class="personnel-container">
        <div class="personnel-list">
          <table class="personnel-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Rank</th>
                <th>Division</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody id="personnel-table-body">
              <!-- Personnel rows will be dynamically populated -->
            </tbody>
          </table>
        </div>
        
        <div class="personnel-details">
          <div class="details-placeholder">
            <p>Select personnel to view details</p>
          </div>
          <div class="details-content" style="display: none;">
            <!-- Content will be dynamically populated -->
          </div>
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

    // Populate and setup interactions
    this.populatePersonnelTable(content);
    // Search functionality
    const searchInput = content.querySelector('.personnel-search');
    const searchButton = content.querySelector('.search-button');
    
    const handleSearch = () => {
      const searchTerm = searchInput.value.toLowerCase();
      const divisionFilter = content.querySelector('.division-filter').value;
      
      content.querySelectorAll('.personnel-row').forEach(row => {
        const personId = row.dataset.id;
        const person = this.personnel.find(p => p.id === personId);
        
        // Check if matches search term and division filter
        const nameMatch = person.name.toLowerCase().includes(searchTerm);
        const idMatch = person.id.toLowerCase().includes(searchTerm);
        const rankMatch = person.rank.toLowerCase().includes(searchTerm);
        // Handle potentially more specific division names like "Tactical (DT9)"
        const divisionMatch = divisionFilter === 'all' 
                              || person.division === divisionFilter 
                              || person.division.startsWith(divisionFilter + ' (');
        
        if ((nameMatch || idMatch || rankMatch) && divisionMatch) {
          row.style.display = '';
        } else {
          row.style.display = 'none';
        }
      });
    };
    
    searchButton.addEventListener('click', handleSearch);
    searchInput.addEventListener('keyup', e => {
      if (e.key === 'Enter') handleSearch();
    });
    
    // Division filter
    content.querySelector('.division-filter').addEventListener('change', handleSearch);

    return new Window(windowElement, this.windowManager);
  }

  populatePersonnelTable(contentElement) {
    const tableBody = contentElement.querySelector('#personnel-table-body');
    tableBody.innerHTML = ''; // Clear existing rows

    this.personnel.forEach(person => {
      const row = document.createElement('tr');
      row.classList.add('personnel-row');
      row.dataset.id = person.id;
      row.innerHTML = `
        <td>${person.id}</td>
        <td>${person.name}</td>
        <td>${person.rank}</td>
        <td>${person.division}</td>
        <td><span class="status-indicator ${person.status.toLowerCase().replace(' ', '-')}">${person.status}</span></td>
      `;

      row.addEventListener('click', () => {
        // Update selected row highlight
        tableBody.querySelectorAll('.personnel-row').forEach(r => r.classList.remove('selected'));
        row.classList.add('selected');
        
        // Show person details
        this.showPersonDetails(person, contentElement);
      });
      tableBody.appendChild(row);
    });
  }

  showPersonDetails(person, contentElement) {
    const detailsPlaceholder = contentElement.querySelector('.details-placeholder');
    const detailsContent = contentElement.querySelector('.details-content');
    
    detailsPlaceholder.style.display = 'none';
    detailsContent.style.display = 'block';
    
    detailsContent.innerHTML = `
      <div class="person-header">
        <div class="person-name-title">
          <h3>${person.name}</h3>
          <div class="person-title">${person.rank} - ${person.division} Division</div>
        </div>
      </div>
      
      <div class="person-details-grid">
        <div class="detail-item">
          <div class="detail-label">ID Number</div>
          <div class="detail-value">${person.id}</div>
        </div>
        <div class="detail-item">
          <div class="detail-label">Clearance Level</div>
          <div class="detail-value clearance-${person.clearance.toLowerCase()}">${person.clearance}</div>
        </div>
        <div class="detail-item">
          <div class="detail-label">Current Status</div>
          <div class="detail-value">${person.status}</div>
        </div>
        <div class="detail-item">
          <div class="detail-label">Specialty</div>
          <div class="detail-value">${person.specialty}</div>
        </div>
      </div>
      

      
      <div class="security-note">
        <div class="note-header">SECURITY NOTE</div>
        <div class="note-content">
          Personnel information classified under Military Protocol 7-B. 
          Unauthorized access or distribution is punishable under Article 15, UCMJ.
        </div>
      </div>
    `;
    
    // Add event listeners to action buttons
    const actionButtons = detailsContent.querySelectorAll('.action-button');
    actionButtons.forEach(button => {
      button.addEventListener('click', () => {
        alert(`Action "${button.textContent}" on ${person.name} requires higher clearance.`);
      });
    });
  }
}