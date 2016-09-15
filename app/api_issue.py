from flask import request, jsonify
from models import Issue, IssueSchema 
from flask_restful import Resource
from app import app, db
from utils import db_do

# marshmallow's schema for Client model class
schema  = IssueSchema()
db      = db.session

def fill_issue(issue, json):
    issue.title        = json['title']
    issue.description  = json['description']
    issue.reporter     = json['reporter']
    issue.status       = json['status']
    issue.dateReported = json['dateReported']
    issue.dateResolved = json['dateResolved']

@app.route('/api/issue')
def issue_all_get():
    return jsonify(schema.dump(db.query(Issue).all(), many=True).data)

@app.route('/api/issue', methods=['POST'])
def issue_new_post():
    issue = Issue()
    fill_issue(issue, request.json)
    db_do(db.add, db.commit, issue)
    return jsonify(schema.dump(issue).data)

@app.route('/api/issue/<int:id>')
def issue_id_get(id):
    return jsonify(schema.dump(db.query(Issue).get(id)).data or {})

@app.route('/api/issue/<int:id>', methods=['DELETE'])
def issue_id_delete(id):
    issue = db.query(Issue).get(id)
    if issue:
        db_do(db.delete, db.commit, issue)
    return jsonify({})

@app.route('/api/issue/<int:id>', methods=['PUT'])
def issue_id_put(id):
    issue = db.query(Issue).get(id)
    # don't allow creating with PUT
    if issue:
        fill_issue(issue, request.json)
        db_do(db.add, db.commit, issue)
    return jsonify({})


