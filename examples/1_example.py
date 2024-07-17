def recurssion(n):
    if n>0:
        for i in range(1,n+1):
            print(n)
            i+=1
        recurssion(n-1)

print(recurssion(2))


        