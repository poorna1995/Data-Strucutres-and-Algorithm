def factorial(n):
    if n==0:
        return 1
    else:
        # print(n)
        return  n*factorial(n-1)
        print(n)

print(factorial(5))



def primeNumb(min,max):
    if (min>max):
        return
    else:
        print(min)
        return primeNumb(min+1,max)

print(primeNumb(1,10))
        