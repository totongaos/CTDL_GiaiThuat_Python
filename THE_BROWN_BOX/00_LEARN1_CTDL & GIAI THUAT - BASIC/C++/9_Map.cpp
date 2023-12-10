#include <iostream>
#include <map>
using namespace std;

int main()
{
    //Tao 1 map kieu key=int ; value=string
    map<int,string> myMap;

    //2. add cac value vao myMap moi tao
    myMap[111] = "Tran Van A";
    myMap[222] = "Nguyen Van A";
    myMap[333] = "Ho Thi A";

    //In size of myMap
    cout << "myMap: " << myMap.size()<< endl;
    //Duyet cac p.tu trong myMap
    for (auto it = myMap.begin(); it != myMap.end(); it++)
    {
        cout << it->first << " : " << it->second << endl;
    }
    return 0;
}
