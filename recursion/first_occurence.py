
array=[3,4,1,8,1,1,1,1,1,1,7]

def FindOcurrence(array,key):
    count=0
    for i in range(len(array)):
        if key == array[i]:
            count=count+1
    return count


print(FindOcurrence(array,1))


def FindOccurenceRecursion(array):
    key=1
    if len(array) == 0:
        return 0
    if array[0] == key:
        return 1 + FindOccurenceRecursion(array[1:])
    else:
        return FindOccurenceRecursion(array[1:])

print(FindOccurenceRecursion (array))
        
    
    