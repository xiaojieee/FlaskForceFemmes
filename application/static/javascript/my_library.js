filterSelection("all")
function filterSelection(c) {
  var x, i;
  x = document.getElementsByClassName("filterDiv");

  // Remove the 'show' class from all elements
  for (i = 0; i < x.length; i++) {
    x[i].classList.remove("show");
  }

  // If 'all' is selected, show all elements
  if (c === "all") {
    for (i = 0; i < x.length; i++) {
      x[i].classList.add("show");
    }
  } else {
    // Otherwise, show only the elements with the selected category
    for (i = 0; i < x.length; i++) {
      if (x[i].classList.contains(c)) {
        x[i].classList.add("show");
      }
    }
  }
}

var btnContainer = document.getElementById("myBtnContainer");
var btns = btnContainer.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    // Remove the 'active' class from all buttons
    var activeBtns = btnContainer.getElementsByClassName("active");
    for (var j = 0; j < activeBtns.length; j++) {
      activeBtns[j].classList.remove("active");
    }

    // Add the 'active' class to the clicked button
    this.classList.add("active");
  });
}

function openPopup(title, imageUrl, author, blurb, genre, pages, readingLevel) {
    const popupOverlay = document.getElementById("popupOverlay");
    const popupTitle = document.getElementById("popupTitle");
    const popupImage = document.getElementById("popupImage");
    const popupAuthor = document.getElementById("popupAuthor");
    const popupBlurb = document.getElementById("popupBlurb");
    const popupGenre = document.getElementById("popupGenre");
    const popupPages = document.getElementById("popupPages");
    const popupReadingLevel = document.getElementById("popupReadingLevel");

    popupOverlay.style.display = "block";
    popupTitle.textContent = title;
    popupImage.src = imageUrl;
    popupAuthor.textContent = 'Author: ' + author;
    popupBlurb.textContent = 'About: ' + blurb;
    popupGenre.textContent = 'Genre: ' + genre;
    popupPages.textContent = 'Pages: ' + pages;
    popupReadingLevel.textContent = 'Reading Level: ' + readingLevel;
  }

  document.addEventListener("DOMContentLoaded", function () {
    const closePopupBtn = document.getElementById("closePopup");
    const popupOverlay = document.getElementById("popupOverlay");

    closePopupBtn.addEventListener("click", function () {
      popupOverlay.style.display = "none";
    });
  });