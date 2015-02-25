#Steal_USB.py 
#Find the usb_drive, and Copy the File in usb_drive

import os		
import os.path 		#Set the path
import glob			#make filelist
import shutil		#copy fun
import time			#for sleep function

print "\n"+"Copy_USB ver_0.1 made by Kali-KM"
#Enter the usb_drive path and save folder path
usb_path=raw_input("Enter the USB Drive Path : ")	#Set the object path
save_path=raw_input("Enter the Save Folder Path: ")	#Set the save path
print '\n'
				
def searchpath():
	if os.path.exists(usb_path)==True:		#Search the Path
		print 'Correctlly Path'
		filelist=glob.glob(usb_path+'\*')	#read the filelist & return the filelist
		for num in range(len(filelist)):	#repeat by length of filelist
			print filelist[num]+'\n'		#Show the copyfilename
			shutil.copy(filelist[num], save_path)	#Copy the file
		exit()
	else:
		print "Wrong Path"	#if it is wrong path, Rescanning
		time.sleep(1)		#Set the pause time
		searchpath()		#Recursion function

searchpath()
#exit the program
