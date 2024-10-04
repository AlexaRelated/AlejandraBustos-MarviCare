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
