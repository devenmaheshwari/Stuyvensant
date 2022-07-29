/*
*   By Gavin Mcginley, Chloe Liu, Deven Maheshwari, Alex Garcia, Oscar Fishman
*   
*   Compilation: javac TimeStrings.java
*   Execution: java TimeStrings
*   Dependencies: StdOut.java, Stopwatch.java
*
*/

public class TimeStrings {
     public static void main(String[] args) {
        String test = "a";

        /*  Experiment for: length
        *   Hypothesis: Constant
        *   Experiment Description: Uses a stopwatch to time the length() method on string test which is doubled each iteration. A small constant is added at the end to avoid division by 0. 
        *   Predictions and Observations: 1.0 for each test
        */ 
        double previous = 1.0; 
        for (int i = 1; i <= 29; i++) {
            Stopwatch timer = new Stopwatch();
            test.length(); 
            double elapsed = timer.elapsedTime();
            StdOut.println("Length ratio:" + "\t" + ((elapsed+0.01) / (previous + 0.01)));
            previous = elapsed;
            test = new String(test+test); // ADVICE: create a new string
        }

        test = "a"; 
        System.out.println(); 

        /*  Experiment for: charAt
        *   Hypothesis: Constant
        *   Experiment Description: Uses a stopwatch to time the chatAt() method on string test which is doubled each iteration. Uses a random index each test. A small constant is added at the end to avoid division by 0. 
        *   Predictions and Observations: 1.0 for each test
        */ 
        previous = 1.0; 
        for (int i = 1; i <= 29; i++) {
            int index = (int) (Math.random() * test.length()); 
            Stopwatch timer = new Stopwatch();
            test.charAt(index); 
            double elapsed = timer.elapsedTime();
            StdOut.println("CharAt ratio:" + "\t" + ((elapsed + 0.01) / (previous + 0.01)));
            previous = elapsed;
            test = new String(test+test); // ADVICE: create a new string
        }

        test = "a"; 
        System.out.println(); 

        /*  Experiment for: toLowerCase
        *   Hypothesis: Linear
        *   Experiment Description: Uses a stopwatch to time the toLowerCase() method on string test which is doubled each iteration. A small constant is added at the end to avoid division by 0. 
        *   Predictions and Observations: Each ratio slowly increments,the final test is around 2.0.
        */ 
        previous = 1.0; 
        for (int i = 1; i <= 29; i++) {
            Stopwatch timer = new Stopwatch();
            test.toLowerCase();
            double elapsed = timer.elapsedTime();
            StdOut.println("toLowerCase ratio:" + "\t" + ((elapsed + 0.01) / (previous + 0.01)));
            previous = elapsed;
            test = new String(test+test); // ADVICE: create a new string
        }

        test = "a"; 
        System.out.println();

        /*  Experiment for: replace
        *   Hypothesis: Quadratic
        *   Experiment Description: Uses a stopwatch to time the replace() method on string test which is doubled each iteration. It replaces a's with b's and vice versa depending on the iteratoon round. A small constant is added at the end to avoid division by 0. 
        *   Predictions and Observations: The values become increasingly greater each iteraetion, the final test at 129.
        */ 
        previous = 1.0; 
        for (int i = 1; i <= 29; i++) {
            Stopwatch timer = new Stopwatch();
            if (i % 2 == 1) test.replace("a", "b");
            else test.replace("b", "a");
            double elapsed = timer.elapsedTime();
            StdOut.println("Replace ratio:" + "\t" + ((elapsed + 0.01) / (previous + 0.01)));
            previous = elapsed;
            test = new String(test+test); // ADVICE: create a new string
        }

        test = "a"; 
        System.out.println();

        /*  Experiment for: compareTo
        *   Hypothesis: Linear
        *   Experiment Description: Uses a stopwatch to time the compareTo() method on string test which is doubled each iteration. The string is being compared to itself, which should take the most time. A small constant is added at the end to avoid division by 0. 
        *   Predictions and Observations: Each ratio slowly increments,the final test is around 2.0.
        */ 
        previous = 1.0; 
        for (int i = 1; i <= 29; i++) {
            Stopwatch timer = new Stopwatch();
            test.compareTo(new String(test));
            double elapsed = timer.elapsedTime();
            StdOut.println("CompareTo ratio:" + "\t" + ((elapsed + 0.01) / (previous + 0.01)));
            previous = elapsed;
            test = new String(test+test); // ADVICE: create a new string
        }

        test = "a"; 
        System.out.println();

        /*  Experiment for: equals
        *   Hypothesis: Linear
        *   Experiment Description: Uses a stopwatch to time the equals() method on string test which is doubled each iteration. The string is tested to itself, which should take the most time. A small constant is added at the end to avoid division by 0. 
        *   Predictions and Observations: The first tests' ratio is 1.0 but eventually increments to 2.0. 
        */ 
        previous = 1.0; 
        for (int i = 1; i <= 29; i++) {
            Stopwatch timer = new Stopwatch();
            test.equals(new String(test));
            double elapsed = timer.elapsedTime();
            StdOut.println("Equals ratio:" + "\t" + ((elapsed + 0.01) / (previous + 0.01)));
            previous = elapsed;
            test = new String(test+test); // ADVICE: create a new string
        }

        test = "a"; 
        System.out.println();

        /*  Experiment for: startsWith
        *   Hypothesis: Linear
        *   Experiment Description: Uses a stopwatch to time the startsWith() method on string test which is doubled each iteration. The string is tested to start with itself, which should take the most time. A small constant is added at the end to avoid division by 0. 
        *   Predictions and Observations: Each ratio slowly increments,the final test is around 2.0.
        */ 
        previous = 1.0; 
        for (int i = 1; i <= 29; i++) {
            Stopwatch timer = new Stopwatch();
            test.startsWith(new String(test)); 
            double elapsed = timer.elapsedTime();
            StdOut.println("StartsWith ratio:" + "\t" + ((elapsed+0.01) / (previous+0.01)));
            previous = elapsed;
            test = new String(test+test); // ADVICE: create a new string
        }

        test = "a"; 
        System.out.println();

        /*  Experiment for: endsWith
        *   Hypothesis: Linear
        *   Experiment Description: Uses a stopwatch to time the endsWith() method on string test which is doubled each iteration. The string is tested to end with itself, which should take the most time. A small constant is added at the end to avoid division by 0. 
        *   Predictions and Observations: Each ratio slowly increments,the final test is around 2.0.
        */
        previous = 1.0; 
        for (int i = 1; i <= 29; i++) {
            Stopwatch timer = new Stopwatch();
            test.endsWith(new String(test)); 
            double elapsed = timer.elapsedTime();
            StdOut.println("EndsWith ratio:" + "\t" + ((elapsed+0.01) / (previous + 0.01)));
            previous = elapsed;
            test = new String(test+test); // ADVICE: create a new string
        }

        test = "a"; 
        System.out.println();

        /*  Experiment for: indexOf
        *   Hypothesis: Linear
        *   Experiment Description: Uses a stopwatch to time the indexOf() method on string test which is doubled each iteration. The string is tested to find a string which is not present, which should take the most time. A small constant is added at the end to avoid division by 0. 
        *   Predictions and Observations: Each ratio slowly increments,the final test is around 2.0.
        */
        previous = 1.0; 
        for (int i = 1; i <= 29; i++) {
            Stopwatch timer = new Stopwatch();
            test.indexOf("b"); 
            double elapsed = timer.elapsedTime();
            StdOut.println("IndexOf ratio:" + "\t" + ((elapsed+0.01) / (previous + 0.01)));
            previous = elapsed;
            test = new String(test+test); // ADVICE: create a new string
        }

        test = "a"; 
        System.out.println();

        /*  Experiment for: substring
        *   Hypothesis: constant
        *   Experiment Description: Uses a stopwatch to time the substring() method on string test which is doubled each iteration. The string is tested to find the substring of the last letter. A small constant is added at the end to avoid division by 0. 
        *   Predictions and Observations: Each ratio slowly increments,the final test is around 2.0.
        */
        previous = 1.0; 
        for (int i = 1; i <= 29; i++) {
            Stopwatch timer = new Stopwatch();
            test.substring(test.length()-1, test.length()); 
            double elapsed = timer.elapsedTime();
            StdOut.println("Substring ratio:" + "\t" + ((elapsed+0.01) / (previous + 0.01)));
            previous = elapsed;
            test = new String(test+test); // ADVICE: create a new string
        }

        

     }
}