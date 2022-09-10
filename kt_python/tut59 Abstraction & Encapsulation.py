## Abstraction means wrapper, a layer,  example print func, mouse, windows etc
# example when designing a game, programmer 1 design a play , prog 2 design city or car
## Encapsulation : To achieve Abstration we need or we do encapsulation meaning hiding details,
# capsule inside medicine works, how it works you are not bothered about it.
# hiding implementation details

## Example Syntax
# from abc import ABC
# Class ClassName(ABC):

from abc import ABC, abstractmethod
class Payment(ABC):
    def print_slip(self, amount):
        print('Purchase of amount- ', amount)
    @abstractmethod
    def payment(self, amount):
        pass

class CreditCardPayment(Payment): #add remove Payment to notice isinstance funtion
    def payment(self, amount):
        print('Credit card payment of- ', amount)

class MobileWalletPayment(Payment):
    def payment(self, amount):
        print('Mobile wallet payment of- ', amount)

class UPI(Payment): 
    def abc():
        print("abc")

obj = UPI()

obj = CreditCardPayment()
obj.payment(100)
obj.print_slip(100)
print(isinstance(obj, Payment)) 
print(isinstance(obj, CreditCardPayment)) 

 
# obj = MobileWalletPayment()
# obj.payment(200)
# obj.print_slip(200)
# print(isinstance(obj, Payment))

## Conclusion: abstractmethod and inherit main class from ABC together provide
# control to design rules for child classes

