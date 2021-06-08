from flask import Flask, render_template
import os

from app import app
from app import db

# get path
pjdir = os.path.abspath(os.path.dirname(__file__))

GOOGLE_MAPS_EMBED_API_KEY='AIzaSyD7mgftibpKJ7FttbOs1FshTQiFN64xGEo'
GOOGLE_PLACE_API_KEY='AIzaSyCSyaSAVqfSwnPHOT563sVq9NIho_E1gB4'

from app.restaurant.init_db import db, Restaurant
from app.restaurant import view