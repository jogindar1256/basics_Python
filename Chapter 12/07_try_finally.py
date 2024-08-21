def main():
  try:
    a = int(input("hey, Enter a number: "))
    print(a)

  except Exception as e:
    print(e)

  finally:
    print("I am inside the finally")  # finally will execute even after we return the function

print("Thanks")
