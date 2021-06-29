# Bubble sort on a 0 - indexed mutable sequence
def bubble_sort(A):
	for i in range(len(A)-1, 0, -1):
		for j in range(0, i):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]

# # simple test
# A = [9, 2, 1, 5, 2, 0]
# bubble_sort(A)
# print(A)