## Example1 of Multilevel Inheritance
# class Dad:
#     pass

# class Son(Dad): # Son is derived from Dad
#     pass

# class Grandson(Son): # Grandson is derived from Son
#     pass

## Example 2
class Dad:
    basketball = 6

class Son(Dad): # Son is derived from Dad
    dance = 1
    # basketball = 10   # comment each basketball and see difference
    def isdance(self):
        return f"Yes i dance {self.dance} no of times"

class Grandson(Son): # Grandson is derived from Son
    dance = 6
    # basketball = 15
#     def isdance(self):            #Comment this isdance and see it take Son isdance
#         return f"\nYes i love to dance\
# {self.dance} no of times" 

papa = Dad()
beta = Son() 
bacha = Grandson()

# print(bacha.isdance())  #first search is in Grandson then in Son then in Dad, 
print(bacha.basketball) # where ever found it will stop and display result


## Exercise make 3 meaningfull class Electronic, Gadjet, Mobile fro Multilevel inheritance






# Example 3 :  
# class Electronic_device:
#     resistor = 10
#     def has_battery(self):
#         print("Electronic device has a battery")

# class Pocket_gadjet(Electronic_device):
#     resistor = 5
#     def has_battery(self):
#         print("Pocket Gadjet has a battery")

# class Mobile(Pocket_gadjet):
#     resistor = 1
#     def has_battery(self):
#         print("Mobile has a battery")

# yantra = Electronic_device()
# chotu = Pocket_gadjet()
# phone = Mobile()

# print(phone.resistor)
# phone.has_battery()     # Comment each has_battery and see a difference


