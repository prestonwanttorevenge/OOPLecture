#include <iostream>
#include <string>

using namespace std;

// ================= LỚP CƠ SỞ =================
class PhuongTien {
protected:
    string maPT;
    string tenPT;
    double giaBan;

public:
    PhuongTien() {
        maPT = "";
        tenPT = "";
        giaBan = 0.0;
    }

    PhuongTien(string ma, string ten, double gia) {
        maPT = ma;
        tenPT = ten;
        giaBan = gia;
    }

    // Bắt buộc phải có virtual ở destructor và các phương thức này!
    virtual ~PhuongTien() {}

    virtual void nhap() {
        cout << "Nhap ma phuong tien: ";
        getline(cin, maPT);
        cout << "Nhap ten phuong tien: ";
        getline(cin, tenPT);
        cout << "Nhap gia ban: ";
        cin >> giaBan;
        cin.ignore();
    }

    virtual void xuat() {
        cout << "Ma: " << maPT << " | Ten: " << tenPT << " | Gia: " << giaBan;
    }

    double getGiaBan() {
        return giaBan;
    }
};

// ================= LỚP DẪN XUẤT 1 =================
class XeOto : public PhuongTien {
private:
    int soChoNgoi;
    string kieuDongCo;

public:
    XeOto() : PhuongTien() {
        soChoNgoi = 0;
        kieuDongCo = "";
    }

    XeOto(string ma, string ten, double gia, int soCho, string dongCo) 
        : PhuongTien(ma, ten, gia) {
        soChoNgoi = soCho;
        kieuDongCo = dongCo;
    }

    void nhap() override {
        cout << "--- NHAP THONG TIN O TO ---\n";
        PhuongTien::nhap();
        cout << "Nhap so cho ngoi: ";
        cin >> soChoNgoi;
        cin.ignore();
        cout << "Nhap kieu dong co (Xang/Dau/Dien): ";
        getline(cin, kieuDongCo);
    }

    void xuat() override {
        cout << "[O to] ";
        PhuongTien::xuat();
        cout << " | So cho: " << soChoNgoi << " | Dong co: " << kieuDongCo << endl;
    }
};

// ================= LỚP DẪN XUẤT 2 =================
class XeMay : public PhuongTien {
private:
    double dungTich;
    string loaiXe; 

public:
    XeMay() : PhuongTien() {
        dungTich = 0.0;
        loaiXe = "";
    }

    XeMay(string ma, string ten, double gia, double dt, string loai) 
        : PhuongTien(ma, ten, gia) {
        dungTich = dt;
        loaiXe = loai;
    }

    void nhap() override {
        cout << "--- NHAP THONG TIN XE MAY ---\n";
        PhuongTien::nhap();
        cout << "Nhap dung tich (cc): ";
        cin >> dungTich;
        cin.ignore();
        cout << "Nhap loai xe (So/Tay ga): ";
        getline(cin, loaiXe);
    }

    void xuat() override {
        cout << "[Xe may] ";
        PhuongTien::xuat();
        cout << " | Dung tich: " << dungTich << "cc | Loai: " << loaiXe << endl;
    }
};

// ================= HÀM MAIN =================
int main() {
    PhuongTien* danhSach[100];
    int soLuong = 0;
    int luaChon;

    do {
        cout << "\n========== QUAN LY PHUONG TIEN ==========\n";
        cout << "1. Nhap them phuong tien vao danh sach\n";
        cout << "2. Xuat toan bo danh sach\n";
        cout << "3. Tim phuong tien co gia ban cao nhat\n";
        cout << "4. Thoat chuong trinh\n";
        cout << "Chon chuc nang (1-4): ";
        cin >> luaChon;
        cin.ignore();

        if (luaChon == 1) {
            int loai;
            cout << "Chon loai xe muon nhap (1 - O to, 2 - Xe may): ";
            cin >> loai;
            cin.ignore();

            if (loai == 1) {
                danhSach[soLuong] = new XeOto();
                danhSach[soLuong]->nhap();
                soLuong++;
                cout << "-> Da them O to thanh cong!\n";
            } 
            else if (loai == 2) {
                danhSach[soLuong] = new XeMay();
                danhSach[soLuong]->nhap();
                soLuong++;
                cout << "-> Da them Xe may thanh cong!\n";
            } 
            else {
                cout << "Loai xe khong hop le!\n";
            }
        } 
        else if (luaChon == 2) {
            if (soLuong == 0) {
                cout << "Danh sach hien tai dang trong!\n";
            } else {
                cout << "\n--- DANH SACH PHUONG TIEN ---\n";
                for (int i = 0; i < soLuong; i++) {
                    cout << i + 1 << ". ";
                    danhSach[i]->xuat(); 
                }
            }
        } 
        else if (luaChon == 3) {
            if (soLuong == 0) {
                cout << "Danh sach trong, khong co xe nao de tim!\n";
            } else {
                int viTriMax = 0;
                for (int i = 1; i < soLuong; i++) {
                    if (danhSach[i]->getGiaBan() > danhSach[viTriMax]->getGiaBan()) {
                        viTriMax = i;
                    }
                }
                cout << "\n--- PHUONG TIEN CO GIA CAO NHAT ---\n";
                danhSach[viTriMax]->xuat();
            }
        } 
        else if (luaChon == 4) {
            cout << "Thoat chuong trinh.\n";
        } 
        else {
            cout << "Lua chon khong hop le, vui long chon lai!\n";
        }

    } while (luaChon != 4);

    for (int i = 0; i < soLuong; i++) {
        delete danhSach[i];
    }

    return 0;
}