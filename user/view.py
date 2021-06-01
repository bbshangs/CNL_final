from user import app
from user import db
from flask import render_template
from user.model import UserRegister
from user.form import FormRegister 

@app.route('/register', methods=['GET', 'POST'])
def register():
    form =FormRegister()
    if form.validate_on_submit():
        user = UserRegister(
            username = form.username.data,
            password = form.password.data
        )
        db.session.add(user)
        db.session.commit()
        return 'Register success!'
    return render_template('register.html', form=form)

