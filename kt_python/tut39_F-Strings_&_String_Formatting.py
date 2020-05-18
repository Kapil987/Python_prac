## Tradational approach, Not readable
# strs = "Kapil"
# a = "My name is: %s"%strs
# print(a)

##
# strs = "Kapil"
# b = 1
# a = "My name is: %s %d"%(strs,b)
# print(a)

## Formating the string new approach
strs = "Rohan"
id_num = 144
# # a = "This is: {} with id: {}"
# a = "This is: {1} with id: {0}" # This has a flexibility 
# print(a.format(strs,id_num))

## F-String or Fast string
import math
# a = f"This is: {strs} with roll number: {id_num} and balance: {5*25}"
# print(a)
# a = f"This is: {strs} with roll number: {id_num} have written: {math.cos(45)}"
# print(a)
print(f"This is: {strs} with roll number: {id_num} have written: {math.cos(45)}")