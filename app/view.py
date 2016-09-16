from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/feature/new')
def requests_new():
    return render_template('feature_new.html')

@app.route('/feature/all')
def requests_all():
    return render_template('feature_all.html')

@app.route('/client/new')
def client_new():
    return render_template('client_new.html')

@app.route('/client/all')
def client_all():
    return render_template('client_all.html')
