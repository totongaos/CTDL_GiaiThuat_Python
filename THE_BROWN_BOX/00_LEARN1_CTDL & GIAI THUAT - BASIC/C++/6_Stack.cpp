#include <iostream>
#include <stack>
using namespace std;

int main()
{
    //Tao 1 stack kieu int
    stack<int> myStack;

    //2. add cac value vao stack moi tao
    myStack.push(1);
    myStack.push(2);
    myStack.push(3);

    cout << "myStack: ";
    while(!myStack.empty()){
        cout << myStack.top() << " "; //ktra p.tu cuoi cua stack la value nao
        myStack.pop(); //loai bo p.tu cuoi
    }
}

