# List -- smilar to String access , enclosed in square brackets, Mutable
grocery = ["Harpic", "vim bar", "deodrant", "bhindi", 
"lolipop", 56]

# print (grocery)
# print(grocery[0])
# print(grocery[5])
# print(grocery[6])
# print(grocery[:])
num = [2, 7, 9, 11, 3]
# print(num)
# print(num[2])
# num.sort()    #changes the original list
# print(num)
# num.reverse() #changes the original list
# print(num)

## Slicing
# print(num[0:5])
# print(num[1:])
# print(num[1:4])
# print(num[0:10])
# print(num[::3]) # avoid taking step greate than -1, like -2 or -3
# print(num[1:5:-3]) # This is due to this
# print(len(num))
# print(max(num))
# print(min(num))
## Functions in list
# num.append(80)
# num.append(101)
# print(num)
# num.insert(1,55)
# print(num)
# num.remove(9)   # Here you can delete number by giving number itself
# print(num)
# num.pop(5)      # Here deletion is with if no index provided then default last is removed
# print(num)
## Mutable and Imutable
num[1] = 77
# print(num) # This shows list is mutable (can change)
tp = (1,2,3)
# print(tp)
# tp[1] = 100 # TypeError: 'tuple' object does not support item assignment
            # Thus shows tupple is immutable
tp = (1,)    # (1,) when declaring single tupple
print(type(tp))
tp = (1)
print(type(tp))
## Swaping of two numbers
a = 10
b = 50
# temp = a
# a = b
# b = temp
# print("a=",a,"b=",b)
a , b = b, a
print("a=",a,"b=",b)