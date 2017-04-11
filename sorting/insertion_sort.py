#Insertion Sort
def insertion_sort(arr, l):
	for i in range(0, l):
		key = arr[i]
		j = i-1

		while(j >= 0 and arr[j] > key):
			arr[j+1], arr[j] = arr[j], arr[j+1]
			j -= 1
		arr[j+1] = key
	return arr 


if __name__ == '__main__':
	arr = [2, 9, 1, 7, 5, 3]
	l = len(arr)
	sorted_array = insertion_sort(arr, l)
	print('Sorted array here is {}' .format(sorted_array))

'''
Best Running Time: O(n^2)
Swapping of elements are less.
'''