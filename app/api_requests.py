from flask import request, jsonify
from models import Request, RequestSchema
from flask_restful import Resource, abort
from app import app, db

request_schema = RequestSchema()

@app.route('/api/request/all')
def request_all_get():
    return jsonify(request_schema.dump(db.session.query(Request).all(), 
        many=True).data)

@app.route('/api/request/new', methods=['POST'])
def request_new_post():
    req = Request(request.json['title'], request.json['descr'], 
        request.json['client'], request.json['priority'], request.json['url'],
        request.json['prodarea'], request.json['deadline'])
    db.session.add(req)
    db.session.commit()
    return jsonify(request_schema.dump(req).data)

@app.route('/api/request/<int:rid>', methods=['GET'])
def request_id_get(rid):
    req = db.session.query(Request).get(rid)
    if not req:
        abort(404, message="Request {} does not exist".format(rid))
    return jsonify(request_schema.dump(req))

@app.route('/api/request/<int:rid>', methods=['DELETE'])
def request_id_delete(rid):
    req = db.session.query(Request).get(rid)
    if not req:
        abort(404, message="Request {} does not exist".format(rid))
    db.session.delete(req)
    db.session.commit()
    return jsonify({})

@app.route('/api/request/<int:rid>', methods=['PUT'])
def request_id_put(rid):
    req = db.session.query(Request).get(rid)
    # don't allow creating with PUT
    if not req:
        abort(404, message="Request {} does not exist".format(rid))
    req.title    = request.json['title']
    req.descr    = request.json['descr']
    req.client   = request.json['client']
    req.priority = request.json['priority']
    req.url      = request.json['url']
    req.prodarea = request.json['prodarea']
    db.session.add(req)
    db.session.commit()
    return jsonify({})


