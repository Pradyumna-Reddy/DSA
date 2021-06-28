# Given a set S of n integers and another integer x, 
# determine whether or not there exist two elements in S whose sum is exactly x
# input : some set, output: bool telling whether such two numbers exists or not
from binary_search import binary_search
def DoesAnyTwoElementsSumInSetEqualsAGivenkey(A, key):
	A.sort() # Actually use your own merge sort after you learn how to get imports right
	n = len(A)
	for i in range(1, n):
		index = binary_search(A, i+1, n-1, key - A[i])
		if index is not None:
			return True
	return False

# # Simple test
# A = [1 , 2, 9, 3, 4] 
# print(DoesAnyTwoElementsSumInSetEqualsAGivenkey(A, 13)) #should be true
# print(DoesAnyTwoElementsSumInSetEqualsAGivenkey(A, 8)) #should be false

