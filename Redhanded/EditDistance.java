/******************************************************************************
 *  By Gavin Mcginley, Chloe Liu, Deven Maheshwari, Alex Garcia, Oscar Fishman\
 *  
 *  Compilation:  javac EditDistance.java 
 *  Execution:    java EditDistance 
 *  Dependencies: StdIn.java, StdOut.java
 *
 *  % java EditDistance
 *      AACAGTTACC
 *      TAAGGTCA
 *      Edit distance = 7
 *      A T 1
 *      A A 0
 *      C - 2
 *      A A 0
 *      G G 0
 *      T G 1
 *      T T 0
 *      A - 2
 *      C C 0
 *      C A 1
 ******************************************************************************/

/*
    By 
//Test Case: AACAGTTACC
//           TAAGGTCA
// https://introcs.cs.princeton.edu/java/assignments/sequence.html
*/

public class EditDistance {
    // return the penalty for aligning character a with character b
    public static int penalty(char a, char b) {
        int total = 0;
        if (a == '-' || b == '-') total += 2;
        else if (a != b) total += 1;
        return total; 
    }

    //  return the min of 3 integers
    public static int min(int a, int b, int c) {
        return Math.min(Math.min(a, b), c); 
    }

    public static void main(String[] args) {
        String one = "";
        String two = "";
        while (!StdIn.isEmpty()) {
            one = StdIn.readLine(); 
            two = StdIn.readLine(); 
            break; 
        }

        int m = one.length();
        int n = two.length(); 
        int[][] opt = new int[m+1][n+1]; 
        for (int i = 0; i < m+1; i++) {
            for (int j = 0; j < n+1; j++) {
                opt[m][j] = 2 * (n - j); 
                opt[i][n] = 2 * (m - i); 
            }
        }
        for (int i = m-1; i >= 0; i--) {
            for (int j = n-1; j >= 0; j--) {
                opt[i][j] = min(opt[i+1][j+1] + penalty(one.charAt(i), two.charAt(j)), opt[i+1][j] + 2, opt[i][j+1] + 2 );
            }
        }
/*         for (int i = 0; i < m+1; i++) {
            for (int j = 0; j < n+1; j++) {
                System.out.printf("%3d", opt[i][j]);
            }
            System.out.println(); 
        } */

        int x = 0; 
        int y = 0;
        while (x < opt.length-2 && y < opt[0].length-2) {
            if (opt[x+1][y+1] == opt[x][y] || opt[x+1][y+1] + 1 == opt[x][y]) {
                x++;
                y++; 
            }
            if (opt[x][y] == opt[x+1][y] + 2) {
                two = two.substring(0, x) + "-" + two.substring(x); 
                x++; 
            }
            if (opt[x][y] == opt[x][y+1] + 2) {
                one = one.substring(0, y) + "-" + one.substring(y); 
                y++; 
            }

        }

        System.out.println("Edit distance = " + opt[0][0]); 

        for (int i = 0; i < one.length(); i++) {
            char a = one.charAt(i); 
            char b = two.charAt(i); 
            System.out.println(a + " " + b + " " + penalty(a,b)); 
        }
        

    }

}