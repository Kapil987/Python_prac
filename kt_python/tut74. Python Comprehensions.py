##EX-1 Number div by 3
# ls = []
# for i in range(100):
#     if i%3 == 0:
#         ls.append(i)
# print(ls)

##EX-2 Other way of writing
# ls = [ a for a in range(100) if a%3 ==0]
# print(ls)

##EX -3
# dict1 = { i:f"item{i}" for i in range(100) }
# # print(dict1)

# dict2 = {value:key for key,value in dict1.items()}
# print(dict1,"\n \n",dict2)

## EX -4 set comprehension
# set_comp = {abc for abc in ["abc1","abc2","abc2","abc1",
#                             "abc1","abc2","abc2","abc1"]}
# print(set_comp)
# print(type(set_comp),"\n")

## EX -5 list comprehension
# list_comp = [abc for abc in ["abc1","abc2","abc2","abc1",
#                             "abc1","abc2","abc2","abc1"]]
# print(list_comp)
# print(type(list_comp))

## EX -6 Generator comprehension
gen_comp = (i for i in range(100) if i%10 == 0)
print(gen_comp.__next__())
print(gen_comp.__next__())
