#include <iostream>
using namespace std;
struct NgayThang{
    int ngay, thang, nam;
};
bool laNamNhuan(int nam){
    return (nam%4==0 && nam%100!=0) || (nam%400==0);
}
int soNgayToiDaTrongThang(int thang, int nam){
    switch(thang){
        case 4 : case 6 : case 9 : case 11 : return 30;
        case 2 : return laNamNhuan(nam) ? 29 : 28;
        default : return 31;
    }
}
NgayThang& operator ++ (NgayThang& dt){
    dt.ngay++;
    if(dt.ngay > soNgayToiDaTrongThang(dt.thang, dt.nam)){
        dt.ngay = 1;
        dt.thang++;
        if(dt.thang > 12){
            dt.thang = 1;
            dt.nam++;
        }
    }
    return dt;
}

void inNgay(const NgayThang& d){
    cout << d.ngay << "/" << d.thang << "/" << d.nam;
}
int main(){
    NgayThang dt;
    cout << "Nhap ngay thang nam: " << endl;
    cin >> dt.ngay >> dt.thang >> dt.nam;
    cout << "Ngay vua nhap la: "<<endl;
    inNgay(dt);
    cout << endl;
    ++dt;
    cout << "Ngay tiep theo la: "<<endl;
    inNgay(dt);
}
