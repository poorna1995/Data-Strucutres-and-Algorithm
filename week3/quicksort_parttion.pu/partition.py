# # def partition(a,i):
#     """
#     The code defines a quicksort algorithm using a partition function to recursively sort a list of
#     elements.
    
#     :param a: The parameter 'a' in the functions 'partition' and 'quicksort' represents the list or
#     array that you want to sort using the quicksort algorithm
#     :param i: In the given code snippet, the parameter `i` represents the starting index of the subarray
#     that you want to sort using the quicksort algorithm. It is used to indicate the beginning of the
#     array or subarray that needs to be sorted
#     :return: The `partition` function is returning the index of the pivot element after partitioning the
#     array `a`. The `quicksort` function is not returning anything as it is a void function that sorts
#     the array in place.
#     """

#     pivot=a[len(a)-1]
#     i=-1
#     # j=0
#     for j in range(i+1 ,len(a)-1):
#         if a[j]<=pivot:
#             i+=1
#             a[i],a[j]=a[j],a[i]
#     a[i+1],a[pivot]=a[pivot],a[i+1]
#     return i+1



# def quicksort(a, i, n):
#     if i < n - 1:
#         pi = partition(a, i)
#         quicksort(a, i, pi - 1)
#         quicksort(a, pi + 1, n)



def partition(a, low, high):
    pivot = a[high]  # pivot value
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1

def quicksort(a, low, high):
    if low < high:
        pi = partition(a, low, high)
        quicksort(a, low, pi - 1)
        quicksort(a, pi + 1, high)






# Example usage
array=[1,5,2,-1,8,19,5,-1,4,2,-4,15,9]
# array=[9,1,4,13,20,1,32,12,12,56,234,12,89,231,6,4,12,5678,831,2,5]
new_partition= partition(array, 0, len(array)-1)
print("partition array",new_partition)
print("Original Array is:", array)

n = len(array)
quicksort(array, 0, n - 1)
print("Sorted array is:", array)


