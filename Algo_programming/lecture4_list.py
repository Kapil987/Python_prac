# List of Stocks
stocks_to_trade = ['TATAMOTORS','CIPLA','MARUTI','HEROMOTOCO','JSWSTEEL']
print(stocks_to_trade[2])
stocks_to_trade[3] = 'AMB'
print(stocks_to_trade[3])
print(stocks_to_trade[0:5])
stocks_to_trade.append("yesbank")
stocks_to_trade.append("addaniports")

print(stocks_to_trade[::-1])
gainer_looser = [1,15,-5,-6,6.2,-9]
gainer_looser.sort()
print(gainer_looser[:-2])
minimum = min(gainer_looser)
maximum = max(gainer_looser)
print(minimum)
print(maximum)
### loop
for temp_var in stocks_to_trade:
    print (temp_var,len(temp_var))

#quantity = 100

## find number of element in list
index = stocks_to_trade.index("JSWSTEEL")
print ("elemnet number:",index)

## 
stocks_to_trade = ['TATAMOTORS','CIPLA','MARUTI','HEROMOTOCO','JSWSTEEL']
quantity = ['10','20','30','40','50']

for var in stocks_to_trade:
    print(var,quantity[stocks_to_trade.index(var)])
    