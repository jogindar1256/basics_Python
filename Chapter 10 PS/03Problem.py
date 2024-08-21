class Demo:
  a = 4

o = Demo()
print(o.a) # Prints the class attibute boc'z instance attribute is not present
o.a = 0 # instance attribute is set
print(o.a) # Prints the Instance attibute boc'z instance attribute is present
print(Demo.a) # Print the class attribute