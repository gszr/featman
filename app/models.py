from sqlalchemy import Column, Integer, String
from marshmallow_sqlalchemy import ModelSchema
from app import db

class Feature(db.Model):
    __tablename__ = "feature"
    id       = Column(Integer, primary_key=True)
    priority = Column(Integer)
    deadline = Column(String(10))
    title    = Column(String(255))
    descr    = Column(String(255))
    client   = Column(String(100))
    url      = Column(String(255))
    prodarea = Column(String(100))

class FeatureSchema(ModelSchema):
    class Meta:
        model = Feature

class Client(db.Model):
    __tablename__ = "client"
    id       = Column(Integer, primary_key=True)
    name     = Column(String(120))

    def __init__(self, name):
        self.name = name

class ClientSchema(ModelSchema):
    class Meta:
        model = Client

class Product(db.Model):
    __tablename__ = "product"
    id   = Column(Integer, primary_key=True)
    name = Column(String(120))

    def __init__(self, name):
        self.name = name

class ProductSchema(ModelSchema):
    class Meta:
        model = Product

class Issue(db.Model):
    __tablename__ = "issue"
    id           = Column(Integer, primary_key=True)
    title        = Column(String(255))
    description  = Column(String(255))
    reporter     = Column(String(100))
    status       = Column(String(30))
    dateReported = Column(String(10))
    dateResolved = Column(String(10))

class IssueSchema(ModelSchema):
    class Meta:
        model = Issue
