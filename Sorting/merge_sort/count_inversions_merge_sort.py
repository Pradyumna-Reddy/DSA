# If used sentinels, that would consider Infinity to some j in R as inversion
# Merge
def merge(A, p, q, r):
	L = []
	R = []
	for i in range(p, q+1):
		L.append(A[i])

	for j in range(q+1, r+1):
		R.append(A[j])

	i = 0
	j = 0
	inversions = 0
	n1 = len(L)
	for k in range(p, r+1):
		if i > len(L)-1:
			A[k] = R[j]
			j = j + 1
		elif j > len(R)-1:
			A[k] = L[i]
			i = i + 1
		elif L[i] > R[j]:
			A[k] = R[j]
			j = j + 1
			inversions = inversions + (n1 - 1) - i + 1 # Add assign number of remaining elements in L
		else:
			A[k] = L[i]
			i = i + 1
	return inversions

## Inversions should not be taken as measure for performance. This can't be.

# Merge sort
def count_inversions_merge_sort(A, p, r):
	if p < r:
		q = (p + r) // 2
		left = count_inversions_merge_sort(A, p, q)
		right = count_inversions_merge_sort(A, q + 1, r)
		inversions = merge(A, p, q, r) + left + right
		return inversions
	else:
		return 0


A = [2, 3, 8, 6, 1] # p = 0, q = 3
print(count_inversions_merge_sort(A, 0, 4)) # 5