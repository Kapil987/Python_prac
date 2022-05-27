# Abstraction : wrapping a layer, example print function, mouse, windows etc, when designing 
# a game, programmer 1 design a play, prog 2 design city or car
## Encapsulation: to achieve abstraction we need or we do encapsulatoin meaning hiding details,
# capsule inside medicine works, how it works you are not bothered about it
# hiding implementation details
# example https://blog.teclado.com/python-abc-abstract-base-classes/

# abc is a builtin module, we have to import ABC and abstractmethod
from abc import ABC, abstractmethod
class Payment(ABC): # Inherit from ABC(Abstract base class)
    def print_slip(self,amount):
        print('Purchase of amount: ', amount)
    
    @abstractmethod # Decorator to define an abstract method
    def payment(self, amount):
        pass

class CreditCardPayment(Payment): # Inherit from Payment class
    def payment(self, amount):
        print('Credit card payment of- ',amount)

class MobileWallerPayment(Payment):
    def payment(self, amount):
        print('Mobile wallet payment of -',amount)

class UPI(Payment): # If you inherit from the Payment class 
    def abc():      # # but don't implement the abstract methods, you'll get an error:
        print('abc')

# obj = UPI()
# obj = CreditCardPayment()

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

