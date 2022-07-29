/*
*   By Deven Maheshwari, Chloe Liu, Gavin Mcginley, Alex Garcia, Oscar Fishman
*   
*   Compilation: javac CoinsClient.java
*   Execution: java CoinsClient trials
*   
*   Simulates a coin flip based on whether the coin is biased or unbiased. The biased coin chance of heads is set at 20%.  
*
*   Task 2:
*       1. 35%
*       2. Does not compile because object does not have a flip method. On compilation, does not check coin for flip, checks object for flip method, but there is none. 
*       3. Does compile. Initializes variable from interface. 
*       4. Runs because BiasedCoin has a flip function as well. 
*
*   Task 3:
*       5. Both compile and execute. a.f() == 12. a.g() == 8. 
*       6. Both compile and execute. b.f() == 3. b.g() == 30. 
*       7. All compile and execute. c.f() == 3. c.g() == 6. c.h() == 19  
*       8. c.f() &  c.g(); compile and execute. c.f() == 3, c.g() == 6. c.h() does not compile.  
*       9. ((A)d).f() & ((A)d).g() compile and execute. ((A)d).f()== 3, ((A)d).g() == 6. c.h() does not compile.  
*       10. (a). t1.f(1); == 2
*           (b). t2.f(1); == 2 
*           (c). t1.g(1); Does not compile
*           (d). t2.g(1); == 10
*           (e). t1.toString(); ==  "Howdy"
*           (f). t2.toString() == "Howdy"
*
*/

public class CoinsClient {
    public static void main(String[] args) {
        int trials = Integer.parseInt(args[0]); 
        double count = 0.0; 
        Coin tester = new Coin(); 
        System.out.println("Unbiased coin:"); 
        for (int i = 0; i < trials; i++) {
            String temp = tester.flip(); 
            if (temp == "H") count++;
            System.out.print(temp); 
        }
        System.out.println();
        System.out.println("observed head %: " +  100*(count/trials) );
        System.out.println(); 

        double count1 = 0.0; 
        Coin tester1 = new BiasedCoin(0.2); 
        System.out.println("Biased coin:");
        for (int i = 0; i < trials; i++) {
            String temp = tester1.flip(); 
            if (temp == "H") count1++;
            System.out.print(temp); 
        }
        System.out.println(); 
        System.out.println("observed head %: " +  100*(count1/trials) );
        System.out.println(); 
        
    }
}
