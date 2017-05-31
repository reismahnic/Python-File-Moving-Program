import shutil
import os

#List the source folder and destination folder
source = 'C:\Users\Reis\Desktop\Folder A'
destination = 'C:\Users\Reis\Desktop\Folder B'

#Print the list of file names
files = os.listdir(source)
print "Moving the files "
print (os.listdir(source))
print " to "
print (destination)
#Move all files in Folder A to Folder B
for f in files:
    shutil.move(os.path.join(source, f), destination)
