import random
def geometric(p):
    count=0
    if random.random()<=p:
        return 1 + geometric(p)
    else :
        return 1

print(geometric(.5))