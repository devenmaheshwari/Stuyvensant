/*
*   By Gavin Mcginley, Chloe Liu, Deven Maheshwari, Alex Garcia, Oscar Fishman
*   
*   Compilation: javac HotPotato.java
*   Execution: java HotPotato k
*
*   Simulates the hot potato game using a round robin scheduler. Input is the probability a child will call hot potato. 
*/

import java.util.LinkedList;
import java.util.Queue;

public class HotPotato {
    public static void main(String[] args) {
        double prob = Double.parseDouble(args[0]); 
        Queue <String> queue = new LinkedList<String>();
        queue.add("Bobby"); 
        queue.add("Sue"); 
        queue.add("Amy"); 
        queue.add("Mark"); 
        queue.add("Danny"); 
        queue.add("Kelly"); 
        queue.add("Yuki"); 

        while (queue.size() != 1) {
            System.out.println("Children: "+queue); 
            String helper = queue.remove(); 
            if (Math.random() < prob) {
                System.out.println("Hot Potato: " + helper);
            } 
            else {
                queue.add(helper); 
                System.out.println("Potato: " + helper);
            }
        }

        System.out.println("Children: "+queue); 
        System.out.println("Winner: "+queue.remove()); 
    }
}
