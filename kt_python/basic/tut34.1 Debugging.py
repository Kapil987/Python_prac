## How to debug using pdb
import pdb
def fibo(n):
    print("\n")
    if n == 0:
        print(0)
    if n == 1:
        print(0,1)
    else:
        n1 = 0
        n2 = 1
        n3 = 0 
        print(0,1)
        pdb.set_trace() # sets the break point in next line
        for i in range(n-1):
            n3 = n1 + n2;    
            print(n3)    
            n1 = n2;    

            n2 = n3;           
var = int(input("Input the number\n"))
fibo(var)