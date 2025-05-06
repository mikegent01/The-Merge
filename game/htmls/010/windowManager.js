export class WindowManager {
  constructor(container) {
    this.container = container;
    this.windowCount = 0; // Initialize window count
  }

  openWindow(windowInstance) {
    const windowElement = windowInstance.windowElement;
    this.container.appendChild(windowElement);
    this.bringToFront(windowElement);
    this.windowCount++; // Increment window count

    // Focus the window
    windowElement.focus();
  }

  closeWindow(windowElement) {
    this.container.removeChild(windowElement);
    this.windowCount--; // Decrement window count
  }

  bringToFront(windowElement) {
    // Find the highest z-index among the windows.
    let highestZIndex = 0;
    const windows = this.container.querySelectorAll('.window');
    windows.forEach(win => {
      const zIndex = parseInt(win.style.zIndex) || 0;
      highestZIndex = Math.max(highestZIndex, zIndex);
    });

    // Set the z-index of the clicked window to be higher than all other windows.
    windowElement.style.zIndex = highestZIndex + 1;
  }
}