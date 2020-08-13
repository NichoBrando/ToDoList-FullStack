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

def login(username, passwd):
  userExists = User.query.filter(username == username).first()
  if userExists:
    if userExists.password == passwd:
      return userExists.id
    return -1
  return 0

def existUser(user):
  result = db.session.query(db.exists().where(User.username == user)).scalar()
  return result

def checkPassword(passwd1, passwd2):
  return passwd1 == passwd2