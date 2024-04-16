function openDeletePopup(account_id, username) {
    const popupOverlay = document.getElementById("popupOverlay");
    const popupUsername = document.getElementById("popupUsername");
    const myAnchor = document.querySelector("deleteAccount");

    popupOverlay.style.display = "block";
    popupUsername.textContent = username;
    }

    document.addEventListener("DOMContentLoaded", function () {
        const popupOverlay = document.getElementById("popupOverlay");
        const deleteAccountBtn = document.getElementById("deleteAccount");
        const closePopupBtn = document.getElementById("closePopup");

        closePopupBtn.addEventListener("click", function () {
          popupOverlay.style.display = "none";
        });

        deleteAccountBtn.addEventListener("click", function () {
          const myAnchor = document.querySelector("deleteAccount");
          deleteAccount.href = "{{ url_for('delete_account/" + account_id + '/' + username + "}}";
        });
      });
