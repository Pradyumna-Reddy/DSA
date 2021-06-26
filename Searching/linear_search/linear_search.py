# Linear Search implementation using 0 indexed sequence
def linear_sort(A, key):
	for i in range(len(A)):
		if A[i] == key:
			return i
		# For loop didn't return means, key didn't appear in A
	return None

# Simple test
A = [1, 2, 3, 4, 5]
print(f'Search an element in sequence: {linear_sort(A,5)}')
print(f'Search for element not in sequence: {linear_sort(A,0)}')
