from flask import Flask
from pymongo import MongoClient
# from flask_pymongo import PyMongo

app = Flask(__name__,template_folder="templates",static_folder="static", instance_relative_config=True)


app.config.from_object('plantbot.config')
app.config.from_pyfile('config.py')

client = MongoClient("mongodb+srv://admin:admin1234@cluster0-rsh71.mongodb.net/test?retryWrites=true&w=majority")

# mongo = PyMongo()
# mongo.init_app(app)

import plantbot.views
