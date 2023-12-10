import java.util.List;
public class ListInJava {
    public static void main(String[] args) {
        List<Integer> myList = new ArrayList<>();
        //KHAI bao ARRAY TINH
        myList.add(1);
        myList.add(2);
        myList.add(3);

        for (int i=0; i< myList.size(); i++){
            System.out.print(myList.get(i) + " ");
        }
        }
    }
}