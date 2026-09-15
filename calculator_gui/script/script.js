const numbers = document.querySelectorAll(".number");
const display = document.getElementById("output-display-main-screen");
const operations = document.querySelectorAll("[data-operators");

numbers
  .forEach(function (number) {
    number.addEventListener("click", function () {
      display.value += number.textContent;
    });
  })

  operations.forEach(function(operator) {
    operator.addEventListener("click", function() {
        display.value += operator.dataset.operators
    })
  })