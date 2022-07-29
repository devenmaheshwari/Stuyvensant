/**************************************************************************
*  By Deven Maheshwari
*
*  Compilation: javac ActivationFunction.javac
*  Execution: java ActivationFunction n 
*
*  A library that computes various activation functions that arise in neural networks. An activation function is a function that maps real numbers into a desired range, such as between 0 and 1 or between –1 and +1.
*
*  % java ActivationFunction 0.0
*   heaviside(0.0) = 0.5
*     sigmoid(0.0) = 0.5
*       tanh(0.0) = 0.0
*     softsign(0.0) = 0.0
*       sqnl(0.0) = 0.0
*
* % java ActivationFunction 1.0
*   heaviside(1.0) = 1.0
*     sigmoid(1.0) = 0.7310585786300049
*       tanh(1.0) = 0.7615941559557649
*     softsign(1.0) = 0.5
*       sqnl(1.0) = 0.75
*
***************************************************************************/
public class ActivationFunction {

  public static double heaviside(double x) {
    if (x < 0.0) return 0; 
    if (x > 0.0) return 1; 
    else return 0.5; 
  }

  public static double sigmoid(double x) {
    return 1 / (1 + Math.exp(-1*x)); 
  }

  public static double tanh(double x) {
    return (Math.exp(x) - Math.exp(-1*x)) / (Math.exp(x) + Math.exp(-1*x)); 
  }

  public static double softsign(double x) {
    return x / (1 + Math.abs(x)); 
  }

  public static double sqnl(double x) {
    if (x<=-2) return -1;
    else if (x<0) return (x + x*x/4); 
    else if (x<2) return (x - x*x/4); 
    else return 1;
  }

  public static void main(String[] args) {
    double x = Double.parseDouble(args[0]); 
    System.out.printf("%17s", "heaviside("+x+") = ");
    System.out.print(heaviside(x)+"\n");
    System.out.printf("%17s", "sigmoid("+x+") = ");
    System.out.print(sigmoid(x)+"\n");
    System.out.printf("%17s", "tanh("+x+") = ");
    System.out.print(tanh(x)+"\n");
    System.out.printf("%17s", "softsign("+x+") = ");
    System.out.print(softsign(x)+"\n");
    System.out.printf("%17s", "sqnl("+x+") = ");
    System.out.print(sqnl(x)+"\n");
  }
}

