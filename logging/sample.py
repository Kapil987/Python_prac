import logging
import employee
import argparse

# Command line setup for setting debug level
parser = argparse.ArgumentParser(prog='samplefile', usage='%(prog)s [options] path,\
-h or --help for more info', description='List logging options')
parser.add_argument('-log',
                    '--log',
                    '-loglevel',
                    '--loglevel',
                    default='warning',
                    help='Provide logging level. Example:\
                    python file.py -log [options], list of options: \
                    critical | error | warning | info | debug, default=warning' )
args = parser.parse_args()
# customLogLevels = { 'critical': 50, 'error': 40, 'warning': 30, 'info': 20, 'debug': 10 }
customLogLevels = { 'critical': logging.CRITICAL, 'error': logging.ERROR, 
    'warn': logging.WARNING, 'warning': logging.WARNING, 'info': logging.INFO,
    'debug': logging.DEBUG
}

# checking if level is none if not get value from available dict
check_level = customLogLevels.get(args.log.lower())
print(check_level)
if check_level is None:
    raise ValueError(
        f"log level given: {args.log}"
        f" -- must be one of: {' | '.join(customLogLevels.keys())}")


# print(customLogLevels[check_level])

# Setting up logger other than root logger
logger = logging.getLogger(__name__)
logger.setLevel(check_level)
formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(funcName)s-%(lineno)d-%(message)s','%Y-%m-%d %H:%M:%S')
file_handler = logging.FileHandler('sample.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


# logging.basicConfig(filename='sample.log',level=logging.INFO,format='%(asctime)s-%(name)s-%(levelname)s-%(funcName)s-%(lineno)d-%(message)s')

def divby(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        logger.error('Tried to divide by zero')
        return 'An error has been occured'
    else:
        return result
    logger.debug(f'Function has val a: {a} and b: {b}')

print(divby(10, 0))

# Conclusion
"""
1. working with root logger is ok for small projects, but its better to log using specific logger
2. When you import a file/module then when you run the main file the imported file will also run
3. if two files has root logger configured a) main file b) file which is imported, then the imported
file logger runs and main file logger does not, and main file logger logs to imported file logs file
4. To solve this we need separate logger
5. if log level is critical then all below level will be logged, if level is 'error' then except 'critical'
all will be logged
"""