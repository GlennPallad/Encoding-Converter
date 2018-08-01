import os
# import pdb

sourceEncoding = 'gb2312'
targetEncoding = 'utf-8'
currPath = '.'
extension = ''
output_log = ''
converted_log = ''
not_converted_log = ''

def encodeConvert(filename, targetEncoding):
	global converted_log
	global not_converted_log
	try:
		file_object = open(filename, 'r', encoding = sourceEncoding)
		contents = file_object.read()
	except UnicodeDecodeError:
		not_converted_log = not_converted_log + filename + '\n'
		return None
	except PermissionError:
		not_converted_log = not_converted_log + filename + '\n'
		return None
	file_object.close()
	encoded_contents = contents.encode(targetEncoding)
	try:
		file_object = open(filename, 'w+b')
		file_object.write(encoded_contents)
	except PermissionError:
		not_converted_log = not_converted_log + filename + '\n'
		return None
	file_object.close()
	converted_log = converted_log + filename + '\n'		

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
if not_converted_log == '':
	print('All files converted!')
else:
	output_log = ('Files converted:\n' + converted_log + '\nFiles didn\'t convert:\n' + not_converted_log)
	file_object = open('EncodingConvert.log', 'w+b')
	file_object.write(output_log.encode('utf-8'))
	file_object.close()