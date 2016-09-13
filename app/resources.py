from flask import request
from models import Request, RequestSchema
from flask_restful import Resource, abort
from app import db

request_schema = RequestSchema()

class RequestListResource(Resource):
    def get(self):
        return request_schema.dump(db.session.query(Request).all(), many=True).data

class RequestResource(Resource):
    def get(self, rid):
        req = db.session.query(Request).get(rid)
        if not req:
            abort(404, message="Request {} does not exist".format(rid))
        return request_schema.dump(req)

    def post(self):
        req = Request(request.json['title'], request.json['descr'], 
            request.json['client'], request.json['priority'], request.json['url'],
            request.json['prodarea'])
        db.session.add(req)
        db.session.commit()
        return request_schema.dump(req).data

    def delete(self, rid):
        req = db.session.query(Request).get(rid)
        if not req:
            abort(404, message="Request {} does not exist".format(rid))
        db.session.delete(req)
        db.session.commit()
        return {}

    def put(self, rid):
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
        return {}


