import { Window } from './window.js';

export class MissionBriefingApp {
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
    windowElement.id = 'mission-briefing-window';
    windowElement.classList.add('window');
    windowElement.style.width = '600px';
    windowElement.style.height = '500px'; 
    windowElement.style.top = '50px';
    windowElement.style.left = '50px';

    const header = document.createElement('div');
    header.classList.add('window-header');
    header.innerHTML = `
      <div class="window-title">Mission Briefing</div>
      <div class="window-controls">
        <button class="close-button">X</button>
      </div>
    `;

    const content = document.createElement('div');
    content.classList.add('window-content');
    content.innerHTML = `
      <h2>Operation White Pincer</h2>
      <h3>Phase 1: Secure</h3>
      <p>We are to secure the target located at ███████. The target is located on the top floor and is currently pending SCP designation. The target is to be secured using a specially designated anti-memetic sack currently stationed at the White Sands Base (declassified by ██████). The target is shown to be non-combative; however, the area around the target and its surroundings have been designated as hazardous, and it will be decided if this phenomenon should also be granted SCP status. Class █ amnestic pills have been requested and confirmed for this mission.</p>
      
      <h3>Phase 2: Contain</h3>
      <p>We are to contain the target and the entire state of █████. Due to the large number of people and the area affected by this event, it has been requested that ██████ ███████ ███████ ████ █████ █████ ████ ███ ████ ████████ ████ ██ ████ ██ ███ ██████ ██. (This part of the record has been requested to be redacted by ███ ██ ██████.)</p>
      
      <h3>Phase 3: Protect</h3>
      <p>We are setting up staging areas for the evacuation of high-profile personnel and civilians from the area. Depending on the success of the mission, we will determine when the designated time for each group to leave will be. Each person will be designated Class A, B, C, or D, and we will conduct 4 rounds of evacuations until all civilians have been evacuated. This process may last days or weeks after the target has been secured, but we cannot take any chances given the severity of the threat.</p>
      
      <!-- The existing audio player remains below -->
      <div class="audio-player">
        <button class="audio-play-button">► Play Briefing Audio</button>
        <div class="audio-waveform" style="display: none;">
          <svg width="200" height="50" viewBox="0 0 200 50">
            <rect x="0" y="20" width="5" height="10" fill="#0f0" class="bar bar1"/>
            <rect x="10" y="20" width="5" height="10" fill="#0f0" class="bar bar2"/>
            <rect x="20" y="20" width="5" height="10" fill="#0f0" class="bar bar3"/>
            <rect x="30" y="20" width="5" height="10" fill="#0f0" class="bar bar4"/>
            <rect x="40" y="20" width="5" height="10" fill="#0f0" class="bar bar5"/>
            <rect x="50" y="20" width="5" height="10" fill="#0f0" class="bar bar6"/>
            <rect x="60" y="20" width="5" height="10" fill="#0f0" class="bar bar7"/>
            <rect x="70" y="20" width="5" height="10" fill="#0f0" class="bar bar8"/>
            <rect x="80" y="20" width="5" height="10" fill="#0f0" class="bar bar9"/>
            <rect x="90" y="20" width="5" height="10" fill="#0f0" class="bar bar10"/>
          </svg>
        </div>
        <audio id="briefing-audio" src="CL4UJ9J4.wav"></audio>
      </div>
    `;

    windowElement.appendChild(header);
    windowElement.appendChild(content);

    const closeButton = header.querySelector('.close-button');
    closeButton.addEventListener('click', () => {
      this.windowManager.closeWindow(windowElement);
      this.windowInstance = null; 
    });

    const playButton = content.querySelector('.audio-play-button');
    const audioElement = content.querySelector('#briefing-audio');
    const waveformContainer = content.querySelector('.audio-waveform');
    let waveformInterval;

    playButton.addEventListener('click', () => {
      if (audioElement.paused) {
        audioElement.play();
        playButton.textContent = "❚❚ Pause Briefing Audio";
        waveformContainer.style.display = 'block';
        waveformContainer.classList.add('playing');
        waveformInterval = setInterval(() => {
          const bars = waveformContainer.querySelectorAll('.bar');
          bars.forEach(bar => {
            const newHeight = Math.floor(Math.random() * 16) + 5; // Random height between 5 and 20
            bar.setAttribute('height', newHeight);
            bar.setAttribute('y', 25 - newHeight/2);
          });
        }, 100);
      } else {
        audioElement.pause();
        playButton.textContent = "► Play Briefing Audio";
        waveformContainer.classList.remove('playing');
        waveformContainer.style.display = 'none';
        clearInterval(waveformInterval);
        const bars = waveformContainer.querySelectorAll('.bar');
        bars.forEach(bar => {
          bar.setAttribute('height', '10');
          bar.setAttribute('y', '20');
        });
      }
    });

    audioElement.addEventListener('ended', () => {
      playButton.textContent = "► Play Briefing Audio";
      waveformContainer.classList.remove('playing');
      waveformContainer.style.display = 'none';
      clearInterval(waveformInterval);
      const bars = waveformContainer.querySelectorAll('.bar');
      bars.forEach(bar => {
        bar.setAttribute('height', '10');
        bar.setAttribute('y', '20');
      });
    });

    return new Window(windowElement, this.windowManager);
  }
}