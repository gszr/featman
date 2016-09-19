from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db_file = os.path.join(os.path.dirname(__file__), 'featreq.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_file)
db  = SQLAlchemy(app)

import models
db.create_all()
