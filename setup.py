#setup.py

from distutils.core import setup
import py2exe

setup(console=['FileName.py'],
	options={
		"py2exe":{
			"bundle_files": 1
		}
	},
	zipfile=None)

#usage:
#Set 'filename.py'
#change the directory 
#python setup.py py2exe
