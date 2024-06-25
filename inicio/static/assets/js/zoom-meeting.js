ZoomMtg.preLoadWasm();
ZoomMtg.prepareJssdk();

function startMeeting(signature, apiKey, meetingNumber, userName, userEmail, passWord) {
    ZoomMtg.init({
        leaveUrl: 'http://www.yourwebsite.com',
        success: function () {
            ZoomMtg.join({
                signature: signature,
                apiKey: apiKey,
                meetingNumber: meetingNumber,
                userName: userName,
                userEmail: userEmail,
                passWord: passWord,
                success: function (res) {
                    console.log('join meeting success');
                },
                error: function (res) {
                    console.log(res);
                }
            });
        },
        error: function (res) {
            console.log(res);
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    // Llamada a la función startMeeting con los valores adecuados
    const signature = 'YOUR_GENERATED_SIGNATURE';
    const apiKey = 'YOUR_API_KEY';
    const meetingNumber = 'YOUR_MEETING_NUMBER';
    const userName = 'YOUR_USER_NAME';
    const userEmail = 'YOUR_USER_EMAIL'; 
    const passWord = 'YOUR_MEETING_PASSWORD';

    startMeeting(signature, apiKey, meetingNumber, userName, userEmail, passWord);
});
