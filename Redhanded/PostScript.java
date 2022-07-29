/*
*   By Deven Maheshwari
*   
*   Compilation: javac PostScript.java
*   Execution: java PostScript n k
*
*   Completes a roll using stacks by removing the top n elements and cycling through k times and replacing. 
*   
*
*
*/

import java.util.Stack;
import java.util.ArrayList;

public class PostScript{

public static void main(String [] args){
    int n = Integer.parseInt(args[0]);
    int k = Integer.parseInt(args[1]);
    Stack<String> s = new Stack<String>();
    s.push("A"); s.push("B"); s.push("C"); s.push("D");
    System.out.println("Initial : " + s);
    roll(s,n,k);
    System.out.println("after roll(" + n + ", " + k + "): " + s);
}

public static void roll(Stack<String> stack, int n, int k){
    if (n < 0 || n > stack.size() || k < 0) {
        throw new RuntimeException ("roll: argument out of range");
    }
    ArrayList<String> list = new ArrayList<String>();
    for (int i = 0; i < n; i++) {
        list.add(stack.pop()); 
    }
    for (int i = 0; i < k; i++) {
        String move = list.remove(0);
        list.add(move); 
    }
    for (int i = n-1; i >= 0; i--) {
        stack.push(list.get(i)); 
    }
}

}
