# Linear Search implementation using 0 indexed sequence
def linear_search(A, key):
	for i in range(len(A)):
		if A[i] == key:
			return i
		# For loop didn't return means, key didn't appear in A
	return None

# Simple test
A = [1, 2, 3, 4, 5]
print(f'Search an element in sequence: {linear_search(A,5)}')
print(f'Search for element not in sequence: {linear_search(A,0)}')
