#include <iostream>
#include <string>
using namespace std;

template<class T>
class IntArray {
private:
    T* p;
    int n;
public:
    IntArray() { n=0; p=nullptr; }

    IntArray(int sl) {
        n=sl > 0 ? sl : 0;
        p = n ? new T[n]() : nullptr;
    }

    IntArray(const T a[], int sl) {
        n=sl > 0 ? sl : 0;
        p = n ? new T[n] : nullptr;
        for(int i=0;i<n;i++) p[i]=a[i];
    }

    IntArray(const IntArray<T>& a) {
        n=a.n;
        p = n ? new T[n] : nullptr;
        for(int i=0;i<n;i++) p[i]=a.p[i];
    }

    ~IntArray() { delete[] p; }

    IntArray<T>& operator=(const IntArray<T>& a) {
        if(this!=&a) {
            T* q = a.n ? new T[a.n] : nullptr;
            for(int i=0;i<a.n;i++) q[i]=a.p[i];
            delete[] p;
            p=q;
            n=a.n;
        }
        return *this;
    }

    T& operator[](int i) { return p[i]; }
    const T& operator[](int i) const { return p[i]; }

    int operator()(const T& x) const {
        for(int i=0;i<n;i++) if(p[i]==x) return i;
        return -1;
    }

    void sapxep(bool tang=true) {
        for(int i=0;i<n-1;i++)
            for(int j=i+1;j<n;j++)
                if(tang ? p[j]<p[i] : p[j]>p[i]) {
                    T x=p[i]; p[i]=p[j]; p[j]=x;
                }
    }

    friend ostream& operator<<(ostream& os, const IntArray<T>& a) {
        for(int i=0;i<a.n;i++) os<<a.p[i]<<"\n";
        return os;
    }

    friend istream& operator>>(istream& is, IntArray<T>& a) {
        for(int i=0;i<a.n;i++) is>>a.p[i];
        return is;
    }
};

class HS {
private:
    string ten, ns;
    float toan, ly, hoa, tb;
public:
    HS() { ten=""; ns=""; toan=ly=hoa=tb=0; }
    HS(string t) { ten=t; ns=""; toan=ly=hoa=tb=0; }

    float diem() const { return tb; }

    bool operator<(const HS& h) const { return tb<h.tb; }
    bool operator>(const HS& h) const { return tb>h.tb; }
    bool operator==(const HS& h) const { return ten==h.ten; }

    friend istream& operator>>(istream& is, HS& h) {
        cout<<"Ten: ";
        is>>ws;
        getline(is,h.ten);
        cout<<"Ngay sinh: ";
        getline(is,h.ns);
        cout<<"Diem Toan Ly Hoa: ";
        is>>h.toan>>h.ly>>h.hoa;
        h.tb=(h.toan+h.ly+h.hoa)/3;
        return is;
    }

    friend ostream& operator<<(ostream& os, const HS& h) {
        os<<"Ten: "<<h.ten<<" | NS: "<<h.ns
          <<" | Toan: "<<h.toan<<" Ly: "<<h.ly<<" Hoa: "<<h.hoa
          <<" | TB: "<<h.tb;
        return os;
    }
};

int main() {
    int n;
    cout<<"So hoc sinh: ";
    cin>>n;
    if(n<0) { cout<<"So luong khong hop le\n"; return 0; }

    IntArray<HS> ds(n);
    cout<<"Nhap ds:\n";
    cin>>ds;
    cout<<"\nDanh sach:\n"<<ds;

    int k;
    cout<<"\n1 tang, 2 giam: ";
    cin>>k;
    IntArray<HS> sx(ds);
    sx.sapxep(k==1);
    cout<<"\nDa sap xep:\n"<<sx;

    string ten;
    cout<<"\nTim ten: ";
    cin>>ws;
    getline(cin,ten);
    int vt=sx(HS(ten));
    if(vt<0) cout<<"Khong thay\n";
    else cout<<"Tim thay: "<<sx[vt]<<"\n";
    return 0;
}
