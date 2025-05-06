// Main script initialization
import { MissionBriefingApp } from './010/missionBriefing.js';
import { SCPDatabaseApp } from './010/scpDatabase.js';
import { SystemDiagnosticsApp } from './010/systemDiagnostics.js';
import { FacilityMapApp } from './010/facilityMap.js';
import { VehicleInventoryApp } from './010/vehicleInventory.js';
import { MissileInventoryApp } from './010/missileInventory.js';
import { LaunchControlApp } from './010/launchControl.js';
import { NewsApp } from './010/newsApp.js';
import { WindowManager } from './010/windowManager.js';
import { WifiSystemApp } from './010/wifiSystem.js';
import { TacticalOverlayApp } from './010/tacticalOverlay.js';
import { PersonnelDatabaseApp } from './010/personnelDatabase.js';
import { WeatherSystemApp } from './010/weatherSystem.js';

document.addEventListener('DOMContentLoaded', () => {
  // Initialize Clock
  function updateClock() {
    const now = new Date();
    const timeString = now.toLocaleTimeString('en-US', { hour12: false });
    document.getElementById('system-time').textContent = timeString;
  }
  updateClock();
  setInterval(updateClock, 1000);

  // Initialize Window Manager
  const windowsContainer = document.getElementById('windows-container');
  const windowManager = new WindowManager(windowsContainer);

  // Initialize Applications
  const missionBriefingApp = new MissionBriefingApp(windowManager);
  const scpDatabaseApp = new SCPDatabaseApp(windowManager);
  const systemDiagnosticsApp = new SystemDiagnosticsApp(windowManager);
  const facilityMapApp = new FacilityMapApp(windowManager);
  const vehicleInventoryApp = new VehicleInventoryApp(windowManager);
  const missileInventoryApp = new MissileInventoryApp(windowManager);
  const launchControlApp = new LaunchControlApp(windowManager, missileInventoryApp);
  const wifiSystemApp = new WifiSystemApp(windowManager);
  const tacticalOverlayApp = new TacticalOverlayApp(windowManager);
  const personnelDatabaseApp = new PersonnelDatabaseApp(windowManager);
  const weatherSystemApp = new WeatherSystemApp(windowManager);
  const newsApp = new NewsApp(windowManager);

  // Taskbar Icon Functionality
  const taskbarIcons = document.querySelectorAll('.taskbar-icon');
  taskbarIcons.forEach(icon => {
    icon.addEventListener('click', () => {
      const appName = icon.dataset.app;
      switch (appName) {
        case 'mission-briefing':
          missionBriefingApp.open();
          break;
        case 'scp-database':
          scpDatabaseApp.open();
          break;
        case 'system-diagnostics':
          systemDiagnosticsApp.open();
          break;
        case 'facility-map':
          facilityMapApp.open();
          break;
        case 'vehicle-inventory':
          vehicleInventoryApp.open();
          break;
        case 'missile-inventory':
          missileInventoryApp.open();
          break;
        case 'launch-control':
          launchControlApp.open();
          break;
        case 'wifi-system':
          wifiSystemApp.open();
          break;
        case 'tactical-overlay':
          tacticalOverlayApp.open();
          break;
        case 'personnel-database':
          personnelDatabaseApp.open();
          break;
        case 'weather-system':
          weatherSystemApp.open();
          break;
        case 'news':
          newsApp.open();
          break;
      }
    });
  });

  // Logout Button
  const logoutButton = document.getElementById('logout-button');
  logoutButton.addEventListener('click', () => {
    window.location.href = '010l.html';
  });
});