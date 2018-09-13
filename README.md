# LieDown

An example REST API using JSON on a Flask server.

This is a demo of the following:
- using the app factory pattern with [Flask](http://flask.pocoo.org/)
- creating an API as a Flask app
- factoring an API using [Flask Blueprints](http://flask.pocoo.org/docs/blueprints/)
- Creating API Resources with [Flask-Restful](http://flask-restful.readthedocs.io/)
- Serializing request and response data with Flask-Marshmallow on top of Marshmallow. This entirely replaces Flask-Restful's notoriously problematic marshalling as suggested [here](https://github.com/flask-restful/flask-restful/issues/335).

Note on rogue fields - extra information notincluded in the schema on requests are ignored by default. Similarly, models such as ORM objects can be used to persist information, and the response will only include schema fields as well. Variables can easily be used to change this behavior.

## Usage

To run the application in development

```
pip install -r requirements.txt -r requirements-dev.txt

ln -s ../../scripts/pre-commit .git/hooks/pre-commit


python manage.py runserver
```

Use a tool like `curl`, [`httpie` (link)](https://httpie.org/), or [Postman](https://www.getpostman.com/) to make requests to `localhost:5000`.

examples with httpie

```
http post :5000/orders/ order_id="number 1"  # returns 201 CREATED

http post :5000/orders/ placed="not a date"  # returns a 400 error
```

required field example
```
http post :5000/orders/ shipping_address:='{"zip_code": "10016"}'  # returns 201 CREATED

http post :5000/orders/ shipping_address:='{"first_name": "Ann"}'  # returns a 400 error
```

All requests can be processed with an ID. A UUID is recommend.
```
http post :5000/orders/ order_id="number 1" Request-Id:ABC-123  # returns 201 CREATED with addditional header
http post :5000/orders/ placed="not a date" Request-Id:ABC-123  # returns a 400 error with addditional header
```
