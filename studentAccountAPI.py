import os.path
from register import register_from_textfile

def StudentAccountAPI():
 file_exists = os.path.exists('studentAccounts.txt')

 #print(file_exists)
 count=0
 if (file_exists): 
  with open("studentAccounts.txt") as fp:
    Lines = fp.readlines()
    
    for line in Lines:
     count += 1
    # print("Line{}: {}".format(count, line.strip()))
     if ( count ==1 ):
        
        value = line.split(',')
        username=value[0]
        fname=value[1]
        lname=value[2]
        
        #print(username)
        #print(fname)
        #print(lname)
    
     elif(count==2):
      password=line

      #print(password)
     elif(count==3):

      register_from_textfile(username,fname,lname,password)
      count=0

#print("Using readlines()")