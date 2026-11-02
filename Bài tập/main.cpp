#include <iostream>
#include "Vector.h"
using namespace std;
int main(){
    cout << "CHUONG TRINH VECTOR" << endl;
    Vector v1;
    cout << "Nhap toa do vector v1 tu ban phim" << endl;
    cin >> v1;
    Vector v2;
    cout << "Nhap toa do vector v2 tu ban phim" << endl;
    cin >> v2;
    cout << "Vector v1 = " << v1 << endl;
    cout << "Vector v2 = " << v2 << endl;
    if (v1.GetDim() > 0) {
        cout << "\nTRUY XUAT TOA DO" << endl;
        cout << "Toa do dau tien v1[0] hien tai = " << v1[0] << endl;

        v1[0] = 3;
        cout << "Sau khi gan v1[0] = 3: v1 = " << v1 << endl;
    }
    Vector v3 = v1;
    cout << "\nVector v3 sao chep tu v1 la = " << v3 << endl;
    if (v1.GetDim() == v2.GetDim()){
        Vector sum = v1 + v2;
        Vector dif = v1 - v2;
        double dotp = v1 * v2;
        cout << "Tong hai vector la: " << sum << endl;
        cout << "Hieu hai vector la: " << dif << endl;
        cout << "Tich vo huong hai vector la: " << dotp << endl;
    } else {
        cout << "Hai vecto khac so chieu! Dung chuong trinh " << endl;
    }
    return 0;
}