# simple file
# DEBUG: Detailed information, for diagnosing problems. Value=10.
# INFO: Confirm things are working as expected. Value=20.
# WARNING: Something unexpected happened, or indicative of some problem. But the software is still working as expected. Value=30.
# ERROR: More serious problem, the software is not able to perform some function. Value=40
# CRITICAL: A serious error, the program itself may be unable to continue running. Value=50
import logging
# import start
#formatting file handler not the logger
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s') 

# Creating logger object for this file
logger = logging.getLogger(__name__) #name will be equal for file/module name
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('temp.log') # file name changed then it will have individual logs else common logs
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def details():
    print('detail function from file2')
    logger.info('running in')

details()