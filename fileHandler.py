#!usr/bin/env python

import os, json

class fileHandler:

	def __init__(self):
		fnfMsg = ["File: ", " could not be found to open!"]		
 
	def readText(self, filePath):

		try:
			with open(filePath, "r") as inTxtFile:

				return inTxtFile.read()
		except FileNotFoundError:
			print(fnfMsg[0], filePath, fnfMsg[1])

	def writeText(self, filePath, strToWrite):

		with open(filePath, "w") as outTxtFile:

			outTxtFile.write(strToWrite)

			outTxtFile.close()

	def readJson(self, filePath):

		try:
			with open(filePath, "r") as inJsonFile:

				return json.load(inJsonFile)

		except FileNotFoundError:
			print(fnfMsg[0], filePath, fnfMsg[1])

	def writeJson(self, filePath, dictToWrite):

		with open(filePath, "w") as outJsonFile:

			json.dump(dictToWrite, outJsonFile)

			outJsonFile.close()

	def basicPath(self, fileName, fileDir=""):

		if fileDir != "":
			fileLocation = fileDir+"/"+fileName
		else:
			fileLocation = fileName

		return os.path.abspath(fileLocation)

	def jsonWhiteStrip(self, filePath):

		try:
			with open(filePath, "r") as inJson:

				contents = json.load(inJson)

			with open(filePath, "w") as outJson:

				json.dump(contents, outJson)
				
		except FileNotFoundError:
			print(fnfMsg[0], filePath, fnfMsg[1])


















