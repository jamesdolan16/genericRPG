class EventReader:
    def __init__(self):
        pass
    def getEvent(self, eventId):
        eventList = fileH.readJson("files/events.json")
        for event in eventList:
            if event["id"] == eventId:
                return event
    def invokeEvent(self, eventId):
        script = getEvent(eventId)["script"]
        inputP.runScript(script)
