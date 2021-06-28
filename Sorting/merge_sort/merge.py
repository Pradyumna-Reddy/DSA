# Merge on a 0 - indexed mutable sub sequence A[1..n], where two sub sequences A[p..q] and A[q+1..r] are already sorted
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

# # Simple merge test
# A = [0, 1, 4, 10, 2, 3, 9, 18] # p = 0, q = 3  and r = 7, remember that p..q and q+1..r must be sorted
# merge(A, 0, 3, 7)
# print(A) # [0, 1, 2, 3, 4, 9, 10, 18]
