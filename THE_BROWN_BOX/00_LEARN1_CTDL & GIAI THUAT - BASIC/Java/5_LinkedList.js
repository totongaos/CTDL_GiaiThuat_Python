public class LinkedListInJava {
    public static class ListNode{
        int val; // mang g.tri value ma minh muon the hien
        ListNode next; //con tro next
        ListNode() { } //1. Ham tao defaut
        //2. Ham co tham so val
        ListNode(int val){
            this.val = val;
        }
    }

    public static void main(String[] args) {
        //Tao ra 3 node
        ListNode n1 = new ListNode(1);
        ListNode n2 = new ListNode(2);
        ListNode n3 = new ListNode(3);

        //noi cac node lai voi nhau
        n1.next = n2;
        n2.next = n3;

        System.out.print("Linked List: ");
        //duyet cac p.tu trong linked list
        ListNode pHead = n1;
        while(pHead != null){
            System.out.print(pHead.val + " ");
            pHead=pHead.next;
        }
    }
}