import java.util.ArrayList;
import java.util.Arrays;

public class SortingInJava {
    public static void main(String[] args) {
    //Java sorting array
		int[] arr = {3,2,1};
    Arrays.sort(arr);
    System.out.print("arr: ");
    for (int i=0; i<arr.length; i++){
        System.out.print(arr[i]+" ");
    }
    System.out.println();
    }
}

//---------------------------------------------
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class SortingInJava {
    public static void main(String[] args) {
    //Java sorting list
		System.out.print("list: ");
    List<Integer> list = new ArrayList<>(List.of(3,2,1));
    Collections.sort(list);
    for (int i=0; i<list.size(); i++){
        System.out.print(list.get(i)+" ");
    }
    }
}