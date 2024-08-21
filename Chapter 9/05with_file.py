f = open('file.txt')
print(f.read())
f.close()   #traditional method to close the file


#The same file will be clsoe using the with statement like this:
with open("file.txt") as f:
  print(f.read())

#you dont have to explicitly close the file