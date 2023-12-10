#include <iostream>
#include <queue>
using namespace std;

int main()
{
    //Tao 1 queue kieu int
    queue<int> myQueue;

    //2. add cac value vao queue moi tao
    myQueue.push(1);
    myQueue.push(2);
    myQueue.push(3);

    cout << "myQueue: ";
    while(!myQueue.empty()){
        cout << myQueue.front() << " "; //ktra p.tu dau cua queue la value nao
        myQueue.pop(); //loai bo p.tu dau
    }
}

