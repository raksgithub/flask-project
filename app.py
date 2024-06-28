from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/<name>")
def hello(name):
    """
    Escapes from any user imput values to avoid injection attacks
    """
    return f"Hello {escape(name)}!!"
