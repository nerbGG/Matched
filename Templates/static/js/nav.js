// linksDiv = document.getElementById("links");
// linksDiv.style.backgroundColor="red";
navBtn = document.getElementById("nav-toggle");
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

navBtn.addEventListener("click", toggleNav);
