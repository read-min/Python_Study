#memo.py
#Simple Notepad in Console
#-v is view the memo, -a is add the memo

import time
import sys

#if don't exist the argc
if not sys.argv[1:] or sys.argv[1] not in ['-v','-a']:
  print"""
  Usage
  -v : View the memo
  -a : Add the memo
  """
  exit()
#type '-a'
if sys.argv[1] == '-a':
  f=open("note.txt",'a')
  word=raw_input("Enter : ")
  f.write(time.ctime()+': ' + word + '\n')
  f.close()

#type '-v'
elif sys.argv[1] == '-v':
  try:  #if 'note.txt' is existed
    f=open("note.txt",'r')
    print f.read()
    f.close()
  except IOError: #if it isn't exigsted
    print "Not Exist Memo, Please Make memofile."
    
    
