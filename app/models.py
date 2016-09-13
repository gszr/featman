from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from marshmallow_sqlalchemy import ModelSchema

Base = declarative_base()

class Request(Base):
    __tablename__ = "request"
    id       = Column(Integer, primary_key=True)
    priority = Column(Integer)
    deadline = Column(Date)
    title    = Column(String(255))
    descr    = Column(String(255))
    client   = Column(String(100))
    url      = Column(String(255))
    prodarea = Column(String(100))

    def __init__(self, title, descr, client, priority, url, prodarea,
        deadline=None):
        self.title    = title
        self.descr    = descr
        self.client   = client
        self.priority = priority
        self.url      = url
        self.prodarea = prodarea
        self.deadline = deadline

class RequestSchema(ModelSchema):
    class Meta:
        model = Request
