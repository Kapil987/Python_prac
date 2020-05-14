# One liner comes with a trade-off readability

a = int (input("enter a \n"))
b = int (input("enter b \n"))

# if a > b: print("a is greater")
print("a is Greater") if a > b else print("b is Greater")

var = a if a>b else b
print(var)
