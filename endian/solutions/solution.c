#include <stdio.h>

#define BUFFER_LEN 8000000

#ifdef DEBUG
#define BYTE_TO_BINARY_PATTERN "%c%c%c%c%c%c%c%c"
#define BYTE_TO_BINARY(byte)  \
  (byte & 0x80 ? '1' : '0'), \
  (byte & 0x40 ? '1' : '0'), \
  (byte & 0x20 ? '1' : '0'), \
  (byte & 0x10 ? '1' : '0'), \
  (byte & 0x08 ? '1' : '0'), \
  (byte & 0x04 ? '1' : '0'), \
  (byte & 0x02 ? '1' : '0'), \
  (byte & 0x01 ? '1' : '0')
#endif

char middle(char b) {
  return ((b & 0b11000000) >> 4) | ((b & 0b00110000) >> 4)
    | ((b & 0b00001100) << 4) | ((b & 0b00000011) << 4);
}

int main(void) {
  char bytes[BUFFER_LEN];
  int read;
  while ((read = fread(bytes, 1, BUFFER_LEN, stdin)) != 0) {
    for (int i = 0; i < read; ++i) {
      bytes[i] = middle(bytes[i]);
#ifdef DEBUG
      fprintf(stderr, "%c is " BYTE_TO_BINARY_PATTERN "\n",
          bytes[i], BYTE_TO_BINARY(bytes[i]));
#endif
    }
    fwrite(bytes, 1, read, stdout);
  }
}
