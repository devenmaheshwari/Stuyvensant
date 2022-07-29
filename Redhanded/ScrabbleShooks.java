/*
*   By Gavin Mcginley, Chloe Liu, Deven Maheshwari, Alex Garcia, Oscar Fishman
*   
*   Compilation: javac ScrabbleShooks.java 
*   Execution: java ScrabbleShooks
*   Dependencies: In.java, ospd.txt
*
*   Makes a list of all words in the scrabble dictionary that can have an s-hooked at the beginning or end. 
*
*
*
*/

import java.util.*;

public class ScrabbleShooks {
    public static void main(String[] args) {
        In in = new In("ospd.txt");
	    Set <String> words = new HashSet<String>();
        while (!in.isEmpty()){
            String line = in.readLine();
            words.add(line); 
        }
        ArrayList<String> result = new ArrayList<String>(); 

        for (String s1: words) {
            if (words.contains("s"+s1) || words.contains(s1+"s")) result.add(s1); 
        }
        System.out.println(result); 
    }
}
