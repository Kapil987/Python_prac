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
# print(mystr[-1:-3]) #14-1 = 13 , 14-3 = 11 # converts to [-1:-3:1] last :1 for forward direction 
# print(mystr[13:11]) # -1(13)--start to -3(11)--end its backward direction but last ":"  
# print(mystr[-1:])   # is takes as ":1" ie forward so conflict and no ouput
                      # for output give ":-1" ie. backward direction,

##Conclusion: start and end parameter should match the direction ie stride

# Extented Slicing
# # 3rd parameter stride, which refers to how many characters to move forward
# print(mystr[0::1]) # str[start:end-1:jump]
# print(mystr[0::2]) 
# print(mystr[0:7:3]) # wre
# print(mystr[0::5555])

#-14                             -3 -2 -1
#  W e     r i s e      a s      o  n  e
#  0 1  2  3 4 5 6  7   8 9  10  11 12 13

## Negative indexing
mystr = "We rise as one"
# print(mystr[-1:0])      #[start:end] not possible to start with -1 and end with 0
# print(mystr[-3:-1]) # [including: excluding(total)]
# print(mystr[11:13])
# print(mystr[-14])
# print(mystr[::])
# print(mystr[::-1])
# print(mystr[::-2])

# String functions
str1 = "hello second"
str2 = "hello one"
str3 = "123"

# print(type(str2))

# print(str2.isalnum()) # as we have spaces in  , either alphabet or numbers
# print(str2.endswith("one"))
# print(str2.count("e"))
# print(str2.capitalize()) # first letter would be capital
# print(str2.find("n")) # count start from zero
# print(str2.replace("second","one"))
# str2[0] = 'g'

## f string in python
# val = 'Good'
# age = 24
# print(f"Rohan is a {val} boy and his age is {age}")

# p   y   t   h   o   n
# 0   1   2   3   4   5
#-6  -5  -4  -3  -2   -1

list1 = "python"
# print(list1[-2:-5:-1])
# print(list1[4:1:-1])
# print(list1[-2:1:-1]) # [-2:-5:-1] = [4:1:-1] = move from 4 to 1 in reverse = [oht]
# print(list1[-2:1:1])  # Move from 4 to 1 in with positive step1 ie. forward direction not possible
                      # The step is telling us the direction in case of 1 its forward 
                      # in case of -1 its backward
                      # start at index -2, end at index 1 
                      # with step 1 is impossible, if you have 
                      # positive step start has to be lower than end
                      # 

