import os

directory_path = '/'

#List all the files and directory

contents = os.listdir(directory_path)


#Print the each files and directory name
for items in contents:
    print(items)