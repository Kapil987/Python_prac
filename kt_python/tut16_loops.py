# list1 = ['potato','tomato','chillies']
# # print(list1[0],list1[1],list1[2])

# for item in list1:  # : means entering inside the for loop
#     print(item)

# list2 = [['potato',1],['tomato',2],['chillies',3]] # list of list

# for item, count in list2:
#     print("item =",item,":: count =",count)

## using dictionaries
## The items() method returns a view object. The view object contains the key-value pairs of the dictionary, 
# as tuples in a list. The view object will reflect any changes done to the dictionary,
# list3 = [['potato',1],['tomato',2],['chillies',3]] # list of list
# dict2 = dict(list3) #typecasting list to dict
# for item, count in dict2.items(): # using only dict2 will give only keys in dict2
#     print("item =",item,":: count =",count)

## Quiz : Print only numbers which are greater than 6 from a list
list4 = [1,'golu', int, float, 10]

for i in list4:
    # print("i=",i)
    if (str(i).isnumeric() and i>6) :
        print(i)

## While loop
i=0
while (i<5):
    print(i)
    i=i+1;
    