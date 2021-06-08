const handlePeriod = () => {
    var period_arrow = document.getElementById("period-arrow")
    var period_option = document.getElementById("period-option");

    if (period_arrow.classList[3] == "fa-angle-down") {
        period_arrow.classList.remove('fa-angle-down')
        period_arrow.classList.add('fa-angle-up')
        period_option.style.display="block"
    }	
    else {
        period_arrow.classList.remove('fa-angle-up')
        period_arrow.classList.add('fa-angle-down')
        period_option.style.display="none"
    }
        
}
const handleFavorite = () => {
    var heart = document.getElementById("heart")
    var heart_text = document.getElementById("heart-text")
    if (heart.classList[2] == "far") {
        heart.classList.remove("far")
        heart.classList.add("fas")
        heart_text.innerText="移除最愛"
        favoriteAdded()
    }
    else {
        heart.classList.remove("fas")
        heart.classList.add("far")
        heart_text.innerText="加到最愛"
        favoriteRemove()
    }
}

function favoriteAdded(){
    $.post( '/<user_id>/restaurant/<place_id>', { action: 'add' });
}

function favoriteAdded(){
    $.post( '/<user_id>/restaurant/<place_id>', { action: 'remove' });
}

/*const handleWheel = () => {
    var wheel = document.getElementById("wheel")
    var wheel_text = document.getElementById("wheel-text")
    if (wheel.classList[2] == "far") {
        wheel.classList.remove("far")
        wheel.classList.add("fas")
        wheel_text.innerText="移除轉盤"
        wheelAdded()
    }
    else {
        wheel.classList.remove("fas")
        wheel.classList.add("far")
        wheel_text.innerText="加到轉盤"
    }
}

function wheelAdded(){
    $.post( '/<user_id>/restaurant/<place_id>', { added: 'wheel' });
}*/