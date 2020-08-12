from toDoAPI import app, db, sessionManager
from toDoAPI.models.user import *
from flask import jsonify, request

@app.route("/api/register", methods = ["POST"])
def register():
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
      return jsonify('Sucess! Your user has been created!')
    return jsonify("none")
  
@app.route("/api/login")
@app.route("/api/haveuser")
@app.route("api/gettasks")
@app.route("api/updatetask/<taskid>")
@app.route("api/deletetask/<taskid>")
