document.addEventListener("DOMContentLoaded", function() {
    const chatLog = document.querySelector('#chat-log');
    const chatMessageInput = document.querySelector('#chat-message-input');
    const chatMessageSubmit = document.querySelector('#chat-message-submit');
    const roomNameSelect = document.querySelector('#room-name');
    const userSelect = document.querySelector('#user-select');

    let roomName = roomNameSelect.value;
    let chatSocket = null;

    function connectToRoom(roomName) {
        if (chatSocket) {
            chatSocket.close();
        }

        chatSocket = new WebSocket(
            'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
        );

        chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);
            const message = data['message'];
            chatLog.value += (message + '\n');
        };

        chatSocket.onclose = function(e) {
            console.error('Chat socket closed unexpectedly');
        };

        chatMessageSubmit.onclick = function(e) {
            const message = chatMessageInput.value;
            chatSocket.send(JSON.stringify({
                'message': message
            }));
            chatMessageInput.value = '';
        };
    }

    roomNameSelect.addEventListener('change', function(e) {
        roomName = roomNameSelect.value;
        connectToRoom(roomName);
    });

    userSelect.addEventListener('change', function(e) {
        const selectedUser = userSelect.value;
        if (selectedUser) {
            roomName = `private-${selectedUser}`;
            connectToRoom(roomName);
        }
    });

    function loadUsers() {
        fetch('/mensajes/get_users/')
            .then(response => response.json())
            .then(users => {
                users.forEach(user => {
                    const option = document.createElement('option');
                    option.value = user.username;
                    option.textContent = user.username;
                    userSelect.appendChild(option);
                });
            });
    }

    loadUsers();
    connectToRoom(roomName);
});
