// POP UP | RECOMMENDED BOOKS
function openPopup(title, imageUrl, author, blurb, genre, pages, readingLevel, book_id) {

    const popupOverlay = document.getElementById("popupOverlay");
    const popupTitle = document.getElementById("popupTitle");
    const popupImage = document.getElementById("popupImage");
    const popupAuthor = document.getElementById("popupAuthor");
    const popupBlurb = document.getElementById("popupBlurb");
    const popupGenre = document.getElementById("popupGenre");
    const popupPages = document.getElementById("popupPages");
    const popupReadingLevel = document.getElementById("popupReadingLevel");
    const addToReadingListBtn = document.getElementById("addToReadinglist");
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
  function openPopupTwo(title, imageUrl, author, blurb, genre, pages, readingLevel, book_id, start_date, current_page,
  completed_date, rating) {

    const popupOverlay = document.getElementById("popupOverlayTwo");
    const popupTitle = document.getElementById("popupTitleTwo");
    const popupImage = document.getElementById("popupImageTwo");
    const popupAuthor = document.getElementById("popupAuthorTwo");
    const popupBlurb = document.getElementById("popupBlurbTwo");
    const popupGenre = document.getElementById("popupGenreTwo");
    const popupPages = document.getElementById("popupPagesTwo");
    const popupReadingLevel = document.getElementById("popupReadingLevelTwo");
    const popupStartDate = document.getElementById("start_stat");
    const popupCurrentPage = document.getElementById("page_stat");
    const popupCompletedDate = document.getElementById("completed_stat");
    const popupRating = document.getElementById("rating_stat");
    const currentPageInput = document.getElementById("current_page");
    const removeFromReadingListBtn = document.getElementById("removeFromReadinglist");
    const formActionUrl = `/update_student_book/${book_id}`;

    // Sets the maximum value of the current_page input to the total pages of the book
    currentPageInput.max = pages;

    removeFromReadingListBtn.addEventListener("click", function () {
    removeFromReadingList(book_id)
    });

    popupOverlay.style.display = "block";
    popupTitle.textContent = title;
    popupImage.src = imageUrl;
    popupAuthor.textContent = 'Author: ' + author;
    popupBlurb.textContent = 'About: ' + blurb;
    popupGenre.textContent = 'Genre: ' + genre;
    popupPages.textContent = 'Pages: ' + pages;
    popupReadingLevel.textContent = 'Reading Level: ' + readingLevel;

    popupStartDate.textContent = start_date;
    popupCurrentPage.textContent = current_page;
    popupCompletedDate.textContent = completed_date;

    // Handle displaying the rating
    if (rating !== 'None') {
        const ratingStars = '★'.repeat(rating); // Repeat the star symbol according to the rating
        popupRating.textContent = 'Rating: ' + ratingStars;
    } else {
        popupRating.textContent = 'Rating: None';
    }

    document.getElementById("bookForm").action = formActionUrl;

  }

    document.addEventListener("DOMContentLoaded", function () {
    const closePopupBtn = document.getElementById("closePopupTwo");
    const popupOverlay = document.getElementById("popupOverlayTwo");
    closePopupBtn.addEventListener("click", function () {
      popupOverlay.style.display = "none";
    });
  });


// ADDS BOOK TO SAVED BOOKS LIST | MY BOOKS PAGE
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


// REMOVES BOOK FROM SAVED AND FINISHED BOOKS LIST | MY BOOKS PAGE
  function removeFromReadingList(book_id) {
    const username = '{{ session.username }}';

    // Create a form element
    const form = document.createElement('form');
    form.method = 'POST';
    form.action = '/remove_book';

    // Create input fields for username book ID

    const usernameInput = document.createElement('input');
    usernameInput.type = 'hidden';
    usernameInput.name = 'username';
    usernameInput.value = username;
    form.appendChild(usernameInput);

    const bookIdInput = document.createElement('input');
    bookIdInput.type = 'hidden';
    bookIdInput.name = 'book_id';
    bookIdInput.value = book_id;
    form.appendChild(bookIdInput);

    // Append the form to the document body and submit it
    document.body.appendChild(form);
    form.submit();

    // Remove form after submitting
    document.body.removeChild(form);
}