from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#using SQLAlchemy ORM

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
from toDoAPI.controllers.loginManager import Sessions
sessionManager = Sessions()

from toDoAPI.controllers import routes
from toDoAPI.models.user import *
from toDoAPI.models.tasks import *

#MVC design

db.create_all()
#db.create_all will create the sqlite database, you dont need to install mysql/postgre

