let expandBtnActive = false;
let toggleNav = false;
toggleShrinkNav = () => {
  let matchedLogo = document.getElementById("matched-logo");
  matchedLogo.classList.toggle("hide");
  document
    .getElementById("logoandburger")
    .classList.toggle("justify-content-center");
  let navBar = document.getElementById("navigation-bar");
  let main = document.getElementById("main");
  navBar.classList.toggle("shrink");
  main.classList.toggle("force-max");
 main.style.width="100%";

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
toggleExpandPage = () => {
    let main = document.getElementById("main");
    let nav = document.getElementById("navigation-bar");
    let button = document.getElementById("expand-btn");
    if(expandBtnActive === false){
        nav.classList.add("hide");
        button.classList.add("rotate");
        nav.style.width="23%";
        main.style.width="100%";
        expandBtnActive = true;
    }
  else{
    nav.classList.remove("hide");
    button.classList.remove("rotate");
    if(window.innerWidth <=999) {
        nav.style.width="50%";
        main.style.width="50%";
    }
    expandBtnActive = false;
  }
};
window.addEventListener('resize',function(event){
    clearTimeout(window.resizedFinished);
    window.resizedFinished = setTimeout(function(){
      resizePage()
    }, 150);
});
resizePage = () => {
    let nav = document.getElementById("navigation-bar");
    let button = document.getElementById("expand-btn");
    clearTimeout(window.resizedFinished);
    // nav.style.width="23%";
    //
    window.resizedFinished = setTimeout(function(){
      if(window.innerWidth <=999) {
          nav.classList.add("hide");
          button.classList.add("rotate");
          expandBtnActive = true;
      }
      else{
        nav.classList.remove("hide");
        button.classList.remove("rotate");
        expandBtnActive = false;
      }
    });
};
resizePage();
expandBtn = document.getElementById("expand-btn");
expandBtn.addEventListener("click", toggleExpandPage);
navBtn = document.getElementById("nav-toggle");
navBtn.addEventListener("click", toggleShrinkNav);
