#6.	String Slicing And Other Functions In Python  # 
# Search in string, its a datatype
#-14                             -3 -2 -1
#  W e     r i s e      a s      o  n  e
#  0 1  2  3 4 5 6  7   8 9  10  11 12 13 
mystr = "We rise as one" # indexation starts from zero
# print (mystr)
# print(len(mystr)) # 14 as from 0 to 13
# print (mystr[14]) # Error because index is from 0 to 13
# print (mystr[13]) #index numbers in square brackets

# String Slicing
# print(mystr[0:14]) # [including: excluding(total)] [start : end-1 ]we saw 14th index is error so ?
# print(mystr[3:7])
# print(mystr[0:])
# print(mystr[:])
# print(mystr[:6])
# print(mystr[:78])
# print(mystr[78]) # let see how it works
# print(mystr[:14]) # will be [0:14])
# print(mystr[10:14]) # then ?

#confusing case # Solution :convert to positive
# print(mystr[-1:-3])
# print(mystr[13:11])
# print(mystr[-1:])


# Extented Slicing
# # 3rd parameter stride, which refers to how many characters to move forward
# print(mystr[0::1]) # str[start:end-1:jump]
# print(mystr[0::2]) 
# print(mystr[0:7:3]) # wre
# print(mystr[0::5555])

#-14                             -3 -2 -1
#  W e     r i s e      a s      o  n  e
#  0 1  2  3 4 5 6  7   8 9  10  11 12 13

# mystr = "We rise as one"
# Negative indexing
print(mystr[-1:0])
# print(mystr[-3:-1]) # [including: excluding(total)]
# print(mystr[11:13])
# print(mystr[-14])
# print(mystr[::])
# print(mystr[::-1])
# print(mystr[::-2])

# String functions
str2 = "hello second" # before
str2 = "hello one"      # after

# print(type(str2))

# print(str2.isalnum()) # as we have spaces in  , either alphabet or numbers
# print(str2.endswith("one"))
# print(str2.count("e"))
# print(str2.capitalize()) # first letter would be capital
# print(str2.find("n"))
# print(str2.replace("second","one"))
# str2[0] = 'g'


##
# Something is mutable only when we are able to change the values held in the memory location without changing the memory location itself.
# The trick is: If you find that the memory location before and after the change are the same, it is mutable.
# For example, list is mutable. How?

a = ['hello']
print(a)
print(hex(id(a)))
# 139767295067632

# # Now let's modify
# #1
a[0] = "hye new"
print(a)
print(hex(id(a)))       # mutable

# ['hello new']
# Now that we have changed "a", let's see the location of a
# >> id(a)
# 139767295067632
# so it is the same as before. So we mutated a. So list is mutable.
# A string is immutable. How do we prove it?

b = "hello"
# print(b[0])
print("b=",hex(id(b)))       # immutable
# 'h'
#Now let's modify it
# print(hex(id(b)))       # immutable
b[0] = 'n'
print(b)
