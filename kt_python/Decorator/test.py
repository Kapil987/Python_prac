a = 10
def repeat(fun):
    def inner_repeat(*arg1):
        print('inside inner')
        fun(*arg1)
        fun(*arg1)
    return inner_repeat
@repeat
def abc():
    print('inside abc')

# abc = repeat(abc)
if __name__ == '__main__':
    abc()