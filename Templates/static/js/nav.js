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
//this is only when the screen is small
let displayNav = false;
console.log(window.innerWidth);
toggleDisplayNavBar = () =>{
    let navBar = document.getElementById("navigation-bar");
    // navBar.classList.toggle("d-none");
    if (displayNav == false) {
        // pageBtn.classList.remove("rotate");
        document.getElementById("main").style.display="none";
        document.getElementById("main").style.width = " 0%";
        navBar.style.display = "flex";
        displayNav = true;
    }
    else if (displayNav == true) {
        document.getElementById("main").style.removeProperty("display");
        // pageBtn.classList.add("rotate");
        document.getElementById("main").style.width = "100%";
        navBar.style.display = "none";
        displayNav = false;
    }
};
window.addEventListener('resize',function(event){
      if(window.innerWidth > 768) {
        document.getElementById("main").style.width ="80%";
        document.getElementById("navigation-bar").style.display ="flex";
      }
      else{
          if(displayNav == true){
              displayNav=false;
          }
          document.getElementById("main").style.width ="100%";
          pageBtn.classList.add("rotate");
          document.getElementById("navigation-bar").style.display ="none";
      }
});


// let navBtn = document.getElementById("nav-toggle");
// navBtn.addEventListener("click", toggleShrinkNav);
const pageBtn = document.getElementById("page-btn");
const navBtn = document.getElementById("nav-btn");
const jobs = Array.from(document.getElementsByClassName("jobs"));
const labels = Array.from(document.getElementsByTagName("label"));

pageBtn.addEventListener("click", toggleDisplayNavBar);
navBtn.addEventListener("click", toggleDisplayNavBar);

jobs.forEach(job => {
  job.addEventListener('mouseenter', function (event) {
    // console.log('box clicked', event);
    // job.setAttribute('style', 'background-color: yellow;');
    job.classList.add("shadow-lg");
  });
  job.addEventListener('mouseleave', function (event) {
    // console.log('box clicked', event);
    job.classList.remove("shadow-lg");
  });
});
labels.forEach(label=>{
    label.setAttribute("style","font-weight: bold;");
})