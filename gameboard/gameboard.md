# Gameboard

---

The queen is trying to repaint her nxn chessboard. Someone decided to repaint the chessboard, so it is no longer in the alternating colors like a chessboard should be. The squares in the chessboard can be of two colors, black, or white. The queen can only work in rectangles(squares included) however, and she doesn't have any paint. The squares are very scared of the frightening queen, so when she orders the squares to switch they switch, from where she is standing to the upper-left most square(in a rectangular fashion).

When she does order the squares, every square to the left most square on the same row, to the top most piece at the top, and all squares from those boundaries to the top left square, flip from black to white, and from white to black. However it is very taxing for the queen to order all of her square. She would like to know what the minimum number of orders would be sufficent for her to get all of her squares so she can bring her pieces to the board.

The board should be such that no square shares a direct border with a same color square. It also should be that the top left square is white.

An example of a valid board is.

0101
1010
0101
1010

An example of one done is starting with the board:  

000  
101  
010  
  
In just two moves we can get to the final board. The first by flipping everything from the middle square to the upper-left most corner. And then again with the upper-left most corner.
  
110  
101  
010  
  
010  
101  
010  

So the output for the inputted board would be 2.

## Input

---

The first line of the input will n, the number of rows and columns of the board.
Every row will then be, 0 for a white square, and 1 for a black square and every row will be on its own line.

### Parameters

3 < n < 100

## Output

---

The ouput should be the minimum number of orders the queen must make so that the board returns to the correct ordering.

