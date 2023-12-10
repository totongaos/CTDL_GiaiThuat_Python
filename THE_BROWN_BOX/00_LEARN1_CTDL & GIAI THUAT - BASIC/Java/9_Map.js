import java.util.HashMap;
import java.util.Map;
public class MapInJava {
    public static void main(String[] args) {
        //Tao 1 map kieu key=int ; value=string
        Map<Integer, String> myMap = new HashMap<>();

        //2. add cac value vao myMap moi tao
        myMap.put(111,"Tran Van A");
        myMap.put(222,"Nguyen Van A");
        myMap.put(333,"Ho Thi A");

        //In size of myMap
        System.out.print("size: " + myMap.size() + " ");
        //Duyet cac p.tu trong myMap
        for (var item : myMap.entrySet())
        {
            System.out.print(item.getKey() + " : " + item.getValue());
        }

    }
}
