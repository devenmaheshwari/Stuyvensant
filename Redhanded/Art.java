/*
*   By Deven Maheshwari
*   
*   Compilation: javac Art.java
*   Execution: java Art n 
*
*   Draws circles of randomly produced colors in a recursive pattern according to the command line variable n. 
*/
public class Art {
    public static void makeArt(int n, double x, double y, double len) {
        StdDraw.setPenRadius(Math.random() / 250); 
        java.awt.Color[] colors = {StdDraw.BLACK, StdDraw.BLUE, StdDraw.RED, StdDraw.GRAY, StdDraw.GREEN, StdDraw.MAGENTA, StdDraw.PINK, StdDraw.YELLOW};
        StdDraw.setPenColor(colors[(int) (Math.random() * 8)]);  
        StdDraw.circle(x, y, len); 
        StdDraw.show();
        StdDraw.pause(60);
        StdDraw.circle(x+len, y+len, len); 
        StdDraw.show();
        StdDraw.pause(60);
        if (n != 1) {
            makeArt(n-1, x+len, y+len, len/2); 
        }
        StdDraw.circle(x+len, y-len, len);
        StdDraw.show();
        StdDraw.pause(60);
        if (n != 1) {
            makeArt(n-1, x+len, y-len, len/2); 
        } 
        StdDraw.circle(x-len, y-len, len); 
        StdDraw.show();
        StdDraw.pause(60);
        StdDraw.circle(x-len, y-len, len); 
        StdDraw.show();
        StdDraw.pause(60);
        if (n != 1) {
            makeArt(n-1, x-len, y+len, len/2); 
        }
        StdDraw.circle(x-len, y+len, len);
        StdDraw.show();
        StdDraw.pause(60);
        if (n != 1) {
            makeArt(n-1, x-len, y-len, len/2); 
        } 

    }
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        StdDraw.enableDoubleBuffering();
        StdDraw.setXscale(-1, 1); 
        StdDraw.setYscale(-1, 1); 
        makeArt(n, 0.0, 0.0, 0.25); 

    }
}
