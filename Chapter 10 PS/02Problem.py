class Calculator:

  def __init__(self, n):
    print("Finding the cube, square, squareroot")
    self.n = n

  def squareRoot(self):
    print(f"The SquareRoot is {self.n**1/2}")

  def square(self):
    print(f"The Square is {self.n*self.n}")
    
  def cube(self):
    print(f"The SquareRoot is {self.n*self.n*self.n}")

a = Calculator(4)
a.square()
a.squareRoot()
a.cube()