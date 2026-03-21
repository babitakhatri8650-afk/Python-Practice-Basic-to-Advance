from  random import randint

class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
    def book(self,fro,to):
        print(f"The train is{self.trainNo} goes {fro} to {to}")
    def getstatus(self):
        print("The train {self.trainNo} is running on time")
    def getfare(self,fro,to):
        print(f"The train is{self.trainNo} goes {fro} to {to} at platform{randint(222,5555)}")
t=Train(34792)
t.book("delhi","pune")
t.getstatus()
t.getfare("delhi","pune")