from abc import ABC, abstractmethod

#Abstract Class
class Bank(ABC):
   def bank_info(self):
       print("Welcome to bank")
   
   @abstractmethod
   def interest(self):
       "Abstarct Method"
       pass
   
   def offers(self):
       print("Providing offers")  


#Sub class/ child class of abstract class
class SBI(Bank):
   def interest(self):
       print("In SBI bank 5 rupees interest")


class HDFC(Bank):
   def interest(self):
       print("In HDFC 7 rupees interest")
  

s= SBI()
h=HDFC()
s.bank_info()
s.interest()
h.bank_info()
h.interest()