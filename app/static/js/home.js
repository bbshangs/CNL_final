function Test() {
    let price_level = sessionStorage.getItem("price_level");
    let rating = sessionStorage.getItem("rating");
    let is_open = sessionStorage.getItem("is_open");

    var selectBox = document.getElementById("price_level");
    selectBox.selectedIndex = price_level;

    var selectBox = document.getElementById("rating");
    selectBox.selectedIndex = rating;

    var checkBox = document.getElementById("is_open");
    if(is_open == "true")
        checkBox.click();
}

function ChangePrice() {
    var selectBox = document.getElementById("price_level");
    var selectedValue = selectBox.selectedIndex;

    sessionStorage.setItem("price_level", selectedValue);
}

function ChangeRating() {
    var selectBox = document.getElementById("rating");
    var selectedValue = selectBox.selectedIndex;
    
    sessionStorage.setItem("rating", selectedValue);
}

function ChangeIsOpen() {
    var checkBox = document.getElementById("is_open");
    var value = checkBox.checked;
    
    sessionStorage.setItem("is_open", value);
}