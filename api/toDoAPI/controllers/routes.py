from toDoAPI import app, db, sessionManager
from toDoAPI.models.user import *
from toDoAPI.models.tasks import *
from flask import jsonify, request

#this is the core of API, the controller. it will receive a request,
#and manage, according to request URL and session in loginManager
#Request.remote_addr is IP from user, this will help to storage the session.
#register a user in database
@app.route("/api/register", methods = ["POST"])
def registerRoute():
  exists = sessionManager.getSession(request.remote_addr)
  if exists == True:
    return jsonify(-1)
  req = request.get_json()
  if len(req['username']) < 5:
    return jsonify(-1)
  if len(req['password']) < 5:
    return jsonify(-1)
  newUser = User(req['username'], hashPassword(req['password']))
  if existUser(req['username']):
    return jsonify(-1)
  else:
    db.session.add(newUser)
    db.session.commit()
    sessionManager.addSession(request.remote_addr, newUser.id)
    return jsonify(1)
  return jsonify(-1)

#log a user, if have not logged on API
@app.route("/api/login", methods = ["POST"])
def loginRoute():
  exists = sessionManager.getSession(request.remote_addr)
  if exists != False:
    return jsonify("Already logged!")
  req = request.get_json()
  loginStatus = login(req['username'], hashPassword(req['password']))
  if loginStatus == -1:
    return jsonify("Invalid password!")
  elif loginStatus == 0:
    return jsonify("Invalid username!")
  else:
    sessionManager.addSession(request.remote_addr, loginStatus)
    return jsonify("Sucess! Redirectioning...")

#logout a user, if have logged on API
@app.route("/api/logout", methods = ["GET"])
def logoutRoute():
  exists = sessionManager.getSession(request.remote_addr)
  if exists != False:
    sessionManager.logout(request.remote_addr)
    return jsonify("Sucessfuly logout")
  else:
    return jsonify("Not logged")

#return tasks as JSON.
@app.route("/api/gettasks", methods=["GET"])
def getTasksRoute():
  exists = sessionManager.getSession(request.remote_addr)
  if exists == False:
    return jsonify([])
  return jsonify(getTasks(exists))

#receive the task from frontend, and create the task and send the id back to front
@app.route("/api/createTask", methods=["POST"])
def createTaskRoute():
  exists = sessionManager.getSession(request.remote_addr)
  if exists == False:
    return jsonify('Not logged')
  req = request.get_json()
  newTasks = Tasks(sessionManager.getSession(request.remote_addr), req['content'], 0)
  db.session.add(newTasks)
  db.session.commit()
  return jsonify(newTasks.id)

#receive id, and update the task, according to task id and user id
@app.route("/api/updateTask/<taskid>", methods=["GET"])
def updateTaskRoute(taskid):
  exists = sessionManager.getSession(request.remote_addr)
  if exists == False:
    return jsonify(0)
  return jsonify(updateTask(taskid, exists))

#receive id and user, if connected, this function will delete the task
@app.route("/api/deleteTask/<taskid>", methods=["GET"])
def deleteTaskRoute(taskid):
  exists = sessionManager.getSession(request.remote_addr)
  if exists == False:
    return jsonify("Not logged")
  return jsonify(deleteTask(taskid, exists))

#return the logged username
@app.route("/api/getuser", methods = ["GET"])
def loguser():
  exists = sessionManager.getSession(request.remote_addr)
  if exists == False:
    return jsonify("")
  return jsonify(getUsername(exists))