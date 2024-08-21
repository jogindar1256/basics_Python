class Animal:
  def __init__(self):
    pass

class Pet(Animal):
  def __init__(self):
    super().__init__()

class Dog(Pet):
  def show(self):
    print("Bow Bow!")
    

e = Dog()
Dog().show
