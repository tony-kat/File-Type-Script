import os
from shutil import copyfile


def getListOfFiles(dir_name):
    listOfFile = os.listdir(dir_name)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dir_name, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    pdfFiles = []
    for file in allFiles:
        if file.endswith('.pdf'):
            pdfFiles.append(file)
    return pdfFiles

dir_mid ='C:/Path/to/main/directory/here'
dir_name = ['/names','/of' , '/sub' , '/directories' , '/here'];
for i in dir_name:
    j = dir_mid + i
    k = getListOfFiles(j)
    print(f"\n{i[1:66]}'s pdf files:")
    print (*k, sep = '\n')