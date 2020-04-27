import datetime
import pprint
# Dictionaries Key:Value Pair
stock_quantity = {"acc": 10, "cipla":20, "gail": 100}
stock_order = {"acc": "buy", "cipla":"notrade", "gail": "sell"}
name = "cipla"
print(name, stock_order[name])
# let say you have buy signal
stock_order["cipla"] =  "buy"
print(stock_order)

for step in stock_order:
    print(step)

for key,val in stock_order.items():
    print(key,val)

## Data from zeroda
data = {'tradable': 'true','mode': 'full', 'instrument_token': 3214,
        'last_price': 1234}
#dict_name[key]
print(data['last_price'])
print(data['mode'])
print(data['tradable'])

for fetch in data:
    print(fetch,data[fetch])