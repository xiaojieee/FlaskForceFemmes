// FOR DELETING AN ACCOUNT
function openDeletePopup(account_id, username) {
    const popupOverlay = document.getElementById("popupOverlay");
    const popupUsername = document.getElementById("popupUsername");
    const deleteAnchor = document.getElementById("deleteAccount");

    popupOverlay.style.display = "block";
    popupUsername.textContent = username;
    deleteAnchor.href = `/delete_account/${account_id}/${username}`;
    }

    document.addEventListener("DOMContentLoaded", function () {
        const popupOverlay = document.getElementById("popupOverlay");
        const closePopupBtn = document.getElementById("closePopup");

        closePopupBtn.addEventListener("click", function () {
          popupOverlay.style.display = "none";
        });
    });
