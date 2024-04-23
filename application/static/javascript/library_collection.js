// FOR DELETING A BOOK
function openDeletePopupTwo(book_id, title) {
    const popupOverlay = document.getElementById("popupOverlay");
    const popupTitle = document.getElementById("popupTitle");
    const deleteBookAnchor = document.getElementById("deleteBook");

    popupOverlay.style.display = "block";
    popupTitle.textContent = title;
    deleteBookAnchor.href = `/delete_book/${book_id}/${title}`;
    }

    document.addEventListener("DOMContentLoaded", function () {
        const popupOverlay = document.getElementById("popupOverlay");
        const closePopupBtn = document.getElementById("closePopup");

        closePopupBtn.addEventListener("click", function () {
          popupOverlay.style.display = "none";
        });
    });