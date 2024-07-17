# a=[1,3,5]
# b=[2,4,6,8]

# def MergeSort(a,b):
#     n=len(a)
#     m=len(b)
#     temp=[]
#     i=0
#     j=0
#     while i<n and j<m:
#         if a[i]<=b[j]:
#             temp.append[a[i]]
#             i+=1
#         else:
#             temp.append(b[j])
#             j+=1
#     while i<n:
#         temp.append(a[i])
#         i+=1

#     while j<m:
#         temp.append(b[j])
#         j+=1
#     return temp



a=[1,4,5]
b=[0,1,3,10]
def MergeSort(a,b):
    m=len(a)
    n=len(b)
    temp=[]
    i=0
    j=0
    while i<m and j<n:
        if a[i]<=b[j]:
            temp.append(a[i])
            i=i+1
        else:
            temp.append(b[j])
            j=j+1
    while i<m:
        temp.append(a[i])
        i=i+1
    while j<n:
        temp.append(b[j])
        j=j+1
    return temp

    

print(MergeSort(a,b))
