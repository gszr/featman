from flask import request, jsonify
from models import Product, ProductSchema
from flask_restful import Resource
from app import app, db
from utils import db_do

# marshmallow's schema for Client model class
schema  = ProductSchema()

@app.route('/api/product')
def product_all_get():
    return jsonify(schema.dump(db.session.query(Product).all(), many=True).data)

@app.route('/api/product', methods=['POST'])
def product_new_post():
    product = Product(request.json['name'])
    db_do(db.session.add, db.session.commit, product)
    return jsonify(schema.dump(product).data)

@app.route('/api/product/<int:id>')
def product_id_get(id):
    return jsonify(schema.dump(db.session.query(Product).get(id)).data or {})

@app.route('/api/product/<int:id>', methods=['DELETE'])
def product_id_delete(id):
    product = db.session.query(Product).get(id)
    if product:
        db_do(db.session.delete, db.session.commit, product)
    return jsonify({})

@app.route('/api/product/<int:id>', methods=['PUT'])
def product_id_put(id):
    product = db.session.query(Product).get(id)
    # don't allow creating with PUT
    if product:
        product.name = request.json['name']
        db_do(db.session.add, db.session.commit, product)
    return jsonify({})


