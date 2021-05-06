import re
input = open("data.txt","r")
# quotes = re.findall(r'"([^"]*)"', input.read(), re.U)
quotes = re.findall(r'"([^"]*)"', input.read())
# print(quotes[1])
list_raw = []
for value in quotes :
    list_raw.append(value)
input.close()
nparc_Pending_syntax
# Separating Database and Table names
count = 0
db_list = []
tb_list = []
for i in list_raw:
    if count%2 == 0:
        db_list.append(i)
    else:
        tb_list.append(i)
    count = count +1

print("\nNumber of Tables =",len(tb_list))
# Deleting Data if exist
with open ("pro_data2.txt",'w') as f:
    f.truncate(0)

# Input Data Processing Function 
def pending_data(start, end):
    tb_len_counter = start
    f = open("pro_data2.txt",'a+')
    f.write('check "')
    for i in range(start, end):
        f.writelines(db_list[i])
        f.write('"."')
        f.writelines(tb_list[i])
        tb_len_counter += 1
        if ((end - tb_len_counter ) != 0):
            f.write('" , "')

    f.write('" at level pendingop in parallel; \n')
    f.close()
    return end

# Logic when to call pending_data function
start = 0
list_factors = []

if (len(db_list) <= 25): # 24
    start = pending_data(start, len(db_list))
else:
    val = len(db_list)
    while (1):
        Remaining_tables = val - 25
        list_factors.append(25)
        val = Remaining_tables
        if Remaining_tables > 25:
            continue
        else:
            list_factors.append(Remaining_tables)
            break

# print("list:: ",list_factors)

start_range = 0
for i in list_factors:
    end_range = i
    end_range = start_range + end_range
    start_range = pending_data(start_range, end_range)
