# Insertion sort implement using a 1 indexed array
def insertion_sort(A):
	for j in range(len(A)):
		key = A[j]
		# Insert A[j] into sorted sequence A[0..j-1]
		i = j - 1		
		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i = i - 1
		# Loop ends when we get an element that is not greater than "key"
		# Or all elements are larger than "key" and we reach position -1 (out of sequence)
		# Loop also copies all elements which were greater to "key" to one index on right
		# Now we just copy key to the it's correct positon A[i+1] = key

A = [9, 2, 1, 5, 2, 0]
insertion_sort(A)
print(A)