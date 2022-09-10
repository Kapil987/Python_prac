"""
Iterable -  __iter__() or __getitem__()
Iterator -  __next__()
Iteration -
"""
# Example1 Where a object is iterabele (has __iter__ , __getitem__) or not
import inspect
abc = [1,2,3,4,5]
# print(inspect.getmembers(abc))
# print(dir(abc))

## Example 2: Here values are not pre-stored they are generated on fly.

# for i in range (10):
#     print("On the fly =",i)

## Making your own Generator Function
# def gen(n):
#     for i in range(n):
#         yield i
# g = gen(3)  # try with '3' and a large number
# print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())     #StopIteration Error

# why we do not get stop iteration Error in for loop ?
# Conclusion: StopIteration Error is auto handled by for loop

##
k = "Sun"       # 12345 int will give error as 'int' are not iterable and also 
                # doesn't have __iter__ defined 
# print(k[0])
# print(iter(k))
ier = iter(k)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

# for i in k:
#     print (i)

## Question
# def gen(n):
#     for i in range(n):
#         return i
# g = gen(100)
# print(g)

## Exercise for fibonaci and factorial

# shit+Alt+down and shift+Alt+Up for copying the line
# Alt + Up/Down for line movement




















