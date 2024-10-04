document.addEventListener('DOMContentLoaded', function() {
    // Obtén las referencias a los elementos del DOM
    const roomSelect = document.getElementById('room');
    const privateRoomInput = document.getElementById('private-room');
    const joinRoomButton = document.getElementById('join-room');
    const chatLog = document.getElementById('chat-log');
    const chatMessageInput = document.getElementById('chat-message-input');
    const chatMessageSubmitButton = document.getElementById('chat-message-submit');

    // Almacena el nombre de usuario desde el contexto de Django
    const username = '{{ user.username }}';

    // Conecta al servidor WebSocket de Django Channels
    const chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
    );

    // Maneja la conexión WebSocket
    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        chatLog.value += (data.username + ': ' + data.message + '\n');
    };

    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

    // Enviar mensaje al presionar Enter
    chatMessageInput.focus();
    chatMessageInput.onkeyup = function(e) {
        if (e.keyCode === 13) {  // Presionar Enter
            chatMessageSubmitButton.click();
        }
    };

    // Enviar mensaje al hacer clic en el botón
    chatMessageSubmitButton.onclick = function(e) {
        const messageInputDom = chatMessageInput.value;
        chatSocket.send(JSON.stringify({
            'username': username,
            'message': messageInputDom
        }));
        chatMessageInput.value = '';
    };

    // Funcionalidad de selección de sala de chat
    joinRoomButton.onclick = function() {
        const selectedRoom = roomSelect.value;
        if (selectedRoom === 'private') {
            const privateRoomId = privateRoomInput.value;
            if (privateRoomId) {
                // Conectar a la sala privada con el ID proporcionado
                chatSocket.send(JSON.stringify({
                    'command': 'join',
                    'room': privateRoomId
                }));
            }
        } else {
            // Conectar a la sala pública
            chatSocket.send(JSON.stringify({
                'command': 'join',
                'room': 'public'
            }));
        }
    };
});
