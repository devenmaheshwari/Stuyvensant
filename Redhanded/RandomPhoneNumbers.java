/*
*   By Deven Maheshwari
*
*   Compilation: javac RandomPhoneNumbers.java 
*   Execution: java RandomPhoneNumbers n
*   Dependencies: Stdin.java, In.java, phone-na.csv
*
*   Takes a command line argument, n, and prints out n unique phonenumbers using area codes from phone-na.csv. 
*   
*/

import java.util.*; 

public class RandomPhoneNumbers {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]); 
        Set<String> area = new HashSet<String>();
        In in = new In("phone-na.csv");
        while (!in.isEmpty()) {
            String line = in.readLine();
            String[] helper = line.split(",");
            if (!helper[0].equals("AREA CODE")) {
                area.add(helper[0]); 
            }
        }

        Object[] helper = area.toArray(); 
        Set<String> phones = new HashSet<String>();

        while (phones.size() < n) {
            String answer = ""; 
            int pos = (int) (Math.random() * helper.length); 
            answer += "(" + helper[pos] + ") "; 
            answer += (int) (Math.random() * 10); 
            answer += (int) (Math.random() * 10); 
            answer += (int) (Math.random() * 10); 
            answer += "-"; 
            answer += (int) (Math.random() * 10); 
            answer += (int) (Math.random() * 10); 
            answer += (int) (Math.random() * 10); 
            phones.add(answer); 
        }
        for (String s1: phones) {
            System.out.println(s1); 
        }
        
    }
}