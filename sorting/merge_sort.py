# An Implementation of Merge Sort.

def merge(arr, low, m, high):
	n1 = m-low+1
	n2 = high - m

	#Create Two Empty Arrays.
	L = [0] * n1
	R = [0] * n2

	# Copying data into tow arrays
	for i in range(0, n1):
		L[i] = arr[low+i]

	for j in range(0, n2):
		R[j] = arr[m+1+j]

	#Merge The temp array L, R into arr
	i = 0
	j = 0
	k = low

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[i]
			j += 1
		k +=1

	# Copying the remaining Elements
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1


def merge_sort(arr, low, high):

	if low < high:
		m = low +(high-low)/2
		merge_sort(arr, low, m)
		merge_sort(arr, m+1, high)
		merge(arr, low, m, high)
	return arr

if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	size = len(arr)
	low = 0
	high = size-1
	sorted_array = merge_sort(arr, low, high)
	print('Sorted array here is {}' .format(sorted_array))