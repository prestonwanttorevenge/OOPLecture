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
ostream& operator << (ostream& out, const Complex c) {
    out << "(" << c.R << "," << c.I << ")";
    return out;
}
Complex operator + (const Complex& c1, const Complex& c2) {
    Complex c;
    c.R = c1.R + c2.R;
    c.I = c1.I + c2.I;
    return c;
}
int main(){
    Complex c1, c2;
    cout << "Nhập số phức c1: "<<endl;
    cin >>c1;
    cout << "Nhập số phức c2: "s<<endl;
    cin >>c2;
    cout << "Số phức c1: " << c1 << endl;
    cout << "Số phức c2: " << c2 << endl;
    cout << "Tổng hai số phức: " << c1 + c2 << endl;

}