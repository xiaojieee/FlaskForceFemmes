function openDeletePopup(username) {
    const popupOverlay = document.getElementById("popupOverlay");
    const popupUsername = document.getElementById("popupUsername");

    popupOverlay.style.display = "block";
    popupUsername.textContent = username;
    }

    document.addEventListener("DOMContentLoaded", function () {
        const closePopupBtn = document.getElementById("closePopup");
        const popupOverlay = document.getElementById("popupOverlay");

        closePopupBtn.addEventListener("click", function () {
          popupOverlay.style.display = "none";
        });
      });
