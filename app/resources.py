from flask import request
from models import Request, RequestSchema
from flask_restful import Resource
from app import db

schema = RequestSchema()

class RequestListResource(Resource):
    def get(self):
        return schema.dump(db.session.query(Request).all(), many=True).data

class RequestResource(Resource):
    def get(self, rid):
        return schema.dump(db.session.query(Request).get(rid)).data

    def post(self):
        req = Request(request.json['title'], request.json['descr'], 
            request.json['client'], request.json['priority'], request.json['url'],
            request.json['prodarea'])
        db.session.add(req)
        db.session.commit()
        return schema.dump(req).data

