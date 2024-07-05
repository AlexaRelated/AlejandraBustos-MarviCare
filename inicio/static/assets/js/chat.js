
// Esta función agrega un mensaje al chat
function addMessage(message) {
    var chatLog = document.getElementById('chat-log');
    var messageElement = document.createElement('div');
    messageElement.textContent = message;
    chatLog.appendChild(messageElement);
}

// Esta función agrega un usuario a la lista de usuarios
function addUser(username) {
    var userList = document.getElementById('user-list');
    var userElement = document.createElement('li');
    userElement.textContent = username;
    userList.appendChild(userElement);
}

// Ejemplo de manejo del formulario de chat
document.getElementById('chat-send').addEventListener('click', function() {
    var messageInput = document.getElementById('chat-message');
    var message = messageInput.value.trim();
    if (message !== '') {
        // Aquí puedes enviar el mensaje a través de WebSocket u otro método
        addMessage('Yo: ' + message);
        messageInput.value = '';
    }
});

// Ejemplo de actualización de usuarios (puedes adaptarlo a tu lógica)
function updateUsers(users) {
    var userList = document.getElementById('user-list');
    userList.innerHTML = ''; // Limpiar la lista actual
    users.forEach(function(user) {
        addUser(user.username);
    });
}

// Aquí puedes agregar más funciones para manejar WebSocket y otras funcionalidades
