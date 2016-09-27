# Custom Lisp interpreter

class LispInterpreter:

	strToInterpret = ""
	scriptList = []

	def parser(self, scripts):
		global shellF
		shellF = False
		for script in scripts:
			print(script)

			if script[0] == "echo":
				print(script[1])
			elif script[0] == "shell": # buggy bit
				shellF = True
				while shellF:
					shellScript = input("SHELL>")
					self.runScript(shellScript)
			elif script[0] == "shellQ":
				shellF = False

			else:
				print("Keyword: ", script[0], " is not valid!")

	def lexer(self, scriptString):
		script = []
		scripts = []
		token = ""
		inQuote = False
		isNewScript = False
		# quick check if semicolon is present at the end of the script
		try:
			if scriptString[-1] == ";":
				pass
			else:
				print("script missing \";\"")
				return []

			for char in scriptString:
				if char == " ":
					if inQuote:
						token += char
					if isNewScript:
						isNewScript = False
					else:
						script.append(token)
						token = ""
						isNewScript = False
				elif char == "\"":
					if inQuote:
						inQuote = False
					else:
						inQuote = True
				elif char == ";":
					if inQuote:
						pass
					else:
						script.append(token)
						scripts.append(script)
						script = []
						token = ""
						isNewScript = True
				else:
					token += char
				print(token, "\n", script, "\n", scripts)
			return scripts
		except IndexError:
			print("null scripts are not valid!")
			return scripts

	def runScript(self, strToInterpret):

		self.scriptList = self.lexer(strToInterpret)
		self.parser(self.scriptList)
