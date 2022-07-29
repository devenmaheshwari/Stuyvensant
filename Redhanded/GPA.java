/*
*   By Gavin Mcginley, Chloe Liu, Deven Maheshwari, Alex Garcia, Oscar Fishman
*   
*   Compilation: javac GPA.java
*   Execution: java GPA
*   Dependencies: StdIn.java
*
*   Calculates the GPA given letter grades. 
*
*
*
*/

import java.util.Map;
import java.util.TreeMap;

public class GPA {
    public static void main(String[] args) {
        Map <String, Double> book = new TreeMap<String,Double>();
        book.put("A+", 4.33); 
        book.put("A", 4.00);
        book.put("A-", 3.67);
        book.put("B+", 3.33); 
        book.put("B", 3.00);
        book.put("B-", 2.67);
        book.put("C+", 2.33); 
        book.put("C", 2.00);
        book.put("C-", 1.67);
        book.put("D", 1.00);
        book.put("F", 0.00);

        double sum = 0.0;
        int count = 0; 
        while (true) {
            String line = StdIn.readLine(); 
            if (line.equals("-1")) break; 
            String[] helper = line.split(" "); 
            for (int i = 0; i < helper.length; i++) {
                if (book.containsKey(helper[i])) {
                    sum += book.get(helper[i]); 
                    count++; 
                }
            }
        }
        System.out.println("Average = " + sum/count); 
    }
    
}