class EventReader:
    def __init__(self):
        pass
    def getEvent(self, eventId):
        eventList = fileH.readJson("files/events.json")
        for event in eventList:
            if event["id"] == eventId:
                return event
    def invokeEvent(self, eventId):
        eventIn = getEvent(eventId)
        if eventIn["flag"] == 0 or eventIn["reinvokable"] == 1:
            eventList = fileH.readJson("files/events.json")
            for event in eventList:
                if event["id"] == eventId:
                    event["flag"] = 1
            fileH.writeJson("files/events.json", eventList)
            script = getEvent(eventId)["script"]
            inputP.runScript(script)
        
