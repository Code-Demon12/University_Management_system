const chatbotIcon = document.getElementById("chatbot-icon")
const chatbotBox = document.getElementById("chatbot-box")
const chatbotClose = document.getElementById("chatbot-close")

const input = document.getElementById("chatbot-input")
const sendBtn = document.getElementById("chatbot-send")
const messages = document.getElementById("chatbot-messages")

// open chatbot
chatbotIcon.onclick = () => {
chatbotBox.style.display = "flex"
}

// close chatbot
chatbotClose.onclick = () => {
chatbotBox.style.display = "none"
}

sendBtn.onclick = sendMessage

input.addEventListener("keypress",function(e){
if(e.key==="Enter") sendMessage()
})


// CSRF helper
function getCookie(name) {
let cookieValue = null;
if (document.cookie && document.cookie !== '') {
const cookies = document.cookie.split(';');
for (let i = 0; i < cookies.length; i++) {
const cookie = cookies[i].trim();
if (cookie.substring(0, name.length + 1) === (name + '=')) {
cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
break;
}
}
}
return cookieValue;
}


// send message
async function sendMessage(){

let message = input.value.trim()

if(message==="") return

messages.innerHTML += `
<div style="text-align:right;margin:6px">
<b>You:</b> ${message}
</div>
`

input.value=""

messages.innerHTML += `
<div id="typing">AI is typing...</div>
`

messages.scrollTop = messages.scrollHeight

let response = await fetch("ai-chatbot/",{
method:"POST",
headers:{
"Content-Type":"application/json",
"X-CSRFToken": getCookie("csrftoken")
},
body:JSON.stringify({message:message})
})

let data = await response.json()

document.getElementById("typing").remove()

messages.innerHTML += `
<div style="margin:6px;color:blue">
<b>Assistant:</b> ${data.reply}
</div>
`

messages.scrollTop = messages.scrollHeight
}