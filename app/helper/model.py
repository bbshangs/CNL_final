from app.user.model import UserRegister
from app.restaurant.model import Restaurant
from sqlalchemy.sql.expression import func, select

import random

def get_random_restaurant(flag, user_id):
    result_list = []

    if flag == "0": #all
        for i in range(8):
            restaurant = Restaurant.query.order_by(func.random()).first()
            result_list.append(restaurant)
    
    elif flag == "1": #favorite
        user = UserRegister.query.filter_by(id=user_id).first()
        favorite_string = user.get_favorite()

        if len(favorite_string) == 0:
            for i in range(8):
                restaurant = Restaurant.query.order_by(func.random()).first()
                result_list.append(restaurant)
        else:
            favorite_list = favorite_string.split()
            
            restaurant_list = []
            for favorite in favorite_list:
                restaurant = Restaurant.query.filter_by(place_id=favorite).first()
                restaurant_list.append(restaurant)

            for i in range(8):
                result_list.append(random.sample(restaurant_list, 1)[0])
    return result_list
