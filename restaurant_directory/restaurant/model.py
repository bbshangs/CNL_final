from flask.helpers import send_file
from restaurant import db
import urllib.request as req
import json

class Restaurant(db.Model):
    __tablename__ = 'Restaurants'
    place_id = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    location = db.Column(db.String(128), unique=True, nullable=False)# tuple, (lat, lng)
    address = db.Column(db.String(128), unique=True, nullable=False)
    phone_number = db.Column(db.String(32), unique=True, nullable=True)
    period = db.Column(db.String(256), unique=False, nullable=True)
    price_level = db.Column(db.String(4), unique=False, nullable=True)
    # picture = db.Column(db.String(128), unique=True, nullable=False)
    
    key = 'AIzaSyCSyaSAVqfSwnPHOT563sVq9NIho_E1gB4'
 
    def __init__(self, place_id):
        self.place_id = place_id
        self.get_attributes_by_place_id()

    def get_attributes_by_place_id(self):
        self.url = ('https://maps.googleapis.com/maps/api/place/details/json?' + 
            'place_id=%s&fields=formatted_address,geometry,icon,name,photo,' +
            'formatted_phone_number,opening_hours,price_level&key=%s') % (self.place_id, self.key)

        # Get infos from Google
        contents = req.urlopen(self.url).read()
        contents = json.loads(contents)['result']
        
        self.name = contents['name']
        self.location = str(tuple(contents['geometry']['location'].values())) # (lat, lng)
        self.address = contents['formatted_address']
        self.phone_number = contents['formatted_phone_number']
        self.period = str(contents['opening_hours']['weekday_text'])
        try:
            self.price_level = contents['price_level']
        except:
            pass
        # self.picture = 
        

    def __repr__(self):
        return '<Restaurant %r>' % self.name