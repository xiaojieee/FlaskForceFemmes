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