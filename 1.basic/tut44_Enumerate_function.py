lst = ["soap","mask","water","gloves"]

## Methond 1
# i=1
# for item in lst:
#     if i%2 != 0:    # !=0 as i value start from 1
#         print(f"Please buy: {item}")
#     i +=1

## Methond 2
# Syntax : enumerate(iterable, start)
# for index,item in enumerate(lst):
#     if index % 2 == 0:
#         print(f"Please buy with enumerate: {item}")

## Methond 3
# for item in lst:
#     # print(lst.index(f'{item}'))
#     if (lst.index(item) % 2 == 0):
#         print(f"Please buy: {item}")

