# Cash Stocks
capital = 1000
stocks_to_trade = ['TATAMOTORS','CIPLA','MARUTI','HEROMOTOCO','JSWSTEEL']
monday = ['TATAMOTORS','CIPLA','MARUTI','HEROMOTOCO','JSWSTEEL']
tuesday = ['TATAMOTORS','CIPLA','MARUTI','HEROMOTOCO']
wed = ['TATAMOTORS','CIPLA','MARUTI']

monday_no_of_trade = len(monday)
tuesday_no_of_trade = len(tuesday)
wed_no_of_trade = len(wed)

mon_cap = capital / monday_no_of_trade
print ("mon_cap",mon_cap)

## Future trades
fut = "AMBUJACEM19JULFUT"
stock = "AMBUJACEM"
#addition = "19JULFUT"
current = "19APR"
nextt = "19MAY"
far = "19JUN"
print(stock + current+"FUT")
print(stock + nextt+"FUT")
print(stock + far+"FUT")

## Options
name = "AMBUJACEM"
month = "30JUL"
price = 210
call_put = "CE"

print(name+month+str(price))