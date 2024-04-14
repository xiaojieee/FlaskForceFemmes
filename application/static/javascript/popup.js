function openDeletePopup(username) {
    const popupOverlay = document.getElementById("popupOverlay");
    popupOverlay.style.display = "block";
    }

    document.addEventListener("DOMContentLoaded", function () {
        const closePopupBtn = document.getElementById("closePopup");
        const popupOverlay = document.getElementById("popupOverlay");

        closePopupBtn.addEventListener("click", function () {
          popupOverlay.style.display = "none";
        });
      });
