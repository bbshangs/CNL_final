from app.user.model import UserRegister
from app.user.form import FormRegister, FormLogin
from app import app, db
from flask import render_template, flash, redirect, url_for

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = FormRegister()
    if form.validate_on_submit():
        user = UserRegister(
            username = form.username.data,
            password = form.password.data,
            favorite = ""
        )
        db.session.add(user)
        db.session.commit()
        return render_template('home/base.html')
    return render_template('user/register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = FormLogin()
    if form.validate_on_submit():
        user = UserRegister.query.filter_by(username=form.username.data).first()
        if user:
            if user.check_password(form.password.data):
                user_id = user.get_id()
                return redirect(url_for('home', user_id=user_id))
            else:
                flash('Wrong Password')
        else:
            flash('Wrong UserName or Password')
    return render_template('user/login.html', form=form)

