/*
*   By Deven Maheshwari, Chloe Liu, Gavin Mcginley, Alex Garcia, Oscar Fishman
*    
*   Compilation: javac Coin.java
*
*/ 

public class Coin implements Flippable {
    public String flip() {
        if (Math.random() < 0.5) return "H";
        else return "T"; 
    } 
}
