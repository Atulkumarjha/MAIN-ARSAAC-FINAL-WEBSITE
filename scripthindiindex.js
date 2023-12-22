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

      function speakTexthindi(text) {
      if ('speechSynthesis' in window) {
        const utterance = new SpeechSynthesisUtterance(text);
        
        
        utterance.lang = 'hi-IN';
        utterance.voice = speechSynthesis.getVoices().find(voice => voice.lang === 'hi-IN');
        
        speechSynthesis.speak(utterance);
      } else {
        alert('Speech synthesis is not supported in your browser. Please use a modern browser that supports the Web Speech API.');
      }
    }
function redirectTohindibody(){
  window.location.href= '/bodyhindi';
}
function redirectTohindiclothes(){
  window.location.href='/clothes_hindi';
}
function redirectTohindifood(){

  window.location.href='/food_hindi';
}
function redirecttohindihygiene(){
  window.location.href='/hygiene_hindi'
}
function redirectTohindisports(){
  window.location.href='/sports_hindi'
}
function goBack() {
    window.history.back();
  }

  function redirectTohindi(){
    window.location.href= '/hindi';
  }
  function clearText(){
    document.getElementById('text').value="";
      }
