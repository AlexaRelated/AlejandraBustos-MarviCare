document.addEventListener('DOMContentLoaded', () => {
    // Establecer conexión WebSocket
    const chatSocket = new WebSocket(
        'ws://' + window.location.hostname + ':8001/ws/chat/'
    );

    // Función para procesar mensajes recibidos desde el servidor
    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        if (data.command === 'new_message') {
            // Mostrar nuevo mensaje en el chat-log
            const messageElement = document.createElement('div');
            messageElement.innerText = `${data.username}: ${data.message}`;
            document.getElementById('chat-log').appendChild(messageElement);
        } else if (data.command === 'user_list') {
            // Actualizar la lista de usuarios conectados
            const userListElement = document.getElementById('user-list');
            userListElement.innerHTML = '';
            data.users.forEach(user => {
                const userElement = document.createElement('div');
                userElement.innerText = user.username;
                userListElement.appendChild(userElement);
            });
        }
    };

    // Manejar cierre inesperado de la conexión WebSocket
    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

    // Enfocar el input de mensaje cuando se carga la página
    document.getElementById('chat-message-input').focus();

    // Enviar mensaje cuando se presiona Enter
    document.getElementById('chat-message-input').onkeyup = function(e) {
        if (e.keyCode === 13) {  // Código 13 es la tecla Enter
            document.getElementById('chat-message-submit').click();
        }
    };

    // Enviar mensaje cuando se hace clic en el botón de enviar
    document.getElementById('chat-message-submit').onclick = function(e) {
        const messageInputDom = document.getElementById('chat-message-input');
        const message = messageInputDom.value.trim();  // Eliminar espacios en blanco al inicio y final
        if (message !== '') {
            // Enviar mensaje al servidor a través de WebSocket
            chatSocket.send(JSON.stringify({
                'command': 'new_message',
                'message': message
            }));
        }
        // Limpiar el input de mensaje después de enviar
        messageInputDom.value = '';
    };

    // Función para actualizar la lista de usuarios conectados
    function updateUserList(users) {
        const userListElement = document.getElementById('user-list');
        userListElement.innerHTML = '';
        users.forEach(user => {
            const userElement = document.createElement('div');
            userElement.innerText = user.username;
            userListElement.appendChild(userElement);
        });
    }
});
