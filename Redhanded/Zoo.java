public class Zoo {
  public static void main(String[] args) {
    Cat myCat = new Cat();
    myCat.setName("Betty");
    myCat.printName();
    myCat.eat();
    myCat.birth();
    myCat.food();
    myCat.identity();
    System.out.println();

    Dinosaur myDino = new Dinosaur();
    myDino.setName("Pho");
    myDino.printName();
    myDino.eat();
    myDino.birth();
    myDino.food();
    myDino.identity(); 
    System.out.println();
  }
}
