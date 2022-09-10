import tut46_if__name__file_CALLED
# two way to import 1. import module/filename or 2. form import module_name function/variable name
# if 1 approach ie. import module/filenam is used then you can directly use funcition/variable from file
# but in case you want to import two files file1 and file2 and both have variable Var1 defined and you tried to
# access Var1 from which file it should access now that's an ambiguity

res = tut46_if__name__file_CALLED.add(10,30)
print("Result form Caller Program:: ",res)