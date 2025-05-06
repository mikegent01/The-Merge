import { Window } from './window.js';

export class NewsApp {
  constructor(windowManager) {
    this.windowManager = windowManager;
    this.windowInstance = null;
    this.articleUpdateInterval = null;
    this.currentArticle = {
      headline: "Breaking: Unidentified Phenomena Persist",
      date: new Date().toLocaleString(),
      content: "In an ongoing crisis, state authorities continue to investigate the mysterious events unfolding across the nation. Residents report strange beams of light emanating from the ground accompanied by inexplicable phenomena that defy conventional explanation. 'I've never seen anything like it,' said one local resident, describing the eerie silence following the mysterious appearance.\n\nIn an exclusive interview, Dr. Elaine Carter, a theoretical physicist, provided further insight into the anomalies. 'The data we're collecting suggests that these phenomena could be linked to alternate dimensions,' Dr. Carter explained. 'While it's too early to draw definitive conclusions, the implications are profound and warrant further investigation.'\n\nGovernment officials have urged the public to remain calm and report any unusual activity. As the situation develops, stay tuned for further updates on this breaking news story."
    };
    this.articleElement = null;
    
    // Custom news content based on URL parameters
    this.customNewsContent = {
      'keepsamuel': {
        headline: "ALERT: Operation Safeguard Activated For Samuel Preservation",
        content: "TOP PRIORITY: All personnel are instructed to implement Protocol 7-B regarding asset 'Samuel'. Intelligence reports indicate heightened risk level. Multiple extraction teams have been dispatched to secure the asset's location.\n\nLt. Colonel Richards stated in today's briefing: 'The preservation of asset Samuel is critical to national security. We're allocating all necessary resources to ensure continuity of protection.'\n\nAll field agents must report any unusual activity through secure channel Delta-9. Maintain radio silence unless absolutely necessary. This situation has been classified as Code Yellow - all standard operating procedures apply."
      },
      // Additional custom content for other potential URL parameters
      'alphasite': {
        headline: "UPDATE: Alpha Site Perimeter Breach Contained",
        content: "Security teams have successfully contained a perimeter breach at Alpha Site facility. Initial reports indicate no data compromise or asset exposure occurred during the incident.\n\nFacility Director Dr. Helen Reeves commented: 'Our response protocols functioned exactly as designed. The breach was identified, isolated, and neutralized within acceptable parameters. A full review of security measures is underway.'\n\nAll personnel are reminded to maintain heightened vigilance and report any suspicious activity immediately. Temporary access restrictions remain in place for sectors 7 through 12 until further notice."
      },
      'convergence': {
        headline: "CRITICAL: Possible K-Class Convergence Scenario Developing",
        content: "ATTENTION ALL PERSONNEL: Monitoring stations have detected energy signatures consistent with the early phases of a K-Class Convergence Scenario. Initial containment measures have been deployed while assessment continues.\n\nDr. Marcus Wei from Theoretical Analysis stated during emergency briefing: 'While preliminary, the data patterns show concerning similarities to the 2019 Incident. We're analyzing incoming telemetry to determine appropriate escalation responses.'\n\nAll non-essential operations are suspended. Essential personnel must report to designated safe zones immediately. This is not a drill."
      }
    };
    
    // Initialize with URL parameters if available
    this.checkUrlParameters();
  }
  
  checkUrlParameters() {
    // Parse URL parameters for news customization
    const urlParams = new URLSearchParams(window.location.search);
    const lastLabel = urlParams.get('lastLabel');
    if (lastLabel && this.customNewsContent[lastLabel]) {
      this.currentArticle.headline = this.customNewsContent[lastLabel].headline;
      this.currentArticle.date = new Date().toLocaleString();
      this.currentArticle.content = this.customNewsContent[lastLabel].content;
      
      // Also update localStorage for the dedicated page
      localStorage.setItem('currentArticle', JSON.stringify({
        headline: this.currentArticle.headline,
        date: this.currentArticle.date,
        fullContent: this.currentArticle.content
      }));
    }
  }
  
  customizeNewsForLabel(label) {
    if (this.customNewsContent[label]) {
      this.currentArticle.headline = this.customNewsContent[label].headline;
      this.currentArticle.date = new Date().toLocaleString();
      this.currentArticle.content = this.customNewsContent[label].content;
      this.renderArticle();
      
      // Also update localStorage for the dedicated page
      localStorage.setItem('currentArticle', JSON.stringify({
        headline: this.currentArticle.headline,
        date: this.currentArticle.date,
        fullContent: this.currentArticle.content
      }));
    }
  }

  open() {
    if (!this.windowInstance) {
      this.windowInstance = this.createWindow();
    }
    this.windowManager.openWindow(this.windowInstance);
    // Initialize the news feed
    this.updateNews();
  }

  createWindow() {
    const windowElement = document.createElement('div');
    windowElement.id = 'news-window';
    windowElement.classList.add('window');
    windowElement.style.width = '800px';
    windowElement.style.height = '600px';
    windowElement.style.top = '120px';
    windowElement.style.left = '300px';

    const header = document.createElement('div');
    header.classList.add('window-header');
    header.innerHTML = `
      <div class="window-title">Latest Military & News</div>
      <div class="window-controls">
        <button class="close-button">X</button>
      </div>
    `;

    const content = document.createElement('div');
    content.classList.add('window-content');
    content.innerHTML = `
      <div id="news-feed"></div>
    `;

    windowElement.appendChild(header);
    windowElement.appendChild(content);

    const closeButton = header.querySelector('.close-button');
    closeButton.addEventListener('click', () => {
      this.windowManager.closeWindow(windowElement);
      this.windowInstance = null;
      if (this.articleUpdateInterval) clearInterval(this.articleUpdateInterval);
    });

    return new Window(windowElement, this.windowManager);
  }

  updateNews() {
    const newsFeed = this.windowInstance.windowElement.querySelector('#news-feed');
    if (!newsFeed) return;
    newsFeed.innerHTML = ''; // Clear previous content
    // Create a single main article element
    const articleEl = document.createElement('div');
    articleEl.classList.add('news-article');
    articleEl.style.cursor = 'pointer';
    articleEl.addEventListener('click', () => this.openArticle(this.currentArticle));
    newsFeed.appendChild(articleEl);
    this.articleElement = articleEl;
    this.renderArticle();
    // Also store the current article in localStorage for the dedicated page
    localStorage.setItem('currentArticle', JSON.stringify({
      headline: this.currentArticle.headline,
      date: this.currentArticle.date,
      fullContent: this.currentArticle.content
    }));
  }

  renderArticle() {
    if (!this.articleElement || !this.currentArticle) return;
    this.articleElement.innerHTML = `
      <div class="news-headline">${this.currentArticle.headline}</div>
      <div class="news-date">${this.currentArticle.date}</div>
      <div class="news-content">${this.currentArticle.content.replace(/\n\n/g, '<br><br>')}</div>
    `;
  }

  openArticle(article) {
    localStorage.setItem('currentArticle', JSON.stringify({
      headline: article.headline,
      date: article.date,
      fullContent: article.content
    }));
    window.location.href = '010news.html';
  }
}