/***********************************************************************************************
* By Deven Maheshwari
* Compilation: javac -classpath .:stdlib.jar ChromaticScale.java
* Execution: java -classpath .:stdlib.jar ChromaticScale 
*
* Plays each note of the A chromatic scale for one second.
*
* % java ChromaticScale
*
*
*****************************************************************************/

public class ChromaticScale {
    public static double[] getNote(double hz, double duration, int SAMPLING_RATE){
        int n = (int) (SAMPLING_RATE * duration);
        double[] a = new double[n+1];
        for (int i = 0; i <= n; i++) {
            a[i] = Math.sin(2 * Math.PI * i * hz / SAMPLING_RATE);
        }
        return a;
    }
    public static void main(String[] args) {
        int SAMPLING_RATE = 44100;
        double duration = 1.0;
        double[] notes = new double[] {440.00, 466.16, 493.88, 523.25, 554.37, 587.33, 622.25, 659.26, 698.46, 739.99, 830.61, 880.00};
        for(double hz: notes){
            StdAudio.play(getNote(hz, duration, SAMPLING_RATE));
        }
    }
}

