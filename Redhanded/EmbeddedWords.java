/*
    By Deven Maheshwari

    Compilation: javac EmbeddedWords.java 
    Execution: java EmbeddedWords str

    Finds the embedded words within a given string.
*/
public class EmbeddedWords {
    public static void main(String args[]){
        In file = new In("words.utf-8.txt");
        String test = args[0];
        while (!file.isEmpty() ) {
            String help = file.readString();
            int index = 0;
            for (int i = 0,k = 0; i<help.length()&&k<test.length(); k++) {
                if (help.substring(i, i+1).equals(test.substring(k, k+1))) {
                    index++; 
                    i += 1;
                }
            }
            if (index == help.length()) {
                System.out.println(help);
            }
        }
    }
}

