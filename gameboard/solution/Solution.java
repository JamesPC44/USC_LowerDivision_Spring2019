import java.io.*;
import java.util.*;

public class Solution {
  public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        int n = keyboard.nextInt();
        char[][] grid = new char[n][n];
        keyboard.nextLine();
        final char UPRIGHT = '0';
        final char WRONG   = '1';
        for(int i = 0; i < n; i++) {
            String line = keyboard.nextLine();
            for(int j = 0; j < n; j++) {
                grid[i][j] = line.charAt(j);
                //Insert character into grid
            }//Per character
        }//Per line
        
        int numOfTips = 0;
        for(int i = n - 1; i >= 0; i--) {
            for(int j = n - 1; j >= 0; j--) {
                if(grid[i][j] != correctSquare(i, j)) {
                    //Add one to the tips we need
                    numOfTips++;
                    //If the one we're looking at is wrong, flip everything
                    for(int ii = 0; ii <= i; ii++) {
                        for(int jj = 0; jj <= j; jj++) {
                            grid[ii][jj] = (grid[ii][jj] == UPRIGHT) ? WRONG : UPRIGHT;
                        }
                    }//Flip them all
                }//Check if the one is wrong
            }//go from column right to left
        }//go from row right to left
        System.out.println(numOfTips);
    }//main

    public static char correctSquare(int i, int j) {
      return (i + j) % 2 == 0 ? '0' : '1';
    }
}//solution
