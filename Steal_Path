#Steal_Path.py 

import os,os.path,glob,shutil,time			

print "\n"+"Copy_USB ver_0.1 made by Kali-KM"

usb_path=raw_input("Enter the USB Drive Path : ")
save_path=raw_input("Enter the Save Folder Path: ")
print '\n'

def searchpath():
	if os.path.exists(usb_path)==True:
		print 'Correctlly Path'
		filelist=glob.glob(usb_path+'\*')	
		for num in range(len(filelist)):
			print filelist[num]+'\n'	
			shutil.copy(filelist[num], save_path)
		exit()
	else:
		print "Wrong Path"
		time.sleep(1)
		searchpath()
searchpath()


