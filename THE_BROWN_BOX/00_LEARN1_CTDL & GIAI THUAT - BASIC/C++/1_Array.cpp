#include <iostream>
#include <cstring> //thu vin cua memset
using namespace std;

int main()
{
    // khai bao mang tinh (vung cap phat nho stack)
    int arr[] = {1,2,3};
    int size = sizeof(arr)/sizeof(int); //q.ly so luong p.tu
    cout << "arr: ";
    for (int i=0; i<size; i++) //xai for duyet cac p.tu trong array
    {
        cout << arr[i] << " ";
    }
    cout << endl;


    // khai bao mang dong (vung cap phat nho heep)
    int *pArr = new int[3]; //dung toan tu new
    int pSize = 3; //q.ly so luong p.tu
		//chon 1 vung nho de cap phat (memset dong bo all cac vung nho ve 0)
    memset(pArr, 0x00, pSize * sizeof(int));
    cout << "pArr: ";
    for (int i=0; i<pSize; i++) //xai for duyet cac p.tu trong array
    {
        cout << pArr[i] << " ";
    }
    cout << endl;
    delete[] pArr;
    return 0;
}