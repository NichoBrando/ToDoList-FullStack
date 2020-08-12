from toDoAPI.models.user import login 

class Sessions():
  def __init__(self):
    self._activeSessions = {}
  
  def addSession(self, ip, userId):
    self._activeSessions.update({ip: userId})
  
  def logout(self, ip):
    try:
      del self._activeSessions[ip]
      return 'deslogado com sucesso'
    except:
      return 'erro'
  
  def getSession(self, ip):
    userid = self._activeSessions.get(ip, -1)
    if userid == -1:
      return False
    else:
      return userid