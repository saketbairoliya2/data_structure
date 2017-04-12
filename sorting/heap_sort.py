#Heap Sort
'''
Algo:
1. Heapify the given array.
2. Now the maximum element would be at root node, so replace it with the last node.
3. Reduce heap size by one and heapify the remaining array.
4. Repeat Step 3-4 until array size is greater then 1
'''

# def heapify(arr, n, i):
# 	largest = i
# 	l = i*2 + 1
# 	r = i*2 + 2

# 	if l < n and arr[i] < arr[l]:
# 		largest = l

# 	if r < n and arr[largest] < arr[r]:
# 		largest = r

# 	if largest != i:
# 		arr[i], arr[largest] = arr[largest], arr[i]

# 		heapify(arr, n, largest)

# def heap_sort(arr, n):

# 	# Building heap(Rearrangement)
# 	for i in range(n, -1, -1):
# 		heapify(arr, n, i)

# 	for i in range(n-1, 0, -1):
# 		arr[i], arr[0] = arr[0], arr[i]
# 		heapify(arr, n, 0)

# Python program for implementation of heap Sort
 
# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
# The main function to sort an array of given size
def heap_sort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)
 
if __name__ == '__main__':
	arr = [2, 10, 5, 7, 1, 9]
	sorted_array = heap_sort(arr)
	print('Sorted Array is {}' .format(sorted_array))
