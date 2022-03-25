from flask import Flask, render_template
import os

from app import app
from app import db

# get path
pjdir = os.path.abspath(os.path.dirname(__file__))

GOOGLE_MAPS_EMBED_API_KEY=input('Please enter your Google maps embed API key: ')
GOOGLE_PLACE_API_KEY=input('Please enter your Google maps place API key: ')

from app.restaurant.init_db import db, Restaurant
from app.restaurant import view