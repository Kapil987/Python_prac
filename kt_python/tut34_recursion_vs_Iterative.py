## n! = n * n-1 * n-2 * n-3 .... 1
## n! = n * (n-1)!
## 1. Iterative approach
def fact_iterate(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

num = int(input("Enter a num: "))
print(fact_iterate(num))

## 2. Recursive approach
# def fact_rec(n):
#     if n == 1 or n == 0:
#         return 1
#     # res = n * fact_rec(n-1)
#     return (n * fact_rec(n-1))

# 3 * fact_rec(3-1) # 3 * 2 = 6
# 2 * fact_rec(2-1) # 2 * 1 = 2
# return 1
# inp = int(input("Enter num for rec approach:"))
# print(fact_rec(inp))

## 3. finbonacci series iterative approach
# def fibo(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         st = 0
#         pre = 1
#         for i in range(n-1): # 1     #1
#             res = st + pre  # res=1     res=2
#             st = pre        # st=1      
#             pre = res       # pre=1
#         return res

#     #     return ((n-2) + (n-1))
# inp = int(input("Enter num for fibonacci index value:"))
# print(fibo(inp))

## 4. finbonacci series recursive approach
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fibo(n-1) + fibo(n-2))

    #     return ((n-2) + (n-1))
inp = int(input("Enter num for fibonacci index value:"))
print(fibo(inp))