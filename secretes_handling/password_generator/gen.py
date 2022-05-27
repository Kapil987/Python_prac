data = input('Enter you pass string: ') # Taking visible input
data.jo
tuple_replacer = (
                ('a','@'),('AND','&'),
                ('i','1'),('o','0'),
                ('I','|'),('s','$'),
                ('c','('),('b',')')
                )

for i,j in tuple_replacer:
    data = data.replace(i,j)
print(data)

## Notes
# print(data.replace(data[0], tuple_replacer[0][1]))
# print(tuple_replacer[0][1])
# for i in tuple_replacer:
#     print(i)

"""
from getpass import getpass
# data = getpass('Enter you pass string: ') # if you need to hide input
"""
