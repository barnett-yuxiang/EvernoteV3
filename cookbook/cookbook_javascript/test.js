// JavaScript 继承的方式

function Parent(name) {
    this.name = 'parent';
}

Parent.prototype.getName = function() {
    return this.name;
}

function Child() {
    this.age = 18;
}

Child.prototype = new Parent();

let child = new Child();
console.log(child.getName()); // parent
console.log(child.age); // 18
