import os
# import pdb

sourceEncoding = 'gb2312'
targetEncoding = 'utf-8'
currPath = '.'
extension = ''

def encodeConvert(filename, targetEncoding):
	file_object = open(filename, 'r', encoding = sourceEncoding)
	contents = file_object.read()
	file_object.close()
	encoded_contents = contents.encode(targetEncoding)
	file_object = open(filename, 'w+b')
	file_object.write(encoded_contents)
	file_object.close()

items = os.listdir()

def convertAll(items):
	global currPath
	global extension
	for itemname in items:
		if os.path.isfile(currPath + '/' + itemname):
			for char in itemname:
				if char == '.':
					extension = ''
				extension = extension + char
			if extension == '.h' or extension == '.c' or extension == '.cpp' or extension == '.txt':
				encodeConvert(currPath + '/' + itemname, targetEncoding)
		elif os.path.isdir(currPath + '/' + itemname):
			pathStack = currPath
			currPath = currPath + '/' + itemname
			i = os.listdir(currPath)
			convertAll(i)
			currPath = pathStack
			pathStack = ''
		else:
			# I don't care
			pass
# pdb.set_trace()
convertAll(items)
