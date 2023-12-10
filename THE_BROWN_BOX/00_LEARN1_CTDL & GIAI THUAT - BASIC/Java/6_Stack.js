import java.util.Stack;
public class StackInJava {
    public static void main(String[] args) {
        //Tao 1 stack kieu int
        Stack<Integer> myStack = new Stack<>();

        //2. add cac value vao stack moi tao
        myStack.add(1);
        myStack.add(2);
        myStack.add(3);

        System.out.print("myStack: ");
        while(!myStack.isEmpty()){
            System.out.print(myStack.peek()+ " "); //ktra p.tu cuoi cua stack la value nao
            myStack.pop(); //loai bo p.tu cuoi
        }

    }
}
