# Abstract Base class: Set of rules which i need to pre-define, example create print_area in
# all inherited classes.
# abc is in-built module, if we inherit from ABC then, we get the power, to define set of rules
# that needs to be followed by child class mandatoryly. 

# from abc import ABCMeta, abstractmethod # syntax before python 3.4
from abc import ABC, abstractmethod        # after python 3.4

class Shape(ABC):
    @abstractmethod
    def print_area(self): 
        return 0

    # @abstractmethod
    # def one_more(self):
    #     return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def print_area(self):
        return self.length * self.breadth

a = Rectangle()

# print(a.print_area())
# b = Shape()     # Error as we cannot create objects from abstractclass

import inspect
print(a.__dict__,"\n")
print(dir(a),"\n")
print(inspect.getmembers(a))