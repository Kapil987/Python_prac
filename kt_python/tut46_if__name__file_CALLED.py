def add(a, b):
    print('from caller function add:: ')
    return a+b

# if __name__ == "__main__":  # Due to this the below add result will not come in caller file
# # calling adding withing this file
#     result = add(10, 20)
#     print(result)

# if without "if __name__ == "__main__":" the below content also gets executed
result = add(10, 20)
print(result)

## Will let us know the name of the file whether its main or not
print("and the name is:: ",__name__)