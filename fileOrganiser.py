import os
import shutil
#C:/Users/Harinarayan/hari/whitehatjr/classes/c99
path1 = input("Enter the Directory to be Sorted ")
listFiles =os.listdir(path1)
for l in listFiles:
    name,ext=os.path.splitext(l)
    print(name);
    print(ext);
    if(ext==""):
        continue
    if(os.path.exists(path1+"/"+ext)):
        shutil.move(path1+"/"+l,path1+"/"+ext+"/"+l)
    else:
        os.mkdir(path1+"/"+ext)
        shutil.move(path1+"/"+l,path1+"/"+ext+"/"+l)