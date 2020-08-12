from toDoAPI import app, db, sessionManager
from toDoAPI.models.user import *
from flask import jsonify, request

@app.route("/api/register", methods = ["POST"])
def registerRoute():
    req = request.get_json()
    print(req)
    if len(req['username']) < 5:
      return jsonify('Invalid username')
    if len(req['password']) < 5:
      return jsonify('Invalid password')
    newUser = User(req['username'], hashPassword(req['password']))
    print(existUser(req['username']))
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

"""
@app.route("/api/login")
@app.route("/api/haveuser")
@app.route("api/gettasks")
@app.route("api/updatetask/<taskid>")
@app.route("api/deletetask/<taskid>")
"""