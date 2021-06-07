from flask import render_template
from app.restaurant.model import Restaurant
from app.restaurant import app, GOOGLE_MAPS_EMBED_API_KEY

from app import app

@app.route('/test')
def test():
    return render_template('restaurant/test.html')

@app.route('/restaurant/<place_id>')
def restaurant(place_id):
    cur_restaurant = Restaurant.query.filter_by(place_id=place_id).first()
    if cur_restaurant == None:
        return render_template('restaurant/restaurant_not_found.html')

    return render_template(
        'restaurant/restaurant.html', 
        GOOGLE_MAPS_EMBED_API_KEY=GOOGLE_MAPS_EMBED_API_KEY, 
        restaurant_name=cur_restaurant.name, 
        restaurant_address=cur_restaurant.address,
        restaurant_phone=cur_restaurant.phone_number,
    )
