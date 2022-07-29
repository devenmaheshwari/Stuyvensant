/*
*   By Deven Maheshwari
*
*   Compilation: javac -cp .:../stdlib.jar FindAreaCode.java 
*   Execution: java -cp .:../stdlib.jar FindAreaCode
*   Dependencies: phone-na.csv, In.java, StdIn.java
*
*   Reads a file of telephone area codes and geographical areas and tells the user telephone codes given a state/province and vice-versa. 
*
*
*/

import java.util.Map;
import java.util.TreeMap;

public class FindAreaCode {
    public static void main(String[] args) {
        In in = new In("phone-na.csv");
	    Map <Integer,String> areaCode = new TreeMap<Integer,String>();
        while (!in.isEmpty()){
            String line = in.readLine();
            String[] helper = line.split(",");
            try {
                int code = Integer.parseInt(helper[0]); 
                String city = helper[2]; 
                areaCode.put(code,city);
            }
            catch (Exception e){
            }
        }

        while (true) {
            System.out.print("Enter area code or state name: ");
            String read = StdIn.readLine();
            if (read.equals("-1")) break;
            try {
                if (areaCode.containsValue(read)) {
                    for (int s1: areaCode.keySet()) {
                        if (areaCode.get(s1).equals(read)) System.out.println(s1); 
                    }
                }
                else if (areaCode.containsKey(Integer.parseInt(read))) System.out.println(areaCode.get(Integer.parseInt(read)));
                else System.out.println("There is no such area code");
            }
            catch (Exception e) {
                System.out.println("There is no such area code");
            } 
        }
    }
}
