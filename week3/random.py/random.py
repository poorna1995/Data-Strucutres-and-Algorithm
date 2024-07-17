def process_array(a):
    n=len(a)
    result=0
    for i in range(0,n):
        for j in range(i+1,n):
            if a[i]-a[j]==30:
                return 1
            else:
                result=result+(a[i]-a[j])
    return result