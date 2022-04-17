// toggleShrinkNav = () => {
//   let matchedLogo = document.getElementById("matched-logo");
//   matchedLogo.classList.toggle("hide");
//   let nav = document.getElementById("navigation-bar");
//   nav.classList.toggle("shrink");
//   document
//     .getElementById("logoandburger")
//     .classList.toggle("justify-content-center");
//   let linkContainers = document.getElementsByClassName("link-container");
//   for (const container of linkContainers) {
//     //hiding the arrow svgs
//     container.lastElementChild.classList.toggle("hide");
//     let iconAndText = container.firstElementChild;
//     //hiding the link text
//     iconAndText.lastElementChild.classList.toggle("hide");
//     iconAndText.firstElementChild.classList.toggle("bigger");
//   }
//   let linkSections = document.getElementsByClassName("link-section-text");
//   for (const section of linkSections) {
//     section.classList.toggle("link-section-text-center");
//   }
//   // document.getElementById("links").classList.toggle("align-items-center")
// };
let displayNav = false;
console.log(window.innerWidth);
toggleDisplayNavBar = () =>{
    let navBar = document.getElementById("navigation-bar");
    // navBar.classList.toggle("d-none");
    if(displayNav == false){
        pageBtn.classList.remove("rotate");
        main = document.getElementById("main").style.width ="50%";
        navBar.style.display ="flex";
        displayNav = true;
    }
    else if(displayNav == true){
        pageBtn.classList.add("rotate");
        main = document.getElementById("main").style.width ="100%";
        navBar.style.display ="none";
        displayNav = false;
    }
};
window.addEventListener('resize',function(event){
    // clearTimeout(window.resizedFinished);
    // window.resizedFinished = setTimeout(function(){
      if(window.innerWidth > 500) {
        document.getElementById("main").style.width ="100%";
        document.getElementById("navigation-bar").style.display ="flex";
      }
      else{
          if(displayNav == true){
              displayNav=false;
          }
          pageBtn.classList.add("rotate");
          document.getElementById("navigation-bar").style.display ="none";
      }
    // }, 150);
});

makePop =()=>{
    this.classList.add("shadow-sm");
}

// let navBtn = document.getElementById("nav-toggle");
// navBtn.addEventListener("click", toggleShrinkNav);
let pageBtn = document.getElementById("page-btn");
let jobs = document.getElementsByClassName("jobs");
Array.from(jobs).forEach(job =>{
    job.addEventListener("hover",makePop);
});


pageBtn.addEventListener("click", toggleDisplayNavBar);