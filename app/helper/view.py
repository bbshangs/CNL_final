from app import app
from flask import render_template
from app.user.model import UserRegister

@app.route('/helper/<user_id>', methods=['GET', 'POST'])  
def helper(user_id):  
	user = UserRegister.query.filter_by(id=user_id).first()
	return render_template('helper/helper.html', user_id=user_id)