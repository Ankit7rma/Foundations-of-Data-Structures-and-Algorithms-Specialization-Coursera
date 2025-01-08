def min_heapify(arr, n, i):
    """
    Ensures the subtree rooted at index `i` satisfies the min-heap property.
    
    Parameters:
    arr (list): The array representing the heap.
    n (int): The size of the heap.
    i (int): The index of the root of the subtree to heapify.
    """
    smallest = i  # Assume the current root is the smallest
    left = 2 * i + 1  # Index of left child
    right = 2 * i + 2  # Index of right child

    # Check if the left child exists and is smaller than the root
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    # Check if the right child exists and is smaller than the smallest so far
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # If the smallest is not the root, swap and heapify the affected subtree
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # Swap
        min_heapify(arr, n, smallest)  # Recursively heapify the affected subtree


def build_min_heap(arr):
    """
    Converts an array into a min-heap using the `MIN-HEAPIFY` function.

    Parameters:
    arr (list): The array to be converted into a min-heap.
    """
    n = len(arr)  # Size of the heap

    # Start from the last non-leaf node and move upwards
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)

def insertInHeap(heap,value):
    if heap is None:
        heap = []
    heap.append(value)
    i = len(heap)-1
    while i>0:
        parentIndex = (i-1)//2
        if heap[parentIndex]>heap[i]:
            heap[parentIndex],heap[i] = heap[i],heap[parentIndex]
            i = parentIndex
        else:
            break

arr = [14, 10, 13, 5, 1,7,9]
 
build_min_heap(arr)
insertInHeap(arr,6)
print(arr)
