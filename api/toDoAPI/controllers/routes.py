from toDoAPI import app, db, sessionManager
from toDoAPI.models.user import *
from toDoAPI.models.tasks import *
from flask import jsonify, request

@app.route("/api/register", methods = ["POST"])
def registerRoute():
    req = request.get_json()
    if len(req['username']) < 5:
      return jsonify('Invalid username')
    if len(req['password']) < 5:
      return jsonify('Invalid password')
    newUser = User(req['username'], hashPassword(req['password']))
    if existUser(req['username']):
      return jsonify('Username already exists')
    else:
      db.session.add(newUser)
      db.session.commit()
      sessionManager.addSession(request.remote_addr, newUser.id)
      return jsonify('Sucess! Your user has been created!')
    return jsonify("none")

@app.route("/api/login", methods = ["POST"])
def loginRoute():
  exists = sessionManager.getSession(request.remote_addr)
  if exists != False:
    return jsonify("Already logged")
  req = request.get_json()
  loginStatus = login(req['username'], hashPassword(req['password']))
  if loginStatus == -1:
    return jsonify("Invalid password")
  elif loginStatus == 0:
    return jsonify("Invalid username")
  else:
    sessionManager.addSession(request.remote_addr, loginStatus)
    return jsonify("Sucess")

@app.route("/api/logout", methods = ["GET"])
def logoutRoute():
  exists = sessionManager.getSession(request.remote_addr)
  if exists != False:
    sessionManager.logout(request.remote_addr)
    return jsonify("Sucessfuly logout")
  else:
    return jsonify("Not logged")

@app.route("/api/gettasks", methods=["GET"])
def getTasksRoute():
  exists = sessionManager.getSession(request.remote_addr)
  if exists == False:
    return jsonify('Not logged')
  return jsonify(getTasks(exists))

@app.route("/api/createTask", methods=["POST"])
def createTaskRoute():
  exists = sessionManager.getSession(request.remote_addr)
  if exists == False:
    return jsonify('Not logged')
  req = request.get_json()
  newTasks = Tasks(sessionManager.getSession(request.remote_addr), req['content'], 0)
  db.session.add(newTasks)
  db.session.commit()
  return jsonify('Create task: {}'.format(req['content']))

@app.route("/api/updateTask/<taskid>", methods=["GET"])
def updateTaskRoute(taskid):
  exists = sessionManager.getSession(request.remote_addr)
  if exists == False:
    return jsonify("Not logged")
  return jsonify(updateTask(taskid, exists))

@app.route("/api/deleteTask/<taskid>", methods=["GET"])
def deleteTaskRoute(taskid):
  exists = sessionManager.getSession(request.remote_addr)
  if exists == False:
    return jsonify("Not logged")
  return jsonify(deleteTask(taskid, exists))