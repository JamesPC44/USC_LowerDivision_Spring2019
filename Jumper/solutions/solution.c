/* Solution to Jumper problem by Hunter Damron */

#include <stdio.h>
#define DEBUG 0
#define DBG(...) if (DEBUG) { fprintf(stderr, __VA_ARGS__); }

int main() {
  int v,  // Velocity of jump
      n,  // Number of spaces
      x,  // x of slope
      y,  // y of slope
      c = 0,   // Count of jumps
      p = 0,   // Jumper index
      g = 10;  // Acceleration due to gravity
  float pp;
  scanf("%d %d", &v, &n);
  float m[n];  // List of slopes m
  for (size_t i = 0; i < n; ++i) {
      scanf("%d %d", &x, &y);
      m[i] = (float) y / x;
  }
  do {
      DBG("%d -> ", p);
      pp = p - 2 * m[p] * v * v / (g * (1 + m[p] * m[p]));
      p = p - 2 * m[p] * v * v / (g * (1 + m[p] * m[p]));  // The provided formula
      DBG("%d [%f]\n", p, pp);
      ++c;
  } while(p);  // Loop until p = 0 again
  printf("%d\n", c);
  return 0;
}
