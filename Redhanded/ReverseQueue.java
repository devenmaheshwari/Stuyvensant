/*
*   By Deven Maheshwari
*
*   Compilation: javac ReverseQueue.java 
*   Execution: java ReverseQueue args
*
*   Reverses a queue both recursively and non-recursively.
*
*   % java ReverseQueue a b c d
*       queue: [a, b, c, d]
*       reversed queue: [d, c, b, a]
*/

import java.util.*;

public class ReverseQueue{
    
    public static void reverseQueue(Queue<String> queue){
        Stack<String> stack = new Stack<String>();
        while (queue.size() != 0) {
            stack.push(queue.remove()); 
        }
        while (stack.size() != 0) {
            queue.add(stack.pop()); 
        }
    	
    }

    public static void reverseQueueR(Queue<String> queue) {
        if (!queue.isEmpty()) {
            String x = queue.remove(); 
            reverseQueueR(queue);
            queue.add(x); 
        }
    }

    public static void main(String [] args) {
        // Declare Queue
        Queue <String> queue = new ArrayDeque<String>();
        // Initialize the queue
        for (String s: args)
            queue.add(s);
        // Print the results
        System.out.println("queue: " + queue);
        reverseQueueR(queue);
        System.out.println("reversed queue: " + queue);
    }
}