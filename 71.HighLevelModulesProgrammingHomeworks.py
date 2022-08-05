#Code1
"""
import os 

print(os.getcwd())
with open("pdf_files.txt","w",encoding="utf-8") as file1:
    for folder_way,folder_names,file_names in os.walk("C:/"):
        for i in file_names:
            if(i.endswith(".pdf")):
                file1.write((folder_way+"\n"+i)+"\n")
                print("a")

with open("mp4_files.txt","w",encoding="utf-8") as file2:
    for folder_way,folder_names,file_names in os.walk("C:/"):
        for j in file_names:
            if(j.endswith(".mp4")):
                file2.write((folder_way+"\n"+j)+"\n")
                print("b")
with open("txt_files.txt","w",encoding="utf-8") as file3:
    for folder_way,folder_names,file_names in os.walk("C:/"):
        for k in file_names:
            if(k.endswith(".txt")):
                file3.write((folder_way+"\n"+k)+"\n")
                print("c")
"""











