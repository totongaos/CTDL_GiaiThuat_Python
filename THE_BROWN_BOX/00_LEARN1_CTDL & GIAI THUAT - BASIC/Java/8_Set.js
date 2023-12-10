import java.util.HashSet;
import java.util.Set;
public class SetInJava {
    public static void main(String[] args) {
        //Tao 1 set kieu int
        Set<Integer> mySet = new HashSet<>();

        //2. add cac value vao set moi tao
        mySet.add(1);
        mySet.add(2);
        mySet.add(3);
        mySet.add(1);

        //In size of mySet
        System.out.print("mySet: " + mySet.size() + " ");
        //Duyet cac p.tu trong mySet
        for (Integer integer:mySet)
        {
            System.out.print(integer + " ");
        }

    }
}
