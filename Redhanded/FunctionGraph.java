/********************************************************************************************************************************************************************
*   By Deven Maheshwari
*
*   Compilation: javac -cp .:../../stdlib.jar FunctionGraph.java
*   Execution: java -cp .:../../stdlib.jar FunctionGraph 1 25 50
*
*   Plots the Complexity Graph showing the growth curves of the most common classes in different colors. 
*
*************************************************************************************************************/
import java.awt.Color;

public class FunctionGraph {

    // plots the function f in the interval [a, b] using n+1 evenly spaced points
    public static void plot(Function f, double a, double b, int n, Color c) {
        double[] y = new double[n+1];
        double delta = (b - a) / n;
        for (int i = 0; i <= n; i++)
            y[i] = f.evaluate(a + delta*i);
        StdDraw.setPenColor(c); 
        StdStats.plotPoints(y);
        StdStats.plotLines(y);
    }



    // sample client program
    public static void main(String[] args) { 
        double a = Double.parseDouble(args[0]);
        double b = Double.parseDouble(args[1]);
        int n = Integer.parseInt(args[2]); 
        StdDraw.setScale(0,600); 
        
        plot(x -> 300, a, b, n, StdDraw.BLUE); 
        plot(x -> x, a, b, n, StdDraw.GREEN); 
        plot(x -> x * x, a, b, n, StdDraw.GRAY); 
        plot(x -> Math.log(x), a, b, n, StdDraw.YELLOW); 
        plot(x -> x * Math.log(x), a, b, n, StdDraw.MAGENTA); 
        plot(x -> Math.pow(2,x), a, b, n, StdDraw.RED); 
    }

}
