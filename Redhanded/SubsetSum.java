/*
*   By Gavin Mcginley, Chloe Liu, Deven Maheshwari, Alex Garcia, Oscar Fishman
*   
*   Compilation: javac -cp .:../stdlib.jar SubsetSum.java
*   Execution: java -cp .:../stdlib.jar SubsetSum num
*   Dependencies: StdIn.java, StdOut.java
*
*   Returns the number of ways in which you can produce the target value by choosing a subset of the specified set of integers. 
*
*/

import java.util.TreeSet;

public class SubsetSum{

    public static int subsetSumWays(TreeSet<Integer> set, int target) {
        if (set.isEmpty()) {
            if (target==0) return 1;
            else return 0; 
        }
        int first = set.first(); 
        TreeSet<Integer> rest = new TreeSet<Integer>(set);
        rest.remove(first); 
        return subsetSumWays(rest,target - first) + subsetSumWays(rest,target);

    }


    public static boolean subsetExists(TreeSet<Integer> set, int target){
        if (set.isEmpty()) return target == 0;
        int first = set.first(); // returns and removes
        TreeSet<Integer> rest = new TreeSet<Integer>(set);
        rest.remove(first);
        return subsetExists(rest,target - first) ||
            subsetExists(rest,target);
    }
    

    public static void main(String [] args){
        TreeSet<Integer> set = new TreeSet<Integer>();
        for (String s : args)
            set.add(Integer.parseInt(s));
        System.out.print("enter target value: ");
        int target = StdIn.readInt();

        System.out.println("set: " + set);
        System.out.println("target: " + target);
        System.out.println("subset exits? " + subsetExists(set,target));
    
        System.out.println("subset sum ways: " + subsetSumWays(set, target)); 
    }



}