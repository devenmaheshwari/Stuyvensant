/*
    By Deven Maheshwari

    Compilation: javac Power.java
    Execution: java Power x n

    Recursively calculates x to the nth power in O(log N) time. 
*/

public class Power {

    public static double raiseToPower(double x, int n) {
        if (n == 0) return 1.0; 
        if (n % 2 == 0) return raiseToPower(x, n/2) * raiseToPower(x, n/2); 
        else return x * raiseToPower(x, n/2) * raiseToPower(x, n/2); 
    }
    public static void main(String[] args) {
        double x = Double.parseDouble(args[0]);
        int n = Integer.parseInt(args[1]); 
        System.out.println(raiseToPower(x, n)); 
    }
}