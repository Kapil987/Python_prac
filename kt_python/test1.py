# Health Manager / Tracker
import datetime,time

def getdate():
    return datetime.datetime.now()

# print(getdate())
# total 4 files , function to take client name: karan , rohan
# Input diet in 1 file with time and print when asked to print

def input_diet():
    diet = input()
    with open("k_data.txt",'a') as f:
        f.write(str(getdate()))
        # f.write(str(localtime))
        f.write(" ")
        f.write(diet)
        f.write("\n")
        # f.write("hello")
        # f.seek(0)

def read_diet():
    column()
    with open("k_data.txt",'r') as f:
        # print(f.tell())
        # f.seek(0)
        while(True):
            line = f.readline()
            print(line)
            if not line:
                break
            
def column():
    print("DATE \t   TIME \t   ITEM")

inp = input("Enter Client Name: ") # karan
choice = int(input("Press 1 to enter Diet, 2 to get the Diet info: "))
if choice == 1:
    input_diet() 
    
elif choice == 2:
    read_diet()

# print(datetime)  