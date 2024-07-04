document.addEventListener("DOMContentLoaded", function () {
    const chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/chat/'
    );

    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        console.log("Data received from WebSocket:", data); // Log para verificar los datos recibidos
        if (data.message && data.username) {
            const chatLog = document.getElementById('chat-log');
            chatLog.innerHTML += `<div><strong>${data.username}:</strong> ${data.message}</div>`;
        } else if (data.users) {
            updateUserList(data.users);
        }
    };

    chatSocket.onopen = function(e) {
        console.log("WebSocket connection opened:", e);
    };

    chatSocket.onclose = function(e) {
        console.log("WebSocket connection closed:", e);
    };

    chatSocket.onerror = function(e) {
        console.log("WebSocket error:", e);
    };

    function updateUserList(users) {
        const userList = document.getElementById('user-list');
        userList.innerHTML = ''; // Clear the current list
        users.forEach(function(user) {
            const userItem = document.createElement('li');
            userItem.textContent = user.username;
            userList.appendChild(userItem);
        });
    }

    document.getElementById('chat-send').onclick = function() {
        const messageInput = document.getElementById('chat-message');
        const message = messageInput.value;
        chatSocket.send(JSON.stringify({
            'message': message
        }));
        messageInput.value = '';
    };
});
