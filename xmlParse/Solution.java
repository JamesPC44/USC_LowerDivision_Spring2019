import java.util.*;
import java.util.Stack;
import java.io.*; 
public class Solution {
  public void printXmlDepth(String input){
    Stack<String> stack = new Stack<String>();
    int depth = 0;
    for(int i = 0; i < input.length(); i++){
      String builder = "";
      if(input.charAt(i) == '<'){
        if(input.charAt(i+1) == '/'){
          System.out.println(stack.pop());
          depth--;
          continue;
        } else {
          i++;
          while(input.charAt(i) != '>'){
            builder += input.charAt(i);
            i++;
          }
          stack.push(builder + " " + depth);
          depth++;
        }
      }
    }
  }
  public static void main(String [] args){
    Scanner fileScanner = new Scanner(System.in);
    String s = "";
    while(fileScanner.hasNext())
      s+= fileScanner.next();
    Solution sol = new Solution();
    sol.printXmlDepth(s);
  }
}
