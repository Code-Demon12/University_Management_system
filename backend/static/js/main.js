"use strict";

// side navigation bar
function toggleSidebar() {

  const sideNav = document.getElementById("side-nav");
  const main = document.getElementById("main");
  const topNavbar = document.getElementById("top-navbar");
  const manageWrap = document.querySelector(".manage-wrap");

  if (sideNav) sideNav.classList.toggle("toggle-active");
  if (main) main.classList.toggle("toggle-active");
  if (topNavbar) topNavbar.classList.toggle("toggle-active");
  if (manageWrap) manageWrap.classList.toggle("toggle-active");

}

// #################################
// popup

var c = 0;
function pop() {
  if (c == 0) {
    document.getElementById("popup-box").style.display = "block";
    c = 1;
  } else {
    document.getElementById("popup-box").style.display = "none";
    c = 0;
  }
}

// const popupMessagesButtons = document.querySelectorAll('popup-btn-messages')

// popupMessagesButtons.forEach(button, () => {
//     button.addEventListener('click', () => {
//         document.getElementById('popup-box-messages').style.display = 'none';
//     })
// })

// const popupMessagesButtom = document.getElementById('popup-btn-messages')
// popupMessagesButtom.addEventListener('click', () => {
//     document.getElementById('popup-box-messages').style.display = 'none';
// })
// ##################################

// Example starter JavaScript for disabling form submissions if there are invalid fields
// Fetch all the forms we want to apply custom Bootstrap validation styles to
var forms = document.getElementsByClassName("needs-validation");

// Loop over them and prevent submission
Array.prototype.filter.call(forms, function (form) {
  form.addEventListener(
    "submit",
    function (event) {
      if (form.checkValidity() === false) {
        event.preventDefault();
        event.stopPropagation();
      }
      form.classList.add("was-validated");
    },
    false
  );
});
// ##################################

// extend and collapse
function showCourses(btn) {
  var btn = $(btn);

  if (collapsed) {
    btn.html('Collapse <i class="fas fa-angle-up"></i>');
    $(".hide").css("max-height", "unset");
    $(".white-shadow").css({ background: "unset", "z-index": "0" });
  } else {
    btn.html('Expand <i class="fas fa-angle-down"></i>');
    $(".hide").css("max-height", "150");
    $(".white-shadow").css({
      background: "linear-gradient(transparent 50%, rgba(255,255,255,.8) 80%)",
      "z-index": "2",
    });
  }
  collapsed = !collapsed;
}

$(document).ready(function () {
  $("#primary-search").focus(function () {
    $("#top-navbar").attr("class", "dim");
    $("#side-nav").css("pointer-events", "none");
    $("#main-content").css("pointer-events", "none");
  });
  $("#primary-search").focusout(function () {
    $("#top-navbar").removeAttr("class");
    $("#side-nav").css("pointer-events", "auto");
    $("#main-content").css("pointer-events", "auto");
  });
});
// chatbot open / close

const chatbotIcon = document.getElementById("chatbot-icon")
const chatbotBox = document.getElementById("chatbot-box")
const chatbotClose = document.getElementById("chatbot-close")

if(chatbotIcon){

chatbotIcon.onclick = function(){
chatbotBox.style.display = "flex"
}

chatbotClose.onclick = function(){
chatbotBox.style.display = "none"
}

}

// chatbot message send

const sendBtn = document.getElementById("chatbot-send")

if(sendBtn){

sendBtn.onclick = async function(){

let input = document.getElementById("chatbot-input")
let message = input.value

if(message.trim() === "") return

let messages = document.getElementById("chatbot-messages")

messages.innerHTML += "<p><b>You:</b> "+message+"</p>"

let response = await fetch("/chatbot/",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({message:message})
})

let data = await response.json()

messages.innerHTML += "<p><b>Bot:</b> "+data.reply+"</p>"

messages.scrollTop = messages.scrollHeight

input.value=""

}

}

