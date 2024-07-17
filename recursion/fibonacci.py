# iternative

def fibonnaci(num):
    n0=0
    n1=1
    for i in range(0,num):
        temp=n0+n1
        n0=n1
        n1=temp
        i=i+1

    return n0
print(fibonnaci(6))


def recurfibonacci(num):
    if num<=1:
        return num
    return (recurfibonacci(num-2) + recurfibonacci(num-1))


print(recurfibonacci(6))

        

  