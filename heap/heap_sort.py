# This is simple code for getting heap sort working.

def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    
    if l < n and arr[i] < arr[l]:
        largest = l
    
    if r < n and arr[largest] < arr[r]:
        largest = r
        
    if largest != i:
        #swap elements
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    
def heap_sort(arr):
    n = len(arr)
    
    #Build a max Heap:
    for i in range(n, -1, -1):
        heapify(arr, n, i)
        
    #one By One extract elements.
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    
a  = raw_input()
arr = list(a)
#arr = [2, 6, 8, 1, 7, 9]
heap_sort(arr)

l = len(arr)

for i in range(l):
    print arr[i]
    
    