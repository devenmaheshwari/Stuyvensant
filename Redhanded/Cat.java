public class Cat extends Mammal implements Carnivore {
  public void meow(){
		System.out.println("Meow!");
	}

  public void food() {
    System.out.println("Carnivore");
  }

  @Override
	public void eat(){
		System.out.println("That mouse was delicious!");
	}
}
