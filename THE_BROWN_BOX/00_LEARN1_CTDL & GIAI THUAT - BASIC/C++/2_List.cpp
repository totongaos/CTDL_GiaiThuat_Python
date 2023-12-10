#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> myList; //value type is storage in stack
    myList.push_back(1);
    myList.push_back(2);
    myList.push_back(3);

    for (int i=0; i < myList.size(); i++){
        cout << myList[i] <<" ";
    }
    return 0;

}
