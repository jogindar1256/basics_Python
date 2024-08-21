import random
n = random.randint(1, 100)
a = -1
guesses = 0
while(a != n):
  a = int(input("Guess the number "))
  if(a>n):
    print("Lower Number Please ")
  elif(a<n):
    print("Higher Number please ")
  guesses +=1

print(f"You have guessed th number {n} in correctly in {guesses} attempts")