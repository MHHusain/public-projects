var name = "hello world";
alert(name);


// content.js
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if( request.massaaag === "have i been clicked" ) {
      var myurl = "https://youtube.com";

      chrome.runtime.sendMessage({"message": "open_new_tab", "url": document.title,url1: myurl});
    }
  }
);