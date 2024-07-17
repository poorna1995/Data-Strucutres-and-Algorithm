
def checkOccurrence(array,key):
    count=0
    if len(array)==0:
        return 0
    for i in range(len(array)):
        if array[i]==key:
            count=count+1
    return count

print(checkOccurrence([1,2,1,2,0,2,2,2,1,1],2))



def chckRecursion(array,key,i):
    if i>=len(array):
        return 0
    if array[i]==key:
        return 1+chckRecursion(array,key,i+1)
    else:
        return chckRecursion(array, key, i + 1)

print(chckRecursion([1,2,1,2,0,2,2,2,1,1],2,0))
