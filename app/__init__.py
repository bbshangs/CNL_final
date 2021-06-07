from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os

# get path
pjdir = os.path.abspath(os.path.dirname(__file__))

# app data db, containing USER db & RESTAURANT db
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(pjdir, 'data.sqlite')
SQLALCHEMY_BINDS = {
    'user_db': SQLALCHEMY_DATABASE_URI,
    'restaurant_db': 'sqlite:///' + os.path.join(pjdir, 'restaurant/data_restaurant.sqlite')
}

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS

# key
app.config['SECRET_KEY']='cnl2021'

bootstrap = Bootstrap(app)

# Remove exsisting db
try: 
    os.remove(os.path.join(pjdir, 'data.sqlite'))
except:
    print('No db to remove')
try: 
    os.remove(os.path.join(pjdir, 'restaurant/data_restaurant.sqlite'))
except:
    print('No db to remove')

db = SQLAlchemy(app)
db.create_all()

from app.home import view as home_view
from app.user import view as user_view
from app.restaurant import view as restaurant_view
from app.favorite import view as favorite_view
from app.helper import view as helper_view
