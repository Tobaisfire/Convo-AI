



document.addEventListener('DOMContentLoaded', function () {
    // Initial setup when the document is loaded
    startNewChat();
});

function startNewChat() {
    // Clear existing conversation
    clearConversation();

    // Update the UI
}

function clearConversation() {
    const messagesSection = document.getElementById('messagesSection');
    messagesSection.innerHTML = '';
}

function displayMessage(message) {
    // Display a message in the chat UI
    const messagesSection = document.getElementById('messagesSection');
    const messageContainer = document.createElement('div');
    messageContainer.className = 'message-container';
    messageContainer.textContent = message;
    messagesSection.appendChild(messageContainer);
}

// function sendMessage() {
//     var userMessage = document.getElementById('userMessage').value;

//     if (userMessage.trim() !== '') {
//         // Display user message immediately
//         var userMessageContainer = createMessageContainer('user-message', 'User', userMessage);
//         document.getElementById('messagesSection').appendChild(userMessageContainer);

//         // Clear the input field
//         document.getElementById('userMessage').value = '';

//         // Send user message to the server and wait for the bot's reply
//         fetch('/send_message', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/x-www-form-urlencoded',
//             },
//             body: 'user_message=' + encodeURIComponent(userMessage),
//         })
//         .then(response => response.json())
//         .then(data => {
//             // Display bot's reply
//             var botReplyContainer = createMessageContainer('bot-message', 'Tobi', data.bot_reply);
//             document.getElementById('messagesSection').appendChild(botReplyContainer);

//             // Scroll to the bottom to show the latest message
//             document.getElementById('messagesSection').scrollTop = document.getElementById('messagesSection').scrollHeight;
//         });
//     }
// }


function sendMessage() {
    var userMessage = document.getElementById('userMessage').value;

    if (userMessage.trim() !== '') {
        // Display user message immediately
        var userMessageContainer = createMessageContainer('user-message', 'User', userMessage);
        document.getElementById('messagesSection').appendChild(userMessageContainer);

        // Clear the input field
        document.getElementById('userMessage').value = '';

        // Display typing animation while waiting for the bot's reply
        displayTypingAnimation();

        // Send user message to the server and wait for the bot's reply
        fetch('/send_message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: 'user_message=' + encodeURIComponent(userMessage),
        })
        .then(response => response.json())
        .then(data => {
            // Remove typing animation
            removeTypingAnimation();

            // Display bot's reply
            var botReplyContainer = createMessageContainer('bot-message', 'Tobi', data.bot_reply);
            document.getElementById('messagesSection').appendChild(botReplyContainer);

            // Scroll to the bottom to show the latest message
            document.getElementById('messagesSection').scrollTop = document.getElementById('messagesSection').scrollHeight;
        });
    }
}

function displayTypingAnimation() {
    var typingContainer = document.createElement('div');
    typingContainer.className = 'message-container typing';
    typingContainer.innerHTML = '<div class="typing-indicator"></div>';
    document.getElementById('messagesSection').appendChild(typingContainer);
}

function removeTypingAnimation() {
    var typingContainer = document.querySelector('.typing');
    if (typingContainer) {
        typingContainer.remove();
    }
}



function createMessageContainer(className, sender, message) {
    var messageContainer = document.createElement('div');
    messageContainer.className = 'message-container ' + className;

    var timestamp = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', hour12: true });

    messageContainer.innerHTML = `<strong>${sender}:</strong> ${message} <span class="timestamp">${timestamp}</span>`;

    return messageContainer;
}

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}



