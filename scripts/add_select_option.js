const chooseLangSelectElement = document.querySelector("#id_choose_language");

const newLang = document.createElement("option");
newLang.setAttribute("value", "6");
newLang.textContent = "Other";

chooseLangSelectElement.appendChild(newLang);
