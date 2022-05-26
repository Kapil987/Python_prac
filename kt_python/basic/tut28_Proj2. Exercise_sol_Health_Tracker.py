# Health Manager / Tracker
# print(getdate())
# total 4 files , function to take client name: karan , rohan
# Input diet in 1 file with time and print when asked to print
# lines = file.readlines()
# lines = lines[:-1]
# f.write(str(localtime))
# print(f.tell())
# f.seek(0)
# print(f.writelines(rm_line))

import datetime,time

# def getdate():
#     return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

## Lambda one-liner
getdate = lambda : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(getdate())
## Function for writing diet into user file
def input_diet(inp):
    diet = input("Please enter your diet: ")          # user enters his diet here
    try:
        with open(inp + "_data.txt",'a') as f:          # Creates a file if not present
            f.write(str(getdate()))                     # karan_data.txt or arjun_data.txt
            f.write(" ")
            f.write(diet)
            f.write("\n")
    except:
        print("Error!:: Unable to perform operation on file in function: ",input_diet.__name__,\
" at this moment")
        print("You may use other options")
        
## Function for reading input from user file
def read_diet(inp):                    # 'w' write mode if no files will create a file
    try:
        with open(inp + "_data.txt",'r') as f:
            test = f.read()     # to test file operation(cursor move forward), 
            # print("in read",test)   # if error no further execution
            column()
            f.seek(0)
            while(True):                          # and program exits abruptly
                # print("in loop tell",f.tell())
                line = f.readline()
                print(line,end="")
                if not line:
                    break
    except Exception as e:
        print("Error!:: Unable to perform this operation on file in function: ",read_diet.__name__,\
" at this moment")
        print("You may use other options")
        print("Actual Error:: ",e)
    # else:
    #     pass
        # For future use
        

## Function for Heading attributes
def column():
    print("\nDATE \t   TIME     ITEM")

## Main Function to take user input
def user_input():
    """
    This function takes 1 user Karan or Arjun as input and Tracks their Diet Plan 
    """
    while(True):
        inp = input("\n\nABC Diet Tracking System:\n\nEnter Client Name Karan or Arjun or 3 to Exit: ")
        inp = inp[0].lower() + inp[1:] 
        if inp == "karan": # if inp.lower() == "karan" #
            user_choice(inp)
        elif inp == "arjun":
            user_choice(inp)
        elif inp == "3":
            print("Program exited")
            break
        else:
            print("invalid input")
        

def user_choice(inp):
    choice = int(input("Please Choose from below choices:\n1.)Press 1: To Enter Diet:: \n\
2.)Press 2: To Get Diet Info:: \n3.)Press 3: To Delete Diet Info:: \n"))
    if choice == 1:
        input_diet(inp)     
    elif choice == 2:
        read_diet(inp)
    elif choice == 3:
        delete_data(inp)
    else:
        print("Your choice is invalid")

def delete_data(inp):
    try:
        check_file = open(inp + "_data.txt")    # remove _ to test the error
        check_file.close()                      # we can use os.path modules also
    except Exception as e:
        print("Unable to perform this operation Actual Error!:: ",e)
    else:
        with open(inp + "_data.txt",'r+') as f:
            rm_line = f.readlines()
            # print(f.readlines())
            # print(rm_line)
            if rm_line:
                print("Diet info before deletion: ")
                read_diet(inp)
                print("\nThe last line removed from",inp + "'s"," diet is::",rm_line.pop(-1))
                f.seek(0)
                f.truncate()
                print("\nDiet info left for:",inp,"is::")
                for l in rm_line:
                    f.write(l)
                f.seek(0)
                read_diet(inp)
            else:
                print(f"The Diet info for {inp} is Empty!")     #using F-String
        
## Calling Required functions
print(user_input.__doc__)
print(dir(user_input))
user_input()
# print(datetime)
# print(getdate())  