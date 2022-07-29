/************************************************************************
*  By Deven Maheshwari
*
*  Compilation: javac Divisors.javac
*  Execution: java Divisors n k
*
*  A library that computes the greatest common divisor and related functions on integers: GCD, LCM, relatively prime, and Euler's totient function. 
*
* % java Divisors 1440 408
*   gcd(1440, 408) = 24
*   lcm(1440, 408) = 24480
*   areRelativelyPrime(1440, 408) = false
*   totient(1440) = 384
*   totient(408) = 128
*
* % java Divisors 987 610
*   gcd(987, 610) = 1
*   lcm(987, 610) = 602070
*   areRelativelyPrime(987, 610) = true
*   totient(987) = 552
*   totient(610) = 240
*
***************************************************************************/
public class Divisors {

  public static int gcd(int a, int b) {
    a = Math.abs(a);
    b = Math.abs(b); 
    if (b == 0) return a;
    else return gcd(b, a % b);
  }

  public static int lcm(int a, int b) {
    int denominator = gcd(a,b); 
    return (Math.abs(a) * Math.abs(b)) / denominator; 
  }

  public static boolean areRelativelyPrime(int a, int b) {
    if (gcd(a,b)==1) return true; 
    else return false; 
  }

  public static int totient(int n) { 
    int result = 1; 
    for (int i = 2; i < n; i++) 
      if (areRelativelyPrime(i, n)) 
        result++; 
    return result; 
    } 

  public static void main(String[] args) {
    int a = Integer.parseInt(args[0]);
    int b = Integer.parseInt(args[1]);

    System.out.println("gcd("+a+", "+b+") = " + gcd(a,b));
    System.out.println("lcm("+a+", "+b+") = " + lcm(a,b));
    System.out.println("areRelativelyPrime("+a+", "+b+") = " + areRelativelyPrime(a,b));
    System.out.println("totient("+a+") = " + totient(a));
    System.out.println("totient("+b+") = " + totient(b)); 

  }
}
