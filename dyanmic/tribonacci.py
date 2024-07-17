def tribo(n):
    memo={}
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    if n in memo:
        return memo[n]
    memo[n]= tribo(n-1)+tribo(n-2)+tribo(n-3)
    return memo[n]
print(tribo(10))