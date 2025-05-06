export class Window {
  constructor(windowElement, windowManager) {
    this.windowElement = windowElement;
    this.windowManager = windowManager;
    this.isDragging = false;
    this.dragOffset = { x: 0, y: 0 };
    this.isResizing = false;
    this.resizeStart = { x: 0, y: 0 };
    this.startWidth = 0;
    this.startHeight = 0;

    this.header = this.windowElement.querySelector('.window-header');
    this.header.addEventListener('mousedown', this.startDrag.bind(this));

    this.windowElement.addEventListener('mouseup', this.endDrag.bind(this));
    document.addEventListener('mousemove', this.dragWindow.bind(this)); 
    this.windowElement.addEventListener('mouseleave', this.endDrag.bind(this));
    this.windowElement.addEventListener('blur', this.endDrag.bind(this)); 

    this.createResizeHandle();
  }

  createResizeHandle() {
    this.resizeHandle = document.createElement('div');
    this.resizeHandle.classList.add('resize-handle');
    this.windowElement.appendChild(this.resizeHandle);
    this.resizeHandle.addEventListener('mousedown', this.startResize.bind(this));
  }

  startDrag(event) {
    if (event.target === this.resizeHandle) return;
    this.isDragging = true;
    this.dragOffset = {
      x: event.clientX - this.windowElement.offsetLeft,
      y: event.clientY - this.windowElement.offsetTop
    };
    this.windowElement.style.cursor = 'grabbing'; 
    event.preventDefault();
  }

  dragWindow(event) {
    if (this.isDragging) {
      const x = event.clientX - this.dragOffset.x;
      const y = event.clientY - this.dragOffset.y;
      this.windowElement.style.left = x + 'px';
      this.windowElement.style.top = y + 'px';
    }
    if (this.isResizing) {
      const dx = event.clientX - this.resizeStart.x;
      const dy = event.clientY - this.resizeStart.y;
      const newWidth = Math.max(this.startWidth + dx, 150); 
      const newHeight = Math.max(this.startHeight + dy, 100); 
      this.windowElement.style.width = newWidth + 'px';
      this.windowElement.style.height = newHeight + 'px';
    }
  }

  endDrag() {
    this.isDragging = false;
    this.isResizing = false;
    this.windowElement.style.cursor = 'grab';
  }

  startResize(event) {
    event.stopPropagation();
    this.isResizing = true;
    this.resizeStart = { x: event.clientX, y: event.clientY };
    this.startWidth = this.windowElement.offsetWidth;
    this.startHeight = this.windowElement.offsetHeight;
    event.preventDefault();
  }
}