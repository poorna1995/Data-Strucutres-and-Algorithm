def heapify(array, n, i):
    smallest = i
    left_child = (2 * i) + 1
    right_child = (2 * i) + 2

    if left_child < n and array[left_child] < array[smallest]:
        smallest = left_child
    if right_child < n and array[right_child] < array[smallest]:
        smallest = right_child

    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        heapify(array, n, smallest)

def heap_sort(array):
    n = len(array)
    # Build a min-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
    
    # One by one extract elements
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]  # Swap
        heapify(array, i, 0)

# Example usage
array = [12, 11, 13, 5, 6, 7]
heap_sort(array)
print('Sorted array is:', array)
