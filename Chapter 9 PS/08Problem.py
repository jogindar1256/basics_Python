#generating the copy of the file

with open("meta.txt") as f:
  content = f.read()


with open("copy_meta.txt", "w") as f:
  f.write(content)
