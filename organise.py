import os
import shutil

from_dir = "C:/Users/adity/OneDrive/Desktop/Project-102 F1"
to_dir = "C:/Users/adity/OneDrive/Desktop/Project-102 F2/"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == '':
        continue 
    if extension in ['.gif','.jpg','.png','.jfif']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Image Files"
        path3 = to_dir + '/' + "Image Files" + '/' + file_name
        #print(path1)
        #print(path3)

        if os.path.exists(path2):
            print("moving" + file_name + "...")
            shutil.copy(path1,path3)
        else :
            os.mkdir(path2)
            print("moving" + file_name + "...")
            shutil.copy(path1,path3)
                

