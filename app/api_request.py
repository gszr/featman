from flask import request, jsonify
from models import Request, RequestSchema
from flask_restful import Resource
from app import app, db
from utils import db_do

# marshmallow's schema for Request model class
schema = RequestSchema()
db     = db.session

@app.route('/api/request')
def request_get():
    return jsonify(schema.dump(db.query(Request).all(), many=True).data)

@app.route('/api/request', methods=['POST'])
def request_post():
    req = Request()
    req.title    = request.json['title']
    req.descr    = request.json['descr']
    req.client   = request.json['client']
    req.priority = request.json['priority']
    req.url      = request.json['url']
    req.prodarea = request.json['prodarea']
    req.deadline = request.json['deadline']
    
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
        req.title    = request.json['title']
        req.descr    = request.json['descr']
        req.client   = request.json['client']
        req.priority = request.json['priority']
        req.url      = request.json['url']
        req.prodarea = request.json['prodarea']

        db_do(db_add, req)
    return jsonify({})

