#Quick sort
def quick_sort(arr, low, high):

	if (low < high):
		# Pi here is the pivot element for doing the partition
		pi = partition(arr, low, high)
		quick_sort(arr, low, pi-1) # Recursively do it for left part
		quick_sort(arr, pi+1, high) # Recursively do it for right part

	return arr

def partition(arr, low, high):
	pivot = arr[high]

	i = (low - 1) # Index of smaller element

	for j in range(low, high):
		#If current element is equal or smaller the pivot then increment index of smaller and swap arr[j]
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i+1

if __name__ == '__main__':
	arr = [2, 9, 1, 7, 5, 3]
	size = len(arr)
	low = 0
	high = size-1
	sorted_array = quick_sort(arr, low, high)
	print('Sorted array here is {}' .format(sorted_array))

'''
Quick sort is based on divide and Conquer approch.
We Select a Pivot element and then place it at the right index, Elements to the left would be smaller and to the right would be greater.
We then do this recursively for both the sides.
Best Case Run time: O(nLogn)
Worst case Run Time: O(n^2)
'''