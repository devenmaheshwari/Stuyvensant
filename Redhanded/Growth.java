/******************************************************************************
 *  By Gavin Mcginley, Chloe Liu, Deven Maheshwari, Alex Garcia, Oscar Fishman\
 *  
 *  Compilation:  javac Growth.java
 *  Execution:    java Growth
 *  Dependencies: Stopwatch.java, StdOut.java
 *
 *
 ******************************************************************************/

public class Growth {
// 1
    // O(n)
    public static String method1(int n){
        if (n == 0) return "";
        String temp = method1(n/2);
        if (n%2 == 0) return temp + temp;
        else          return temp + temp + "x";
    }
    // O(n^2)
    public static String method2(int n){
        String s = "";
        for (int i = 0; i < n; i++)
            s = s + "x";
        return s;
    }
    // O(nlog(n))
    public static String method3(int n){
        if (n == 0) return "";
        if (n == 1) return  "x";
        return method3(n/2) + method3(n - n / 2);
    }
    // O(n)
    public static String method4(int n){
        char [] temp = new char[n];
        for (int i  = 0; i < n; i++){
               temp[i] = 'x';
        }
        return new String(temp);
    }

    public static double timeTrial(int n) {
        Stopwatch s = new Stopwatch();
        method1(n); // method1(n), method2(n), method3(n), method4(n); 
        return s.elapsedTime();
    }
    public static void main(String[] args) { 
        StdOut.printf("%7s %7s %4s\n", "size", "time", "ratio");
        double previous = timeTrial(256);
        for (int n = 512; true; n += n) {
            double current = timeTrial(n);
            StdOut.printf("%7d %7.2f %4.2f\n", n, current, current / previous);
            previous = current;
        } 
    }

// 2    
    // O(n^2)
    public static String reverse1(String s){
        int n = s.length();
        String reverse = "";
        for (int i = 0; i < n; i++){
            reverse = s.charAt(i) + reverse;
        }
        return reverse;
    }
    // O(nlog(n))
    public static String reverse2(String s){
        int n = s.length();
        if (n <= 1) return s;
        String left = s.substring(0,n/2);
        String right = s.substring(n/2, n);
        return reverse2(right) + reverse2(left);
    }

// 3
    public static String reverseTime(String str) {
        int len = str.length(); 
        char[] c = new char[len]; 
        for (int i = 0; i < str.length(); i++) {
            c[i] = str.charAt(str.length()-1-i); 
        }
        return c.toString(); 
    }

    public static double TimeTrial(String str) {
        Stopwatch s = new Stopwatch();
        reverseTime(str);  
        return s.elapsedTime();
    }

/* Interview:
    This findMajorityElement algorithm is based on Moore's Voting Algorithm, which iterates through the array keeping a count of the majority element and compares it to the size of the array. Uses O(N) time and O(1) additional space. 
    Credit: geeksforgeeks.org   (https://www.geeksforgeeks.org/majority-element/)
        This code has been contributed by Mayank Jaiswal
*/

    public static int findMajorityElement(int [] array) {
        int cand = findCandidate(array, array.length);
        if (isMajority(array, array.length, cand)) return cand; 
        else return -1; 
    }
 
    public static int findCandidate(int a[], int size) {
        int maj_index = 0, count = 1;
        int i;
        for (i = 1; i < size; i++) {
            if (a[maj_index] == a[i])
                count++;
            else
                count--;
            if (count == 0) {
                maj_index = i;
                count = 1;
            }
        }
        return a[maj_index];
    }

    public static boolean isMajority(int a[], int size, int cand) {
        int i, count = 0;
        for (i = 0; i < size; i++) {
            if (a[i] == cand)
                count++;
        }
        if (count > size / 2)
            return true;
        else
            return false;
    }
 
}


