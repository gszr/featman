from flask import request, jsonify
from models import Client, ClientSchema
from flask_restful import Resource
from app import app, db
from utils import db_do

# marshmallow's schema for Client model class
schema  = ClientSchema()
db      = db.session

@app.route('/api/client')
def client_all_get():
    return jsonify(schema.dump(db.query(Client).all(), many=True).data)

@app.route('/api/client', methods=['POST'])
def client_new_post():
    client = Client(request.json['name'])
    db_do(db.add, db.commit, client)
    return jsonify(schema.dump(client).data)

@app.route('/api/client/<int:id>')
def client_id_get(id):
    return jsonify(schema.dump(db.query(Client).get(id)).data or {})

@app.route('/api/client/<int:id>', methods=['DELETE'])
def client_id_delete(id):
    client = db.query(Client).get(id)
    if client:
        db_do(db.delete, db.commit, client)
    return jsonify({})

@app.route('/api/client/<int:id>', methods=['PUT'])
def client_id_put(id):
    client = db.query(Client).get(id)
    # don't allow creating with PUT
    if client:
        client.name = request.json['name']
        db_do(db.add, db.commit, client)
    return jsonify({})


