from toDoAPI.models.user import login 

class Sessions():
  def __init__(self):
    self._activeSessions = {}
  
  def addSession(self, ip, user, passwd):
    userid = login(user, passwd)
    if type(userid) == "int":
      self._activeSession.update({ip: userid})
      return 'Session added'
    elif type(userid) == "str":
      return userid
  
  def logout(self, ip):
    try:
      del self._activeSessions[ip]
      return 'deslogado com sucesso'
    except:
      return 'erro'
  
  def getSession(self, ip):
    userid = self._activeSession.get(ip, -1)
    if userid == -1:
      return False
    else:
      return userid