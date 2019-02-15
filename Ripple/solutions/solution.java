import java.util.LinkedList;
import java.util.Scanner;

class solution {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    System.out.println(new solution(in.nextInt(), in.nextInt(), in.nextInt(), in)
      .numberPresent(in.nextInt()));
  }

  private final int width, height;
  private final LinkedList<Drop> drops = new LinkedList<>();
  private static final boolean DEBUG = false;
  private static final char WHITE_BOX = '□', BLACK_BOX = '■';

  private solution(int width, int height, int n, Scanner in) {
    this.width = width;
    this.height = height;
    for (int i = 0; i < n; ++i) {
      drops.add(new Drop(in.nextInt(), in.nextInt(), in.nextInt()));
    }
  }

  private int numberPresent(int at) {
    boolean[][] board = new boolean[height][width];

    for (Drop drop : drops) {
      calculate(board, drop, at);
    }

    int sum = 0;
    for (int y = 0; y < height; ++y) {
      for (int x = 0; x < width; ++x) {
        if (board[y][x]) ++sum;
        if (DEBUG) System.out.print(board[y][x] ? BLACK_BOX : WHITE_BOX);
      }
      if (DEBUG) System.out.println();
    }

    return sum;
  }

  private static String printBoard(boolean[][] board) {
    StringBuilder ret = new StringBuilder();
    for (int y = board.length - 1; y >= 0; --y) {
      for (int x = 0; x < board[0].length; ++x) {
        ret.append(board[y][x] ? BLACK_BOX : WHITE_BOX);
      }
      ret.append('\n');
    }
    return ret.toString();
  }

  /* modifies board in-place, making sure to cancel out collisions */
  private void calculate(boolean[][] board, Drop drop, int originalTime) {
    int time = originalTime - drop.time, i = time - 1;

    /* handle the edge cases */
    if (time < 0) return;
    if (time == 0) {
      /* flip the bit */
      board[drop.y][drop.x] ^= true;
      return;
    }

    /* calculate the diagonals */
    while (i >= 0) {
      /* do the work */
      final int bottom = mod(drop.y - i, height), top = mod(drop.y + i, height),
          xoffset = time - i,
          left = mod(drop.x - xoffset, width) , right =  mod(drop.x + xoffset, width);
      board[bottom][right] ^= true;
      board[bottom][left] ^= true;
      board[top][right] ^= true;
      board[top][left] ^= true;
      --i;
    }

    /* edge case: the corners have two of these with the same result,
     * but we don't count it as a collision */
    //if ((time & 1) == 1) {
    /*
      int py = mod(drop.y + time, height), ny = mod(drop.y - time, height),
          px = mod(drop.x + time, width), nx = mod(drop.x - time, width);
      board[py][drop.x] ^= true;
      board[drop.y][px] ^= true;
      board[ny][drop.x] ^= true;
      board[drop.y][nx] ^= true;
    //}
    */
  }

  /* handle negative values of n */
  private static int mod(int n, int max) {
    if (n >= 0) return n % max;
    return (max + (n % max)) % max;
  }

  class Drop {
    final int time, x, y;

    Drop(int time, int x, int y) {
      this.time = time;
      this.x = x;
      this.y = y;
    }

    public String toString() {
      return String.format("Drop(time=%d, x=%d,y=%d)", time, x, y);
    }
  }
}
