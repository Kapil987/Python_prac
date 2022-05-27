#!/usr/bin/env python
import os
import datetime
import logging
import file2 # if you use same logging then file2 log file will only be created to resolve these use different loggers

local_time = datetime.datetime.now().strftime("%Y-%m-%d__%H-%M-%S")
#now we will Create and configure logger
logging.basicConfig(filename='temp.log',level=logging.DEBUG, format='%(asctime)s,%(message)s')
# logging.basicConfig(filename="py_Scripts_"+local_time+".log",format='%(asctime)s:%(name)s:%(levelname)s,%(message)s',filemode='w')

#Let us Create an object
# logger=logging.getLogger(__name__)
# file_handler = logging.FileHandler("py_Scripts_"+local_time+".log")

# logger.addHandler(file_handler)

#Now we are going to Set the threshold of logger to DEBUG
# logger.setLevel(logging.INFO)
file2.details()
print('\n')
print ("Script Started at : ")
print(local_time)
print('\n')

logging.info("The script has been Started ")

d = '/root/py_scripts/'

for f in os.listdir(d):
    # logging.info(f)
    # logger.info('val')
    if os.path.isfile(d + f):
        print(f)


logging.info("The script has been Ended ")
logging.debug('this is debug message')
print ('\nScript Ended \n')
