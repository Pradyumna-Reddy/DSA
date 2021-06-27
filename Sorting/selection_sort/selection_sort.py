# Selection Sort using a 0 - indexed sequence
def selection_sort(A):
	for i in range(len(A)-1):
		min_index = i
		for j in range(i+1, len(A)):
			if A[j] < A[min_index]:
				min_index = j
		A[min_index], A[i] = A[i], A[min_index]

# Simple test
A = [1, 8 ,4, 2, 0]
selection_sort(A)
print(A)