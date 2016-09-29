from libraries import fileHandler, lispInterpreter

class EventReader:
    def __init__(self):
        self.fh = fileHandler.FileHandler()
        self.li = lispInterpreter.LispInterpreter()
    def getEvent(self, eventId):
        eventList = self.fh.readJson("files/events.json")
        for event in eventList:
            if event["id"] == eventId:
                return event
    def invokeEvent(self, eventId):
        eventIn = self.getEvent(eventId)
        if eventIn["flag"] == 0 or eventIn["reinvokable"] == 1:
            eventList = self.fh.readJson("files/events.json")
            for event in eventList:
                if event["id"] == eventId:
                    event["flag"] = 1
            self.fh.writeJson("files/events.json", eventList)
            script = self.getEvent(eventId)["script"]
            self.li.runScript(script)
        
