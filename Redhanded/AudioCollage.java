/**************************************************************************
*  By Deven Maheshwari
*
*  Compilation: javac AudioCollage.javac
*  Execution: java AudioCollage n k
*
*  A library that is able to manipulate audio by amplifying, reversing, merging, mixing, or changing the speed of it. Plays the audio then each of the manipulations.
*
*  % java AudioCollage beatbox.wav cow.wav
*
*
*  Dependencies: StdAudio library.
***************************************************************************/
public class AudioCollage {

    public static double[] amplify(double[] a, double alpha) {
      for (int i = 0; i < a.length; i++) {
        a[i] = a[i] * alpha;
      }
      return a;
    }


    public static double[] reverse(double[] a) {
      int n = a.length;
      for (int i = 0; i < n/2; i++ ) {
        double curr = a[i];
        a[i] = a[n-1-i];
        a[n-1-i] = curr;
      }
      return a;
    }


    public static double[] merge(double[] a, double[] b) {
      int n = a.length + b.length;
      double[] combined = new double[n];
      for (int i = 0; i < n; i++) {
        if (i < a.length) combined[i] = a[i];
        else combined[i] = b[i - a.length];
      }
      return combined;
    }


    public static double[] mix(double[] a, double[] b) {
      int n = 0;
      boolean agreater = false;
      if (a.length > b.length) {
        n = a.length;
        agreater = true;
       }
      else {
        n = b.length;
        agreater = false;
      }
      double[] helper = new double[n];
      double[] hi = new double[n];
      if (agreater) {
        for (int i = 0; i < b.length; i++) {
          helper[i] = b[i];
        }
        for (int i = 0; i < n; i++) {
          hi[i] = a[i] + helper[i];
        }
      }
      else {
        for (int i = 0; i < a.length; i++) {
          helper[i] = a[i];
        }
        for (int i = 0; i < n; i++) {
          hi[i] = b[i] + helper[i];
        }
      }
      return hi;
   }


    public static double[] changeSpeed(double[] a, double alpha) {
      int length = (int) (a.length / alpha);
      double[] speed = new double[length];
      for (int i = 0; i < speed.length; i++) {
        int pos = (int) (alpha * i);
        speed[i] = a[pos];
      }
      return speed;
    }


    public static void main(String[] args) {
      double[] record = StdAudio.read(args[0]);
      double[] record1 = StdAudio.read(args[1]);
      StdAudio.play(record);
      StdAudio.play(amplify(record, 2));
      StdAudio.play(reverse(record));
      StdAudio.play(merge(record, record1));
      StdAudio.play(mix(record, record1));
      StdAudio.play(changeSpeed(record, 2));
    }
}

