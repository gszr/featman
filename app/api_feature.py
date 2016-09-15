from flask import request, jsonify
from models import Feature, FeatureSchema
from flask_restful import Resource
from app import app, db
from utils import db_do

# marshmallow's schema for Feature model class
schema = FeatureSchema()
db     = db.session

def fill_feature(feature, json):
    feature.title    = json['title']
    feature.descr    = json['descr']
    feature.client   = json['client']
    feature.priority = json['priority']
    feature.url      = json['url']
    feature.prodarea = json['prodarea']
    feature.deadline = json['deadline']

@app.route('/api/feature')
def feature_get():
    return jsonify(schema.dump(db.query(Feature).all(), many=True).data)

@app.route('/api/feature', methods=['POST'])
def feature_post():
    req = Feature()
    fill_feature(req, request.json)
    db_do(db.add, db.commit, req)
    return jsonify(schema.dump(req).data)

@app.route('/api/feature/<int:id>')
def feature_id_get(id):
    return jsonify(schema.dump(db.query(Feature).get(id) or {}).data)

@app.route('/api/feature/<int:id>', methods=['DELETE'])
def feature_id_delete(id):
    req = db.query(Feature).get(id)
    if req:
        db_do(db.delete, db.commit, req)
    return jsonify({})

@app.route('/api/feature/<int:id>', methods=['PUT'])
def feature_id_put(id):
    req = db.query(Feature).get(id)
    # TODO should we allow creation with PUT?
    if req:
        fill_feature(req, request.json)
        db_do(db.add, db.commit, req)
    return jsonify({})

