
import os
import subprocess
#from subprocess import call
lsCommand = subprocess.Popen('ls', stdout=subprocess.PIPE)

lsOutput = lsCommand.stdout.read()

eachEntry = lsOutput.splitlines(True) 


print('eachEntry = ', eachEntry)

for i in range(len(eachEntry)):
    fileName = eachEntry[i].split('\n')[0]
    fileNameWithoutSpaces = str(fileName).replace(' ', '_')
    os.rename(fileName, fileNameWithoutSpaces)
    
