// linksDiv = document.getElementById("links");
// linksDiv.style.backgroundColor="red";
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
  let navWidth = nav.offsetWidth
  nav.classList.toggle("hide");
  button.classList.toggle("rotate");
  // console.log(navWidth)
  // if(expandBtnActive == false){
  //    nav.style.transform ="translateX(-"+navWidth+"px)";
    // main.style.transform ="translateX(-"+navWidth+"px)";
    // let newMainWidth = main.offsetWidth + navWidth;
    // let divisor  = newMainWidth / navWidth;
    //  let newWidthStr = newMainWidth +"%";
    // console.log(newWidthStr);
    // main.style.width = newWidthStr;
    // button.classList.toggle("rotate");
    // expandBtnActive = true;
  // }
  // else{
  //    nav.style.removeProperty("transform");
  //   // main.style.removeProperty("transform");
  //   button.classList.remove("rotate")
  //   // nav.style.width="23%";
  //   // main.style.width ="100%";
  //   expandBtnActive = false;
  // }
};

expandBtn = document.getElementById("expand-btn");
expandBtn.addEventListener("click", togglePage);
navBtn = document.getElementById("nav-toggle");
navBtn.addEventListener("click", toggleNav);
