var productBox = document.getElementById("productBox");

function flipRight() {
  productBox.style.transform = "rotateY(180deg)";
}
function flipLeft() {
  productBox.style.transform = "rotateY(0deg)";
}

$(document).ready(function () {
  $(".select-item").click(function () {
    var productBox = $(this).parent().parent().parent().parent();
    productBox.toggleClass("show");
    var currRotateY = productBox.css("transform");
    console.log(currRotateY);
  });
});
