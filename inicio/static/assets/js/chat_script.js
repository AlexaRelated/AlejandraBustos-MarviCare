// chat_script.js

let ws;
const chatLog = document.querySelector('#chat-log');
const messageInput = document.querySelector('#chat-message-input');
const messageSubmit = document.querySelector('#chat-message-submit');
const roomSelect = document.querySelector('#room');
const privateRoomInput = document.querySelector('#private-room');

document.addEventListener('DOMContentLoaded', function() {
    const joinRoomButton = document.querySelector('#join-room');

    joinRoomButton.addEventListener('click', () => {
        if (ws) {
            ws.close();
        }
        const selectedRoom = roomSelect.value;
        const privateRoom = privateRoomInput.value;

        const room = selectedRoom === 'public' ? 'public' : privateRoom;
        ws = new WebSocket('ws://localhost:3000');

        ws.onopen = function() {
            console.log('WebSocket connection established');
            ws.send(JSON.stringify({ type: 'join', room: room, username: username }));
        };

        ws.onmessage = function(event) {
            const data = JSON.parse(event.data);
            if (data.type === 'message') {
                chatLog.innerHTML += '<p>' + data.message + '</p>';
            }
        };

        ws.onerror = function(error) {
            console.error('WebSocket error ', error);
        };

        ws.onclose = function(event) {
            console.log('WebSocket connection closed', event);
        };
    });

    messageSubmit.addEventListener('click', function() {
        const message = messageInput.value;
        ws.send(JSON.stringify({ type: 'message', message: message }));
        messageInput.value = '';
    });

    messageInput.addEventListener('keyup', function(event) {
        if (event.key === 'Enter') {
            messageSubmit.click();
        }
    });
});
