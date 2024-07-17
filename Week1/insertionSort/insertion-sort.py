# def insetSort(arr):
#     for i in range(1,len(arr)):
#         j=i-1
#         temp=arr[i]
#         while j >= 0 and temp < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = temp
#     return arr

# print(insetSort([4,3,2,5,10,23,1,0,12,42,11]))  



# def insert(array):
#     for i in range(1,len(array)): # (1,5)
#         j=i-1  # j=0
#         temp=array[i] # temp = a[1] = 3
#         while j >= 0 and temp < array[j]: # 3 < 4:
#             array[j+1]=array[j]: # a[1]=4
#             j -= 1 # j = 0 - 1 = -1
#             arr[j + 1] = temp # a[0]= 3
#     return array





# array=[ 41, 59,26, 41, 58]

# def insertion(array):
#     for i in range(1, len(array)):
#         key= array[i]
#         j=i-1

#         while key<array[j] and j>=0:
#             array[j+1]=array[j]
#             j-=1
#             array[j+1]=key
#     return array

# print(insertion(array))

# n=[12,2,23,55,643]
# def sum(n):
#     sum=0
#     for i in range(len(n)):
#         sum= sum+n[i]
#     return sum
# print(sum(n))
                  
          


# array=[ 41, 59,26, 41, 58]

# def insertionIncreasing(array):
#     for i in range(1, len(array)):
#         key= array[i] # key= a[1] = 59
#         j=i-1 #0

#         while keyarray[j] and j>=0: #59>41
#             array[j+1]=array[j]  # a[1]=59
#             j-=1 # j=0-1 = -1
#             array[j+1]=key # array[0] =41
#     return array


# print(insertionIncreasing(array))


       



array= [8,1,3,1,2,5,0]

def insertionNew(a):
    for i in range(len(a)):
        key= a[i]
        j=i-1
        while key<a[j] and j>=0:
            a[j+1]=a[j]
            j-=1
            a[j+1]=key
    return array

print(insertionNew(array))
