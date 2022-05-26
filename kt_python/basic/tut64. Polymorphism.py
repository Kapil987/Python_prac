# Polymorphism in python defines methods in the child class that have the same name as the 
# methods in the parent class. In inheritance, the child class inherits the methods from the 
# parent class. Also, it is possible to modify a method in a child class that it has inherited 
# from the parent class.

# This is mostly used in cases where the method inherited from the parent class doesn’t 
# fit the child class. This process of re-implementing a method in the child class is known 
# as Method Overriding. Here is an example that shows polymorphism with inheritance:
# Example: was Gangadhar now Shaktiman,was Peter parker

## Example: Polymorphism in len() function in Python
# print(len("Programs")) 
# print(len(["Python", "Java", "C"])) 
# print(len({"Name": "John", "Address": "Nepal"})) 

## Example 1:
# print(5 + 6)
# print("5" + "6")



##Example 2
class Bird:         # fuction works for class Bird
     def intro(self):
       print("\nThere are different types of birds")
 
     def flight(self):
       print("Most of the birds can fly but some cannot")
 
class Parrot(Bird):     # intro() works for Parrot class as well once inherited 
     def flight(self):
       print("Parrots can fly")
 
class Penguin(Bird):    # intro() works for Penguin class as well once inherited
     def flight(self):
       print("Penguins do not fly")
 
obj_bird = Bird()
obj_parr = Parrot()
obj_peng = Penguin()
 
# obj_bird.intro()
# obj_bird.flight()

# obj_parr.intro()
# obj_parr.flight()
 
obj_peng.intro()
obj_peng.flight()

