from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///featreq.db'
db  = SQLAlchemy(app)

import models
db.create_all()
