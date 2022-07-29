public abstract class Animal {
  private String name;

  public void setName(String name){
		this.name = name;
	}

  public void printName(){
		System.out.println("My name is: " + name);
	}

  public void eat(){
		System.out.println("munch munch");
	}

  @Override
	public String toString(){
		return "I'm an animal! My name is " + name + "!";
	}
}
