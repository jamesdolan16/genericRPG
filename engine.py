from libraries import fileHandler

class Engine:
	def __init__(self):
	        self.fh = fileHandler.FileHandler()
	def _getNextEvent(self,eventPtr):
		eventMapPath = self.fh.basicPath("eventMap.json", "files")
	def run(self):
		eventPtr = 0
		isRun = True
		while isRun:
			self._getNextEvent(eventPtr)
