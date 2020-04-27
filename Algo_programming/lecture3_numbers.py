capital = 1000
ltp = 362
openn = 120
buying_price = openn + openn*0.01
stoploss = openn - 0.05
acc_lot = 400
no_of_lot = 10
print(acc_lot * no_of_lot)
#// used for whole number output
print("quatity =",capital//openn)

# when time frame is over ask zerodha data
time_frame = 5 
#time_complete = 5 % 5 if ==0 # time completed
# zerodha takes tick size in terms of 5 at 2nd decimal place
# we cannot give 150.71,150.72,150.73
# round(value,place after decimal want to display)
print(round(150.7234324,1))
print(abs(-5)) # used when rsi is calculated
stoploss = 10
print (stoploss == 10) # verification True or False
hour = 9
minute = 30
#if latop.hour == 9 and latop.minute == 30:
    #start something
ltp = 97
stoploss = 98
print(ltp < stoploss)
#exit from trade

ltp = 1400
buying_price = 1500
print(ltp > buying_price)
    
