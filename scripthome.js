
function redirectToIndex() {
    window.location.href = '/index'; // Adjust the path based on your Flask routes
  }
  function goBack() {
    window.history.back();
  }
  function redirectToIndex1() {
    window.location.href = '/index1'; // Adjust the path based on your Flask routes
  }

  function redirectTochatbot(){
    window.location.href='/chatbot'
  }
  function changeLanguage(language) {
    // You can redirect the user to a different page based on the selected language
    if (language === 'english') {
      window.location.href = '/';  // Replace 'index.html' with the English version of your site
    } else if (language === 'hindi') {
      window.location.href = '/hindi';  // Replace 'index_hindi.html' with the Hindi version of your site
    }
  }
  function redirectTohindi(){
    window.location.href='/hindi_index'
  }
  
function redirectToIndexhindi(){
  window.location.href='/indexhindi';
}
