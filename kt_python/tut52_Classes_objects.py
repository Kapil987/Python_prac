# Class - Template -- Make one time use multiple time. Example Marriage Card Template
# Object - is Card, instance of the class
# Attribute - dot Attributename
# DRY -- Do not repeat youreself

class Student:
    pass

kapil = Student() #kapil is object here and is instance of class Student
ram =    Student()   #kapil and ram are two different objects

# print(kapil,ram)  # two different memory location shows these are different
kapil.name = "Kapil Kapil"
kapil.roll_num = 123
kapil.section = "b"
print(kapil.name)

ram.name = "ram"
ram.std = 11
ram.subjects = ["english", "hindi"]
print(kapil.section,ram.name)
print(kapil.section,ram.subjects)