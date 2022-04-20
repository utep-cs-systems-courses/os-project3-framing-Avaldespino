#! /usr/bin/python3
import os,re,sys

#format of arch data should be <file name length> <File name> <Contents length> <Contents> repeating

def dearch(archData):

    file = open(archData, 'rb')
    data = file.read()


    while len(data) > 0:   #while there is still data left
        fileNameLen = int.from_bytes(data[:8],'big')
        fileName = data[8:8+fileNameLen]
        
        data = data[8+fileNameLen:]

        fileContentsLen = int.from_bytes(data[:8], 'big')
        fileContents = data[8:8+fileContentsLen]
        
        data = data[8:8+fileContentsLen]
        
        targetFile = open(fileName.decode(), "wb")
        targetFile.write(fileContents)
        targetFile.close()


    file.close()



 #Will take just one arch file in format ./dearch.py <arch file>

if len(sys.argv) > 2:
     os.write(2,"Too many arguments, use format ./dearch.py <arch file>\n".encode())
     sys.exit(1)

os.write(1, "Decompressing arch file\n".encode())
dearch(sys.argv[1])
os.write(1, "Task done\n".encode())
