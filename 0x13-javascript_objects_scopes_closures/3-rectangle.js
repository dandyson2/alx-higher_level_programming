#!/usr/bin/node
#!/usr/bin/node
module.exports = class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    if (this.width && this.height) {
      console.log('X'.repeat(this.width).repeat(this.height));
    }
  }
};
