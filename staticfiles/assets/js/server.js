const express = require('express');
const crypto = require('crypto');
const app = express();

app.use(express.static('static'));
app.set('view engine', 'ejs');

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

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
