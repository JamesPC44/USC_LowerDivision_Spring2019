import java.util.Scanner;

public class solution {
  public static void main(String[] args) {
    Scanner stdin = new Scanner(System.in);
    double g = 10.;
    int v = stdin.nextInt();
    int n = stdin.nextInt();
    double[] m = new double[n];
    for (int i = 0; i < n; ++i) {
      int x = stdin.nextInt();
      int y = stdin.nextInt();
      m[i] = (double) y / x;
    }
    int i = 0;
    int c = 0;
    do {
      i = (int) (i - 2 * m[i] * v * v / (g * (1 + m[i] * m[i])));
      ++c;
    } while (i != 0);
    System.out.println(c);
  }
}
