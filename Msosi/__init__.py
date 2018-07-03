
from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config.from_object('config')
db = MongoEngine(app)


from .home.controllers.home import home
app.register_blueprint(home, url_prefix='/home')