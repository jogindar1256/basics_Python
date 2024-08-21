marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))
marks4 = int(input("Enter Marks 4: "))

#Check for Total Percentage
total_percentage = (100*(marks1 + marks2 + marks3 + marks4))/400

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 and marks4>=33):
  print("You are passed: ", total_percentage)

else:
  print("You failed, try again next year: ", total_percentage)