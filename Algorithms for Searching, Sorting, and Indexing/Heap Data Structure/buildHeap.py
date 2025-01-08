# In this approach Bubble down (sink) approach is used to create min heap 
def build_min_heap(arr):
    n = len(arr)
    def minHeapify(arr,n,i):
        smallest = i
        left = 2*i +1
        right = 2*i+2
        if left<n and arr[left]<arr[smallest]:
            smallest = left 
        
        if right<n and arr[right]<arr[smallest]:
            smallest = right
        if smallest!= i:
            arr[i] , arr[smallest] = arr[smallest], arr[i]
            minHeapify(arr,n,smallest) 
        
     # Start from the last non-leaf node and move upwards
    for i in range(n//2 -1 ,-1 ,-1):
        minHeapify(arr,n,i)
    return arr
    
arr = [4, 10, 3, 5, 1]
build_min_heap(arr)
print(arr)