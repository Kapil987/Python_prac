#Dictionay : is a combination of key and value pairs, represented by {}, its case sensitive,
# list, tupple , dict, keys immutable

# Empty Dictionary
# d1 = {}
# print(type(d1))

# Simple Dictionary
# d2 = {"Kapil":"Burger","rohan":"Fish",
#         "Shyam":"roti"}
# print(d2)
# print(d2["Kapil"])

# Nested Dictionary
d3 = {"Kapil":"Burger","rohan":"Fish",
        "Shyam":"roti", "mohan":{"B":"maggie","L":"roti","D":"Chicken"}}
# print(d3)
# print(d3["mohan"]["B"])
d3["Ankit"] = "Idly"

d3[420] = "Kebabs"
# print(d3)

# Dictionary Functions
del d3 [420]
# print(d3)
d4 = d3 # d3--> 100 , d4 -->100
# print(d3)
# del d3 ["mohan"]
# print(d3)
# print(d4)
d4 = d3.copy()  # d3--> 100(Kapil) , d4 --> 200 (kapil)
del d3["Ankit"]
# print(d3)
# print(d4)
d3.update({"ramu":"Chocolate"})
# print(d3)
# print(d3.get("ramu"))
print(d3.keys())
print(d3.items())
print(d3.values())

# Exercise 
# Create a dictionary and take input from user and return the meaning of work from dictionary

