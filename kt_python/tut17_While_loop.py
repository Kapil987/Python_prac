# While Loop used when we dont know the end
# i = 0
# while(i < 20):
#     print(i+1,end=' ')
#     i=i+1

# counter = 0
# while(counter < 3):
#     counter = counter + 1
#     print(counter)

num = [1,2,3,4,5] 
while num:              
    print(num.pop())

# # 1st itr
# num = [1, 2, 3, 4]      # 5 
# # 2st itr
# num = [1, 2, 3]         # 4 
# # 3st itr
# num = [1, 2]            # 3 
# # 4st itr
# num = [1]   # 2
# # 5st itr
# num = []   # 1
# # while num conditional false(0)
## list of list addition with while loop
# list1 = [[1,2],[2,4],[1,1],[4,5]]

# def sep_list(inp_list):
#     while list1:
#         # print(list1.pop())
#         add_list(list1.pop())
# sum_list = []
# def add_list(val_list):
#     i = len(val_list)
#     total = 0
#     global sum_list
#     while i:
#         print(val_list[i-1])
#         total = total + val_list[i-1]
#         i -=1
#     sum_list.append(total)

# sep_list(list1)
# sum_list.sort()
# print(sum_list[-1])