from flask import Flask

app = Flask(__name__,template_folder="templates",static_folder="static", instance_relative_config=True)


app.config.from_object('config')
app.config.from_pyfile('config.py')

import plantbot.views
