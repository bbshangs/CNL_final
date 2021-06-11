from app import app
from flask import render_template
from app.user.model import UserRegister
from app.helper.model import get_random_restaurant

@app.route('/helper/<flag>/<user_id>', methods=['GET', 'POST'])  
def helper(flag, user_id):  
    restaurant_list, err_msg = get_random_restaurant(flag, user_id)
    print(f'Error message in view: {err_msg}')
    return render_template('helper/helper.html', user_id=user_id, restaurant_list=restaurant_list, err_msg=err_msg)
