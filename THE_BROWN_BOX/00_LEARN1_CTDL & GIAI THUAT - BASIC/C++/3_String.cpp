#include <iostream>
#include <string>

using namespace std;

int main()
{
    string str = "hello word";

    for (int i=0; i < str.size(); i++){
        if(i%2 == 0){
            str[i] = '_';
        }
    }
    cout << "str: " << str;
    return 0;
}