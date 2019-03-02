#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <time.h>

char middle(char b) {
  return ((b & 0b11000000) >> 4) | ((b & 0b00110000) >> 4)
    | ((b & 0b00001100) << 4) | ((b & 0b00000011) << 4);
}

int main(int argc, char* argv[]) {
    if (argc > 1) {
        srand(atoi(argv[1]));
    } else {
        struct timespec ts;
        clock_gettime(CLOCK_MONOTONIC, &ts);
        srand((time_t)ts.tv_nsec);
    }

    char valid[256];
    int n = 0;
    for (int c = 0; c < 256; ++c) {
        if (c && isprint(c) && isprint(middle(c))) {
            valid[n] = c;
            ++n;
        }
    }

    int nbytes = rand() % (1<<16);
    for (int i = 0; i < nbytes; ++i) {
        putchar(valid[rand() % n]);
    }
}
