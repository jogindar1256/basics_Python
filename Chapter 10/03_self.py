class Employee:
  language = "py"  #This is class attribute 
  salary=120000

  def getInfo(self):
    print(f"The language is {self.language} and the salary is {self.salary}")

  @staticmethod  #this allows to use the geet function with any object or class attributes
  def greet():
    print("Good Morning")

Jogindar = Employee()
Jogindar.language = "Javascript"
print(Jogindar.language, Jogindar.salary)


Jogindar.getInfo()
Employee.getInfo(Jogindar)