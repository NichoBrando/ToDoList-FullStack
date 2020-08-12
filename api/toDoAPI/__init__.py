from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
from toDoAPI.controllers.loginManager import Sessions
sessionManager = Sessions()
db.create_all()
from toDoAPI.controllers import routes
from toDoAPI.models import user



