# Dictionary -- represented by {}, Key - Value pair , try to keep keys as immutalble
d1 = {}
# print(type(d1))
d4 = {'Kapil':"Fruits", "vinod":"Roti", "james":"Biryani",
        "rohan":{"B":"maggie","L":"rice","D":"Chicken"}}
# print(d4["Rohan"]["B"])
# print(d4["rohan"]["B"])
# d4[420] = "Junk Food"
# print(d4)
# d4["Salman"] = "Kebabs"
# print(d4)
# del d4["rohan"]
# print(d4)
# d3 = d4               # d3 and d4 are pointing to same location
# print(d4.copy)
# del d3['Kapil']
print(d4) # it deletes from both so better use .copy
d3 = d4.copy()
del d4['vinod']
print(d3)
print(d4)
d4.update({'heema':'chocolate'})
print(d4)
print(d4.keys())
print(d4.values())
print(d4.items())