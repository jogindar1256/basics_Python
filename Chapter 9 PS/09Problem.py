# check if the file are identicaly same

with open("meta.txt") as f:
  content1 = f.read()

with open("copy_meta.txt") as f:
  content2 = f.read()


if(content1 == content2):
  print("The files are identicaly same")

else:
  print("No files are identicaly same")