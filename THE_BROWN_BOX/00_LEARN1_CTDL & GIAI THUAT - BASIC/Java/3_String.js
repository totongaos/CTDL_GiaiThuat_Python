public class StringInJava {
    public static void main(String[] args) {
    String str = "hello word"; //NOTE: String ko the thay doi dc cac p.tu ben trong no
    String res = "";

    for (int i=0; i < str.length(); i++){
        if(i%2 == 0){
            res += "_";
        }else{
            res += str.charAt(i);
        }
    }
    System.out.println("result: " + res);
    }
}