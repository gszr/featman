# Projects Management App 

This is my solution to the project specified at [specification.md](specification.md).

## Features

As specified, the app handles "feature requests", allowing one to add and view
features requested by users. Each request has the following fields:

* Title
* Description
* Client (selected among clients recorded in the app)
* Client priority: numbered prioriry (1..n). New requests are inserted with the
highest possible priority; e.g., if there are no requests, a new one will have
priority "1". If there is a request with the given priority, requests for that
client will be reordered
* Target Date
* Ticket URL
* Product (selected among the list of projects in the app)

Similar interfaces were provided for "Products", "Clients", and "Issues".
"Clients" and "Products" only have an ID and a Name. "Issues" have the following
fields:

* Title
* Description
* Reporter (which is selected among clients recorded in the system)
* Status (open, fixed, deployed, ...)
* Reported on: date the issue was reported
* Resolved on: optional field to show the date it was resolved

All of these entities can be displayed in their own page, in a table which
allows for sorting and filtering by any column.

## Tech stack

The tools I used -- most of which were recommended:

* Ubuntu for the deployed instance (on AWS free tier); FreeBSD on my dev
machine
* Backend:
  - Python 2.7
    - Flask
    - SQLAlchemy
    - Marshmallow and its integration with SQLAlchemy
    - pysqlite
  - SQLite
* Frontend:
  - Bootstrap v4 alpha
  - bootstrap-datepicker
  - jQuery
  - Knockout.js

## App structure

Structure of the implementation

### API

The API handlers are implemented in api\_(client, feature, issue, product).py
files and [app/api.py](app/api.py) file which simply imports all of them and
gets improted in [run.py](run.py).

The structure of the RESTful API is as follows, where "entity" refers to any
of client, feature, issue, product entities:

GET    /api/entity:    gets the JSON representation of all entities of that class  
POST   /api/entity:    adds a new entity  
GET    /api/entity/id: gets the JSON representation of entity whose ID is id  
PUT    /api/entity/id: updates entity whose ID is id  
DELETE /api/entity/id: deletes entity whose ID is id  

### Views

[app/view.py](app/view.py) contains the handlers that render HTML templates.

The pages follow a similar pattern to the APIs:

/entity/new: page to create a new entity  
/entity/all: page to view all entities of that class  

## Running

* Requirements
  - Python 2.7
  - pip Python modules manager
  - virtualenv

* Steps to run

  $ virtualenv env  
  $ pip install -r pip\_deps  
  $ source env/bin/activate  
  (env) $ python run.py

## TODO

* Frontend to PUT & DELETE methods for each of the entities; the API is
already there
* Automated deployment
* Tests (not really helping myself here, but I didn't write a single line of
(automated) test yet; the API I tested with curl)


## References

To implement the sorting feature I studied and based my code on 
[this](https://github.com/pstricker/koTableSort/).

