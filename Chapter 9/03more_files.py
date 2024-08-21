f = open("file.txt")

#for multiple lines
# lines = f.readlines()
# print(lines, type(lines))

#for 1 line
line1 = f.readline()
print(line1, type(line1))

#for 2 line
line2 = f.readline()
print(line2, type(line2))

#Performing same with while loop
line = f.readline()
while(line != ""):
  print(line)
  line = f.readline()


f.close()