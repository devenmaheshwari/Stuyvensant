// Deven Maheshwari
// SoftDev 
// K32 More Moving Parts
// 2022-02-18

// access canvas and buttons via DOM
let c = document.getElementById("playground");
let dotButton = document.getElementById("buttonCircle");
let logoButton = document.getElementById("buttonLogo");
let stopButton = document.getElementById("buttonStop");

// prepare to interact with canvas in 2D
let ctx = c.getContext("2d");

// set fill color to team color
ctx.fillStyle = "purple";

// create image instance
let logo = new Image(50, 100); 
logo.src = "logo_dvd.jpg";

let requestID;  // init global let for use with animation frames


let clear = (e) => {
  console.log("clear invoked...");
  ctx.clearRect(0, 0, c.clientWidth, c.clientHeight);
};


let radius = 0;
let growing = true;


let drawDot = () => {
  console.log("drawDot invoked...");

  window.cancelAnimationFrame(requestID);
  clear();

  if (growing) {
    radius += 2;
  } else {
    radius -= 2;
  }
  
  ctx.beginPath();
  ctx.arc(c.clientWidth/2, c.clientHeight/2, radius, 0, 360);
  ctx.fill();
  ctx.stroke();
  
  if (radius >= c.clientWidth/2) {
    growing = false;
  } else if (radius <= 0) {
    growing = true;
  }

  requestID = window.requestAnimationFrame(drawDot);
};

let xcor = Math.floor(Math.random() * (c.width - logo.width)); // Values can be switched based on canvas and img size
let ycor = Math.floor(Math.random() * (c.height - logo.height));
let movex = -1;
let movey = 1;

let moveLogo = () => { 
    console.log("moveLogo invoked...");
  
    requestID = window.cancelAnimationFrame(requestID);
    clear();
    ctx.beginPath(); 
    ctx.drawImage(logo, xcor, ycor, logo.width, logo.height); 

    if (xcor <= 0 || xcor >= (c.width - logo.width)) {
        movex = -1 * movex; 
    };
    if (ycor <= 0 || ycor >= (c.height - logo.height)) {
        movey *= -1 * movey; 
    };

    xcor += movex; 
    ycor += movey; 

    requestID = window.requestAnimationFrame(moveLogo);
  };


let stopIt = () => {
  console.log("stopIt invoked...")
  console.log(requestID);
  window.cancelAnimationFrame(requestID);
};


dotButton.addEventListener("click", drawDot);
logoButton.addEventListener("click", moveLogo);
stopButton.addEventListener("click", stopIt);
