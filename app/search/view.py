from app import app
from app.restaurant.model import Restaurant
from flask import request, render_template
import json

date = {1:'星期一: ', 2:'星期二: ', 3:'星期三: ', 4:'星期四: ', 5:'星期五: ', 6:'星期六: ', 7:'星期日: '}

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        param = request.values
        # param = json.loads(request.get_data())
        # print(param)
        search = param.get('search', '')    #搜尋關鍵詞，可空著
        order = param.get('order')  #排序：'price'
        day = param.get('day')  #星期幾：1~7
        start = param.get('start')  #開始時間：24小時製，小時分鐘都要兩位數，如'07'或'17:05'
        end = param.get('end')  #結束時間：24小時製，小時分鐘都要兩位數，如'07'或'17:05'
        price_max = param.get('price_max')  #最高價格：int。若DB中沒有存價格，在價格搜尋時會被過濾
        price_min = param.get('price_min', 0)   #最低價格：int

        rate = param.get('rate')
        tag = param.get('tag')
        lat = param.get('lat')
        lng = param.get('lng')

        # 搜尋
        # 關鍵詞
        restaurant_list = Restaurant.query.filter(Restaurant.name.ilike('%'+search+'%'))
        # 價格範圍
        if price_max != None and price_max != '':
            restaurant_list = restaurant_list.filter(Restaurant.price_level.between(price_min, price_max))


        # 排序
        # 距離（需要用戶個人定位）

        # 評價（DB缺rating）
        # 價格
        if order == 'price':
            restaurant_list = restaurant_list.order_by(Restaurant.price_level)

        # 我的最愛(需要user DB)

        # 綜合（需要計算公式）

        result = []
        # 時間範圍（僅保存週三的時間會不會比較好？）
        day = date.get(day)
        if day != None and start != None and end != None:
            for restaurant in restaurant_list:
                r = restaurant.period.split(day)
                if len(r)<0:
                    continue
                r = r[1].split('\',')[0].split(', ')
                flag = False
                for time in r:
                    if time == "休息":
                        continue
                    if time.split(' – ')[0]<=start and time.split(' – ')[1]>=end:
                        flag = True
                        break
                if flag == True:
                    result.append({'place_id' : restaurant.place_id,
                                    'name' : restaurant.name,
                                    'location' : restaurant.location,
                                    'address' : restaurant.address,
                                    'phone_number' : restaurant.phone_number,
                                    'period' : restaurant.period,
                                    'price_level' : restaurant.price_level})
        else:
            for restaurant in restaurant_list:
                result.append({'place_id' : restaurant.place_id,
                                'name' : restaurant.name,
                                'location' : restaurant.location,
                                'address' : restaurant.address,
                                'phone_number' : restaurant.phone_number,
                                'period' : restaurant.period,
                                'price_level' : restaurant.price_level})
                                
        return render_template('/search/search.html', result=result)
        # return json.dumps({'count':len(result), 'result':result}, default=str)
    else:
        result = []
        return render_template('/search/search.html', result=result)
