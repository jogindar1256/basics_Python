import random
def game():
  print("You are playing the random num game")
  score = random.randint(1, 62)
  #Fetch the hiscore
  with open("hiscore.txt") as f:
    hiscore = f.read()
    if(hiscore!=""):
      hiscore = int(hiscore)
    else:
      hiscore = 0

  print(f"You score: {score}")
  if(score>hiscore):
    #write this hiscore to the file
    with open("hiscore.txt", "w") as f:
      f.write(str(score))

  return score



game()