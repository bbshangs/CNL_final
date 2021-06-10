from app.user.model import UserRegister
from app.user.form import FormRegister, FormLogin
from app import app, db
from flask import render_template, flash, redirect, url_for
from hashlib import sha256

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = FormRegister()
    if form.validate_on_submit():
        id_hash = sha256(form.username.data.encode()).hexdigest()
        password_hash = sha256(form.password.data.encode()).hexdigest()
        user = UserRegister(
            id = id_hash,
            username = form.username.data,
            password = password_hash,
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
        password_hash = sha256(form.password.data.encode()).hexdigest()
        if user:
            if user.check_password(password_hash):
                user_id = user.get_id()
                return redirect(url_for('home', user_id=user_id))
            else:
                flash('Wrong Password')
        else:
            flash('Wrong UserName or Password')
    return render_template('user/login.html', form=form)

