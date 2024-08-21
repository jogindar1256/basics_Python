try:
  a = int(input("hey, Enter a number: "))
  print(a)

except ValueError as v:
  print(v)

except Exception as e:
  print(e)


print("Thanks")
