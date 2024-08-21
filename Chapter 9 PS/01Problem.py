f = open("poem.txt")
content = f.read()

if("twinkle" in content):
  print("The word twinkle is present in the poem")

else:
  print("Oops! the word twinkle is not present in poem")

f.close()