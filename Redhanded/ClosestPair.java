/******************************************************************************
 *  By Gavin Mcginley, Chloe Liu, Deven Maheshwari, Alex Garcia, Oscar Fishman\
 *  
 *  Compilation:  javac ClosestPair.java 
 *  Execution:    java ClosestPair 
 *
 *  3.   (a) n^4/24
 *       (b) n
 *       (c) n^2/2
 *  6.  O(n^4), O(n^2), O(n)
 * 
 *
 ******************************************************************************/
public class ClosestPair {
    public static String pair(int[] a) {
        int one = 0; 
        int two = 0; 
        int diff = Math.abs(a[0] - a[1]); 
        for (int i = 0; i < a.length; i++) {
            for (int j = i+1; j < a.length; j++) {
                if ( Math.abs(a[i] - a[j]) < diff ) {
                    diff = Math.abs(a[i] - a[j]); 
                    one = a[i]; 
                    two = a[j]; 
                }
            }
        }
        String result = "(" + one + "," + two + ")"; 
        return result; 
    }

    public static void main(String[] args) {
        int[] a = {1001, 200, 205, 201, 123213}; 
        System.out.println(pair(a)); 
    }
}   
