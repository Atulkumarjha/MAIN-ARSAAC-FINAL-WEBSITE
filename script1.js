document.addEventListener('DOMContentLoaded', function () {
    const images = document.querySelectorAll(".op1");
    images.forEach(image => {
        image.addEventListener('click', function () {
            const altText = image.alt;
            console.log("Alt Text:", altText);
            document.getElementById('text').value = image.alt;
        });
    });
});

    function clearText(){
    document.getElementById('text').value="";
      }
      function goBack() {
        window.history.back();
      }
      function speakText(text) {
        const speech = new SpeechSynthesisUtterance(text);
        speechSynthesis.speak(speech);
      }
      function redirectTobodyPage(){
        window.location.href = '/body'; // Adjust the path based on your Flask routes
    }
    function redirectTodishespage(){
      window.location.href= '/dishes';
    }
    function redirectToclothesPage(){
      window.location.href= '/clothes';
    }
    function redirectTosportsPage(){
      window.location.href= '/sports';
    }
    function redirectTohygienePage(){
      window.location.href= '/hygiene';
    }
    function redirectToHome(){
      window.location.href= '/';
    }
    function speakTextFromTextBox() {
      const textToSpeak = document.getElementById('myvalue1').value;
      speakText(textToSpeak);
  }
  function changeFont(fontFamily) {
    document.body.style.fontFamily = fontFamily;
  }
  function adjustBrightness(factor) {
    document.body.style.filter = `brightness(${factor})`;
  }

  function changeFontSize(size) {
    // You can modify this function to apply the selected font size to your text or other elements
    switch (size) {
      case 'small':
        document.getElementById('display').style.fontSize = '12px';
        break;
      case 'medium':
        document.getElementById('display').style.fontSize = '16px';
        break;
      case 'large':
        document.getElementById('display').style.fontSize = '30px';
        break;
      // Add more cases as needed
    }
  }