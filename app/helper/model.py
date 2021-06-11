from app.user.model import UserRegister
from app.restaurant.model import Restaurant
from sqlalchemy.sql.expression import func
from flask import session

import random

def get_random_restaurant(flag, user_id):
    result_list = []
    if flag == "0": #all
        for i in range(8):
            restaurant = session.query(Restaurant).order_by(func.rand()).first
            print(f'Choose Restaurant: {restaurant.name}')
            result_list.append(restaurant)
    
    elif flag == "1": #favorite
        user = UserRegister.query.filter_by(id=user_id).first()
        favorite_list = user.get_favorite().split()
        for favorite in favorite_list:
            restaurant = Restaurant.query.filter_by(place_id=favorite).first()
            restaurant_list.append(restaurant)
        result_list = random.sample(restaurant_list, 8)
    print(f'Restaurant List at backend: {result_list}')
    return result_list
