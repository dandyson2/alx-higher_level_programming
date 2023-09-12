#!/usr/bin/node

class MyObject {
  constructor() {
    this.type = 'object';
    this.value = 12;
  }
}

const myObject = new MyObject();
console.log(myObject);

myObject.value = 89;
console.log(myObject);
