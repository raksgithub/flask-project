from flask import Flask, make_response
from markupsafe import escape
from db import create_db


app = Flask(__name__)

db = create_db(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/authors")
def authors():
    """
    Returns a list of authors
    """
    response = make_response(list(db.authors.find({}, {"_id": 0})))
    response.headers["Content-Type"] = "application/json"
    return response

@app.route("/posts")
def posts():
    """
    Returns a list of posts
    """
    response = make_response(list(db.posts.find({}, {"_id": 0})))
    response.headers["Content-Type"] = "application/json"
    return response


@app.route("/<name>")
def hello(name):
    """
    Escapes from any user imput values to avoid injection attacks
    """
    return f"Hello {escape(name)}!!"
