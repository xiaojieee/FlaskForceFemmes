// POP UP | RECOMMENDED BOOKS
function openPopup(title, imageUrl, author, blurb, genre, pages, readingLevel, book_id, isSavedBook=false) {
    console.log("isSavedBook:", isSavedBook);
    const popupOverlay = document.getElementById("popupOverlay");
    const popupTitle = document.getElementById("popupTitle");
    const popupImage = document.getElementById("popupImage");
    const popupAuthor = document.getElementById("popupAuthor");
    const popupBlurb = document.getElementById("popupBlurb");
    const popupGenre = document.getElementById("popupGenre");
    const popupPages = document.getElementById("popupPages");
    const popupReadingLevel = document.getElementById("popupReadingLevel");
    const addToReadingListBtn = document.getElementById("addToReadinglist");
//    addToReadingListBtn.style.display = isSavedBook ? 'none' : 'block';
//    if (isSavedBook){
//    document.getElementById("addToReadinglist").style.display = 'none';
//    }
//    else
//    {
//    document.getElementById("addToReadinglist").style.display = 'block';
//    }
    addToReadingListBtn.addEventListener("click", function () {
    activateAddToButton(book_id);
    });

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


// POP UP | SAVED BOOKS & FINISHED BOOKS
  function openPopupTwo(title, imageUrl, author, blurb, genre, pages, readingLevel, book_id, isSavedBook=false) {
    console.log("isSavedBook:", isSavedBook);
    const popupOverlay = document.getElementById("popupOverlayTwo");
    const popupTitle = document.getElementById("popupTitleTwo");
    const popupImage = document.getElementById("popupImageTwo");
    const popupAuthor = document.getElementById("popupAuthorTwo");
    const popupBlurb = document.getElementById("popupBlurbTwo");
    const popupGenre = document.getElementById("popupGenreTwo");
    const popupPages = document.getElementById("popupPagesTwo");
    const popupReadingLevel = document.getElementById("popupReadingLevelTwo");
    const removeFromReadingListBtn = document.getElementById("removeFromReadinglist");

    removeFromReadingListBtn.addEventListener("click", function () {

    });

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
    const closePopupBtn = document.getElementById("closePopupTwo");
    const popupOverlay = document.getElementById("popupOverlayTwo");
    closePopupBtn.addEventListener("click", function () {
      popupOverlay.style.display = "none";
    });
  });


// ADDS BOOKS TO MY BOOKS PAGE
  function activateAddToButton(book_id)
  {
    const username = '{{session.username}}';
    console.log("Add to Reading List button clicked!");

    // Create a form element
    const form = document.createElement('form');
    form.method = 'POST';
    form.action = '/save_book';

    // Create input fields for book ID and username
    const bookIdInput = document.createElement('input');
    bookIdInput.type = 'hidden';
    bookIdInput.name = 'book_id';
    bookIdInput.value = book_id;
    form.appendChild(bookIdInput);

    const usernameInput = document.createElement('input');
    usernameInput.type = 'hidden';
    usernameInput.name = 'username';
    usernameInput.value = username;
    form.appendChild(usernameInput);

    // Append the form to the document body and submit it
    document.body.appendChild(form);
    form.submit();
   // remove form after submitting
    document.body.removeChild(form);
    }