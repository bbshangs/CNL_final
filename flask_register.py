from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os
from form import FormRegister

# get path
pjdir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(pjdir, 'data_register.sqlite')

# key
app.config['SECRET_KEY']='cnl2021'

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form =FormRegister()
    if form.validate_on_submit():
        return 'Register success!'
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.debug = True
    app.run()
