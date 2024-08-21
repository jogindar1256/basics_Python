class Employee:
  language = "py"  #This is class attribute 
  salary=120000
  def __init__(self, name, salary, language):  #dunder method, which is automatically called
    self.salary = salary
    self.name = name
    self.language = language
    print("I am creatig an object")

  def getInfo(self):
    print(f"The language is {self.language} and the salary is {self.salary}")

  @staticmethod  #this allows to use the geet function with any object or class attributes
  def greet():
    print("Good Morning")

Jogindar = Employee("Jogndar", 120000, "Javascript")
print(Jogindar.name, Jogindar.salary, Jogindar.language)
# Rohan = Employee()