# import packages to get arg and list folders files into that path
import sys
import os
#assing the path argument to a variable named path
path=sys.argv[1]

#function in charge of listing the folder and files 
def ListFiles(pathList):
   print(os.listdir(pathList))


ListFiles(path)