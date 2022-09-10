# Mutable: Numbers (int, float, Booleans,etc), Strings, Tuples, Frozen sets, User-Defined Classes
# Immutable: List, sets, Dictionaries, User-defined Classes
# Mutable(Can Change) are easy to change
# Immutable(Cannot Change) are expensive to change because it involves creation of copy

# my_list = [1, 2, 3]   # Mem loc: 500
# print(id(my_list))

# my_list.append(100)
# print(id(my_list))     # Mem loc: 500
# As Memory location of 'my_list' is UN-CHANGED before and after the value of 'my_list' is changed, 
# Hence its Mutable.


# a = "Hello"       # Mem loc: 600
# print(id(a))
# a = "Hello World" # Mem loc: 700
# a[0] = 'y'
# print(id(a))

# As Memory location of 'a' is Changed before and after the value of 'a' is changed, Hence its Immutable.

# Case 1: Mem loc: 100
tup = (1, 2, 3) # Tuples are immutable, elements cannot be modified , 
#tup[0] = 10
# print(id(tup))
# print(tup[0])
# tup[0].append(10) # as elements are immutable, here tup is bhehaving as a tuple

# Case 2: Mem loc: 200, Contentents are not changed refrence is changed
a = [1, 2]  # its a list which is mutable
b = [3, 4]  # # its a list
# a[0] = 6
# print(a)
tup = (a, b)
tup[0].append(10)   # here tup is bhehaving as a list, as elements are mutable[List]
# tup[0] = 6
# print("Before",tup)
# print(id(tup))

# a.append(5)
# b.append(6)
# print("After",tup)  # Mem loc: 200, Here tuple is immutable but its elements are not. Object reference in the 
#                     # tuple did not change but the reference objects did mutate
# print(id(tup))

