onload = function() {
 console.log(Date.now());
 // wait for 500 milliseconds
 setTimeout(function() {
  let lv = document.children[0].children[2].children[0].children[0].children[1].children[1].children[2].children[1].children[0];
  let text;
  for (let i = 0; i < lv.children[2].children.length; i++) {
   console.log("Saved.");
   text = (lv.children[2].children[i].children[0].innerHTML);
   // if text is in localStorage
   if (localStorage.text === undefined) {
    // append text in localStorage
    localStorage.setItem("text", text);
    // genmore
    document.children[0].children[2].children[0].children[0].children[1].children[1].children[1].children[4].click();
   } else {
    // append text in localStorage
    localStorage.setItem("text", localStorage.text + "\n" + text);
    // genmore
    document.children[0].children[2].children[0].children[0].children[1].children[1].children[1].children[4].click();
   };
  };
 }, 500);
};