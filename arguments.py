# default arguments = A default value for certain parameters
#                     default is used when argument is omitted
#                     make your function more flexible ,reduces # of arguments
#                     1. positional 2.default 3. keyword 4. arbitrary


## Calculate net price

def net_price(list_price,discount=0,tax=0.05): ## kicchu nh dile default argument
    return list_price*(1-discount)*(1+tax)

#print(net_price(500))
print(net_price(500,0.1,))


## make counter
import time
def count(start,end):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)

    print('Done!')

count(2,8)


