const socket = io();

function sendMessage() {
    const msgInput = document.getElementById("msg");
    const msg = msgInput.value;
    socket.emit("message", msg);
    msgInput.value = "";
}

socket.on("response", function(msg) {
    const li = document.createElement("li");
    li.textContent = msg;
    document.getElementById("messages").appendChild(li);
});
