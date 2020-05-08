# List -- Similar to string access represented by [] square brackets, Mutable
# () -- parenthesis , {} -- curly braces

grocery = ["Harpic", "vim bar", "deo", 
            "loki", "lollipop", 45]
# print(grocery)
# print(type(grocery))
# print(grocery.index("vim bar"))

## List access
# print(len(grocery))
# print(grocery[0])
# print(grocery[5])
# print(grocery[6])
# print(grocery[:])

## List Functions , index function
# num = [2, 7, 5, 11, 3]
# print(num)
# # print(num[2])
# num.sort()
# print(num)
# num.reverse()
# print(num)
# print(len(num))
# print(max(num))
# print(min(num))
# num.append(100)
# num.insert(1,55)
# num.remove(11)
# num.pop(2)      # default last index val remove, if provided index , index val is removed
# print(num)


## List Slicing
# num = [2, 7, 5, 11, 3]
# print(num[0:5]) # strt : end -1
# print(num[1:])
# print(num[1:4])
# print(num[0:10])

## Extended Slicing
# print(num[::1])
# print(num[::3])
# print(num[::-1])
# print(num[1:5:-1])

num = [2, 7, 5, 11, 3]
## Mutalble (can change ) and Immutalbe (cannot change)
# num[1] = 10
# print(num) 

## Tupel
tp = (1, 2, 3)
# tup = (1,)    # (1,) when declaring single tupple
# print(tp)
# tp[2] = 22    #TypeError: 'tuple' object does not support item assignment
                ## Thus shows tupple is immutable
# print(tp)
# print(type(tp))
# print(type(tup))

## Swapping of two numbers
a = 10
b = 20
print(a, b)
# temp = a
# a = b
# b = temp
a , b = b , a
print(a, b)
