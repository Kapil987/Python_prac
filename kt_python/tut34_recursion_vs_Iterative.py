## n! = n * n-1 * n-2 * n-3 .... 1
## n! = n * (n-1)!
def fact_iterate(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

num = int(input("Enter a num: "))
print(fact_iterate(num))