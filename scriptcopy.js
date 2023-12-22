  function clearText() {
    document.getElementById('myvalue1').value = "";
  }

  function goBack() {
    window.history.back();
  }
  

  function redirectToHome() {
    window.location.href='/';
  }

  function setTextAndSpeak(text) {
    document.getElementById('myvalue1').value = text;
    speakText(text);
  }
  
  function speakText(text) {
    if ('speechSynthesis' in window) {
      const utterance = new SpeechSynthesisUtterance(text);
      speechSynthesis.speak(utterance);
    } else {
      alert("Text-to-speech is not supported in this browser.");
    }
  }

  
  function redirectToDrinkPage() {
    window.location.href = '/drink'; // Adjust the path based on your Flask routes
}

  function redirectToFoodPage() {
    window.location.href = '/food'; // Adjust the path based on your Flask routes
}
  function redirectToPlacesPage() {
    window.location.href = '/places'; // Adjust the path based on your Flask routes
}
function redirectToActivitiesPage() {
    window.location.href = '/activities'; // Adjust the path based on your Flask routes
}
function redirectToFeelingPage() {
    window.location.href = '/feeling'; // Adjust the path based on your Flask routes
}

function redirectToMedicalPage() {
    window.location.href = '/medical'; // Adjust the path based on your Flask routes
}
function speakTextFromTextBox() {
    const textToSpeak = document.getElementById('myvalue1').value;
    speakText(textToSpeak);
}
