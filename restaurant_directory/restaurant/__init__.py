from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_googlemaps import GoogleMaps, Map
import os

# get path
pjdir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(pjdir, 'data_restaurant.sqlite')
GoogleMaps(app)

# key
app.config['SECRET_KEY']='cnl2021'

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

# db.init_app(app)
from restaurant.init_db import db, Restaurant
from restaurant import view