import java.util.LinkedList;
import java.util.Queue;
public class QueueInJava {
    public static void main(String[] args) {
        //Tao 1 Queue kieu int
        Queue<Integer> myQueue = new LinkedList<>();

        //2. add cac value vao Queue moi tao
        myQueue.add(1);
        myQueue.add(2);
        myQueue.add(3);

        System.out.print("myQueue: ");
        while(!myQueue.isEmpty()){
            System.out.print(myQueue.peek()+ " "); //ktra p.tu dau cua Queue la value nao
            myQueue.remove(); //loai bo p.tu dau
        }

    }
}
