/*
*   By Deven Maheshwari, Chloe Liu, Gavin Mcginley, Alex Garcia, Oscar Fishman
*    
*   Compilation: javac BiasedCoin.java
*
*/ 

public class BiasedCoin extends Coin{
    public double chance; 

    public BiasedCoin(double x) {
        chance = x; 
    }

    public String flip() {
        if (Math.random() < chance) return "H";
        else return "T"; 
    } 
}
