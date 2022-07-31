"""
import os 

#print(dir(os)) 
os.chdir("C:/Users/yasir/Desktop")
#print(os.getcwd())

print(os.listdir())
"""

import os 
from datetime import datetime
print(os.getcwd())

#os.mkdir("Trying1")

#os.makedirs("Trying2/Trying3")

#os.rmdir("Trying2/Trying3")

#os.mkdir("Trying2/Trying3")

#os.rmdir("Trying1")

#os.removedirs("Trying2/Trying3")

#os.rename("textttt.txt","Text5.txt")

#print(datetime.fromtimestamp(os.stat("Text5.txt").st_mtime))

"""
print(os.walk("C:/Users/yasir/Desktop/Stackoverflow Using Notes"))

for i in os.walk("C:/Users/yasir/Desktop/Stackoverflow Using Notes"):
    print(i)
"""
"""
for folder_way,folder_names,file_names in os.walk("C:/Users/yasir/Desktop/Karısık Dosyalar/wordbitle alakalı"):
    print("Folder way",folder_way)
    print("Folder names",folder_names)
    print("File names",file_names)
    print("*********************")
"""
"""
for folder_way,folder_names,file_names in os.walk("C:/Users/yasir/Desktop/Karısık Dosyalar/wordbitle alakalı"):
    for i in file_names:
        print(i)
"""
"""
for folder_way,folder_names,file_names in os.walk("C:/Users/yasir/Desktop/Karısık Dosyalar/wordbitle alakalı"):
    for i in file_names:
        if(i.endswith(".pdf")):
            print(i)
"""




