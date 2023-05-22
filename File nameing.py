# -*- coding: utf-8 -*-
"""
Created on Wed May 17 09:16:49 2023

@author: tomer
"""

database = input("insert file pathway: ")
splitpath=database.rfind("\\")
endfile=database.rfind(".")
filename= database[splitpath+1:endfile]
print(filename+"_Encoded"+database[endfile:])

with open(database) as text:
    textlist=text.read()
    textlist=textlist.split(" ")
    
textchar=""
for i in range(len(textlist)):
     textchar += chr(int(textlist[i])-1)
    
print (textchar)
    