# This sort uses merge sort but when the splits are small enough, we use insertion sort

# Insertion sort
def part_insertion_sort(A, p, r):
	for j in range(p+1, r+1):
		key = A[j]
		i = j - 1		
		while i >= p and A[i] > key:
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key

# Merge algorithm
def merge(A, p, q, r):
	L = []
	R = []
	for i in range(p, q+1):
		L.append(A[i])
	L.append(float('inf'))

	for j in range(q+1, r+1):
		R.append(A[j])
	R.append(float('inf'))

	i = 0
	j = 0
	for k in range(p, r+1):
		if L[i] > R[j]:
			A[k] = R[j]
			j = j + 1
		else:
			A[k] = L[i]
			i = i + 1

# Have to decide on isort_size, it can be found mathematically I guess
def merge_insertion_sort(A, p, r, isort_size = 50):
	if r - p + 1 <= isort_size:
		part_insertion_sort(A, p, r)
	else:
		q = (p + r) // 2
		merge_insertion_sort(A, p, q, isort_size)
		merge_insertion_sort(A, q+1, r, isort_size)
		merge(A, p, q, r)

# # Simple test
# A = [3, 2, 9, 1, 0]
# merge_insertion_sort(A, 0, len(A)-1)
# print(A)