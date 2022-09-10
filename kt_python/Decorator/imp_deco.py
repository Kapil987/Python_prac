import deco
  
@deco.do_twice
def cat():
    print('inside cat')

cat()

@deco.do_twice
def argu_dog(food):
    print('from dog food= ' + food)

argu_dog('abc')
# from deco import twice_out
# @deco.twice_out
# def simple():
#     print('This is simple')

# simple()
 
# @deco.twice_out 
# def new(*var,**accept):
#     print('new from var: ' + str(var) + str(accept.items()))

# new('aft','night',name = 'Morning')