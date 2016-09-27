from libraries import fileHandler, lispInterpreter

class Engine:
	def __init__(self):
		global fileH
		fileH = fileHandler.FileHandler()
		global inputP
		inputP = lispInterpreter.LispInterpreter()

	def run(self):
		toLisp = input(">")
		inputP.runScript(toLisp)