// Solution for Code-a-thon Spr2019 Problem.
// - Brady O'Leary 2019

#include <stdio.h>
#include <stdlib.h>

int nimSum(int *arr, int len) {
	int toRet = arr[0];
	for (int i = 1; i < len; i++) {
		toRet ^= arr[i];
	}
	return toRet;
}

void printArr(int *arr, int len) {
	for (int i = 0; i < len; i++) {
		printf("%d ", arr[i]);
	}
	printf("\n");
}

int main() {
	int N;
	int *A;
	int sum = 0;
	int AX = 0, BX = 0;
	
	scanf("%d", &N);
	
	A = (int *)malloc(N * sizeof(int)); // Dynamically Allocate the Array of Nim Stacks
	
	// Read in List of A
	for (int i = 0; i < N; i++) {
		scanf("%d", &A[i]);
	}
	
	printArr(A, N);
	
	sum = nimSum(A, N);
	
	//Choose Pile to Remove from
	for (int i = 0; i < N; i++) {
		if (A[i] != 0 && (A[i] ^ sum) < A[i]) {
			AX = A[i];
			BX = A[i] - (A[i] - (A[i] ^ sum)); // Gets New Value, not amount to remove
			A[i] = BX; //TODO Remove ME
			break;
		}
	}
	
	if (BX == 0) {
		printf("WARNING: BX is 0\n");
	}
	
	sum = nimSum(A, N);
	
	if (sum != 0) {
		printf("WARNING: NimSum Not 0 %d\n", sum);
	}
	
	printf("%d %d\n", AX, BX);
	
	return 0;
}
