/*
*   By Gavin Mcginley, Chloe Liu, Deven Maheshwari, Alex Garcia, Oscar Fishman
*   
*   Compilation: javac -cp .:../stdlib.jar MorseCode.java
*   Execution: java -cp .:../stdlib.jar MorseCode
*   Dependencies: StdIn.java, In.java
*
*   Translates between morsecode and english. 
*/

import java.util.Map;
import java.util.HashMap;

public class MorseCode {
    public static void main(String[] args) {
        In in = new In("morse.txt");
	    Map <String,String> translator = new HashMap<String,String>();
        Map <String,String> translator2 = new HashMap<String,String>();
        while (!in.isEmpty()){
            String line = in.readLine();
            if (!line.isEmpty()) {
                String english = line.substring(0,2); 
                english = english.trim(); 
                String code = line.substring(2); 
                code = code.trim(); 
                translator.put(english,code);
                translator2.put(code,english);
                
            }
        }

        while (!StdIn.isEmpty()) {
            String read = StdIn.readString();
            char[] helper = read.toCharArray();
            String[] helper2 = read.split(" ");  
            if (read.equals("-1")) break;
            if (Character.isLetter(helper[0])) {
                for (int i = 0; i < helper.length; i++) {
                    if (Character.isLetter(helper[i])) {
                        System.out.print(translator.get(String.valueOf(helper[i]))); 
                    }   
                }
            }
            else if (helper[0] == '-' || helper[0] == '.') {
                for (int i = 0; i < helper2.length; i++) {
                    System.out.print(translator2.get(String.valueOf(helper2[i]))); 
                }
            }
        }
    }
}

