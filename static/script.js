function sendMessage() {
    var userInput = document.getElementById('user-input').value;
    var imageInput = document.getElementById('image-input');
    var imageFile = imageInput.files[0];

    var formData = new FormData();
    formData.append('user-input', userInput);
    formData.append('image-input', imageFile);



    document.getElementById("loader").style.display = "block";
    if (userInput.trim() === '' && !imageFile) {
        return; // Do nothing if both input and image are empty
    }


    fetch('/process_message', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            // appendMessage('user', data.userInput);
            appendMessage('bot', data.botResponse);
            // createNumberAttributes();
            textToSpeech();
            document.getElementById("loader").style.display = "none";
        })
        .catch(error => console.error('Error:', error));



    if (imageFile) {
        // Handle image upload
        var reader = new FileReader();
        reader.onload = function (e) {
            var imageData = e.target.result;
            appendMessage('user', '<img src="' + imageData + '" alt="user image" class="user-image" style="max-width: 80%; max-height: 300px;" >');
            // Add logic here to send the image data to the server (Flask) for processing
            // and receive the bot's response.
            // Update the chat display with the bot's response using appendMessage('bot', response);
        };
        reader.readAsDataURL(imageFile);
        imageInput.value = ''; // Clear the input after reading the image
    }

    if (userInput.trim() !== '') {
        appendMessage('user', userInput);
        // Add logic here to send the user input to the server (Flask) for processing
        // and receive the bot's response.
        // Update the chat display with the bot's response using appendMessage('bot', response);
        document.getElementById('user-input').value = '';
    }
}

function appendMessage(sender, message) {
    var chatDisplay = document.getElementById('chat-display');
    var newMessage = document.createElement('div');
    newMessage.className = sender;
    if (newMessage.className === 'bot')
        newMessage.innerHTML = `<img class="chatImg" src="static/assets/ctuIcon.png" /><p class="txt">${message}</p><button class="playButton"><i class="ri-volume-up-fill"></i></button>`;
    else if (newMessage.className === 'user')
        newMessage.innerHTML = `<img class="chatImg" src="static/assets/userIcon.png" /><p class="txt">${message}</p>`;
    chatDisplay.appendChild(newMessage);
    chatDisplay.scrollTop = chatDisplay.scrollHeight;
}

function createNumberAttributes() {
    const messageId = document.querySelectorAll('.bot');
    for (let i = 0; i < messageId.length; i++) {
        messageId[i].setAttribute('messageId', i + 1);
    }
}
/* ----------------------------- Text to Speech ----------------------------- */
function textToSpeech() {
    var playButtons = document.querySelectorAll('.playButton');

    playButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var textToSpeak = this.previousElementSibling.innerText;
            console.log(textToSpeak);
            // Gửi văn bản đến server để chuyển thành giọng nói và trả về URL audio
            fetch('/speak', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ tts: textToSpeak })
            })
                .then(response => response.json())
                .then(data => {
                    // Tạo và phát audio
                    var audio = new Audio(data.audio_url);
                    audio.play();
                })
                .catch(error => console.error('Error:', error));
        });
    });
}


