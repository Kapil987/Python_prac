import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(funcName)s-%(lineno)d-%(message)s')
file_handler = logging.FileHandler('employee_prog.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


# logging.basicConfig(filename='employee_prog.log',level=logging.DEBUG,format='%(asctime)s-%(name)s-%(levelname)s-%(funcName)s-%(lineno)d-%(message)s')


def addit(a,b):
    """this function adds two integer variables"""
    # logging.debug('proceeding with adding two variables')
    print('result: ',a+b)

# result = addit(10, 20)

class Employee:
    leaves = 10

    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        logger.info(f'Constructor for class: {type(self).__name__}, has been called by object: {self.fname}')
        logger.debug(f'Constructor for class: {type(self).__name__}, has been called by object: {self.fname}')
        # self.email = f"{fname}.{lname}@email.com"
    
    def explain(self):
        # logging.debug('Function has been called')
        print(f'Fname: {self.fname}, Lname: {self.lname}')
        # logging.debug(f'Instance variable values are: Fname: {self.fname}, Lname: {self.lname}')
    
    @property
    def email(self):
        if self.fname == None and self.lname == None:
            print('Email not set')
            # logging.debug(f'Property - has not been set: Fname: {self.fname}, Lname: {self.lname}')
            return
        print(f'{self.fname}.{self.lname}@email.com')
        # logging.debug(f'Property - has values as: Fname: {self.fname}, Lname: {self.lname}')
    
    @email.setter
    def email(self,string):
        names = string.split('@')[0]
        self.fname = names.split('.')[0]
        self.lname = names.split('.')[1]
        # logging.debug(f'Setter - has values as: Fname: {self.fname}, Lname: {self.lname}')
        # return cls(*string.split)
    
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None
        # logging.debug(f'Deleter - has values as: Fname: {self.fname}, Lname: {self.lname}')
    

kapil = Employee('kapil', 'kumar')
kapil.explain()
kapil.email
kapil.lname = 'sharma'
kapil.email = 'kapil.verma22email.com'
kapil.email
del kapil.email
# print((addit.__doc__))