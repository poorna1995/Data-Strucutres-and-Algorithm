# def BinarySearch(array, k):
#     left, right = 0, len(array) - 1
    
#     while left <= right:
#         mid = (left + right) // 2
#         if array[mid] == k:
#             return True
#         elif array[mid] > k:
#             right = mid - 1
#         else:
#             left = mid + 1
            
#     return False



# array=[1,4,5,2,10,23]
# k=13

# print(BinarySearch(array,k))






# def BinarySearch(array,k):
#     left,right =0,len(array)-1
    
#     while left<=right:
#         mid=(left+right)//2
#         if array[mid]==k:
#             return True
#         elif k>array[mid]:
#             left=mid+1
#         elif k<array[mid]:
#             right=mid-1
#     return False




# array=[1,4,5,2,10,23]
# k=1
# print(BinarySearch(array,k))




def BinarySearchNew(array,k):
    left,right=0,len(array)-1

    while left <=right:
        mid= (left+right)//2
        if array[mid]==k:
            return True
        elif k>array[mid]:
            left=mid+1
        elif  k<array[mid]:
            right=mid-1
    return False

array=[1,3,6,10,8]
k=10
print(BinarySearchNew(array,k))