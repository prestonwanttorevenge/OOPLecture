/*Cài đặt struct Complex biểu diễn số phức gồm phần thực và phần ảo
Định nghĩa phép toán >>, << để nhập, xuất số phức
Phép toán +,-,*,/,<,>,!=,== của hai số phức
Hàm tính Modulo số phức
*/
#include <iostream>
#include <cmath>
using namespace std;
struct Complex {
    double R, I;
};
istream& operator >> (istream& in, Complex& c) {
    cout << "Phần thực: "; in>>c.R;
    cout << "Phần ảo: "; in>>c.I;
    return in;
}
int main(){
    Complex C1, C2;
    cout << "Nhập số phức C1: ";<<endl;
    cin >>C1;
}