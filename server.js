const express = require('express');
const crypto = require('crypto');
const WebSocket = require('ws');
const http = require('http');
const path = require('path');
const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

app.use(express.static('static'));
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'inicio'));  // Ajusta la ruta a la carpeta "inicio"

function generateSignature(apiKey, apiSecret, meetingNumber, role) {
    const timestamp = new Date().getTime() - 30000;
    const msg = Buffer.from(apiKey + meetingNumber + timestamp + role).toString('base64');
    const hash = crypto.createHmac('sha256', apiSecret).update(msg).digest('base64');
    const signature = Buffer.from(`${apiKey}.${meetingNumber}.${timestamp}.${role}.${hash}`).toString('base64');
    return signature;
}

app.get('/', (req, res) => {
    const apiKey = 'YOUR_API_KEY';
    const apiSecret = 'YOUR_API_SECRET';
    const meetingNumber = 'YOUR_MEETING_NUMBER';
    const role = 0; // 0 para participante, 1 para anfitrión

    const signature = generateSignature(apiKey, apiSecret, meetingNumber, role);
    res.render('index', { signature: signature });
});

wss.on('connection', (ws) => {
    console.log('New WebSocket connection');
    ws.on('message', (message) => {
        console.log('Received:', message);
        // Broadcasting the message to all connected clients
        wss.clients.forEach(client => {
            if (client.readyState === WebSocket.OPEN) {
                client.send(message);
            }
        });
    });

    ws.on('close', () => {
        console.log('WebSocket connection closed');
    });
});

server.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});
