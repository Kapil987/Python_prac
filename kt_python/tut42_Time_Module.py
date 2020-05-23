#epoch is January 1, 1970, 00:00:00 (UTC)
import time

##
# initial = time.time()
# print(initial)
# k = 0
# while(k<45):
#     print("k value: ",k)
#     k = k+1
# print("While loop ran in time=",time.time(),"and intial = ",initial,\
#     "res=",time.time() - initial,"Seconds")

# initial2 = time.time()
# for i in range(45):
#     print("i value: ",i)
# print("For loop ran in: ",time.time() - initial2,"Seconds")

# final = time.time()
# print("Total time: ",final - initial)

##
# localtime = time.asctime(time.localtime(time.time()))
# t = time.localtime(time.time())
# # print(localtime)
# print(t)
# print(t[5])

##
a = 1
while(a < 10):
    print("val: ",a)
    a +=1
    time.sleep(2)

