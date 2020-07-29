import time
from functools import lru_cache
## without cache
# def work(n):
#     #Some task takin n seconds
#     time.sleep(n)
#     return n

## with caching
@lru_cache(maxsize=1) # last 3 call are cached
def work(n):
    #Some task takin n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    work(3)
    print("first3")
    # input()
    work(3)
    work(3)
    work(3)
    print("second3")
    work(4)
    work(4)
    print("four4")
    work(5)
    print("caching limit reached")
    work(6)
    print("Quick6??")
    work(6)
    print("No cache")

