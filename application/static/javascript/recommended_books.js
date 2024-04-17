filterSelection("all")
function filterSelection(c) {

  var x, i;
  x = document.getElementsByClassName("recBooksList");

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

var btnContainer = document.getElementById("recBooksButton");
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

