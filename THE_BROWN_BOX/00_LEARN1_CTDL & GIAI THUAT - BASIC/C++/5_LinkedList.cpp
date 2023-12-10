#include <iostream>
using namespace std;

struct ListNode
{
    int val; // mang g.tri value ma minh muon the hien
    ListNode* next; //con tro next
    //1. Ham tao ko co tham so
    ListNode()
    {
        val = 0;
        next = nullptr;
    }
    //2. Ham tao cos tham so minh muon truyen vao
    ListNode(int x)
    {
        val = x;
        next = nullptr;
    }
};
int main()
{
    //Tao ra 3 node
    ListNode* n1 = new ListNode(1);
    ListNode* n2 = new ListNode(2);
    ListNode* n3 = new ListNode(3);

    //noi cac node lai voi nhau
    n1->next = n2;
    n2->next = n3;

    cout<< "Linked List: ";
    //duyet cac p.tu trong linked list
    ListNode* pHead = n1;
    while(pHead != nullptr){
        cout<< pHead->val <<" ";
        pHead=pHead->next;
    }
		//vi sd toan tu new nen can delete no di
    delete n1;
    delete n2;
    delete n3;
}