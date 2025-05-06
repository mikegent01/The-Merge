import { Window } from './window.js';

export class WeatherSystemApp {
  constructor(windowManager) {
    this.windowManager = windowManager;
    this.windowInstance = null;
    this.location = "Fort Belvoir, VA";
    this.currentWeather = {
      temperature: 72,
      condition: "Partly Cloudy",
      humidity: 45,
      windSpeed: 8,
      windDirection: "SW",
      pressure: 1015,
      visibility: 12,
    };
    this.forecast = [
      { day: "Today", high: 75, low: 58, condition: "Partly Cloudy" },
      { day: "Tomorrow", high: 77, low: 60, condition: "Mostly Sunny" },
      { day: "Wednesday", high: 80, low: 62, condition: "Sunny" },
      { day: "Thursday", high: 76, low: 59, condition: "Scattered Showers" },
      { day: "Friday", high: 72, low: 57, condition: "Partly Cloudy" }
    ];
    this.alerts = [
      { level: "low", message: "Training exercises may impact local traffic" },
      { level: "moderate", message: "UV index high between 11:00 and 15:00" }
    ];
    this.updateInterval = null;
  }

  open() {
    if (!this.windowInstance) {
      this.windowInstance = this.createWindow();
    }
    this.windowManager.openWindow(this.windowInstance);
    
    // Start auto-update of weather data
    this.startWeatherUpdates();
  }

  createWindow() {
    const windowElement = document.createElement('div');
    windowElement.id = 'weather-system-window';
    windowElement.classList.add('window');
    windowElement.style.width = '700px';
    windowElement.style.height = '500px';
    windowElement.style.top = '100px';
    windowElement.style.left = '180px';

    const header = document.createElement('div');
    header.classList.add('window-header');
    header.innerHTML = `
      <div class="window-title">Weather System</div>
      <div class="window-controls">
        <button class="close-button">X</button>
      </div>
    `;

    const content = document.createElement('div');
    content.classList.add('window-content');
    content.innerHTML = `
      <div class="weather-header">
        <h3>${this.location}</h3>
        <div class="location-selector">
          <select class="location-dropdown">
            <option value="Fort Belvoir, VA" selected>Fort Belvoir, VA</option>
            <option value="Pentagon, VA">Pentagon, VA</option>
            <option value="White Sands, NM">White Sands, NM</option>
            <option value="Quantico MCB, VA">Quantico MCB, VA</option>
          </select>
        </div>
      </div>
      
      <div class="weather-container">
        <div class="current-weather">
          <div class="weather-primary">
            <div class="weather-icon">
              ${this.getWeatherIcon(this.currentWeather.condition)}
            </div>
            <div class="temperature">${this.currentWeather.temperature}°F</div>
            <div class="condition">${this.currentWeather.condition}</div>
          </div>
          
          <div class="weather-details">
            <div class="detail-item">
              <div class="detail-label">Humidity</div>
              <div class="detail-value">${this.currentWeather.humidity}%</div>
            </div>
            <div class="detail-item">
              <div class="detail-label">Wind</div>
              <div class="detail-value">${this.currentWeather.windSpeed} mph ${this.currentWeather.windDirection}</div>
            </div>
            <div class="detail-item">
              <div class="detail-label">Pressure</div>
              <div class="detail-value">${this.currentWeather.pressure} hPa</div>
            </div>
            <div class="detail-item">
              <div class="detail-label">Visibility</div>
              <div class="detail-value">${this.currentWeather.visibility} miles</div>
            </div>
          </div>
        </div>
        
        <div class="forecast-container">
          <h4>5-Day Forecast</h4>
          <div class="forecast-grid">
            ${this.forecast.map(day => `
              <div class="forecast-day">
                <div class="forecast-date">${day.day}</div>
                <div class="forecast-icon">${this.getWeatherIcon(day.condition)}</div>
                <div class="forecast-temps">
                  <span class="high">${day.high}°</span>
                  <span class="low">${day.low}°</span>
                </div>
                <div class="forecast-condition">${day.condition}</div>
              </div>
            `).join('')}
          </div>
        </div>
        
        ${this.alerts.length > 0 ? `
          <div class="weather-alerts">
            <h4>Weather Alerts</h4>
            ${this.alerts.map(alert => `
              <div class="alert-item alert-${alert.level}">
                <div class="alert-icon">⚠️</div>
                <div class="alert-message">${alert.message}</div>
              </div>
            `).join('')}
          </div>
        ` : ''}
        
        <div class="weather-radar">
          <h4>Radar View</h4>
          <div class="radar-container">
            <svg viewBox="0 0 300 200" class="radar-svg">
         
       
              
              <circle cx="150" cy="100" r="95" fill="none" stroke="#0f0" stroke-width="1" />
              <circle cx="150" cy="100" r="65" fill="none" stroke="#0f0" stroke-width="1" />
              <circle cx="150" cy="100" r="35" fill="none" stroke="#0f0" stroke-width="1" />
              
              <line x1="150" y1="100" x2="245" y2="100" stroke="#0f0" stroke-width="2" class="radar-sweep">
                <!-- <animateTransform
                  attributeName="transform"
                  type="rotate"
                  from="0 150 100"
                  to="360 150 100"
                  dur="4s"
                  repeatCount="indefinite" /> -->
              </line>
              

              <circle cx="150" cy="100" r="5" fill="#f00"/>
            </svg>
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
      // Clear the interval when closing the window
      if (this.updateInterval) {
        clearInterval(this.updateInterval);
        this.updateInterval = null;
      }
    });

    // Location change handler
    const locationDropdown = content.querySelector('.location-dropdown');
    locationDropdown.addEventListener('change', (e) => {
      this.location = e.target.value;
      this.updateWeatherData();
    });

    return new Window(windowElement, this.windowManager);
  }
  
  getWeatherIcon(condition) {
    // Return appropriate icon based on weather condition
    switch(condition.toLowerCase()) {
      case 'sunny':
      case 'clear':
        return '';
      case 'partly cloudy':
        return '';
      case 'cloudy':
        return '';
      case 'rain':
        return '';
      case 'thunderstorm':
        return '';
      case 'snow':
        return '';
      case 'fog':
        return '';
      default:
        return '';
    }
  }
  
  startWeatherUpdates() {
    // Update weather every 30 seconds with slight variations
    this.updateInterval = setInterval(() => {
      this.updateWeatherData();
    }, 30000);
  }
  
  updateWeatherData() {
    if (!this.windowInstance) return;
    
    // Simulate weather changes based on location
    switch(this.location) {
      case 'Fort Belvoir, VA':
        this.currentWeather.temperature = Math.floor(72 + (Math.random() * 6));
        this.currentWeather.humidity = Math.floor(45 + (Math.random() * 5));
        this.currentWeather.condition = "Partly Cloudy";
        break;
      case 'Pentagon, VA':
        this.currentWeather.temperature = Math.floor(73 + (Math.random() * 4));
        this.currentWeather.humidity = Math.floor(48 + (Math.random() * 5));
        this.currentWeather.condition = "Mostly Sunny";
        break;
      case 'White Sands, NM':
        this.currentWeather.temperature = Math.floor(74 + (Math.random() * 7));
        this.currentWeather.humidity = Math.floor(50 + (Math.random() * 10));
        this.currentWeather.condition = "Partly Cloudy";
        break;
      case 'Quantico MCB, VA':
        this.currentWeather.temperature = Math.floor(71 + (Math.random() * 8));
        this.currentWeather.humidity = Math.floor(46 + (Math.random() * 10));
        this.currentWeather.condition = "Cloudy";
        break;
    }
    
    // Update wind and pressure with small variations
    this.currentWeather.windSpeed = Math.floor(8 + (Math.random() * 6));
    this.currentWeather.pressure = Math.floor(1010 + (Math.random() * 5));
    
    // Update the display
    const content = this.windowInstance.windowElement.querySelector('.window-content');
    if (!content) return;
    
    // Update location
    content.querySelector('.weather-header h3').textContent = this.location;
    
    // Update current weather
    content.querySelector('.temperature').textContent = `${this.currentWeather.temperature}°F`;
    content.querySelector('.condition').textContent = this.currentWeather.condition;
    content.querySelector('.weather-icon').innerHTML = this.getWeatherIcon(this.currentWeather.condition);
    
    // Update details
    const detailItems = content.querySelectorAll('.detail-value');
    detailItems[0].textContent = `${this.currentWeather.humidity}%`;
    detailItems[1].textContent = `${this.currentWeather.windSpeed} mph ${this.currentWeather.windDirection}`;
    detailItems[2].textContent = `${this.currentWeather.pressure} hPa`;
  }
}