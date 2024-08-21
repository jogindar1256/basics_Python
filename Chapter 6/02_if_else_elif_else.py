#if else elif else ladder
a = int(input("Enter you age: "))

if(a>=18):
  print("You are above the age of concent")
  print("Good For You")
elif(a<0):
  print("You are Entering an invalid age")

elif(a==0):
  print("You are entering 0 which is invalid age")
else:
  print("You are below the age of concent")


print("End of Program")