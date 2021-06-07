from app import app
from flask import render_template
from app.user.model import UserRegister

@app.route('/favorite/<user_id>', methods=['GET', 'POST']) 
def favorite(user_id):
    user = UserRegister.query.filter_by(id=user_id).first()
    f = user.get_favorite()
    print("favorite = ", f)
    return render_template('favorite/favorite.html', user_id=user_id)

