/*!
* Start Bootstrap - Grayscale v7.0.6 (https://startbootstrap.com/theme/grayscale)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-grayscale/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            rootMargin: '0px 0px -40%',
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});

const submitButton = document.getElementById("submit-button");
const commentInput = document.getElementById("comment-input");
const commentsContainer = document.getElementById("comments-container");

submitButton.addEventListener("click", function() {
  const comment = commentInput.value;
  const commentElement = document.createElement("div");
  commentElement.innerHTML = comment;
  commentsContainer.appendChild(commentElement);
  commentInput.value = "";
    
});

document.addEventListener('DOMContentLoaded', (event) => {
    let ws;
    const chatLog = document.querySelector('#chat-log');
    const messageInput = document.querySelector('#chat-message-input');
    const messageSubmit = document.querySelector('#chat-message-submit');
    const roomSelect = document.querySelector('#room');
    const privateRoomInput = document.querySelector('#private-room');
    const joinRoomButton = document.querySelector('#join-room');
    const username = 'username'; // Cambia esto según sea necesario

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
