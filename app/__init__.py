from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Base

app = Flask(__name__)
db  = SQLAlchemy(app)

Base.metadata.drop_all(bind=db.engine)
Base.metadata.create_all(bind=db.engine)
