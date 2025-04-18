import moment from "https://unpkg.com/moment@2.29.4/dist/moment.js"
document.addEventListener('DOMContentLoaded', () => {
  const windows = new Set();
  let activeWindow = null;
  let nextZIndex = 100;
  let currentNetwork = null; // Track network connection state

  // Update clock
  const updateClock = () => {
    const timeElement = document.getElementById('time');
    // Use Moment.js for real time if preferred, or keep fixed time
    // timeElement.textContent = moment().format('HH:mm');
    timeElement.textContent = "08:32"; // Fixed time as requested
  };

  setInterval(updateClock, 1000);
  updateClock();

  function createWindow(title, content, width = 500, height = 'auto') {
    const windowEl = document.createElement('div');
    windowEl.className = 'window';
    windowEl.style.width = `${width}px`;
    if (height !== 'auto') {
      windowEl.style.height = `${height}px`;
    }

    // Position windows with offset but ensure they stay in viewport
    const offset = windows.size * 20;
    const maxOffset = Math.min(window.innerWidth, window.innerHeight) / 4;
    const adjustedOffset = offset % maxOffset;
    windowEl.style.transform = `translate(${adjustedOffset}px, ${adjustedOffset}px)`;

    const windowHTML = `
      <div class="title-bar">
        <div class="title-bar-text">${title}</div>
        <div class="title-bar-controls">
          <button class="minimize">-</button>
          <button class="maximize">□</button>
          <button class="close">×</button>
        </div>
      </div>
      <div class="window-content">${content}</div>
    `;

    windowEl.innerHTML = windowHTML;
    document.body.appendChild(windowEl);
    windows.add(windowEl);
    windowEl.dataset.title = title;

    makeWindowDraggable(windowEl);
    setupWindowControls(windowEl);
    activateWindow(windowEl);
    updateTaskbar();

    // Make window resizable (basic implementation)
    makeWindowResizable(windowEl);

    // Ensure content area takes up available space if height is set
    if (height !== 'auto') {
        const titleBarHeight = windowEl.querySelector('.title-bar').offsetHeight;
        const contentEl = windowEl.querySelector('.window-content');
        contentEl.style.height = `calc(100% - ${titleBarHeight}px)`;
        contentEl.style.overflow = 'auto'; // Add scroll if needed
    }

    return windowEl;
  }

  function makeWindowDraggable(windowEl) {
    const titleBar = windowEl.querySelector('.title-bar');
    let isDragging = false;
    let startX, startY, initialX, initialY;

    titleBar.addEventListener('mousedown', e => {
      // Only drag if clicking the title bar itself, not controls
      if (e.target === titleBar || e.target === titleBar.querySelector('.title-bar-text')) {
        isDragging = true;
        // Bring window to front when starting drag
        activateWindow(windowEl);

        startX = e.clientX;
        startY = e.clientY;
        // Get current transform values
        const style = window.getComputedStyle(windowEl);
        const matrix = new DOMMatrixReadOnly(style.transform);
        initialX = matrix.m41; // translateX
        initialY = matrix.m42; // translateY

        windowEl.style.cursor = 'grabbing'; // Indicate dragging
        document.body.style.userSelect = 'none'; // Prevent text selection during drag
      }
    });

    document.addEventListener('mousemove', e => {
      if (isDragging) {
        e.preventDefault();
        const currentX = initialX + (e.clientX - startX);
        const currentY = initialY + (e.clientY - startY);
        windowEl.style.transform = `translate(${currentX}px, ${currentY}px)`;
      }
    });

    document.addEventListener('mouseup', () => {
      if (isDragging) {
        isDragging = false;
        windowEl.style.cursor = 'grab'; // Restore cursor
        document.body.style.userSelect = ''; // Restore text selection
      }
    });

    // Set initial cursor
     titleBar.style.cursor = 'grab';
  }

    function makeWindowResizable(windowEl) {
        const handle = document.createElement('div');
        handle.className = 'resize-handle';
        windowEl.appendChild(handle);

        let isResizing = false;
        let startX, startY, initialWidth, initialHeight;

        handle.addEventListener('mousedown', (e) => {
            isResizing = true;
            startX = e.clientX;
            startY = e.clientY;
            initialWidth = windowEl.offsetWidth;
            initialHeight = windowEl.offsetHeight;
            windowEl.style.cursor = 'nwse-resize';
            document.body.style.userSelect = 'none';
            e.stopPropagation(); // Prevent dragging while resizing
        });

        document.addEventListener('mousemove', (e) => {
            if (isResizing) {
                const newWidth = initialWidth + (e.clientX - startX);
                const newHeight = initialHeight + (e.clientY - startY);
                // Set minimum dimensions
                windowEl.style.width = `${Math.max(200, newWidth)}px`;
                windowEl.style.height = `${Math.max(150, newHeight)}px`;

                 // Adjust content height dynamically
                const titleBarHeight = windowEl.querySelector('.title-bar').offsetHeight;
                const contentEl = windowEl.querySelector('.window-content');
                contentEl.style.height = `calc(100% - ${titleBarHeight}px)`;
            }
        });

        document.addEventListener('mouseup', () => {
            if (isResizing) {
                isResizing = false;
                windowEl.style.cursor = 'default';
                document.body.style.userSelect = '';
            }
        });
    }

  function setupWindowControls(windowEl) {
    const closeBtn = windowEl.querySelector('.close');
    const minimizeBtn = windowEl.querySelector('.minimize');
    const maximizeBtn = windowEl.querySelector('.maximize');

    closeBtn.addEventListener('click', () => {
      windowEl.remove();
      windows.delete(windowEl);
      if (activeWindow === windowEl) {
        // Find the next highest z-index window to activate
        let nextActive = null;
        let maxZ = -1;
        windows.forEach(w => {
            const z = parseInt(w.style.zIndex || '0');
            if (z > maxZ) {
                maxZ = z;
                nextActive = w;
            }
        });
        activeWindow = nextActive;
        if (activeWindow) {
            activateWindow(activeWindow, false); // Activate without incrementing z-index
        }
      }
      updateTaskbar();
    });

     minimizeBtn.addEventListener('click', () => {
        windowEl.style.display = 'none';
        if (activeWindow === windowEl) {
          // Find next highest z-index window to activate
          let nextActive = null;
          let maxZ = -1;
          windows.forEach(w => {
              if (w !== windowEl && w.style.display !== 'none') {
                  const z = parseInt(w.style.zIndex || '0');
                  if (z > maxZ) {
                      maxZ = z;
                      nextActive = w;
                  }
              }
          });
          activeWindow = nextActive;
          if (activeWindow) {
            activateWindow(activeWindow, false);
          } else {
            // If no other windows are open, make the desktop active implicitly
            if (activeWindow) {
                activeWindow.classList.remove('active');
                activeWindow.querySelector('.title-bar').classList.add('inactive');
            }
             activeWindow = null;
          }
        }
        updateTaskbar();
    });

     maximizeBtn.addEventListener('click', () => {
        // Basic toggle: maximize/restore (no true OS maximization)
        if (windowEl.classList.contains('maximized')) {
            windowEl.classList.remove('maximized');
            windowEl.style.top = windowEl.dataset.originalTop || '50%';
            windowEl.style.left = windowEl.dataset.originalLeft || '50%';
            windowEl.style.width = windowEl.dataset.originalWidth || '500px';
            windowEl.style.height = windowEl.dataset.originalHeight || 'auto';
            windowEl.style.transform = windowEl.dataset.originalTransform || 'translate(-50%, -50%)';
            makeWindowResizable(windowEl); // Re-enable resizing
             if (windowEl.querySelector('.resize-handle')) {
                 windowEl.querySelector('.resize-handle').style.display = 'block';
             }

             // Re-adjust content height if original was auto
            if (windowEl.dataset.originalHeight === 'auto') {
                windowEl.querySelector('.window-content').style.height = 'auto';
            } else {
                 const titleBarHeight = windowEl.querySelector('.title-bar').offsetHeight;
                windowEl.querySelector('.window-content').style.height = `calc(100% - ${titleBarHeight}px)`;
            }

        } else {
            windowEl.classList.add('maximized');
            // Store original position and size
            windowEl.dataset.originalTop = windowEl.style.top;
            windowEl.dataset.originalLeft = windowEl.style.left;
            windowEl.dataset.originalWidth = windowEl.style.width;
            windowEl.dataset.originalHeight = windowEl.style.height;
            windowEl.dataset.originalTransform = windowEl.style.transform;

            // Maximize (fill screen minus taskbar)
            const taskbarHeight = document.querySelector('.taskbar').offsetHeight;
            windowEl.style.top = '0px';
            windowEl.style.left = '0px';
            windowEl.style.width = '100vw';
            windowEl.style.height = `calc(100vh - ${taskbarHeight}px)`;
            windowEl.style.transform = 'translate(0, 0)';

            // Adjust content height
            const titleBarHeight = windowEl.querySelector('.title-bar').offsetHeight;
            windowEl.querySelector('.window-content').style.height = `calc(100% - ${titleBarHeight}px)`;


            // Disable resizing when maximized
            if (windowEl.querySelector('.resize-handle')) {
                 windowEl.querySelector('.resize-handle').style.display = 'none';
             }
        }
    });
  }

  function activateWindow(windowEl, incrementZ = true) {
    if (activeWindow === windowEl) {
        // If already active, ensure it's at the top
        if (incrementZ) {
            windowEl.style.zIndex = nextZIndex++;
        }
        return; // No need to deactivate/reactivate
    }
    if (activeWindow) {
      activeWindow.classList.remove('active');
      activeWindow.querySelector('.title-bar').classList.remove('active'); // Use .active on title bar
      activeWindow.querySelector('.title-bar').classList.add('inactive');
    }
    windowEl.classList.add('active');
    windowEl.querySelector('.title-bar').classList.add('active');
    windowEl.querySelector('.title-bar').classList.remove('inactive');
    if (incrementZ) {
      windowEl.style.zIndex = nextZIndex++;
    }
    activeWindow = windowEl;
    updateTaskbar();
  }

  function updateTaskbar() {
    const taskbarItems = document.querySelector('.taskbar-items');
    taskbarItems.innerHTML = '';

    windows.forEach(window => {
      const title = window.dataset.title; // Use stored title
      const item = document.createElement('div');
      item.className = `taskbar-item ${window === activeWindow ? 'active' : ''} ${window.style.display === 'none' ? 'minimized' : ''}`;
      item.textContent = title;
      item.addEventListener('click', () => {
        if (window === activeWindow) {
          // If active, minimize it
          window.style.display = 'none';
          // Activate next window or null
           let nextActive = null;
          let maxZ = -1;
          windows.forEach(w => {
              if (w !== window && w.style.display !== 'none') {
                  const z = parseInt(w.style.zIndex || '0');
                  if (z > maxZ) {
                      maxZ = z;
                      nextActive = w;
                  }
              }
          });
          activeWindow = nextActive;
          if (activeWindow) {
            activateWindow(activeWindow, false);
          } else {
             // If minimizing the last visible window
             if (activeWindow) {
                 activeWindow.classList.remove('active');
                 activeWindow.querySelector('.title-bar').classList.add('inactive');
             }
              activeWindow = null;
          }

        } else {
          // If not active or minimized, bring to front and activate
          window.style.display = 'block';
          activateWindow(window);
        }
         updateTaskbar(); // Update immediately after click
      });
      taskbarItems.appendChild(item);
    });
  }

  // Function to show loading indicator
  function showLoading(windowContentElement) {
      windowContentElement.innerHTML = `
          <div class="loading-indicator">
              <div class="spinner"></div>
              Loading...
          </div>`;
      windowContentElement.classList.add('loading');
  }

  // Function to hide loading indicator and show content
  function showContent(windowContentElement, content) {
      windowContentElement.innerHTML = content;
      windowContentElement.classList.remove('loading');
  }

  // Program handlers
  const programs = {
    'my-computer': () => {
      const driveContent = {
        'c-drive': (callback) => {
          setTimeout(() => {
            callback(`
              <div class="folder-content">
                <div class="error-message">
                  ACCESS DENIED: This drive has been locked by system administrator.
                  <br><br>
                  Error code: 0x80070005
                  <br>
                  Contact your system administrator for access.
                </div>
              </div>
            `);
          }, 1500); // Loading delay
        },
        'd-drive': (callback) => {
          // Check network connection status
          const isConnected = !!currentNetwork; // Check if currentNetwork is not null/undefined

          setTimeout(() => {
            if (isConnected) {
              // If connected, show inaccessible content (simulating permissions issue)
              callback(`
                <div class="folder-content">
                  <div class="error-message">
                    NETWORK DRIVE CONTENTS INACCESSIBLE (Drive D:)
                    <br><br>
                    Error code: 0x80070035 (Network path not found or insufficient permissions)
                    <br>
                    Connection established to: ${currentNetwork}
                    <br>
                    Please contact network administrator for drive access permissions.
                  </div>
                </div>
              `);
            } else {
              // If not connected, show network error
              callback(`
                <div class="folder-content">
                  <div class="error-message">
                    NETWORK ERROR: Unable to establish connection to network drive (D:).
                    <br><br>
                    Error code: 0x80070035
                    <br>
                    Check your network connection status in 'Network Connections' and try again.
                    <br>
                    No active network connection detected.
                  </div>
                </div>
              `);
            }
          }, 2000);
        },
        'internet': (callback) => {
          setTimeout(() => {
            callback(`
              <div class="folder-content">
                <div class="error-message">
                  This shortcut is deprecated.
                  <br><br>
                  Please use the 'Secure Browser' icon on the desktop or Start Menu.
                </div>
              </div>
            `);
          }, 1200);
        },
        'reports': (callback) => {
          setTimeout(() => {
            callback(`
              <div class="folder-content">
                <div class="error-message">
                  FOLDER EMPTY
                  <br><br>
                  No mission reports or documents found in this location.
                  <br>
                  Ensure sync with central command is complete.
                </div>
              </div>
            `);
          }, 1800);
        },
        'system32': (callback) => {
          setTimeout(() => {
            callback(`
              <div class="folder-content">
                <div class="error-message">
                  CRITICAL SYSTEM FILES - ACCESS RESTRICTED
                  <br><br>
                  Modification or deletion of files in this directory is prohibited under DoD Directive 8500.1 and UCMJ Article 92.
                  <br>
                  Unauthorized access attempts are logged and subject to disciplinary action.
                </div>
              </div>
            `);
          }, 2000);
        },
        'threshold': (callback) => { // Keep existing Threshold functionality
           setTimeout(() => {
            callback(`
              <div class="threshold-viewer">
                <div class="threshold-header">
                  <h3>PROJECT THRESHOLD v2.3.1</h3>
                  <p class="warning">CLASSIFIED - LEVEL 5 CLEARANCE REQUIRED</p>
                </div>
                <div class="threshold-content">
                  <div class="threshold-visualization">
                     <svg viewBox="0 0 500 300" class="noclip-space">
                        <defs>
                          <pattern id="glitch-pattern" patternUnits="userSpaceOnUse" width="50" height="50">
                            <path d="M0 0h50v50H0z" fill="none" stroke="#0f0" stroke-width="0.5"/>
                            <path d="M25 0v50M0 25h50" stroke="#0f0" stroke-width="0.5" opacity="0.5"/>
                          </pattern>
                           <filter id="glitch-filter">
                              <feTurbulence type="fractalNoise" baseFrequency="0.1 0.9" numOctaves="3" result="warp"/>
                              <feDisplacementMap xChannelSelector="R" yChannelSelector="G" scale="20" in="SourceGraphic" in2="warp"/>
                           </filter>
                        </defs>
                        <rect width="500" height="300" fill="#001"/>
                        <rect x="100" y="50" width="300" height="200" fill="url(#glitch-pattern)" opacity="0.7" class="glitch-rect"/>
                        <rect x="150" y="100" width="200" height="100" fill="#300" opacity="0.5" class="unstable-zone"/>
                      </svg>
                  </div>
                   <div class="threshold-parameters">
                       <div class="parameter">
                        <label>Ground Stability Index:</label>
                        <div class="meter">
                          <div class="bar stability-bar" style="width: ${Math.random() * 100}%"></div>
                        </div>
                        <span class="stability-value">${(Math.random() * 1).toFixed(2)}</span>
                      </div>
                      <div class="parameter">
                        <label>Noclip Potential:</label>
                        <div class="meter">
                          <div class="bar noclip-bar" style="width: ${Math.random() * 100}%"></div>
                        </div>
                        <span class="noclip-value">${(Math.random() * 1).toFixed(2)}</span>
                      </div>
                      <div class="parameter">
                        <label>Dimensional Stress:</label>
                        <div class="meter critical">
                          <div class="bar stress-bar" style="width: ${Math.random() * 100}%"></div>
                        </div>
                        <span class="stress-value">${(Math.random() * 1).toFixed(2)}</span>
                      </div>
                      <div class="threshold-warning">
                        WARNING: Dimensional Instability Increasing. Monitor Threshold Values.
                      </div>
                    </div>
                </div>
              </div>
            `);

            // Animate parameters and maybe the SVG glitch effect
            const winContent = document.querySelector('.threshold-viewer'); // Need specific window
            if (winContent) {
              const parameterInterval = setInterval(() => {
                 if (!document.body.contains(winContent)) { // Stop if window closed
                    clearInterval(parameterInterval);
                    return;
                 }
                  const stabilityBar = winContent.querySelector('.stability-bar');
                  const noclipBar = winContent.querySelector('.noclip-bar');
                  const stressBar = winContent.querySelector('.stress-bar');
                  const unstableZone = winContent.querySelector('.unstable-zone');

                  stabilityBar.style.width = `${Math.random() * 100}%`;
                  noclipBar.style.width = `${Math.random() * 100}%`;
                  stressBar.style.width = `${Math.random() * 100}%`;

                  winContent.querySelector('.stability-value').textContent = (Math.random() * 1).toFixed(2);
                  winContent.querySelector('.noclip-value').textContent = (Math.random() * 1).toFixed(2);
                  winContent.querySelector('.stress-value').textContent = (Math.random() * 1).toFixed(2);

                  unstableZone.style.opacity = 0.3 + (Math.random() * 0.7);
              }, 1000);
            }
          }, 1500);
        }
      };

      const mainWindow = createWindow('My Computer', `
        <div class="folder-content">
          <div class="loading-indicator">Loading...</div>
        </div>
      `);

      setTimeout(() => {
        mainWindow.querySelector('.folder-content').innerHTML = `
          <div class="folder-item" data-folder="c-drive">
            <svg class="folder-item-icon" viewBox="0 0 24 24">
              <rect x="2" y="4" width="20" height="16" fill="#FFD700"/>
            </svg>
            <span>Local Disk (C:)</span>
          </div>
          <div class="folder-item" data-folder="d-drive">
            <svg class="folder-item-icon" viewBox="0 0 24 24">
              <rect x="2" y="4" width="20" height="16" fill="#A0A0A0"/>
            </svg>
            <span>Network Drive (D:)</span>
          </div>
          <div class="folder-item" data-folder="internet">
            <svg class="folder-item-icon" viewBox="0 0 24 24">
              <path d="M4 4h16v16H4z" fill="#4169E1"/>
            </svg>
            <span>Internet Explorer</span>
          </div>
          <div class="folder-item" data-folder="reports">
            <svg class="folder-item-icon" viewBox="0 0 24 24">
              <path d="M4 4h16v16H4z" fill="#008000"/>
              <text x="12" y="14" text-anchor="middle" fill="white" font-size="10">DOC</text>
            </svg>
            <span>Reports</span>
          </div>
          <div class="folder-item" data-folder="system32">
            <svg class="folder-item-icon" viewBox="0 0 24 24">
              <path d="M4 4h16v16H4z" fill="#800000"/>
              <text x="12" y="14" text-anchor="middle" fill="white" font-size="10">SYS</text>
            </svg>
            <span>System32</span>
          </div>
          <div class="folder-item" data-folder="threshold">
            <svg class="folder-item-icon" viewBox="0 0 24 24">
              <rect x="2" y="4" width="20" height="16" fill="#666"/>
            </svg>
            <span>Threshold</span>
          </div>
        `;

        mainWindow.querySelector('.folder-content').addEventListener('click', (e) => {
          const item = e.target.closest('.folder-item');
          if (!item) return;

          const folderId = item.dataset.folder;
          if (driveContent[folderId]) {
            const window = createWindow(item.querySelector('span').textContent, `
              <div class="loading-indicator">
                <div class="spinner"></div>
                Loading...
              </div>
            `);
            
            driveContent[folderId]((content) => {
              window.querySelector('.window-content').innerHTML = content;
            });
          }
        });
      }, 1000);
    },
    'internet': () => {
      const win = createWindow('Internet Explorer', `
        <div class="browser">
          <div class="browser-toolbar">
            <button>←</button>
            <button>→</button>
            <button>⟳</button>
            <input type="text" value="http://www.google.com" class="address-bar">
          </div>
          <div class="browser-content">
            <div class="loading-indicator">
              <div class="spinner"></div>
              Connecting to www.google.com...
            </div>
          </div>
        </div>
      `, 800);

      setTimeout(() => {
        win.querySelector('.browser-content').innerHTML = `
          <div class="google-page">
            <img src="data:image/svg+xml,${encodeURIComponent(`
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 272 92">
                <path d="M115.75 47.18c0 12.77-9.99 22.18-22.25 22.18s-22.25-9.41-22.25-22.18c0-12.85 9.99-22.18 22.25-22.18s22.25 9.32 22.25 22.18zm-9.74 0c0-7.98-5.79-13.44-12.51-13.44s-12.51 5.46-12.51 13.44c0 7.9 5.79 13.44 12.51 13.44s12.51-5.55 12.51-13.44z" fill="#EA4335"/>
                <path d="M163.75 47.18c0 12.77-9.99 22.18-22.25 22.18s-22.25-9.41-22.25-22.18c0-12.85 9.99-22.18 22.25-22.18s22.25 9.32 22.25 22.18zm-9.74 0c0-7.98-5.79-13.44-12.51-13.44s-12.51 5.46-12.51 13.44c0 7.9 5.79 13.44 12.51 13.44s12.51-5.55 12.51-13.44z" fill="#FBBC05"/>
                <path d="M209.75 26.34v39.82c0 16.38-9.66 23.07-21.08 23.07-10.75 0-17.22-7.19-19.66-13.07l8.48-3.53c1.51 3.61 5.21 7.87 11.17 7.87 7.31 0 11.84-4.51 11.84-13v-3.19h-.34c-2.18 2.69-6.38 5.04-11.68 5.04-11.09 0-21.25-9.66-21.25-22.09 0-12.52 10.16-22.26 21.25-22.26 5.29 0 9.49 2.35 11.68 4.96h.34v-3.61h9.25zm-8.56 20.92c0-7.81-5.21-13.52-11.84-13.52-6.72 0-12.35 5.71-12.35 13.52 0 7.73 5.63 13.36 12.35 13.36 6.63 0 11.84-5.63 11.84-13.36z" fill="#4285F4"/>
                <path d="M225 3v65h-9.5V3h9.5z" fill="#34A853"/>
                <path d="M262.02 54.48l7.56 5.04c-2.44 3.61-8.32 9.83-18.48 9.83-12.6 0-22.01-9.74-22.01-22.18 0-13.19 9.49-22.18 20.92-22.18 11.51 0 17.14 9.16 18.98 14.11l1.01 2.52-29.65 12.28c2.27 4.45 5.8 6.72 10.75 6.72 4.96 0 8.4-2.44 10.92-6.14zm-23.27-7.98l19.82-8.23c-1.09-2.77-4.37-4.7-8.23-4.7-4.95 0-11.84 4.37-11.59 12.93z" fill="#EA4335"/>
              </svg>
            `)}" alt="Google" class="google-logo">
            <div class="connection-info">
              <p>Status: Connected</p>
              <p class="warning">Internet Access Restricted</p>
            </div>
            <div class="search-box">
              <input type="text" placeholder="Enter network credentials">
              <button>Login</button>
            </div>
            <div class="error-message">
              ERROR: Access to internet resources is restricted.
              <br>Only authorized personnel may proceed.
              <br>Error code: AUTH_403
            </div>
          </div>
        `;
      }, 2500);
    },
    'scp': () => {
      createWindow('SCP Foundation Database', `
        <div class="scp-database">
          <div class="scp-header">
            <h2>SCP Foundation</h2>
            <p>Secure. Contain. Protect.</p>
          </div>
          <div class="scp-list">
            <div class="scp-item" data-scp="pipes">
              <h3>Space Pipes</h3>
              <p>Pipes of Space</p>
            </div>
            <div class="scp-item" data-scp="096">
              <h3>SCP-████</h3>
              <p>The "████ ████"</p>
            </div>
            <div class="scp-item" data-scp="682">
              <h3>SCP-████</h3>
              <p>Hard-to-Destroy Reptile</p>
            </div>
            <div class="scp-item" data-scp="049">
              <h3>SCP-████</h3>
              <p>Plague Doctor</p>
            </div>
          </div>
        </div>
      `);

      const scpData = {
        'pipes': {
          title: 'Space Pipes',
          class: 'Euclid',
          description: `Object Class: Euclid

Special Containment Procedures:
Item is to be kept in a locked container at all times. When personnel must enter item's container, no fewer than 3 may enter at any time and the door is to be relocked behind them. At all times, two persons must maintain direct eye contact with item until all personnel have vacated and relocked the container.

Description:
Moved to Site-19 1993. Origin is as of yet unknown. It is constructed from concrete and rebar with traces of Krylon brand spray paint. Item is animate and extremely hostile. The object cannot move while within a direct line of sight. Line of sight must be broken in order for item to move. This is invariably fatal to personnel. Personnel assigned to enter container are instructed to alert one another before blinking.`
        },
        '096': {
          title: 'SCP-096',
          class: 'Euclid',
          description: `Object Class: Euclid

Special Containment Procedures:
SCP-096 is to be contained in its cell, a 5m x 5m x 5m airtight steel cube, at all times. Weekly checks for any cracks or holes are mandatory. There are to be absolutely no video surveillance or optical tools of any kind inside SCP-096's cell. Security personnel will use pre-installed pressure sensors and laser detectors to ensure SCP-096's presence inside the cell.

Description:
SCP-096 is a humanoid creature measuring approximately 2.38 meters in height. Subject shows very little muscle mass, with preliminary analysis of body mass suggesting mild malnutrition. Arms are grossly out of proportion with the rest of the subject's body, with an approximate length of 1.5 meters each. Skin is mostly devoid of pigmentation, with no sign of any body hair.`
        }
      };

      document.querySelector('.scp-list').addEventListener('click', (e) => {
        const item = e.target.closest('.scp-item');
        if (!item) return;

        const scpId = item.dataset.scp;
        if (scpData[scpId]) {
          const detailWindow = createWindow(scpData[scpId].title, `
            <div class="scp-details">
              <div class="scp-warning">WARNING: LEVEL 4 CLEARANCE REQUIRED</div>
              <div class="scp-content">
                <h3>${scpData[scpId].title}</h3>
                <p class="scp-class">Object Class: ${scpData[scpId].class}</p>
                <div class="scp-description">
                  ${scpData[scpId].description}
                </div>
              </div>
            </div>
          `);

          // Trigger lockdown after random delay
          setTimeout(() => {
            const lockdownWindow = document.createElement('div');
            lockdownWindow.className = 'lockdown-screen';
            lockdownWindow.innerHTML = `
              <div class="lockdown-content">
                <div class="warning-symbol">⚠</div>
                <h1>SECURITY BREACH DETECTED</h1>
                <p>Unauthorized access to classified SCP Foundation files.</p>
                <p>System lockdown initiated.</p>
                <p>Process code: 78391</p>
                <p>Please wait for administrator assistance.</p>
                <div class="lockdown-footer">
                  SITE-19 SECURITY PROTOCOL ACTIVATED
                </div>
              </div>
            `;
            document.body.appendChild(lockdownWindow);
          }, (Math.random() * 4000 + 1000));
        }
      });
    },
    'network': () => {
      const win = createWindow('Network Connections', `
        <div class="network-interface">
          <div class="network-header">
            <h3>Available Networks</h3>
          </div>
          <div class="network-list">
            <div class="network-item">
              <div class="network-info">
                <div class="network-name">SITE-19-SECURE</div>
                <div class="network-type">Secured</div>
                <div class="network-strength">Signal Strength: Strong</div>
              </div>
              <button class="connect-btn" disabled>Access Denied</button>
            </div>
            <div class="network-item">
              <div class="network-info">
                <div class="network-name">BackroomsNet</div>
                <div class="network-type">Unknown Protocol</div>
                <div class="network-strength">Signal Strength: ??????????</div>
              </div>
              <button class="connect-btn" disabled>ERROR</button>
            </div>
            <div class="network-item">
              <div class="network-info">
                <div class="network-name">Level_0_Public</div>
                <div class="network-type">Unsecured</div>
                <div class="network-strength">Signal Strength: Weak</div>
              </div>
              <button class="connect-btn">Connect</button>
            </div>
            <div class="network-item connected">
              <div class="network-info">
                <div class="network-name">SCPF-Guest</div>
                <div class="network-type">Secured</div>
                <div class="network-strength">Signal Strength: Medium</div>
              </div>
              <button class="connect-btn">Connected</button>
            </div>
          </div>
          <div class="network-status">
            <p>Current Connection: SCPF-Guest</p>
            <p>Status: Connected</p>
            <div class="network-drives">
              <h4>Available Network Drives</h4>
              <div class="drive-item" data-drive="archives">
                <span>Site Archives</span>
                <button class="access-btn">Access Restricted</button>
              </div>
              <div class="drive-item" data-drive="research">
                <span>Research Logs</span>
                <button class="access-btn">Access Restricted</button>
              </div>
              <div class="drive-item" data-drive="transit">
                <span>Transit Logs</span>
                <button class="access-btn">View Log</button>
              </div>
            </div>
          </div>
        </div>
      `);

      win.querySelector('.network-drives').addEventListener('click', (e) => {
        const driveItem = e.target.closest('.drive-item');
        if (!driveItem) return;

        const drive = driveItem.dataset.drive;
        if (drive === 'transit') {
          createWindow('Transit Logs', `
            <div class="transit-logs">
              <h3>Interdimensional Transit Logs</h3>
              <div class="log-entries">
                ${Array.from({length: 20}, (_, i) => `
                  <div class="log-entry">
                    <div class="log-time">${moment().subtract(i, 'hours').format('YYYY-MM-DD HH:mm')}</div>
                    <div class="log-route">Route ${['A', 'B', 'C'][Math.floor(Math.random() * 3)]}-${Math.floor(Math.random() * 999)}</div>
                    <div class="log-destination">Level ${Math.floor(Math.random() * 1000)}</div>
                    <div class="log-status">${['Completed', 'Interrupted', 'Unknown', 'Anomaly Detected'][Math.floor(Math.random() * 4)]}</div>
                  </div>
                `).join('')}
              </div>
            </div>
          `);
        } else {
          alert('Access to this drive is currently restricted.');
        }
      });
    },
    'timetable': () => {
      createWindow('Backrooms Transit Authority', `
        <div class="transit-timetable">
          <div class="timetable-header">
            <h2>INTERDIMENSIONAL TRANSIT SCHEDULE</h2>
            <p class="warning">※ Schedule subject to non-euclidean distortions</p>
          </div>
          <div class="timetable-content">
            ${Array.from({ length: 20 }, (_, i) => `
              <div class="timetable-row">
                <div class="time">${moment().add(Math.random() * 60, 'minutes').format('HH:mm')}</div>
                <div class="route">Route ${['A', 'B', 'C'][Math.floor(Math.random() * 3)]}-${Math.floor(Math.random() * 999)}</div>
                <div class="destination">Level ${Math.floor(Math.random() * 1000)}</div>
                <div class="status">${['On Time', 'Delayed', 'Unknown', 'Time Paradox'][Math.floor(Math.random() * 4)]}</div>
              </div>
            `).join('')}
          </div>
        </div>
      `, 600);
    },
    'classified': () => {
      const win = createWindow('CLASSIFIED FILES', `
        <div class="password-prompt">
          <p>ENTER SECURITY CLEARANCE CODE:</p>
          <input type="password" class="password-input">
          <button class="submit-password">SUBMIT</button>
        </div>
        <div class="files" style="display: none;">
          <div class="file" data-file="scp1">
            <h3>SCP-████████.doc</h3>
            <p>19:23:25</p>
          </div>
          <div class="file" data-file="scp2">
            <h3>SCP-████████.doc</h3>
            <p>Pending name and classifications</p>
          </div>
          <div class="file" data-file="backrooms">
            <h3>BACKROOMS-INCIDENT-LOG.txt</h3>
            <p>Level 0 Breach Report - Security Level 5</p>
          </div>
          <div class="file" data-file="threshold">
            <h3>PROJECT-THRESHOLD.log</h3>
            <p>Noclip Investigation Tool - Security Level 6</p>
          </div>
          <div class="file" data-file="trainmap">
            <h3>BACKROOMS-TRAIN-SYSTEM.svg</h3>
            <p>Interdimensional Rail Network - Security Level 5</p>
          </div>
        </div>
      `);

      const input = win.querySelector('.password-input');
      const submit = win.querySelector('.submit-password');
      const files = win.querySelector('.files');

      submit.addEventListener('click', () => {
        if (input.value === 'wspg') {
          win.querySelector('.password-prompt').style.display = 'none';
          files.style.display = 'block';
        } else {
          alert('ACCESS DENIED - SECURITY VIOLATION LOGGED');
        }
      });

      const fileContents = {
        'scp1': `              SCP-████████████
OBJECT CLASS: Pending

SPECIAL CONTAINMENT PROCEDURES:
Unable to contain at this time. Current Status is to observe all actions of ████████████ and report any changes or abnormalities in behavior. 

DESCRIPTION:
SCP-██████████ is a humanoid entinty that currently resides in ████████████ . The entity has gained notoriety on the internet and displayed the power to see other ████████████ throughout the universe. A holding site located in the North Atlantic Ocean (Latitude: 37.02806, Longitude: -30.54940, Distortion: 1.57) was prepared on ████████████ to contain the entity. Currently the site is abandoned after a earthquake due to a seismic shifts damaged the holding equipment, although new containment procedures are currently being made they are not expected to finish until 2042. Most of the anomalous properties of SCP-██████████ do not effect others however, the possibility of a Great Convergence K-Class Scenario remains possible.`,

        'backrooms': `              BACKROOMS INCIDENT LOG - 05/23/20██

0300 hrs: First reports of wall phasing incident outside of testing room █████ at Site-████.
0317 hrs: Multiple personnel reported missing.
0330 hrs: Recovery team shota-A assembled and deployed to Site-████.
0345 hrs: Recovery team reports breach at Site-████.
0350 hrs: Remaning personnel evacuated and recovery team deployed to backrooms.
0355 hrs: Pending incident report from recovery team.`,

        'threshold': `              PROJECT THRESHOLD
STATUS: MAINTENANCE
CLEARANCE: LEVEL 6

Warning: This program is currently in autonomus mode actions will be taken by the system.
Any system readings currently displayed are not accurate. The pulse of the program is to monitor the quantum fluctuations of object ████████ at site ████████. If there is any value above the safety threshold please consult the system administrator at 612-861-3421`
      };

      files.addEventListener('click', (e) => {
        const file = e.target.closest('.file');
        if (!file) return;

        if (fileContents[file.dataset.file]) {
          createWindow(file.querySelector('h3').textContent, `
            <div class="text-viewer">
              ${fileContents[file.dataset.file]}
            </div>
          `);
        }
      });
    },
    'recycle-bin': () => {
      createWindow('Recycle Bin', `
        <div class="folder-content">
          <p style="padding: 20px;">Recycle Bin is empty</p>
        </div>
      `);
    },
    'metro': () => {
      const trainData = {
        locations: [
          { id: 'hub', name: 'The Hub', x: 400, y: 200, central: true },
          { id: 'pi', name: 'Level π', x: 200, y: 100 },
          { id: '0', name: 'Level 0', x: 600, y: 100 },
          { id: '9', name: 'Level 9', x: 300, y: 300 },
          { id: '36b', name: 'Level 36-B', x: 500, y: 300 },
          { id: '11', name: 'Level 11', x: 700, y: 200 },
          { id: '990', name: 'Level 990', x: 200, y: 400 },
          { id: '3', name: 'Level 3', x: 600, y: 400 }
        ],
        connections: [
          ['hub', 'pi'],
          ['hub', '0'],
          ['hub', '9'],
          ['hub', '36b'],
          ['hub', '11'],
          ['hub', '990'],
          ['hub', '3']
        ],
        trains: [
          {
            id: 'A1',
            type: 'a',
            route: ['pi', 'hub', '0', 'hub', '9', 'hub'],
            speed: 0.0005,
            position: 0,
            progress: 0,
            waiting: 0
          },
          {
            id: 'B1',
            type: 'b',
            route: ['36b', 'hub', '11', 'hub', '990', 'hub'],
            speed: 0.0005,
            position: 0,
            progress: 0,
            waiting: 0
          },
          {
            id: 'STEAM1',
            type: 'steam',
            route: ['3', 'hub', '990', 'hub'],
            speed: 0.0007, 
            position: 0,
            progress: 0,
            waiting: 0
          }
        ]
      };

      const win = createWindow('Metro Network Monitor', `
        <div class="network-monitor">
          <div class="monitor-split">
            <div class="map-container">
              <div class="map-controls">
                <button class="zoom-in">+</button>
                <button class="zoom-out">-</button>
                <button class="pan-reset">R</button>
              </div>
              <div class="map-viewport">
                <svg viewBox="0 0 800 500" class="network-map">
                  <defs>
                    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5"
                      markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                      <path d="M 0 0 L 10 5 L 0 10 z" fill="#00ff00"/>
                    </marker>
                  </defs>
                  <g class="connections"></g>
                  <g class="stations"></g>
                  <g class="trains"></g>
                </svg>
              </div>
            </div>
            <div class="info-panel">
              <div class="system-status">
                <h3>SYSTEM STATUS</h3>
                <div class="status-details">
                  <p>Active Trains: <span class="train-count">3</span></p>
                  <p>System Status: <span class="system-status">OPERATIONAL</span></p>
                  <p>Next Maintenance: <span class="next-maintenance">12:00</span></p>
                </div>
              </div>
              <div class="train-list">
                <h3>ACTIVE TRAINS</h3>
                <div class="train-details"></div>
              </div>
            </div>
          </div>
        </div>
      `, 900);

      const svg = win.querySelector('.network-map');
      let scale = 1;
      let panX = 0;
      let panY = 0;
      
      const updateTransform = () => {
        const g = svg.querySelector('g.connections').parentElement;
        g.style.transform = `scale(${scale}) translate(${panX}px, ${panY}px)`;
      };

      win.querySelector('.zoom-in').addEventListener('click', () => {
        scale = Math.min(scale * 1.2, 2);
        updateTransform();
      });

      win.querySelector('.zoom-out').addEventListener('click', () => {
        scale = Math.max(scale / 1.2, 0.5);
        updateTransform();
      });

      win.querySelector('.pan-reset').addEventListener('click', () => {
        scale = 1;
        panX = 0;
        panY = 0;
        updateTransform();
      });

      let isDragging = false;
      let startX, startY;

      svg.addEventListener('mousedown', (e) => {
        isDragging = true;
        startX = e.clientX - panX;
        startY = e.clientY - panY;
      });

      window.addEventListener('mousemove', (e) => {
        if (isDragging) {
          panX = e.clientX - startX;
          panY = e.clientY - startY;
          updateTransform();
        }
      });

      window.addEventListener('mouseup', () => {
        isDragging = false;
      });

      const drawNetwork = () => {
        const stations = win.querySelector('.stations');
        const connections = win.querySelector('.connections');
        const trains = win.querySelector('.trains');
        
        connections.innerHTML = trainData.connections.map(([from, to]) => {
          const fromStation = trainData.locations.find(l => l.id === from);
          const toStation = trainData.locations.find(l => l.id === to);
          return `<path 
            d="M ${fromStation.x} ${fromStation.y} L ${toStation.x} ${toStation.y}"
            class="track"
            data-from="${from}"
            data-to="${to}"
          />`;
        }).join('');

        stations.innerHTML = trainData.locations.map(loc => `
          <g class="station" data-id="${loc.id}" onclick="showStationInfo('${loc.id}')">
            <circle cx="${loc.x}" cy="${loc.y}" r="10" />
            <text x="${loc.x}" y="${loc.y + 25}" text-anchor="middle">${loc.name}</text>
          </g>
        `).join('');

        trainData.trains.forEach(train => {
          const fromStation = trainData.locations.find(l => l.id === train.route[train.position]);
          const toStation = trainData.locations.find(l => l.id === train.route[(train.position + 1) % train.route.length]);
          
          const x = fromStation.x + (toStation.x - fromStation.x) * train.progress;
          const y = fromStation.y + (toStation.y - fromStation.y) * train.progress;

          const trainEl = trains.querySelector(`[data-id="${train.id}"]`) || document.createElementNS("http://www.w3.org/2000/svg", "g");
          trainEl.setAttribute('class', `train ${train.type}`);
          trainEl.setAttribute('data-id', train.id);
          trainEl.innerHTML = `<circle cx="${x}" cy="${y}" r="5" class="train-marker"/>`;
          
          if (!trainEl.parentElement) {
            trains.appendChild(trainEl);
          }
        });
      };

      const updateTrains = () => {
        trainData.trains.forEach(train => {
          if (train.waiting > 0) {
            train.waiting -= 1;
            return;
          }
          
          train.progress += train.speed;
          if (train.progress >= 1) {
            train.progress = 0;
            train.position = (train.position + 1) % train.route.length;
            train.waiting = 200; 
          }
        });
        drawNetwork();
      };

      const animationInterval = setInterval(updateTrains, 100);

      win.addEventListener('remove', () => {
        clearInterval(animationInterval);
      });

      drawNetwork();

      window.showStationInfo = (stationId) => {
        const station = trainData.locations.find(l => l.id === stationId);
        const info = win.querySelector('.station-info') || document.createElement('div');
        info.className = 'station-info';
        info.innerHTML = `
          <h4>${station.name}</h4>
          <p>Status: OPERATIONAL</p>
          <p>Security Level: UNKNOWN</p>
          <p>Current Occupancy: --</p>
          <p>Next Arrival: ${moment().add(Math.floor(Math.random() * 10), 'minutes').format('HH:mm')}</p>
          <p style="color: #666">Note: Further information unavailable due to ERROR CODE 451</p>
        `;
        win.querySelector('.info-panel').appendChild(info);
      };

      const updateTrainInfo = () => {
        const trainDetails = win.querySelector('.train-details');
        trainDetails.innerHTML = trainData.trains.map(train => {
          const currentStation = trainData.locations.find(l => l.id === train.route[train.position]);
          const nextStation = trainData.locations.find(l => l.id === train.route[(train.position + 1) % train.route.length]);
          const status = train.waiting > 0 ? 'STOPPED' : 'IN TRANSIT';
          return `
            <div class="train-info ${train.type}">
              <h4>Train ${train.id}</h4>
              <p>Type: ${train.type.toUpperCase()}</p>
              <p>Status: ${status}</p>
              <p>Current: ${currentStation.name}</p>
              <p>Next: ${nextStation.name}</p>
              <p>Progress: ${Math.round(train.waiting > 0 ? 100 : train.progress * 100)}%</p>
            </div>
          `;
        }).join('');

        let schedule = document.querySelector('.schedule');
        if (!schedule) {
          schedule = document.createElement('div');
          schedule.className = 'schedule';
          schedule.innerHTML = '<h3>TIMETABLE</h3><div class="schedule-content"></div>';
          win.querySelector('.network-monitor').appendChild(schedule);
        }

        const scheduleContent = schedule.querySelector('.schedule-content');
        scheduleContent.innerHTML = trainData.trains.map(train => {
          const currentStation = trainData.locations.find(l => l.id === train.route[train.position]);
          const time = moment().add(Math.round((1 - train.progress) * 5), 'minutes').format('HH:mm');
          return `
            <div class="schedule-entry ${train.type}">
              <span>${train.id}</span>
              <span>${time}</span>
              <span>${currentStation.name}</span>
            </div>
          `;
        }).join('');
      };

      setInterval(updateTrainInfo, 1000);
      updateTrainInfo();
    },
    'threshold': () => {
      const win = createWindow('PROJECT THRESHOLD', `
        <div class="threshold-window">
          <div class="threshold-header">
            <h2>Controlled Noclip Experiment</h2>
            <p class="warning">SYSTEM STABILITY CRITICAL</p>
          </div>
          <div class="threshold-content">
            <div class="threshold-diagram">
              <svg viewBox="0 0 500 300" class="noclip-space">
                <defs>
                  <pattern id="glitch" patternUnits="userSpaceOnUse" width="50" height="50">
                    <path d="M0 0h50v50H0z" fill="none" stroke="#0f0" stroke-width="0.5"/>
                    <path d="M25 0v50M0 25h50" stroke="#0f0" stroke-width="0.5" opacity="0.5"/>
                  </pattern>
                </defs>
                <rect width="500" height="300" fill="#001"/>
                <rect x="100" y="50" width="300" height="200" fill="url(#glitch)" opacity="0.7"/>
                <rect x="150" y="100" width="200" height="100" fill="#300" opacity="0.5" class="unstable-zone"/>
              </svg>
            </div>
            <div class="threshold-parameters">
              <div class="parameter">
                <label>Ground Stability Index</label>
                <div class="meter">
                  <div class="bar stability-bar"></div>
                </div>
                <span class="stability-value">0.00</span>
              </div>
              <div class="parameter">
                <label>Noclip Potential</label>
                <div class="meter">
                  <div class="bar noclip-bar"></div>
                </div>
                <span class="noclip-value">0.00</span>
              </div>
              <div class="parameter">
                <label>Dimensional Stress</label>
                <div class="meter critical">
                  <div class="bar stress-bar"></div>
                </div>
                <span class="stress-value">0.00</span>
              </div>
              <div class="threshold-warning">
                WARNING: Dimensional Instability Increasing
              </div>
            </div>
          </div>
        </div>
      `);

      const updateParameters = () => {
        const stabilityBar = win.querySelector('.stability-bar');
        const noclipBar = win.querySelector('.noclip-bar');
        const stressBar = win.querySelector('.stress-bar');
        const unstableZone = win.querySelector('.unstable-zone');

        const stability = Math.random();
        const noclip = Math.random();
        const stress = Math.random();

        stabilityBar.style.width = `${stability * 100}%`;
        noclipBar.style.width = `${noclip * 100}%`;
        stressBar.style.width = `${stress * 100}%`;

        win.querySelector('.stability-value').textContent = stability.toFixed(2);
        win.querySelector('.noclip-value').textContent = noclip.toFixed(2);
        win.querySelector('.stress-value').textContent = stress.toFixed(2);

        unstableZone.style.opacity = 0.3 + (stress * 0.7);
      };

      const parameterInterval = setInterval(updateParameters, 1000);
      updateParameters();

      win.addEventListener('remove', () => {
        clearInterval(parameterInterval);
      });
    },
  };

  Object.assign(programs, {
    'ops-center': () => {
      createWindow('Ops Center', `
        <div class="folder-content">
          <h2>Operations Center</h2>
          <p style="margin-bottom:15px">Unified Command Operations Dashboard</p>
          <div class="file" style="font-size:16px;margin-bottom:10px;" data-file="logistics-report">
            <b>LOGISTICS-OPS-REPORT.doc</b>
            <p>Division Readiness & Supply Chain Summary</p>
          </div>
          <div class="file" style="font-size:16px;margin-bottom:10px;" data-file="ops-orders">
            <b>OPERATIONS-ORDERS.log</b>
            <p>Mission Assignment Queue - Clearance Required</p>
          </div>
          <div class="file" style="font-size:16px;" data-file="critical-alerts">
            <b>CRITICAL-ALERTS.txt</b>
            <p>Active Station Warnings</p>
          </div>
        </div>
      `);
      const win = document.querySelector('.window.active');
      win.querySelector('.folder-content').addEventListener('click', (e) => {
        const file = e.target.closest('.file');
        if (!file) return;
        if(file.dataset.file === "logistics-report"){
          createWindow('LOGISTICS-OPS-REPORT.doc', `
            <div class="text-viewer" style="font-size:15px;">LOGISTICS REPORT - ALL SITES<br>
            --------------------------------<br>
            Overall Supply Status: GREEN<br>
            Emergency Reserves: 89.7%<br>
            <br>
            Latest shipment arrival delayed (Level 11)<br>
            <br>
            Note: Order #L1847-22 is missing – escalation required.<br>
            <br>
            Memo: Do NOT allow unscheduled movement of classified materials via metro.<br>
            </div>
          `);
        } else if(file.dataset.file === "ops-orders") {
          createWindow('OPERATIONS-ORDERS.log', `
            <div class="text-viewer" style="font-size:15px;">
            ACTIVE MISSION QUEUE:<br>
            [ ] 0932Z: Recon - Observe the location as described in Addendum 0001-A <br>
            [X] 0700Z: Secure - ██████████ <br>
            [ ] 1005Z: Deliver - Deliver recovered materials directly to Site-19 <br>
            <br>
            See site commander for full access.
            </div>
          `);
        } else if(file.dataset.file === "critical-alerts") {
          createWindow('CRITICAL-ALERTS.txt', `
            <div class="text-viewer" style="color:#f00;font-size:15px;">
            <b>//CRITICAL ALERTS//</b>
            1. Unusual electromagnetic output: County of Ruckersville.
            2. Threshold controller reporting "high instability".
            3. Train System Alert: STEAM1 requires preventive maintenance.<br>
            <br>
            See Ops Center manager for incident codes and documentation.
            </div>
          `);
        }
      });
    },
    'personnel': () => {
      createWindow('Personnel Records', `
        <div class="folder-content">
          <h2>Personnel Database</h2>
          <div class="file" style="font-size:15px;" data-file="staff-list">
            <b>STAFF-ROSTER.csv</b><br>
            <p>Personnel List</p>
          </div>
          <div class="file" style="font-size:15px;" data-file="incident-log">
            <b>INCIDENT-LOG.txt</b><br>
            <p>Recent Incidents - Access: LEVEL 3</p>
          </div>
        </div>
      `);
      const win = document.querySelector('.window.active');
      win.querySelector('.folder-content').addEventListener('click', (e) => {
        const file = e.target.closest('.file');
        if (!file) return;
        if(file.dataset.file === "staff-list") {
          // Use characters from script.rpy
          createWindow('STAFF-ROSTER.csv', `
            <div class="text-viewer" style="font-size:14px;">
LASTNAME,FIRSTNAME,RANK/ID,LAST SEEN<br>
Jones,J.J.,DRILL SGT,Projector Room<br>
Miller,[REDACTED],CMD OFC,Command Center<br>
Smith,Benjamin,PVT987,Bootcamp Wing<br> <!-- Assuming player character -->
Miller,Samuel,PVT123,Bootcamp Wing<br> <!-- Samuel -->
Khan,Sultan,SPC456,Projector Room<br> <!-- Guy from projector room -->
Smith,Emma,CIV001,[REDACTED]/Deceased<br> <!-- From file found -->
[REDACTED],[REDACTED],SEC LVL 5,Unknown<br> <!-- Placeholder for mystery -->
            </div>
          `);
        } else if(file.dataset.file === "incident-log") {
          createWindow('INCIDENT-LOG.txt', `
            <div class="text-viewer" style="font-size:14px;">
[15:44] ALERT: Personnel Lewis missing, last seen entering Level 0 east access.
[17:20] INFO: Security check, all accounted.
[19:05] NOTE: Restricted area breach attempt - ALERT sent to security.
[21:10] WARNING: System32 access flag raised on terminal 2392 - NO FURTHER ACTION.
            </div>
          `);
        }
      });
    },
    'logistics': () => {
      createWindow('Logistics', `
        <div class="folder-content">
          <h2>Logistics Field Suite</h2>
          <div class="file" style="font-size:15px;" data-file="supply-status">
            <b>SUPPLY-STATUS.xlsx</b>
            <p>Automated Depot Report</p>
          </div>
          <div class="file" style="font-size:15px;" data-file="vehicle-schedule">
            <b>VEHICLE-SCHEDULE.csv</b>
            <p>On-site Transports</p>
          </div>
        </div>
      `);
      const win = document.querySelector('.window.active');
      win.querySelector('.folder-content').addEventListener('click', (e) => {
        const file = e.target.closest('.file');
        if (!file) return;
        if(file.dataset.file === "supply-status") {
          createWindow('SUPPLY-STATUS.xlsx', `
            <div class="text-viewer" style="font-size:14px;">
DEPOT,FOOD,WATER,TOOLS,NOTES<br>
Main Building,95%,93%,85%,Nominal<br>
Level 0,49%,80%,22%,Backorder queued<br>
Site 19,100%,100%,92%,-<br>
LOG-Wing,76%,66%,68%,Restocking
            </div>
          `);
        } else if(file.dataset.file === "vehicle-schedule") {
          createWindow('VEHICLE-SCHEDULE.csv', `
            <div class="text-viewer" style="font-size:14px;">
ID,TYPE,LOCATION,STATUS<br>
TR0976,KAT1,Depot,Queued<br>
SR0431,Leichttraktor,Depot,Ready<br>
MT1420,Kettenkrad,Depot,In Use
            </div>
          `);
        }
      });
    },
    'comms': () => {
      createWindow('Secure Comms', `
        <div class="folder-content">
          <h2>Secure Communications</h2>
          <div class="file" style="font-size:15px;" data-file="message-inbox">
            <b>MESSAGE-INBOX</b><br>
            <p>3 Unread Messages</p>
          </div>
          <div class="file" style="font-size:15px;" data-file="outbox">
            <b>OUTBOX</b>
            <p>No outgoing messages</p>
          </div>
        </div>
      `);
      const win = document.querySelector('.window.active');
      win.querySelector('.folder-content').addEventListener('click', (e) => {
        const file = e.target.closest('.file');
        if (!file) return;
        if(file.dataset.file === "message-inbox") {
          createWindow('MESSAGE-INBOX', `
            <div class="text-viewer" style="font-size:14px;">
[UNREAD] From: SYSTEM<br>
"Network access logs locked down. Code Yellow is initialized."<br><br>
[UNREAD] From: Site Security<br>
"This weeks password is: WSPG. Remember be safe, be smart, be vigilant. Your life can depend on it."<br><br>
[UNREAD] From: Ops Center<br>
"Project Threshold: monitor instability metrics closely."
            </div>
          `);
        } else if(file.dataset.file === "outbox") {
          createWindow('OUTBOX', `<div class="text-viewer">No outgoing messages.</div>`);
        }
      });
    },
    'threat': () => {
      createWindow('Threat Assessment', `
        <div class="folder-content">
          <h2>Threat Assessment Hub</h2>
          <div class="file" data-file="latest-briefing" style="font-size:15px;">
            <b>LATEST-BRIEFING.pdf</b>
            <p>Threat Report: Unauthorized Noclip</p>
          </div>
          <div class="file" data-file="threat-list" style="font-size:15px;">
            <b>THREAT-LIST.log</b>
            <p>Potential Anomalies Detected 4</p>
          </div>
        </div>
      `);
      const win = document.querySelector('.window.active');
      win.querySelector('.folder-content').addEventListener('click', (e) => {
        const file = e.target.closest('.file');
        if (!file) return;
        if(file.dataset.file === "latest-briefing") {
          createWindow('LATEST-BRIEFING.pdf', `
            <div class="text-viewer" style="font-size:14px;">
<big><b>CONFIDENTIAL</b></big><br>
The people deserve the truth. You must bring me that projector at all costs. I have swapped the tapes at base ████ it seems he hasn't realized it yet. The plan is proceeding well we need to get the projector closer to point V. Once the tape is played all will be known. The full extent of what is going on will be known..
            </div>
          `);
        } else if(file.dataset.file === "threat-list") {
          createWindow('THREAT-LIST.log', `
            <div class="text-viewer" style="font-size:14px;">
# List of Current Threats:
1) Level 990 - Unstable ground detected
2) Secure ████
3) Discrepancy: Staff count for the Hub is diffrent from the count in the logs.
4) Unauthorized device connected (SCP-2306)
            </div>
          `);
        }
      });
    },
    'internet': () => {
      createWindow('USDOD SECURE BROWSER', `
        <div class="browser">
          <div class="browser-toolbar">
            <svg viewBox="0 0 24 24" style="width:24px;height:24px;margin-right:8px;">
              <circle cx="12" cy="12" r="10" fill="#003366"/>
              <rect x="6" y="6" width="12" height="4" fill="#fff"/>
              <rect x="6" y="14" width="12" height="4" fill="#fff"/>
            </svg>
            <span style="font-family:monospace;">https://secure-intranet.mil/landing</span>
          </div>
          <div class="browser-content">
            <h1 style="color:#003366;margin-bottom:10px;">USDOD SECURE INTRANET</h1>
            <p>This workstation is connected to a secure Department of Defense network.</p>
            <div style="margin:18px 0;">

            </div>
            <div style="background:#eef;border:1px solid #ccd;padding:18px;font-size:15px;max-width:370px;">
              <b>Notice:</b> Web browsing, search, and external access are disabled.
              <br>For approved resources, open local documentation.
              <br><span style="color:#f00;">INTERNET ACCESS: <b>RESTRICTED TO AUTHORIZED PERSONNEL</b></span>
              <br>(Contact Network Administrator for access escalation.)
            </div>
          </div>
        </div>
      `, 650);
    },
    'network': () => {
      createWindow('WiFi Networks', `
        <div class="network-interface">
          <div class="network-header">
            <h3>WiFi Network Connections</h3>
            <p>Select a network to connect:</p>
          </div>
          <div class="network-list" style="margin-bottom:12px;">
            <div class="network-item" data-ssid="SITE-19-SECURE">
              <div>
                <div class="network-name">SITE-19-SECURE</div>
                <div class="network-type">Secured</div>
                <div class="network-strength">Signal: Strong</div>
              </div>
              <button class="connect-btn" disabled>Access Denied</button>
            </div>
            <div class="network-item" data-ssid="BackroomsNet">
              <div>
                <div class="network-name">BackroomsNet</div>
                <div class="network-type">Unknown</div>
                <div class="network-strength">Signal: ???</div>
              </div>
              <button class="connect-btn" disabled>Error</button>
            </div>
            <div class="network-item" data-ssid="Level_0_Public">
              <div>
                <div class="network-name">Level_0_Public</div>
                <div class="network-type">Open</div>
                <div class="network-strength">Signal: Weak</div>
              </div>
              <button class="connect-btn">Connect</button>
            </div>
            <div class="network-item${currentNetwork==='SCPF-Guest'?' connected':''}" data-ssid="SCPF-Guest">
              <div>
                <div class="network-name">SCPF-Guest</div>
                <div class="network-type">WPA2</div>
                <div class="network-strength">Signal: Medium</div>
              </div>
              <button class="connect-btn">${currentNetwork==='SCPF-Guest'?'Connected':'Connect'}</button>
            </div>
          </div>
          <div class="network-status">
            <p>Current Connection: <b class="curr-network">${currentNetwork||'--'}</b></p>
            <p>Status: <span class="net-status">${currentNetwork?'Connected':'--'}</span></p>
          </div>
        </div>
      `);
      // Add logic for connecting
      const win = document.querySelector('.window.active');
      win.querySelector('.network-list').addEventListener('click', e => {
        const btn = e.target.closest('.connect-btn');
        if(!btn || btn.disabled) return;
        const netItem = btn.closest('.network-item');
        const ssid = netItem.dataset.ssid;
        if (['Level_0_Public','SCPF-Guest'].includes(ssid)) {
          btn.textContent='Connecting...';
          btn.disabled = true;
          setTimeout(()=>{
            currentNetwork = ssid;
            btn.textContent="Connected";
            Array.from(win.querySelectorAll('.connect-btn')).forEach(b=>{if(b!==btn) b.textContent='Connect';});
            win.querySelector('.curr-network').textContent = currentNetwork;
            win.querySelector('.net-status').textContent = "Connected";
          },1200);
        } else {
          alert('Access Denied.');
        }
      });
    }
  });

  // update icons to be consistently interactable, but leave handler as above (already attaches event listener to all .icon)
  // No further code needed here because all relevant icons now have a handler in `programs`.

  const startMenu = {
    init() {
      const startButton = document.querySelector('.start-button');
      const menu = document.createElement('div');
      menu.className = 'start-menu';
      menu.innerHTML = `
        <div class="start-menu-header">
          <div class="user-info">
            <svg viewBox="0 0 32 32" class="user-icon">
              <circle cx="16" cy="16" r="16" fill="#008080"/>
              <text x="16" y="20" text-anchor="middle" fill="white" font-size="12">U</text>
            </svg>
            <span>USDOD-USER</span>
          </div>
        </div>
        <div class="start-menu-items">
          <div class="start-item" data-program="my-computer">
            <svg viewBox="0 0 24 24" class="start-icon">
              <rect x="4" y="4" width="16" height="12" fill="#ccc"/>
              <rect x="7" y="16" width="10" height="4" fill="#999"/>
            </svg>
            My Computer
          </div>
          <div class="start-item" data-program="internet">
            <svg viewBox="0 0 24 24" class="start-icon">
              <circle cx="12" cy="12" r="10" fill="#0078D7"/>
              <text x="12" y="16" text-anchor="middle" fill="white" font-size="12">e</text>
            </svg>
            Internet
          </div>
          <div class="start-item" data-program="network">
            <svg viewBox="0 0 24 24" class="start-icon">
              <circle cx="12" cy="12" r="8" fill="#4169E1"/>
              <path d="M8 12h8M12 8v8" stroke="white" stroke-width="2"/>
            </svg>
            Network
          </div>
          <div class="start-menu-separator"></div>
          <div class="start-item" data-program="classified">
            <svg viewBox="0 0 24 24" class="start-icon">
              <path d="M4 4h16v16H4z" fill="#fc0"/>
              <text x="12" y="14" text-anchor="middle" font-size="8" fill="black">TOP</text>
              <text x="12" y="20" text-anchor="middle" font-size="8" fill="black">SECRET</text>
            </svg>
            Classified Files
          </div>
          <div class="start-item" data-program="scp">
            <svg viewBox="0 0 24 24" class="start-icon">
              <rect x="2" y="2" width="20" height="20" fill="#000"/>
              <text x="12" y="14" text-anchor="middle" fill="#f00" font-size="8">SCP</text>
              <text x="12" y="20" text-anchor="middle" fill="#f00" font-size="6">DATABASE</text>
            </svg>
            SCP Database
          </div>
          <div class="start-menu-separator"></div>
          <div class="start-item shutdown">
            <svg viewBox="0 0 24 24" class="start-icon">
              <circle cx="12" cy="12" r="10" fill="#ff0000"/>
              <path d="M8 12h8M12 8v8" stroke="white" stroke-width="2"/>
            </svg>
            Shut Down...
          </div>
        </div>
      `;
      
      document.body.appendChild(menu);
      
      let isMenuOpen = false;
      
      startButton.addEventListener('click', (e) => {
        e.stopPropagation();
        isMenuOpen = !isMenuOpen;
        menu.style.display = isMenuOpen ? 'block' : 'none';
        startButton.classList.toggle('active', isMenuOpen);
      });
      
      menu.addEventListener('click', (e) => {
        const item = e.target.closest('.start-item');
        if (!item) return;
        
        if (item.classList.contains('shutdown')) {
          alert('ACCESS DENIED: System shutdown requires ADMIN clearance.');
          return;
        }
        
        const program = item.dataset.program;
        if (programs[program]) {
          programs[program]();
        }
        
        isMenuOpen = false;
        menu.style.display = 'none';
        startButton.classList.remove('active');
      });
      
      document.addEventListener('click', (e) => {
        if (!menu.contains(e.target) && !startButton.contains(e.target)) {
          isMenuOpen = false;
          menu.style.display = 'none';
          startButton.classList.remove('active');
        }
      });
    }
  };

  startMenu.init();

  document.querySelectorAll('.icon').forEach(icon => {
    icon.addEventListener('click', () => {
      const program = icon.dataset.program;
      if (programs[program]) {
        programs[program]();
      }
    });
  });
});