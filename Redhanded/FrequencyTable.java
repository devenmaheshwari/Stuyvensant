/*
*   By Gavin Mcginley, Chloe Liu, Deven Maheshwari, Alex Garcia, Oscar Fishman
*   
*   Compilation: javac FrequencyTable.java
*   Execution: java FrequencyTable 
*   Dependencies: In.java, words.utf-8.txt
*
*   Displays a table showing the number of words that appear in the English lexicon, sorted by lenth of the word.
*
*
*
*/

import java.util.*; 

public class FrequencyTable {
    public static void main(String[] args) {
        In in = new In("words.utf-8.txt");
	    Map <Integer,List<String>> words = new TreeMap<Integer, List<String>>();
        while (!in.isEmpty()){
            String line = in.readLine();
            if (!line.isEmpty()) {
                if (!words.containsKey(line.length())) {
                    words.put(line.length(), new ArrayList<String>()); 
                }
                words.get(line.length()).add(line);
            } 
        }

        for (int i: words.keySet()) {
            System.out.println(i+": " + words.get(i).size()); 
        }
}
}
