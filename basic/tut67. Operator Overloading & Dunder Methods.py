##Dunder Method = __functionName__ , function start with "__" and end with "__" are called as
# Dunder Method , example __init__ ie. constructor

## Example1: Operator Over loading: Python program to show use of 
# + operator for different purposes. 

# print(1 + 2) 
# # concatenate two strings 
# print("Hello"+"World")  
# # Product two numbers 
# print(3 * 4) 
# # Repeat the String 
# print("Sun"*4) 

# Conclusion
# notice that the same built-in operator or function shows different behavior for 
# objects of different classes(int,string),example: operator "+"" is used to add two 
# integers as well as join two strings this is called Operator Overloading.

#Example2: Python Program illustrate how to overload an binary + operator 
# class A: 
#     def __init__(self, a): 
#         self.a = a 
  
#     # adding two objects  
#     def __add__(self, o): 
#         print("__add__ is called")
#         return self.a + o.a  
# ob1 = A(1) 
# ob2 = A(2) 
# ob3 = A("Good") 
# ob4 = A("Morning") 
  
# print(ob1 + ob2) 
# print(ob3 + ob4) 

# Example3: Operator Over Loading in classes
class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):  # This is constructor, called by default
        self.name = aname       # name is instance variable and aname is just an argument
        self.salary = asalary
        self.role = arole
        print("constructor/init function is called for: ",aname)
        

    def __add__(self,other):        #Dunder Method , called as Dunder add
        print("\nDunder add is called")
        return self.salary + other.salary
    
    def __truediv__(abc,other):
        print("Truediv / is called")
        return abc.salary / other.salary

ram = Employee("vijay",100,"Tutor")
karan = Employee("Karan",200,"Engineer")

# print(ram+karan) 
# print(ram/karan)
# When you add this without "Dunder add" method it will not allow
                 # When you add after making __add__ it will give addtion of salary
                 # its called in backgroud as __init__ is called

# Reference: https://docs.python.org/3/library/operator.html#mapping-operators-to-functions

# print(ram)