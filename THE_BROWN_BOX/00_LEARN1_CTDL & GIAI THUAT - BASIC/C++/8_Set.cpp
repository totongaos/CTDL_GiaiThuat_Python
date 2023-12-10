#include <iostream>
#include <set>
using namespace std;

int main()
{
    //Tao 1 set kieu int
    set<int> mySet;

    //2. add cac value vao set moi tao
    mySet.insert(1);
    mySet.insert(2);
    mySet.insert(3);
    mySet.insert(1);

    //In size of mySet
    cout << "mySet: " << mySet.size()<< endl;
    //Duyet cac p.tu trong mySet
    for (auto it = mySet.begin(); it != mySet.end(); it++)
    {
        cout << (*it) << " ";
    }
    return 0;
}
