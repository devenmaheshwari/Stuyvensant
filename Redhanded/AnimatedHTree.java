/*
*   By Gavin Mcginley, Chloe Liu, Deven Maheshwari, Alex Garcia, Oscar Fishman
*   
*   Compilation: javac -cp .:../stdlib.jar AnimatedHTree.java
*   Execution: java -cp .:../stdlib.jar AnimatedHTree n
*   Dependencies: StdDraw.java
*
*   Recursively draws the H-tree pattern. 
*
*   d) By rearranging the order of the recursive calls, the resulting H's are drawn in a different order, but the final image is the same across all attempts. This code draws the H's beginnging in the top left, then bottom left, then top right, then bottom right.  
*
*/

public class AnimatedHTree {
    public static void htree(int n, double x, double y, double len) {
        StdDraw.line(x, y, x+len, y); 
        StdDraw.show();
        StdDraw.pause(60);
        StdDraw.line(x+len, y, x+len, y+len); 
        StdDraw.show();
        StdDraw.pause(60);
        if (n != 1) {
            htree(n-1, x+len, y+len, len/2); 
        }
        StdDraw.line(x+len, y+len, x+len, y-len);
        StdDraw.show();
        StdDraw.pause(60);
        if (n != 1) {
            htree(n-1, x+len, y-len, len/2); 
        } 
        StdDraw.line(x, y, x-len, y); 
        StdDraw.show();
        StdDraw.pause(60);
        StdDraw.line(x-len, y, x-len, y+len); 
        StdDraw.show();
        StdDraw.pause(60);
        if (n != 1) {
            htree(n-1, x-len, y+len, len/2); 
        }
        StdDraw.line(x-len, y+len, x-len, y-len);
        StdDraw.show();
        StdDraw.pause(60);
        if (n != 1) {
            htree(n-1, x-len, y-len, len/2); 
        } 

    }
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        StdDraw.enableDoubleBuffering();
        StdDraw.setXscale(-1, 1); 
        StdDraw.setYscale(-1, 1); 
        htree(n, 0.0, 0.0, 0.25); 

    }
}
