let redHeaderElement = document.getElementById("red_header");
let headerElement = document.querySelector('header');

function header_color_change() {
  headerElement.style.color = "#FF0000";
}

redHeaderElement.addEventListener("click", header_color_change);
