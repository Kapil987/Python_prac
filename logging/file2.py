# simple file
# DEBUG: Detailed information, for diagnosing problems. Value=10.
# INFO: Confirm things are working as expected. Value=20.
# WARNING: Something unexpected happened, or indicative of some problem. But the software is still working as expected. Value=30.
# ERROR: More serious problem, the software is not able to perform some function. Value=40
# CRITICAL: A serious error, the program itself may be unable to continue running. Value=50
import logging
logging.basicConfig(filename='sample.log',level=logging.INFO,format='%(asctime)s:%(name)s:%(levelname)s,%(message)s')
def details():
    print('detail function from file2')
    logging.info('running in')