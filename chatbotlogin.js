function startVoiceRecognition() {
    var recognition = new webkitSpeechRecognition();
    
    recognition.onresult = function (event) {
        var transcript = event.results[0][0].transcript;
        document.getElementById("user_input").value = transcript;
        submitUserInput();
    };

    recognition.start();
}

function submitUserInput() {
    var userInput = document.getElementById("user_input").value;
    appendUserMessage(userInput);

    $.ajax({
        type: "POST",
        url: "/process_input",
        data: {
            user_input: userInput
        },
        success: function (data) {
            console.log("AJAX Success - Received data:", data);
            appendAssistantMessage("SUNOH: " + data.response);
        },
        error: function (error) {
            console.error("AJAX Error:", error);
        }
    });
}

function appendUserMessage(message) {
    var chatDiv = document.getElementById("chat");
    var userMessageDiv = document.createElement("div");
    var messageSpan = document.createElement("span"); // Create a span for the message content
    userMessageDiv.className = "user-message";
    messageSpan.textContent = "You: " + message; // Set the content of the span
    userMessageDiv.appendChild(messageSpan); // Append the span to the user message div
    chatDiv.appendChild(userMessageDiv);
    document.getElementById("user-input-form").reset();
    chatDiv.scrollTop = chatDiv.scrollHeight; // Scroll to the bottom
}
function appendAssistantMessage(message) {
var chatDiv = document.getElementById("chat");
var assistantMessageDiv = document.createElement("div");
var span = document.createElement("span"); // Create a span element
var awaazIcon = document.createElement("span"); // Create a span for the AWAAZ icon

// Set the inner HTML content of the AWAAZ icon
awaazIcon.innerHTML = '<i class="bi bi-chat"></i>';
awaazIcon.id = "awaaz-icon";

span.innerHTML = message; // Set the inner HTML content to the message
assistantMessageDiv.className = "assistant-message";
assistantMessageDiv.appendChild(awaazIcon); // Append the AWAAZ icon to the assistantMessageDiv
assistantMessageDiv.appendChild(span); // Append the span to the assistantMessageDiv
chatDiv.appendChild(assistantMessageDiv);
chatDiv.scrollTop = chatDiv.scrollHeight; // Scroll to the bottom
}
function redirectToHome(){
    window.location.href= '/signup';
  }