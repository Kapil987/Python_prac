## Need for super:
# as class A constructor is over-rided by class B constructor, class A constructor wont
# exist for object b but what if i want to still run class A constructor,ex: to access special
# variable
class A:
    classvarA = "class variable A"
    def __init__(self):
        self.var1 = "I am inside class A's Constructor"
        self.classvarA = "Instance var in class A"  #This is instance variable whoever calls it
        print("\nClass A constructor called!!")
        self.special = "Special"

class B(A):
    classvarA = "class variable: classvarA of class B"
    def __init__(self):     # Over-riding  constructor of class A
        # super().__init__()
        self.var1 = "I am inside class B's Constructor"
        self.classvarA = "\ninstance variable of class B"
        print("\nClass B constructor called")
# a = A()
# b = B()
# print(b.classvarA)
# print(b.special) 

## Flow of program: When super is used in next line in init of class B
# 1. super in class B is called, control goes to class A constructor
# 2. var1 and classvarA values are set as per class A constructor
# 3. control comes to self.var1 of class B and value of var1 and classvarA are over-ridden
# 4. when b.classvarA is accessed now we get values mentioned in class B constructor

# Conclusion:
# when super() is used for b = B() both constructor were called and b was able to access
# special variable else it would not.

## When changing position of super see difference
class A:
    classvarA = "class variable A"
    def __init__(self):
        self.var1 = "I am inside class A's Constructor"
        self.classvarA = "\nInstance var in class A"  #This is instance variable whoever calls it
        print("\nClass A constructor called!!")
        self.special = "\nSpecial\n"

class B(A):
    classvarA = "class variable: classvarA of class B"
    def __init__(self):     # Over-riding constructor of class A
        self.var1 = "\nI am inside class B's var1"
        self.classvarA = "\ninstance variable of class B"
        print("Class B constructor called")
        super().__init__()
        

a = A()
b = B()
print(b.special,b.var1,b.classvarA)

## Flow of program: When super is used in last line in init of class B
# 1. class B constructor is called, var1 and classvarA values are set as per class B constructor
# 2. then control goes to class A constructor 
# 3. var1 and classvarA values are set as per class A constructor 
#    (access granted to special variable)
