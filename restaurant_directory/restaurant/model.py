from flask.helpers import send_file
from restaurant import db

class Restaurant(db.Model):
    __tablename__ = 'Restaurants'
    place_id = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, place_id):
        self.place_id = place_id
        self.get_attributes_by_place_id()

    def get_attributes_by_place_id(self):
        self.name = self.place_id + 'cc'

    def __repr__(self):
        return '<Restaurant %r>' % self.name