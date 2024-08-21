a = int(input('Enter a First Number: '))
b = int(input('Enter a First Number: '))

if(b==0):
  raise ZeroDivisionError("Hey our program is not meant to divide by numbers zero")
else:
  print(f"The division a/b is {a/b}")