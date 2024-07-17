# def heap(array,i):
#     n=len(array)
#     root=i # root=1
#     left=2*i +1# left=2
#     right=(2*i)+2 #right 3

#     if left<=n and array[left]>array[root]: # if r <=5 and array[2]>array[1]
#         root=left
#     if right<=n and array[right]>array[root]:
#         root=right
    
#     if root!=i:
#         array[i],array[root]=array[root],array[i]
#         heap(array,root)



       
# array=[5,2,3,1,10]

# heap(array,0)

# print(array)




# def heap(array,n, i):
#     root = i
#     left = 2 * i 
#     right = 2 * i + 1

   

#     # Compare root with left child
#     if left < n and array[left] < array[root]:
#         root = left

#     # Compare root with right child
#     if right < n and array[right] < array[root]:
#         root = right

#     # Swap if root is not the largest
#     for i in range(n):
#         if root != i:
#             array[i], array[root] = array[root], array[i]
#         heap(array,n, root)  # Recursively heapify the affected subtree




# def build_heap(array):
#     n = len(array)

#     # Build a max heap
#     for i in range(n // 2 - 1, -1, -1):
#         heap(array, n, i)

# # Example usage:
# arr = [5, 2, 3, 1, 10]
# build_heap(arr)
# print(arr)  # Output: [10, 5, 3, 1, 2]




def heapify(array, n, i):
    root = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than root
    if left < n and array[left] < array[root]:
        root = left

    # Check if right child exists and is greater than root so far
    if right < n and array[right] < array[root]:
        root = right

    # Change root if needed
    if root != i:
        array[i], array[root] = array[root], array[i]  # Swap

        # Recursively heapify the affected sub-tree
        heapify(array, n, root)

def build_heap(array):
    n = len(array)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

# Example usage:
arr = [1,2,3,4,5,6]
build_heap(arr)
print(arr)  # Output: [10, 5, 3, 1, 2]
