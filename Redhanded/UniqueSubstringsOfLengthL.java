/*
*   By Deven Maheshwari
*
*   Compilation: javac UniqueSubstringsOfLengthL.java  
*   Execution: jjava UniqueSubstringsOfLengthL L
*   Dependencies: Stdin.java
*
*   Takes a command line argument, n, and prints out the unique substrings of length L of the input. 
*   
*/
import java.util.*;

public class UniqueSubstringsOfLengthL {
    public static void main(String[] args) {
        int L = Integer.parseInt(args[0]); 
        Set<String> helper = new HashSet<String>();
        while (!StdIn.isEmpty()) {
            String read = StdIn.readLine(); 
            for (int i = 0; i < read.length()-L; i++) {
                helper.add(read.substring(i, i+L));
            }
            System.out.println(helper.size());  
        }
        
    }
}
