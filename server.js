const express = require('express');
const bodyParser = require('body-parser');
const session = require('express-session');
const WebSocket = require('ws');
const http = require('http');

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

app.use(express.static('static'));
app.set('view engine', 'ejs');
app.set('views', './inicio');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(session({
    secret: 'your-secret-key',
    resave: false,
    saveUninitialized: true,
}));

app.get('/', (req, res) => {
    if (!req.session.username) {
        return res.redirect('/login');
    }
    res.render('index', { username: req.session.username });
});

app.get('/login', (req, res) => {
    res.render('login');
});

app.post('/login', (req, res) => {
    req.session.username = req.body.username;
    res.redirect('/');
});

let publicClients = [];
let privateClients = {};

wss.on('connection', (ws) => {
    let room = null;
    let username = null;

    ws.on('message', (message) => {
        const data = JSON.parse(message);

        if (data.type === 'join') {
            room = data.room;
            username = data.username;

            if (room === 'public') {
                publicClients.push({ ws, username });
            } else {
                if (!privateClients[room]) {
                    privateClients[room] = [];
                }
                privateClients[room].push({ ws, username });
            }
        } else if (data.type === 'message') {
            if (room === 'public') {
                publicClients.forEach(client => {
                    if (client.ws !== ws && client.ws.readyState === WebSocket.OPEN) {
                        client.ws.send(JSON.stringify({ type: 'message', username: username, content: data.content }));
                    }
                });
            } else {
                if (privateClients[room]) {
                    privateClients[room].forEach(client => {
                        if (client.ws !== ws && client.ws.readyState === WebSocket.OPEN) {
                            client.ws.send(JSON.stringify({ type: 'message', username: username, content: data.content }));
                        }
                    });
                }
            }
        }
    });

    ws.on('close', () => {
        if (room === 'public') {
            publicClients = publicClients.filter(client => client.ws !== ws);
        } else {
            if (privateClients[room]) {
                privateClients[room] = privateClients[room].filter(client => client.ws !== ws);
            }
        }
    });
});

server.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});
