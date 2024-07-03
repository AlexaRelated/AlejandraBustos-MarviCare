document.addEventListener('DOMContentLoaded', (event) => {
    const chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/chat/'
    );

    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        const messageElement = document.createElement('div');
        messageElement.innerText = `${data.username}: ${data.message}`;
        document.getElementById('chat-log').appendChild(messageElement);
    };

    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

    document.getElementById('chat-message-input').focus();
    document.getElementById('chat-message-input').onkeyup = function(e) {
        if (e.keyCode === 13) {  // Presiona Enter para enviar
            document.getElementById('chat-message-submit').click();
        }
    };

    document.getElementById('chat-message-submit').onclick = function(e) {
        const messageInputDom = document.getElementById('chat-message-input');
        const message = messageInputDom.value;
        chatSocket.send(JSON.stringify({
            'message': message
        }));
        messageInputDom.value = '';
    };
});
