# Solution in Python

N = int(input())

A = []
for i in range(0, N):
	A.append(int(input()))
	
# Debug
#print(A)

# Find Value
AX = 0
BX = 0

# Calc Nimsum
nimsum = A[0]
for i in range(1, N):
	nimsum ^= A[i]

# Choose the Pile to Remove from
for i in range(0, N):
	if A[i] != 0 and (A[i] ^ nimsum) < A[i]:
		AX = A[i]
		BX = A[i] - (A[i] - (A[i] ^ nimsum)) # Getting new Value, not the amount to remove.
		A[i] = BX # Just For Testing!
		break

if BX == 0:
	#print("WARNING: BX is 0")

# For Testing!
nimsum = A[0]
for i in range(1, N):
	nimsum ^= A[i]
	
if nimsum != 0:
	print("WARNING: nimsum not 0: " + str(nimsum))
	
print(str(AX) + " " + str(BX))
