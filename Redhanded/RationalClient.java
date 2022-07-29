/******************************************************************************
 *  Deven Maheshwari & Daniela Maksin
 *  Period 3, Assignment 37
 *
 *  Compilation: javac Rational.java RationalClient.java
 *  Execution: java RationalClient
 ****************************************************************************/

import java.util.ArrayList;

public class RationalClient {
    //15
    public static int factorial(int d) {
        int num = 1;
        for (int i = 1; i <= d; i++) {
            num *= i;
        }
        return num;
    }

    //17
    public static int linearSearch(Rational[] rats, Rational key) {
        for (int i = 0; i < rats.length; i++) {
            if (rats[i].equals(key)) return i;
        }
        return -1;
    }

    public static void main(String[] args) {
        //10
        System.out.println("Rational(): " + new Rational());
        System.out.println("Rational(0,3): " + new Rational(0, 3));
        System.out.println("Rational(0): " + new Rational(0));
        System.out.println("Rational(0,-3): " + new Rational(0, -3));
        System.out.println();

        //Constructor Methods
        Rational a = new Rational();
        Rational b = new Rational(0, 3);
        Rational c = new Rational(1, -3);
        Rational d = new Rational(24, 8);

        System.out.println("a = " + a);
        System.out.println("b = " + b);
        System.out.println("c = " + c);
        System.out.println("d = " + d);
        System.out.println();

        //12
        System.out.println("a. a + b + c + d = " + ((a.plus(b)).plus(c)).plus(d));
        System.out.println("b. a(b + c) - d = " + ((b.plus(c)).times(a)).minus(d));
        System.out.println("c. (a + b) / (c + d) = " + (a.plus(b)).dividesBy(c.plus(d)));
        System.out.println();

        //13
        ArrayList<Rational> rats = new ArrayList<Rational>();
        rats.add(a);
        rats.add(b);
        rats.add(c);
        rats.add(d);
        Rational sum = new Rational();
        for (int i = 0; i < rats.size(); i++) {
            sum = sum.plus(rats.get(i));
        }
        System.out.println("sum of the rationals from list rats: " + sum);
        System.out.println();

        //14
        Rational tester = new Rational(1,2); 
        System.out.println("1/2 inverted: "+ tester.invert());
        System.out.println("1/2 negated: "+ tester.negate());
        System.out.println("1/2 abs: "+ tester.abs());
        System.out.println("1/2 double: "+ tester.doubleValue());
        System.out.println();

        //15
        Rational e = new Rational();
        for (int i = 0; i <= 10; i++) {
          System.out.printf("%-4d %-18s %-11f\n", i, e, e.doubleValue());
          e = e.plus(new Rational(1, factorial(i)));
        }
        System.out.println();

        //17
        Rational[] ratss = { a, b, c, d };
        System.out.println(linearSearch(ratss, c));
        System.out.println();

        //18
        System.out.println(a.equals(d));  //false
        System.out.println(rats.contains(d)); //true
    }
}

