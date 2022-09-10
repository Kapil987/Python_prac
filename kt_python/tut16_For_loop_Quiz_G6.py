#For Loop
for x in range(6): # list in [0,1,2,3,4,5,6]
    print(x)


# list1 = ["Biscuit", "Namkeen", "Bread"]
# for item in list1:
#     print(item)

# tup1 = ("Biscuit", "Namkeen", "Bread") # With tupple
# for item in tup1:
#     print(item)


list3 = [ ["Biscuit",1], ["Namkeen",5], ["Bread",3] ] # list of list
# for item in list3:
#     print(item)
# print(list3[0])
# for item,count in list3:
#     print("item =",item,",count =",count)

# Working with dict in loops 
# [ ["Biscuit",1], ["Namkeen",5], ["Bread",3] ]
#   0              1              2
dict1 = dict(list3)         #Type casting list to dictionary
# print(dict1)
# print(dict1[1])            # it cannot work as print(list3[0]) as it tries to look for keyword 0 in the dict, 
                            # where list tries to resolve its subscript [0]
# for item in dict1:
#     print(item) 

# Problem: Will the following work?  Ans: nop because ['Biscuit', 1] is at 0th location ["Namkeen",5] is at 1st location 
                                    # so its dificuilt to traverse between 0th and 1st location to get value "1" for biscuit
# for item,count in dict1:
#     print("item =",item,"count =",count)

# Solution
# for item,count in dict1.items():
#     print(item,count)

## Quiz : Print only numbers which are greater than 6 from a list
# list4 = [1,'golu', int, float, 10]

## Quiz : Taking input list of list and add individual list, print only the max value from addition of list

"""
list1=[ [4,6] , [2,4], [1,2] ]

## Separating individual list from list of list
def sep_item(val):
  for item in val:
    add_list(item) # calling add_list
    # print(item)

## Taking global variables
count = 0
list_sum = []

## Adding individual lists
def add_list(num_list):
  a = 0
  global count
  global list_sum
  for i in num_list:
    a = i + a
  count = count + 1
  list_sum.append(a)
  print(f'sum{count}: ',a)

sep_item(list1)

## Sorting list so the max value comes at the end or you can use max function
list_sum.sort()
print(list_sum[-1])
# print(max(list_sum))

"""

    