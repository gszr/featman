from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from marshmallow_sqlalchemy import ModelSchema

Base = declarative_base()

class Request(Base):
    __tablename__ = "request"
    id       = Column(Integer, primary_key=True)
    priority = Column(Integer)
    deadline = Column(String(10))
    title    = Column(String(255))
    descr    = Column(String(255))
    client   = Column(String(100))
    url      = Column(String(255))
    prodarea = Column(String(100))

class RequestSchema(ModelSchema):
    class Meta:
        model = Request

class Client(Base):
    __tablename__ = "client"
    id       = Column(Integer, primary_key=True)
    name     = Column(String(120))

    def __init__(self, name):
        self.name = name

class ClientSchema(ModelSchema):
    class Meta:
        model = Client

class Product(Base):
    __tablename__ = "product"
    id   = Column(Integer, primary_key=True)
    name = Column(String(120))

    def __init__(self, name):
        self.name = name

class ProductSchema(ModelSchema):
    class Meta:
        model = Product
