from app import app
from flask import render_template, request
from app.user.model import UserRegister
from app.restaurant.model import Restaurant
import random
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
def base():  
    return render_template('home/base.html')

@app.route('/home/<user_id>', methods=['GET', 'POST'])  
def home(user_id):
    user = UserRegister.query.filter_by(id=user_id).first()


    if request.method == 'POST':
        param = request.values
        print("param = ", param)
        result = _search(param)
    else:
        result = _search(0)
        result = random.sample(result,min(16,len(result)))

    # print(r)

    return render_template(
        'home/home.html', 
        user_id=user_id,
        restaurant=result
    )


date = {1:'星期一: ', 2:'星期二: ', 3:'星期三: ', 4:'星期四: ', 5:'星期五: ', 6:'星期六: ', 7:'星期日: '}

def _search(param):
    if param == 0:
        all_restaurant = Restaurant.query.all()
        return all_restaurant
    else:
        search = param.get('search', '')    #搜尋關鍵詞，可空著
        price_level = param.get('price_level')
        rating = param.get('rating')
        is_open = param.get('is_open')

        # 搜尋
        # 關鍵詞
        restaurant_list = Restaurant.query.filter(Restaurant.name.ilike('%'+search+'%'))
        # 價格範圍
        if price_level != '':
            restaurant_list = restaurant_list.filter(Restaurant.price_level.is_(price_level))
        # 評分
        if rating != None:
            print(rating)
            restaurant_list = restaurant_list.filter(Restaurant.rating.between(int(rating),int(rating) + 1))

        # 是否營業
        result = []
        if is_open != None:
            cur_datetime = datetime.now()
            day = date.get(cur_datetime.weekday() + 1) #拿到星期x
            time = cur_datetime.strftime("%H:%M") #拿到格式化的時間
            for restaurant in restaurant_list:
                period = restaurant.period.split(day)
                print("name = ", restaurant.name)
                # print("first = ", period)
                if len(period)<0:
                    continue
                period = period[1].split('\',')[0].split(', ')
                # print("second = ", period)
                
                flag = False
                for p in period:
                    if p == "休息":
                        continue
                    if p.split(' – ')[0] <= time and p.split(' – ')[1] >= time:
                        flag = True
                        break
                # print("flag = ", flag)
                print("rating = ", restaurant.rating)
                print("\n")
                if flag:
                    result.append(restaurant)
        else:
            result = restaurant_list

        return result