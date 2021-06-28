# binary search on a sorted sequence using loops
def binary_search(A, low, high, key):
	if low > high:
		return None
	mid = (low + high) // 2
	if key == A[mid]:
		return mid
	elif key < A[mid]:
		return binary_search(A, low, mid - 1, key)
	else
		return binary_search(A, mid + 1, high, key)