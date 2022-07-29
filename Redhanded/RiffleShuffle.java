/***********************************************************************************************
*  By Deven Maheshwari
*
* Compilation: javac -classpath .:stdlib.jar RiffleShuffle.java
* Execution: java -classpath .:stdlib.jar RiffleShuffle n
*
* Represents the shuffling of a deck using the Gilbert-Shannon-Reeds model of a "riffle-shuffle." (https://www.youtube.com/watch?v=AxJubaijQbI)
*
*
* % java -classpath .:stdlib.jar RiffleShuffle  4
  4
          1         0         2         3 
*
*
*
*****************************************************************************/

class RiffleShuffle {

   public static int coin(int x) {
    int heads = 0;
    for (int j = 0; j < x; j++) {
      if ( StdRandom.bernoulli() ) heads++;
    }
    return heads; 
  }

  public static int[] riffleShuffle(int[] newcards, int[] n1, int[] n2) {
    int l1 = n1.length;
    int l2 = n2.length; 
    int total = l1 + l2;
    int k1 = 0;
    int k2 = 0; 

    for (int i = 0; i < total; i++) {
      double help = (double) total; 
      if ( StdRandom.bernoulli(l1 / help) ) { 
        newcards[i] = n1[k1]; 
        l1 -= 1; 
        ++k1; 
      } 
      if ( StdRandom.bernoulli(l2 / help) ) {
        newcards[i] = n2[k2]; 
        l2 -= 1;  
        ++k2; 
      }
      help = help - 1.0; 
    }
    return newcards; 
  }

  public static void main(String[] args) {

    int n = Integer.parseInt(args[0]); 
    int r = coin(n);

    int[] cards = new int[n]; 
    for (int i = 0; i < n; i++) {
      cards[i] = i; 
    }

    int[] deck1 = new int[r];
    for (int i = 0; i < r; i++) {
      deck1[i] = cards[i]; 
    }
    int[] deck2 = new int[n-r]; 
    for (int i = 0; i < n-r; i++) {
      deck2[i] = cards[i]+r; 
    }

    int[] finaldeck = riffleShuffle(cards, deck1, deck2); 
    StdArrayIO.print(finaldeck); 
  }

}



