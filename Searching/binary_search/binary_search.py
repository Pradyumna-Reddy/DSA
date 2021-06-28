# binary search on a sorted sequence using loops
def binary_search(A, low, high, key):
	while low <= high:
		mid = (low + high) // 2
		if key == A[mid]:
			return mid
		elif key < A[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return None

# # Simple test
# A = [1, 2, 3, 4, 5]
# print(f'Search an element in sequence: {binary_search(A, 0, 4, 5)}')
# print(f'Search for element not in sequence: {binary_search(A, 0, 4, 0)}')