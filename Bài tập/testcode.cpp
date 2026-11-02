#include <iostream>
using namespace std;
template <typename T>
class Matrix {
private:
    int n;       
    T* data;     
    void alloc(int sz) {
        n = sz;
        if (n > 0) { data = new T[n * n]; } 
        else { data = nullptr;
        }
    }
    void del() {
        if (data != nullptr) {
            delete[] data;
            data = nullptr;
        }
    }
public:
    Matrix(int size = 0) {
        alloc(size);
    }
    Matrix(const Matrix& b) {
        alloc(b.n);
        for (int i = 0; i < n * n; ++i) {
            data[i] = b.data[i];
        }
    }
    ~Matrix() {
        del();
    }
    Matrix& operator=(const Matrix& b) {
        if (this != &b) {
            del();
            alloc(b.n);
            for (int i = 0; i < n * n; ++i) {
                data[i] = b.data[i];
            }
        }
        return *this;
    }
    T& operator()(int r, int c) {
        return data[r * n + c];
    }
    const T& operator()(int r, int c) const {
        return data[r * n + c];
    }
    Matrix operator+(const Matrix& b) const {
        Matrix res(n);
        for (int i = 0; i < n * n; ++i) {
            res.data[i] = this->data[i] + b.data[i];
        }
        return res;
    }
    Matrix operator-(const Matrix& b) const {
        Matrix res(n);
        for (int i = 0; i < n * n; ++i) {
            res.data[i] = this->data[i] - b.data[i];
        }
        return res;
    }
    Matrix operator*(const Matrix& b) const {
        Matrix res(n);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                res(i, j) = 0; 
                for (int k = 0; k < n; ++k) {
                    res(i, j) += (*this)(i, k) * b(k, j);
                }
            }
        }
        return res;
    }
    friend istream& operator>>(istream& is, Matrix<T>& m) {
        for (int i = 0; i < m.n * m.n; ++i) {
            is >> m.data[i];
        }
        return is;
    }
    friend ostream& operator<<(ostream& os, const Matrix<T>& m) {
        for (int i = 0; i < m.n; ++i) {
            for (int j = 0; j < m.n; ++j) {
                os << m(i, j) << "\t";
            }
            os << "\n";
        }
        return os;
    }
};

int main() {
    int n;
    cout<<"Nhap n: "; cin>>n;
    Matrix<int> a(n),b(n);
    cout<<"Nhap ma tran 1:\n";
    cin>>a;
    cout<<"Nhap ma tran 2:\n";
    cin>>b;

    cout<<"\nA:\n"<<a;
    cout<<"\nB:\n"<<b;
    Matrix<int> c=a+b;
    cout<<"\nA+B:\n"<<c;
    Matrix<int> d=a-b;
    cout<<"\nA-B:\n"<<d;
    Matrix<int> e=a*b;
    cout<<"\nA*B:\n"<<e;

    cout<<"\nA[0][0] = "<<a(0,0)<<endl;
    a(0,0)=999;
    cout<<"A sau khi sua:\n"<<a;
    return 0;
}