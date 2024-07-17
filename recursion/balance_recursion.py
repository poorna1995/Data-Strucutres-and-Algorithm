#  input =['(',')']


def balancePara(array,startIndex=0,currentIndex=0):
    if len(array)==startIndex:
        return currentIndex==0 
    if currentIndex<0:
        return False
    
    if array[startIndex]=='(':
        return balancePara( array,startIndex+1,currentIndex+1)
    elif:
        array[startIndex]==')':
        return balancePara(array,startIndex+1,currentIndex-1)
    else:
        return False
