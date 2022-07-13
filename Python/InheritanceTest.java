// super class
class Fruit
{
    public Fruit()
    {
        System.out.println("Super class constructor");
        System.out.println("Super class object hashcode :" +
                           this.hashCode());
        System.out.println(this.getClass().getName()); // this is also an apple! the only thing this program does is creating one apple
    }
}
  
// sub class
class Apple extends Fruit
{
    public Apple()
    {
        System.out.println("Subclass constructor invoked");
        System.out.println("Sub class object hashcode :" +
                           this.hashCode());
        System.out.println(this.hashCode() + "   " +
                           super.hashCode());
  
        System.out.println(this.getClass().getName() + "  " +
                           super.getClass().getName());
    }
}
  
// driver class
public class InheritanceTest
{
    public static void main(String[] args)
    {
        Apple myApple = new Apple();
    }
}

