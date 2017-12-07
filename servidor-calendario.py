# saved as greeting-server.py
from datetime import datetime, date, time, timedelta
import calendar
# saved as greeting-server.py
import Pyro4

@Pyro4.expose
class GreetingMaker(object):
    def get_fortune(self, anio):
        return calendar.TextCalendar(calendar.MONDAY).formatyear(anio, 
                                                        2, 1, 1, 2)

daemon = Pyro4.Daemon("192.168.45.100")                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
uri = daemon.register(GreetingMaker)
print uri   # register the greeting maker as a Pyro object
ns.register("example.greeting", uri)   # register the object with a name in the name server

print("Ready.")
daemon.requestLoop()                   # start the event loop of the server to wait for calls