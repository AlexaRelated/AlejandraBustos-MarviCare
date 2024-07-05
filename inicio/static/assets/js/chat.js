const chatLog = document.querySelector('#chat-log');
const messageInput = document.querySelector('#chat-message');
const messageSubmit = document.querySelector('#chat-send');

const ws = new WebSocket('ws://localhost:3000');

ws.onopen = function() {
    console.log('WebSocket connection established');
};

ws.onmessage = function(event) {
    const messageData = JSON.parse(event.data);
    const username = messageData.username;
    const message = messageData.message;
    chatLog.innerHTML += `<p><strong>${username}</strong>: ${message}</p>`;
};

ws.onerror = function(error) {
    console.error('WebSocket error ', error);
};

ws.onclose = function(event) {
    console.log('WebSocket connection closed', event);
};

messageSubmit.addEventListener('click', function() {
    const message = messageInput.value;
    // Simplemente envía el mensaje como JSON con 'username' y 'message'
    ws.send(JSON.stringify({ username: 'NombreUsuario', message: message }));
    messageInput.value = '';
});

messageInput.addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        messageSubmit.click();
    }
});
