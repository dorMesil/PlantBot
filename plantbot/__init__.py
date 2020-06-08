from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__,template_folder="templates",static_folder="static", instance_relative_config=True)

app.config.from_object('plantbot.config')

client = MongoClient(app.config["MONGO_URI"])

import plantbot.views
