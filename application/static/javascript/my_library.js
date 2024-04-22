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

    if (addToReadingListBtn) {
    addToReadingListBtn.addEventListener("click", function () {
    activateAddToButton(book_id);
    });
  }


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
//  const addToReadingListBtn = document.getElementById("addToReadinglist");
    closePopupBtn.addEventListener("click", function () {
    popupOverlay.style.display = "none";
    });

  });

  function activateAddToButton(book_id)
  {

     const username = '{{session.username}}';
//   const redirectUrl = '{{ url_for('save_book') }}' + '?book_id=' + book_id + '&username=' + username;
//   const book_id = book_id;
//   //display a confirmation message
     console.log("Add to Reading List button clicked!");
//   alert('Book saved to reading list successfully');

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
//  Append the form to the document body and submit it
    document.body.appendChild(form);
    form.submit();
//  remove form after submitting
    document.body.removeChild(form);
//  //Redirect to the specified route
//  window.location.href = "{{ url_for('/save_book/', book_id=book_id, username=username) }}"
//  window.location.href = "/save_book/?book_id=" + book_id;
    }

