car = {
    "brand": "ford",
    "model": "Mustang",
    "year" : "1964"
}
x = car.setdefault("model","Bronco")

print(x)
print(car)
# cuts = [('00:00:00.00','00:00:26.00'),('00:00:31.00','00:01:49.00'),
#         ('00:01:55.00','00:02:16.00'),('00:02:21.00','00:03:21.00'),
#         ('00:03:26.00','00:04:10.00'),('00:04:15.00','00:04:50.00')]

# val = '00:00:00.00'
# # print(val.split(':'))
# temp_list = []
# for i in val.split(':'):
#     if i.endswith('.00'):
#         out = i.split('.')
#         print(out)
#         temp_list.extend(out)
#         continue
#     temp_list.append(i)

# for j in range(0,len(temp_list)):
#     temp_list[j] = int(temp_list[j])

# print(temp_list)
# add = [0,0,5,0]
# for index,item  in enumerate(temp_list):
#     print(index,item)
#     if item < 60:
#         temp_list[index] = temp_list[index] + add[index]

# print('After add',temp_list)

# a=5
# print("%.2f" % a)

# print(empy_list)
# sys.path is a list of absolute path strings
# os.startfile('C:')
# sys.path.append('/path/to/application/app/folder')

# cuts = [('00:00:00.00','00:00:22.00'),
#         ('00:00:27.00','00:01:19.00'),
#         ('00:01:26.00','00:02:07.00'),
#         ('00:02:12.00','00:03:10.00'),
#         ('00:03:16.00','00:03:30.00')]