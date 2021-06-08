from flask.helpers import send_file
from app.restaurant import db, GOOGLE_PLACE_API_KEY
import urllib.request as req
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

class Restaurant(db.Model):
    __tablename__ = 'Restaurants'
    __bind_key__ = 'restaurant_db'
    place_id = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    location = db.Column(db.String(128), unique=True, nullable=False)# tuple, (lat, lng)
    address = db.Column(db.String(128), unique=False, nullable=False)
    phone_number = db.Column(db.String(32), unique=True, nullable=True)
    period = db.Column(db.String(256), unique=False, nullable=True)
    price_level = db.Column(db.String(4), unique=False, nullable=True)
    # picture = db.Column(db.String(128), unique=True, nullable=False)
    
 
    def __init__(self, place_id):
        self.place_id = place_id
        self.get_attributes_by_place_id()

    def get_attributes_by_place_id(self):
        self.url = ('https://maps.googleapis.com/maps/api/place/details/json?' + 
            'place_id=%s&fields=formatted_address,geometry,icon,name,photo,' +
            'formatted_phone_number,opening_hours,price_level' +
            '&language=zh-TW&key=%s') % (self.place_id, GOOGLE_PLACE_API_KEY)

        # Get infos from Google
        contents = req.urlopen(self.url).read()
        contents = json.loads(contents)
        # print(contents)
        try: 
            contents = contents['result']
        except Exception as e:
            if 'error_message' in contents.keys():
                print('Request error: ', contents['error_message'])
            else:
                print('Other error happened.')
            print(e)
            exit(0) 

        
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