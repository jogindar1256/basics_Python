# for one word
words = "donkey"

# with open("meta.txt", "r") as f:
#   content = f.read()
# 
# contentNew = content.replace(words, "######")
# 
# with open("meta.txt", "w") as f:
#   f.write(contentNew)



#For Multiple Words

words = ["donkey", "ganda"]

with open("meta.txt", "r") as f:
  content = f.read()

for word in words:
  content = content.replace(word, "#"* len(word))

with open("meta.txt", "w") as f:
  f.write(content)
