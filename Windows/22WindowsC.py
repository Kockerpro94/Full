import os


Input_fileToCp = input("enter the folder you want to cp: ")
Input_folderTp = input("enter the path you want to copy: ")

os.system("copy " + Input_fileToCp + Input_folderTp)