# find the line number in the meta

with open("meta.txt") as f:
  lines = f.readlines()
  
lineno = 1
for line in lines:
  if("donkey" in line):
    print(f"yes donkey is present. Line no:{line}")
  lineno += 1
else:
  print("No donkey is present in the meta")




#chat Gpt given code
# with open("meta.txt") as f:
  # found = False
  # for i, line in enumerate(f, start=1):
    # if "donkey" in line:
      # print(f"Yes, 'donkey' is present. Line no: {i}")
      # found = True
#      break  # If you want to stop after finding the first occurrence
  # if not found:
    # print("No donkey is present in the meta")