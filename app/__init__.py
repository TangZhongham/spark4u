from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('settings.py')

db = SQLAlchemy(app)


from . import views, settings, commands

