# find gcd of the two numbers
# imput 42,23
# output=?
#  42 divisor are 1,2,3,6


def gcd (m,n):
    if m==n:
        return m
    if (m>n):
        print(m,n)
        return gcd(m-n,n)
    else:
        return gcd(m,n-m)

print(gcd(42,62))
    
    
