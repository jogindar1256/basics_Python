from random import randint

class Train:


  def __init__(self, trainNo):
    self.trainNo = trainNo

  def book(self, fro, to):
    print(f"Ticket is booked in train no: {self.trainNo} From {fro} to {to}")

  def getUpdate(self):
    print(f"The Train No:{self.trainNo} is Running on time")

  def getFare(self, fro, to):
    print(f"Ticket Frain of Train no: {self.trainNo} From {fro} To {to} is {randint(222, 5555)}")

t = Train(12399)
t.book("Rampur", "Delhi")
t.getUpdate()
t.getFare("Rampur", "Delhi")