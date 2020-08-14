from toDoAPI.models.user import login 

#this class manage the sessions in this API. each time that anyone want to use, they will need
#to register or login in API.

class Sessions():
  def __init__(self):
    self._activeSessions = {}
  
  def addSession(self, ip, userId):
    self._activeSessions.update({ip: userId})
  
  def logout(self, ip):
    try:
      del self._activeSessions[ip]
      return 1
    except:
      return 0
  
  def getSession(self, ip):
    userid = self._activeSessions.get(ip, -1)
    if userid == -1:
      return False
    else:
      return userid