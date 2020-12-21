import shutil
import os
source = input("Enter the Source ")
destination = input("Enter the Destination ")
listFiles = os.listdir(source)
print(listFiles)
for l in listFiles:
    shutil.move((source+"/"+l),destination)