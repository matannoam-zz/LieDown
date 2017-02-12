#LieDown

An example REST API using JSON on a Flask server.

This is a demo of the following:
- using the app factory pattern with [Flask](http://flask.pocoo.org/)
- creating an API as a Flask app
- factoring an API using [Flask Blueprints](http://flask.pocoo.org/docs/blueprints/)
- Creating API Resources with [Flask-Restful](http://flask-restful.readthedocs.io/)
- Serializing request and response data with Flask-Marshmallow on top of Marshmallow. This entirely replaces Flask-Restful's notoriously problematic marshalling as suggested [here](https://github.com/flask-restful/flask-restful/issues/335).

## Usage

To run the application in development

```
pip install -r requirements.txt
pip install -r requirements-dev.txt
ln -s ../../scripts/pre-commit .git/hooks/pre-commit


python manage.py runserver
```

Use a tool like `curl`, [`httpie` (link)](https://httpie.org/), or [Postman](https://www.getpostman.com/) to make requests to `localhost:5000`.

example with httpie

```
http post :5000/orders/ order_id="number 1"
```
