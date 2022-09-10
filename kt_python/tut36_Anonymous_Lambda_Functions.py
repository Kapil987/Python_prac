##
# def add(a,b):
#     return a+b

# add = lambda a,b:a+b
# print(add(5,10))

##
# def str_fun(strs):
#     return strs[-1]
# ab = lambda strs:strs[-1]
# print(ab(strs))           # str = wa 0=w 1 =a , -1=a
# strs = ['xc', 'zb', 'yd' ,'wa']
# strs = ['xc', 'zb', 'yz' ,'wy']
# simple = ['c','b','a','z']
# print(sorted(simple))
# print(str_fun(strs))

# print(sorted(strs,key=lambda strs: strs[-1]))

votes = {'Charlie': 20, 'Able': 10, 'Baker': 20, 'Dog': 15}
#If we apply .items() on the votes dictionary above we get:
#[('Charlie', 20), ('Baker', 20), ('Able', 10), ('Dog', 15)]
# 0(0        , 1), 1(0     , 1 ), 2(0     , 1 ),3(0     , 1 )
#a list of tuples, each tuple having two items indexed 0 and 1
list_1 = [votes.items()]
tup1 = (list_1)
# print("list: ",list_1)
# print("tup: ",tup1)
# print(sorted(votes.items(),key=lambda x:x[1]))
#lambda x = ('Charlie', 20) or ('Baker', 20) or ('Able', 10) or ('Dog', 15)
# x[1]  =               20  or           20  or          10  or         15
# Where there is a tie in the key, the items are ranked in the order they are originally 
# in the dictionary. (so ('Charlie', 20) is before ('Baker', 20) because there is a 20==20 
# tie on the key but ('Charlie', 20) comes before ('Baker', 20) in the original votes 
# dictionary).
