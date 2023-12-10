public class ArrayJava {
    public static void main(String[] args) {
        //KHAI bao ARRAY TINH
        int[] arr = {1,2,3};
        //Voi Java k can q.ly so luong p.tu
        System.out.print("arr: ");
        for (int i=0; i< arr.length; i++){
            System.out.print(arr[i] + " ");
        }
        System.out.println();

        //KHAI BAO ARRAY DONG
        int[] pArr = new int[3]; //value ban dau luon = 0 -> ko can memset nhu C++
        //Voi Java k can q.ly so luong p.tu
        System.out.print("pArr: ");
        for (int i=0; i<pArr.length; i++){
            System.out.print(pArr[i] + " ");

        }
    }
}