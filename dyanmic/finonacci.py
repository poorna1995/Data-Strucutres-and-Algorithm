def fiboMemo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fiboMemo(n-1, memo) + fiboMemo(n-2, memo)
    return memo[n]

print(fiboMemo(10))