from merge2 import merge
def merge_sort(A, p, r):
	if p < r:
		q = (p + r) // 2
		merge_sort(A, p, q)
		merge_sort(A, q+1, r)
		merge(A, p, q, r)

# # Simple test
# A = [3, 2, 9, 1, 0]
# merge_sort(A, 0, len(A)-1)
# print(A)