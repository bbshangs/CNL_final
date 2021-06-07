from app import app
from flask import render_template

@app.route('/helper')  
def helper():  
    return render_template('helper/helper.html')