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
function updateTextBox(text) {
    document.getElementById('myvalue1').value = text;
    speakText(text);
  }
  
function speakText(text) {
    if ('speechSynthesis' in window) {
      const utterance = new SpeechSynthesisUtterance(text);
      // Specify the Hindi language and select the Hindi voice
      utterance.lang = 'hi-IN';
      utterance.voice = speechSynthesis.getVoices().find(voice => voice.lang === 'hi-IN');
      speechSynthesis.speak(utterance);
    } else {
      alert('Speech synthesis is not supported in your browser. Please use a modern browser that supports the Web Speech API.');
    }
  }
  function gotopage(){
    window.location.href="/foodhindi";
  }
  
  function gotopage1(){
    window.location.href="/drinkhindi";
  }
  
  function gotopage2(){
    window.location.href="/placeshindi";
  }
  
  function gotopage3(){
    window.location.href="/activitieshindi";
  }
  
  function gotopage4(){
    window.location.href="/feelinghindi";
  }
  
  function gotopage5(){
    window.location.href="/medicalhindi";
  }
  function redirectTohindi(){
    window.location.href= '/hindi';
  }
  function clearText(){
    document.getElementById('text').value="";
      }
      function speakTextFromTextBox() {
        const textToSpeak = document.getElementById('myvalue1').value;
        speakText(textToSpeak);
    }
    function clearText() {
      document.getElementById('myvalue1').value = "";
    }
  
    function goBack() {
      window.history.back();
    }