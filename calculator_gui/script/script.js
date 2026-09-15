const numbers = document.querySelectorAll(".number");
const display = document.getElementById("output-display-main-screen");
const operations = document.querySelectorAll("[data-operators]");
const deleteButton = document.getElementById("delete");
const clearButton = document.getElementById("clear");
const equalButton = document.getElementById("equal");

const operatorSymbols = ["+", "-", "x", "÷"]; // operator utama (bukan titik/persen)

// ==== INPUT ANGKA ====
numbers.forEach(function (number) {
  number.addEventListener("click", function () {
    display.value += number.textContent;
  });
});

// ==== INPUT OPERATOR & TITIK & PERSEN ====
operations.forEach(function (operator) {
  operator.addEventListener("click", function () {
    const symbol = operator.dataset.operators;
    const lastChar = display.value.slice(-1);

    if (symbol === ".") {
      // cegah titik dobel dalam satu angka
      const lastNumber = display.value.split(/[\+\-x÷]/).pop();
      if (lastNumber.includes(".")) return;
      if (display.value === "" ) {
        display.value += "0.";
        return;
      }
    }

    if (operatorSymbols.includes(symbol)) {
      // jangan biarkan operator jadi karakter pertama (kecuali minus, buat angka negatif)
      if (display.value === "" && symbol !== "-") return;

      // kalau karakter terakhir udah operator, ganti aja (bukan numpuk)
      if (operatorSymbols.includes(lastChar)) {
        display.value = display.value.slice(0, -1) + symbol;
        return;
      }
    }

    if (symbol === "%") {
      // langsung convert angka terakhir jadi bentuk persen (dibagi 100)
      const parts = display.value.split(/([\+\-x÷])/);
      const lastNumber = parseFloat(parts[parts.length - 1]);
      if (isNaN(lastNumber)) return;
      parts[parts.length - 1] = (lastNumber / 100).toString();
      display.value = parts.join("");
      return;
    }

    display.value += symbol;
  });
});

// ==== HAPUS SATU KARAKTER ====
deleteButton.addEventListener("click", function () {
  display.value = display.value.slice(0, -1);
});

// ==== CLEAR SEMUA ====
clearButton.addEventListener("click", function () {
  display.value = "";
});

// ==== HITUNG HASIL (=) ====
equalButton.addEventListener("click", function () {
  if (display.value === "") return;

  try {
    let expression = display.value.replaceAll("x", "*").replaceAll("÷", "/");

    let result = Function('"use strict"; return (' + expression + ")")();

    if (result === Infinity || result === -Infinity) {
      display.value = "Error";
    } else {
      // biar gak nampilin desimal kepanjangan (floating point issue)
      display.value = Math.round(result * 1e10) / 1e10;
    }
  } catch (error) {
    display.value = "Error";
  }
});

// ==== KEYBOARD SUPPORT (bonus, opsional) ====
document.addEventListener("keydown", function (e) {
  if (e.key >= "0" && e.key <= "9") display.value += e.key;
  if (e.key === ".") display.value += ".";
  if (e.key === "+") display.value += "+";
  if (e.key === "-") display.value += "-";
  if (e.key === "*") display.value += "x";
  if (e.key === "/") display.value += "÷";
  if (e.key === "Enter") equalButton.click();
  if (e.key === "Backspace") deleteButton.click();
  if (e.key === "Escape") clearButton.click();
});