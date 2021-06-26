# Algorithm for adding two binaries of size n to get another binary of size n+1
# Binaries are stored in a sequence
def add_binaries_contained_in_sequence(A, B): # A and B must be of same length
	carry = 0
	C = []
	for i in range(len(A)-1, -1, -1):
		rem = (A[i] + B[i] + carry) % 2 # I at first made a mistake of exhanging this line and next line, carry gets modified 
		carry = (A[i] + B[i] + carry) // 2 # --cotd. this shows importance of sequence checking variable value and type change while debugging
		C.append(rem)
	C.append(carry)
	# We are reversing bcz the list formed by appending is in reverse of actual order. We can LSBs first, but we need MSBs first in sequence (just for convenience)
	# You can prepend the rem to C, but that move needs shifting the list everytime which takes time 1, 2, 3, ... n in each consequetive iter #(link). which makes it whole O(n^2) time
	# reversing C at end takes only O(n) time
	return C[::-1]

# Simple test
A = [1, 1, 0, 0] #12
B = [0, 1, 1, 0] #6
print(add_binaries_contained_in_sequence(A,B)) #18 [1, 0, 0, 1, 0]

# You can use another method which is similar, except that it looks whether the carry is 0 or 1
# Depending on the carry, we can get the sum and reminder
# But other method uses conditionals