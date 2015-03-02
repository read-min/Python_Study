#Del_file.py

import os,os.path,glob

print"Del_File ver_0.1 made by Kali-KM\n"

del_path=raw_input("Enter the Path : ")

def searchpath():
	if os.path.exists(del_path)==True:
		print "Correctly Path"
		filelist=glob.glob(del_path)
		for num in range(len(filelist)):
			word="rmdir /s /q %s"%filelist[num]
			os.system(word)
	else:
		print "Wrong Path"
		time.sleep(1)
		searchpath()

searchpath()
