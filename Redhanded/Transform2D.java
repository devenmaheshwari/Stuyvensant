/*
*   By Gavin Mcginley, Chloe Liu, Deven Maheshwari, Alex Garcia, Oscar Fishman
*   
*   Compilation: javac -cp .:../stdlib.jar Transform2D.java
*   Execution: java -cp .:../stdlib.jar Transform2D 
*   Dependencies: StdDraw.java
*
*/


public class Transform2D {
    // Returns a new array object that is an exact copy of the given array.
    // The given array is not mutated.
    public static double[] copy(double[] array) {
        double[] result = array.clone(); 
        return result; 
    }
    // Scales the polygon by the factor alpha.
    public static void scale(double[] x, double[] y, double alpha) {
        for (int i = 0; i < x.length; i++) {
            x[i] *= alpha; 
            y[i] *= alpha; 
        }
    }
    // Translates the polygon by (dx, dy).
    public static void translate(double[] x, double[] y, double dx, double dy) {
        for (int i = 0; i < x.length; i++) {
            x[i] += dx; 
            y[i] += dy; 
        }
    }
    // Rotates the polygon theta degrees counterclockwise, about the origin.
    public static void rotate(double[] x, double[] y, double theta) {
        double help = Math.toRadians(theta); 
        double[] cx = copy(x); 
        double[] cy = copy(y); 
        for (int i = 0; i < x.length; i++) {
            x[i] = cx[i] * Math.cos(help) - cy[i] * Math.sin(help); 
            y[i] = cy[i] * Math.cos(help) + cx[i] * Math.sin(help); 
        }
    }
    // Tests each of the API methods by directly calling them.
    public static void main(String[] args) {
        StdDraw.setScale(-5.0, 5.0);

        double[] x = { 0, 1, 1, 0 };
        double[] y = { 0, 0, 2, 1 };

        double[] cx = copy(x);
        double[] cy = copy(y);

        rotate(cx, cy, -45.0);
        translate(cx, cy, 1.0, 2.0);

        StdDraw.setPenColor(StdDraw.BLUE);
        StdDraw.polygon(cx, cy);

        StdDraw.setPenColor(StdDraw.RED);
        StdDraw.polygon(x, y);

        scale(x, y, 2.0);
        StdDraw.setPenColor(StdDraw.ORANGE);
        StdDraw.polygon(x, y);
    }
}