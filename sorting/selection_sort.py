#Selection sort

def selection_sort(arr, l):
	for i in range(0, l):
		min_element = i

		for j in range(i+1, l):
			if (arr[j] < arr[min_element]):
				min_element = j

		arr[i], arr[min_element] = arr[min_element], arr[i]

	return arr

if __name__ == "__main__":
	arr = [2, 9, 1, 7, 5, 3]
	l = len(arr)
	sorted_array = selection_sort(arr, l)
	print('Sorted array here is {}' .format(sorted_array))

'''
Runtime is O(n^2)
In place Sorting. Minimum number of swaps.

'''