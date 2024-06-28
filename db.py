from flask_pymongo import PyMongo
from config import MONGO_URI

def create_db(app):
    return PyMongo(app, uri=MONGO_URI).db

