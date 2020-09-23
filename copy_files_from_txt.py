import sys
import os
import shutil
from pathlib import Path

def copy_files_from_txt(*args):
	'''
	Look for filenames in .txt list in the system and copy them to new folder.
	args: (filePath, aproxPath, outPath)

	filePath: full path to .txt file including filenames.
	aproxPath: closest estimated path to make lookup faster (make sure the file is somewhere inside this
		directory or subdirectories).
	outPath: full path to where the files will be coppied.
	'''
	filePath = sys.argv[1]
	aproxPath = sys.argv[2]
	outPath = sys.argv[3]

	if not os.path.isfile(filePath):
		print(f'File {filePath} does not exist')
		sys.exit()

	if not os.path.isdir(aproxPath):
		print(f'Folder {aproxPath} does not exist')
		sys.exit()

	if not os.path.isdir(outPath):
		print(f'Creating new output folder at: {outPath}')
		os.mkdir(outPath)

	print(filePath)
	print(aproxPath)
	print(outPath)

	with open(filePath, 'r') as files:
		for file in files.readlines():
			try:
				for path in Path(aproxPath).rglob(file.rstrip('\n') + '.wav'):
					print(path)
					shutil.copy(path, outPath)
			except FileNotFoundError as e:
				print(e)
				sys.exit()


if __name__ == '__main__':
	copy_files_from_txt()