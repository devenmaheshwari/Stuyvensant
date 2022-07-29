/*
*   By Deven Maheshwari
*
*   Compilation: javac Josephus.java
*   Execution: java Josephus n k 
*
*   Simulates the classical Josephus problem where n people line up in a circle, eliminating the kth person until only one remains. 
*/

import java.util.Queue;
import java.util.ArrayDeque;

public class Josephus {
    public static void move(Queue<Integer> queue, int k) {
        for (int i = 0; i < k-1; i++) {
            queue.add(queue.remove()); 
        }
    }
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]); 
        int k = Integer.parseInt(args[1]); 

        Queue <Integer> queue = new ArrayDeque<Integer>();
        for (int i = 1; i <= n; i++) {
            queue.add(i);
        }
        System.out.println(queue); 
        while (queue.size() > 1) {
            move(queue, k); 
            System.out.println("poisoned: " + queue.remove());
        }
        System.out.println("Survivor: " + queue.remove()); 
    }
}