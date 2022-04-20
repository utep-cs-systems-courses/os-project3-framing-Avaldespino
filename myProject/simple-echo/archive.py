#! /usr/bin/python3
import os,re,sys

#Takes in list of files and an output file
#recieve file descriptor for write binary
#iterate through files


def archive(files, outputFile):
    archOutFile = open(outputFile, 'wb')
    
    for file in files:
        f = open(file,'r')
        data = bytearray()

        fileNameData = get_data(file, len(file.encode()))
        data += fileNameData
        print(data)

        contents = get_data(f.read(), os.path.getsize(file))
        data += contents
        
        archOutFile.write(data)
        f.close()


    archOutFile.close()





#get data and size of data
#Encode size of data with 8 bytes
#then encode and add contents
        
def get_data(data, size):
    archData = bytearray()
    archData += bytearray(size.to_bytes(8,'big'))
    archData += bytearray(data.encode())

    return archData


if (len(sys.argv) < 3):
    os.write(2, "Not enough arguments, ./archive.py <FileoutName> <list of files...>".encode())
    sys.exit(1)

os.write(1, "Archiving files\n".encode())
files = sys.argv[2:]
outFile = sys.argv[1]
archive(files,outFile)
os.write(1, "Archived to {}\n".format(sys.argv[1]).encode())
 
