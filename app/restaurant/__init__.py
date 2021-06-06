from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_googlemaps import GoogleMaps, Map

import os
from dotenv import load_dotenv, find_dotenv

from app import app

# get path
pjdir = os.path.abspath(os.path.dirname(__file__))

#app = Flask(__name__)
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(pjdir, 'data_restaurant.sqlite')
GoogleMaps(app)

# key
#app.config['SECRET_KEY']='cnl2021'

# get google api key
# dotenv_path = os.path.join(pjdir, '.env')
# load_dotenv(dotenv_path, override=True) 
# GOOGLE_MAPS_EMBED_API_KEY = os.environ.get("GOOGLE_MAPS_EMBED_API_KEY")
# GOOGLE_PLACE_API_KEY=os.environ.get("GOOGLE_PLACE_API_KEY")
GOOGLE_MAPS_EMBED_API_KEY='AIzaSyD7mgftibpKJ7FttbOs1FshTQiFN64xGEo'
GOOGLE_PLACE_API_KEY='AIzaSyCSyaSAVqfSwnPHOT563sVq9NIho_E1gB4'



#bootstrap = Bootstrap(app)
#db = SQLAlchemy(app)

#from restaurant.init_db import db, Restaurant
#from restaurant import view
