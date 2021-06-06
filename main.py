#from werkzeug.middleware.dispatcher import DispatcherMiddleware
#from werkzeug.serving import run_simple
#from user import app as user_app
#from restaurant import app as restaurant_app

#app = DispatcherMiddleware(user_app, {
#    '/user': user_app,
#    '/restaurant': restaurant_app,
#    })

from app import app
app.debug = True
app.run()
#if __name__ == '__main__':
#    run_simple('127.0.0.1', 5000, app)
