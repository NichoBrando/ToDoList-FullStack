from toDoAPI import db
from datetime import datetime
import hashlib

def hashPassword(password):
  password = bytearray(password, 'utf-8')
  m = hashlib.sha256()
  m.update(password)
  return m.hexdigest()

class User(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(50))
  password = db.Column(db.String(64))

  def __init__(self, username, password):
    self.username = username
    self.password = password

def login(user, passwd):
  userExists = User.query.filter(User.username == user)
  if userExists != None:
    if userExists.password == passwd:
      return UserExists.id
    return "Invalid password"
  return "Username doesn\'t exists"

def existUser(user):
  result = User.query.filter(User.username == user)
  return 1 if type(result) == "str" else 0 