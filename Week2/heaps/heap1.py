def heapify(array, n, i): 
    root = i
    left = 2 * i 
    right = 2 * i +1
    
    if left < n and array[left] > array[root]:
        root = left #root=2
        
    if right < n and array[right] > array[root]:
        root = right # root =3
        
    if root != i: # 
        array[root], array[i] = array[i], array[root]
        heapify(array, n, root)

def build_heap(array):
    n = len(array) 
    for i in range(n//2 - 1, -1, -1):
        heapify(array, n, i)

array = [4, 2, 3, 1, 0, 12, 10]
build_heap(array)

print(array)
