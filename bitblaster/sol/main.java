// Java Solution for Nim Program

import java.util.Scanner;

public class main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		int[] arr = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = scan.nextInt();
		}
		int AX = 0, BX = 0;
		int nimsum = nimsum(arr);
		for (int i = 0; i < N; i++) {
			if (arr[i] != 0 && (arr[i] ^ nimsum) < arr[i]) {
				AX = arr[i];
				BX = arr[i] - (arr[i] - (arr[i] ^ nimsum)); //Getting New Value, not amount to remove
				arr[i] = BX; //For Testing
				break;
			}
		}
		if (BX == 0) {
			//System.out.println("WARNING: BX is 0");
		}
		
		//Testing
		nimsum = nimsum(arr);
		if (nimsum != 0) {
			System.out.println("WARNING: nimsum not 0: " + nimsum);
		}
		
		System.out.println(AX + " " + BX);
	}
	
	public static int nimsum(int[] arr) {
		int toRet = arr[0];
		for (int i = 1; i < arr.length; i++) {
			toRet ^= arr[i];
		}
		return toRet;
	}
}
