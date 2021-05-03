## Python pdb debugger
def add (x, y):
    sum = x + y
    return sum

if __name__ == "__main__":
    # x = (input("num1: "))
    # y = (input("num2: "))
    x = int(input("num1: "))
    y = int(input("num2: "))
    import pdb;pdb.set_trace()
    z = add(x, y)
    print(z)

# add()
this program will work fine