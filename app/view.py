from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/requests/new')
def requests_new():
    return render_template('new.html')

@app.route('/requests/all')
def requests_all():
    return render_template('reqs.html')

