# We directly use employee class in any other class this is called inheritance 
class Employee:
  company = "ITC"
  name = "Jogindar"
  def show(self):
    print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
  language = "Python"
  def printLanguages(self):
    print(f"Out of all languages {self.language} is your language")

class Programmer(Employee, Coder):
  company = "ITC Infotech"
  def showLanguage(self):
    print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()

print(a.company, b.company)
