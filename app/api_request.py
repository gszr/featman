from flask import request, jsonify
from models import Request, RequestSchema
from flask_restful import Resource
from app import app, db
from utils import db_do

# marshmallow's schema for Request model class
schema = RequestSchema()
db     = db.session

def fill_request(request, json):
    request.title    = json['title']
    request.descr    = json['descr']
    request.client   = json['client']
    request.priority = json['priority']
    request.url      = json['url']
    request.prodarea = json['prodarea']
    request.deadline = json['deadline']

@app.route('/api/request')
def request_get():
    return jsonify(schema.dump(db.query(Request).all(), many=True).data)

@app.route('/api/request', methods=['POST'])
def request_post():
    req = Request()
    fill_request(req, request.json)
    db_do(db.add, db.commit, req)
    return jsonify(schema.dump(req).data)

@app.route('/api/request/<int:id>')
def request_id_get(id):
    return jsonify(schema.dump(db.query(Request).get(id) or {}).data)

@app.route('/api/request/<int:id>', methods=['DELETE'])
def request_id_delete(id):
    req = db.query(Request).get(id)
    if req:
        db_do(db.delete, db.commit, req)
    return jsonify({})

@app.route('/api/request/<int:id>', methods=['PUT'])
def request_id_put(id):
    req = db.query(Request).get(id)
    # TODO should we allow creation with PUT?
    if req:
        fill_request(req, request.json)
        db_do(db.add, db.commit, req)
    return jsonify({})

