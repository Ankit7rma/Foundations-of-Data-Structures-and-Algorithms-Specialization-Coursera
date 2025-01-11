def heapify(arr, n, i):
    smallest = i  # Initialize smallest as root
    left = 2 * i + 1  # left child
    right = 2 * i + 2  # right child

    # Check if left child is smaller than root
    if left < n and arr[smallest] > arr[left]:
        smallest = left

    # Check if right child is smaller than smallest so far
    if right < n and arr[smallest] > arr[right]:
        smallest = right

    # Change root if necessary
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # swap

        # Heapify the affected subtree
        heapify(arr, n, smallest)

def heapSort(arr):
    n = len(arr)

    # Build a Min-Heap (starting from the last non-leaf node)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one and build the sorted array in reverse order
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    # Reverse the array to get it sorted in ascending order
    arr.reverse()

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
print("Unsorted array:", arr)
heapSort(arr)
print("Sorted array:", arr)
