from fun1 import a
from fun2 import a
print(a)

# problem here is both files have same variable name so output is the one which is imported at last
# solution or better approach is
"""
use import as:
import fun1,fun2
print(fun1.a)
print(fun2.a)

"""
import fun1,fun2
print(fun2.a)
print(fun1.a)