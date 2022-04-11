// linksDiv = document.getElementById("links");
// linksDiv.style.backgroundColor="red";
console.log(window.innerWidth)
toggleNav = () => {
  let matchedLogo = document.getElementById("matched-logo");
  matchedLogo.classList.toggle("hide");
  document
    .getElementById("logoandburger")
    .classList.toggle("justify-content-center");
  let navBar = document.getElementById("navigation-bar");
  navBar.classList.toggle("shrink");
  let linkContainers = document.getElementsByClassName("link-container");
  for (const container of linkContainers) {
    //hiding the arrow svgs
    container.lastElementChild.classList.toggle("hide");
    let iconAndText = container.firstElementChild;
    //hiding the link text
    iconAndText.lastElementChild.classList.toggle("hide");
    iconAndText.firstElementChild.classList.toggle("bigger");
  }
  let linkSections = document.getElementsByClassName("link-section-text");
  for (const section of linkSections) {
    section.classList.toggle("link-section-text-center");
  }
  // document.getElementById("links").classList.toggle("align-items-center")
};
let expandBtnActive = false;
togglePage = () => {
  let main = document.getElementById("main");
  let nav = document.getElementById("navigation-bar");
  let button = document.getElementById("expand-btn");
  if(expandBtnActive === false){
    nav.classList.add("hide");
    button.classList.add("rotate");
    expandBtnActive = true;
  }
  else{
    nav.classList.remove("hide");
    button.classList.remove("rotate");
    expandBtnActive = false;
  }
  // nav.classList.toggle("hide");
  // button.classList.toggle("rotate");
};
window.addEventListener('resize',function(event){
  // let nav = document.getElementById("navigation-bar");
  // let button = document.getElementById("expand-btn");
  // if(window.innerWidth <= 975) {
  //   nav.style.display = "none";
  //   button.classList.add("rotate");
  // }else{
  //   nav.style.removeProperty("display");
  //   button.classList.remove("rotate");
  // }
      let main = document.getElementById("main");
      let nav = document.getElementById("navigation-bar");
      let button = document.getElementById("expand-btn");
    clearTimeout(window.resizedFinished);
    window.resizedFinished = setTimeout(function(){
      if(window.innerWidth <=999) {
        if (expandBtnActive == false) {
          nav.classList.add("hide");
          button.classList.add("rotate");
          expandBtnActive = true;
        }
      }
      // else{
      //   nav.classList.remove("hide");
      //   button.classList.remove("rotate");
      //   expandBtnActive = false;
      // }
    }, 150);



});
 expandBtn = document.getElementById("expand-btn");
expandBtn.addEventListener("click", togglePage);
navBtn = document.getElementById("nav-toggle");
navBtn.addEventListener("click", toggleNav);
