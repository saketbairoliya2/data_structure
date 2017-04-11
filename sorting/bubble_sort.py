#Bubble Sort

def bubble_sort(arr, l):
	for i in range(0, l):
		for j in range(0, l-i-1):
			if (arr[j] > arr[j+1]):
				#swap the elements
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr

# Program Execution starts from here.
if __name__ == '__main__':
	arr = [2, 9, 1, 7, 5, 3]
	l = len(arr)
	sorted_array = bubble_sort(arr, l)
	print('Sorted array here is {}' .format(sorted_array))

'''
Run time: O(n^2)
In Place Algorithm.
This algorithm can be Optimized to reduce number of element swaps with
keeping the count of swaps inside if stmt, if it is equal to '0' then break the loop.
Incase of Already sorted array, runtime would be O(n) in this case.
'''
