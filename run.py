from app.resources import RequestResource, RequestListResource
from flask_restful import Api
from flask import render_template
from app import app

api = Api(app)

api.add_resource(RequestListResource, '/api/request/all')
api.add_resource(RequestResource,     '/api/request/<int:rid>', endpoint='requestget')
api.add_resource(RequestResource,     '/api/request/new', endpoint='requestpost')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/new')
def new():
    return render_template('new.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
