#include <iostream>
#include <algorithm> //de sd ham sorting san trong thu vien
#include <vector>

using namespace std;

int main(){
    int arr[] = {3,2,1};

    //sorting array
    int size = sizeof(arr) / sizeof(int);
    sort(arr, arr + size); //ham sort truyen address head & tail
    cout << "arr: ";
    for (int i=0; i<size; i++){
        cout << arr[i] << " ";
    }
    cout << endl;

    //sorting vector
    vector<int> list(arr, arr+size);
    sort(list.begin(), list.end());
    cout << "list: ";
    for (int i=0; i<list.size(); i++){
        cout << list[i]<< " ";
    }
}