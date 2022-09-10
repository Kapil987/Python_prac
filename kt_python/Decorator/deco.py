def do_twice(func):
    def inner_twice(*args):
        print('inner twice')
        func(*args)
        func(*args)
        # func()
    return inner_twice

if __name__ == 'main':
    @do_twice
    def abc():
        print('inside abc')

# abc()
