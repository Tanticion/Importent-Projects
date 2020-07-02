document.querySelector(".w").addEventListener("click",w)
document.querySelector(".a").addEventListener("click",a)
document.querySelector(".s").addEventListener("click",s)
document.querySelector(".d").addEventListener("click",d)
document.querySelector(".j").addEventListener("click",j)
document.querySelector(".k").addEventListener("click",k)
document.querySelector(".l").addEventListener("click",l)
document.addEventListener("keydown",wa)
document.addEventListener("keydown",wa)
document.addEventListener("keydown",wa)
document.addEventListener("keydown",wa)
document.addEventListener("keydown",wa)
document.addEventListener("keydown",wa)
document.addEventListener("keydown",wa)



function w() {
  this.style.color ='white'
  var audio = new Audio("sounds/crash.mp3")
  audio.play()
  var v = document.querySelectorAll(".drum")[0]
  v.classList.add("pressed")
  setTimeout(function () {
    v.classList.remove("pressed")
  }, 100);


}
function a() {
  this.style.color ='white'
  var audio = new Audio("sounds/kick-bass.mp3")
  audio.play()
  var v = document.querySelectorAll(".drum")[1]
  v.classList.add("pressed")
  setTimeout(function () {
    v.classList.remove("pressed")
  }, 100);

}
function s() {
  this.style.color ='white'
  var audio = new Audio("sounds/snare.mp3")
  audio.play()
  var v = document.querySelectorAll(".drum")[2]
  v.classList.add("pressed")
  setTimeout(function () {
    v.classList.remove("pressed")
  }, 100);

}
function d() {
  this.style.color ='white'
  var audio = new Audio("sounds/tom-1.mp3")
  audio.play()
  var v = document.querySelectorAll(".drum")[3]
  v.classList.add("pressed")
  setTimeout(function () {
    v.classList.remove("pressed")
  }, 100);

}
function j() {
  this.style.color ='white'
  var audio = new Audio("sounds/tom-2.mp3")
  audio.play()
  var v = document.querySelectorAll(".drum")[4]
  v.classList.add("pressed")
  setTimeout(function () {
    v.classList.remove("pressed")
  }, 100);
}
function k() {
  this.style.color ='white'
  var audio = new Audio("sounds/tom-3.mp3")
  audio.play()
  var v = document.querySelectorAll(".drum")[5]
  v.classList.add("pressed")
  setTimeout(function () {
    v.classList.remove("pressed")
  }, 100);
}
function l() {
  this.style.color ='white'
  var audio = new Audio("sounds/tom-4.mp3")
  audio.play()
  var v = document.querySelectorAll(".drum")[6]
  v.classList.add("pressed")
  setTimeout(function () {
    v.classList.remove("pressed")
  }, 100);
}


function wa(val) {

  switch (val.key) {
    case "w":
    var audio = new Audio("sounds/crash.mp3")
    audio.play()
    var v = document.querySelectorAll(".drum")[0]
    v.classList.add("pressed")
    setTimeout(function () {
      v.classList.remove("pressed")
    }, 100);
      break;
    case "a":
    var audio = new Audio("sounds/kick-bass.mp3")
    audio.play()
    var v = document.querySelectorAll(".drum")[1]
    v.classList.add("pressed")
    setTimeout(function () {
      v.classList.remove("pressed")
    }, 100);
    break;
    case "s":
    var audio = new Audio("sounds/snare.mp3")
    audio.play()
    var v = document.querySelectorAll(".drum")[2]
    v.classList.add("pressed")
    setTimeout(function () {
      v.classList.remove("pressed")
    }, 100);
    break;
    case "d":
    var audio = new Audio("sounds/tom-1.mp3")
    audio.play()
    var v = document.querySelectorAll(".drum")[3]
    v.classList.add("pressed")
    setTimeout(function () {
      v.classList.remove("pressed")
    }, 100);
    break;
    case "j":
    var audio = new Audio("sounds/tom-2.mp3")
    audio.play()
    var v = document.querySelectorAll(".drum")[4]
    v.classList.add("pressed")
    setTimeout(function () {
      v.classList.remove("pressed")
    }, 100);
    break;
    case "k":
    var audio = new Audio("sounds/tom-3.mp3")
    audio.play()
    var v = document.querySelectorAll(".drum")[5]
    v.classList.add("pressed")
    setTimeout(function () {
      v.classList.remove("pressed")
    }, 100);
    break;
    case "l":
    var audio = new Audio("sounds/tom-4.mp3")
    audio.play()
    var v = document.querySelectorAll(".drum")[3]
    v.classList.add("pressed")
    setTimeout(function () {
      v.classList.remove("pressed")
    }, 100);
    break;




  }
}
