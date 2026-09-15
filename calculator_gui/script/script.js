const numbers = document.querySelectorAll(".number");
const display = document.getElementById("output-display-main-screen");
const operations = document.querySelectorAll("[data-operators");
const deleteButton = document.getElementById('delete');
const clearButton = document.getElementById('clear')

numbers.forEach(function (number) {
  number.addEventListener("click", function () {
    display.value += number.textContent;
  });
});

operations.forEach(function (operator) {
  operator.addEventListener("click", function () {
    display.value += operator.dataset.operators;
  });
});

deleteButton.addEventListener('click', function() {
    display.value = display.value.slice(0,-1);
})

clearButton.addEventListener('click', function() {
    display.value='';
})
