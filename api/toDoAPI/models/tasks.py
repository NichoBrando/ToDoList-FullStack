from toDoAPI import db

class Tasks(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  user_id = db.Column(db.String(50))
  task = db.Column(db.String(100))
  status = db.Column(db.Integer)

  def __init__(self, userid, task, status):
    self.user_id = userid
    self.task = task
    self.status = status

def getTasks(userid):
  tasks = Tasks.query.filter(Tasks.user_id == userid).all()
  toReturn = []
  for i in tasks:
    toReturn.append({'id': i.id, 'task': i.task, 'status': i.status})
  return toReturn

def updateTask(task, userid):
  taskQuery = Tasks.query.filter(Tasks.user_id == userid).filter(Tasks.id == task).first()
  if taskQuery != None:
    taskQuery.status = not(taskQuery.status)
    db.session.commit()
    return "Sucess"
  return 0