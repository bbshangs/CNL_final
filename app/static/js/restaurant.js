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
const handleFavorite = (user_id, place_id) => {
    var heart = document.getElementById("heart")
    var heart_text = document.getElementById("heart-text")
    if (heart.classList[2] == "far") {
        heart.classList.remove("far")
        heart.classList.add("fas")
        heart_text.innerText="移除最愛"
        favoriteAdded(user_id, place_id)
    }
    else {
        heart.classList.remove("fas")
        heart.classList.add("far")
        heart_text.innerText="加到最愛"
        favoriteRemove(user_id, place_id)
    }
}

function favoriteAdded(user_id, place_id){
    $.post( '/post_sth', { action: 'add', user_id: user_id, place_id: place_id } );
}

function favoriteRemove(user_id, place_id){
    $.post( '/post_sth', { action: 'remove', user_id: user_id, place_id: place_id } );
}