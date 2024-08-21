# print the multiplication of table from taking the input form user

n = int(input("Enter the Number to get table:"))

def multiply(n):
  for i in range(n, 11):
    print(f"{n} X {i} {n*i}")

multiply(n)