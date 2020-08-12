from toDoAPI import db

class Tasks(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  task = db.Column(db.String(50), unique = True)
  taskStatus = db.Column(db.Integer)

def getTasks(userid):
  tasks = User.query.filter(User.id == userid)
  return tasks if tasks != None else []
