public class Dinosaur extends Reptile implements Herbivore {
  public void roar(){
		System.out.println("Roar!");
	}

  public void food() {
    System.out.println("Herbivore");
  }

  @Override
	public void eat(){
		System.out.println("That tree was delicious!");
	}
}
