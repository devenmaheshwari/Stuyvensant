// Team Always Late :: Deven Maheshwari, David Chong
// SoftDev pd0
// K29 -- DOMfoolery++
// 2022-02-10
// --------------------------------------------------


// send diagnostic output to console
// (Ctrl-Shift-J in Firefox to reveal console)
console.log("AYO");

let i = "hello";
let j = 20;


// assign an anonymous fxn to a var
let f = function (x) {
  let j = 30;
  return j + x;
};


// instantiate an object
let o = {
  'name': 'Thluffy',
  age: 15,
  items: [10, 20, 30, 40],
  morestuff: { a: 1, b: 'ayo' },
  func: function (x) {
    return x + 30;
  }
};


let addItem = function (text) {
  let list = document.getElementById("thelist");
  let newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


let removeItem = function (n) {
  let listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


let red = function () {
  let items = document.getElementsByTagName("li");
  for (let i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


let stripe = function () {
  let items = document.getElementsByTagName("li");
  for (let i = 0; i < items.length; i++) {
    if (i % 2 == 0) {
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

// insert your implementations here for...
// FIB

let fib_index = 0; 
function fib (n) {
  let item = document.getElementById("fib");
  item.innerHTML = `fib(${fib_index}) = ${fib2(fib_index)}`; 
  fib_index++; 
}

function fib2 (n) {
  if (n <= 1) return n;
  return (fib2(n-1) + fib2(n-2))
}

document.getElementById("fibin").addEventListener("click", fib);

// FAC
let fac_index = 0; 
function fac (n) {
  let item = document.getElementById("fac");
  item.innerHTML = `fac(${fac_index}) = ${fac2(fac_index)}`
  fac_index++; 
}

function fac2 (n) {
  if (n <= 1) return 1;
  return n * fac2(n-1);
}

document.getElementById("facin").addEventListener("click", fac);

// GCD
let gcd_one = Math.round(Math.random() * 100);
let gcd_two = Math.round(Math.random() * 100);

function gcd (a, b) {
  let item = document.getElementById("gcd");
  item.innerHTML = `gcd(${gcd_one}, ${gcd_two}) = ${gcd2(gcd_one, gcd_two)}`; 
  gcd_one = Math.round(Math.random() * 100);
  gcd_two = Math.round(Math.random() * 100);
}

function gcd2 (a, b) {
  if (a == 0) return b;
  if (b == 0) return a;

  let c = Math.max(a, b);
  let d = Math.min(a, b);

  return gcd2(d, c % d);
}

document.getElementById("gcdin").addEventListener("click", gcd);