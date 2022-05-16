const name = prompt("enter your name: ", "jack");
const element = document.createElement("p");
element.textContent(`hello ${name}`);
document.append(element);