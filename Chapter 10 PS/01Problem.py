class Programer:
  Company = "Microsoft"
  def __init__(self, name, salary, pin):  
    self.name = name
    self.salary = salary
    self.pin = pin


p = Programer("Jogindar", 1200000, 272701)
print(p.name, p.salary, p.pin, p.Company)

r = Programer("Jogindar", 1200000, 272701)
print(r.name, r.salary, r.pin, r.Company)
