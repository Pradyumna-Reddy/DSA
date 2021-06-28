# Insertion sort implement using a 0 indexed mutable sequence using recusrsion (divide and conquer)
def insertion_sort(A, p, r):
	if p < r:
		insertion_sort(A, p, r-1)
		key = A[r]
		i = r - 1
		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key

# simple test
A = [9, 2, 1, 5, 2, 0]
insertion_sort(A, 0, len(A)-1)
print(A)
