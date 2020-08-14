from toDoAPI import db
import hashlib

#hashPassword will return a hash, which represents your password

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

#login user, if exists

def login(username, passwd):
  userExists = User.query.filter(User.username == username).first()
  if userExists:
    if userExists.password == passwd:
      return userExists.id
    return -1
  return 0

#check if user exists
def existUser(user):
  result = db.session.query(db.exists().where(User.username == user)).scalar()
  return result

#compare the password in db and received by user.
def checkPassword(passwd1, passwd2):
  return passwd1 == passwd2

#return id from user
def getUsername(id):
  user = User.query.filter(User.id == id).first()
  return user.username