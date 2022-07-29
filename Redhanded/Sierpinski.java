/*
*   By Gavin Mcginley, Chloe Liu, Deven Maheshwari, Alex Garcia, Oscar Fishman
*   
*   Compilation: javac -cp .:../stdlib.jar Sierpinski.java
*   Execution: java -cp .:../stdlib.jar Sierpinski n 
*   Dependencies: StdDraw.java
*
*/

public class Sierpinski {
    // Height of an equilateral triangle with the specified side length.
    public static double height(double length) {
        return length * Math.sqrt(3) / 2;

    }

    // Draws a filled equilateral triangle with the specified side length
    // whose bottom vertex is (x, y).
    public static void filledTriangle(double x, double y, double length) {
        double[] dx = new double[] { x + length / 2, x, x - length / 2 };
        double[] dy = new double[] { y + height(length), y, y + height(length) };
        StdDraw.filledPolygon(dx, dy);

    }

    // Draws a Sierpinski triangle of order n, such that the largest filled
    // triangle has the specified side length and bottom vertex (x, y).
    public static void sierpinski(int n, double x, double y, double length) {
        if (n >= 1) {

            filledTriangle(x, y, length);
            sierpinski(n - 1, x - length / 2, y, length / 2);
            sierpinski(n - 1, x + length / 2, y, length / 2);
            sierpinski(n - 1, x, y + height(length), length / 2);
        }
    }

    // Takes an integer command-line argument n;
    // draws the outline of an upwards equilateral triangle of length 1
    // whose bottom-left vertex is (0, 0) and bottom-right vertex is (1, 0);
    // and draws a Sierpinski triangle of order n that fits inside the outline.
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        double[] dx = new double[] { 0, .5, 1 };
        double[] dy = new double[] { 0, Math.sqrt(3) / 2, 0 };
        StdDraw.polygon(dx, dy);
        sierpinski(n, .5, 0, .5);

    }
}
