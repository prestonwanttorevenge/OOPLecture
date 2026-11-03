#include <iostream>
#include <string>
#include <exception>
#include <limits>
using namespace std;

class MatrixException : public exception {
    const char* loi;
public:
    MatrixException(const char* s) { loi = s; }
    const char* what() const noexcept { return loi; }
};

template <typename T>
class Matrix {
private:
    int n;       
    T* data;     
    void alloc(int sz) {
        if (sz < 0) throw MatrixException("Kich thuoc ma tran khong the am.");
        if (sz > 0 && sz > numeric_limits<int>::max() / sz)
            throw MatrixException("Kich thuoc ma tran qua lon.");

        T* newData = nullptr;
        if (sz > 0) newData = new T[sz * sz];
        n = sz;
        data = newData;
    }
    void del() {
        if (data != nullptr) {
            delete[] data;
            data = nullptr;
        }
    }
    void checkIndex(int r, int c) const {
        if (r < 0 || r >= n || c < 0 || c >= n)
            throw MatrixException("Chi so nam ngoai kich thuoc ma tran.");
    }
    void checkSameSize(const Matrix& b) const {
        if (n != b.n)
            throw MatrixException("Hai ma tran phai co cung kich thuoc.");
    }
public:
    Matrix(int size = 0) : n(0), data(nullptr) {
        alloc(size);
    }
    Matrix(const Matrix& b) : n(0), data(nullptr) {
        alloc(b.n);
        try {
            for (int i = 0; i < n * n; ++i) {
                data[i] = b.data[i];
            }
        } catch (...) {
            del();
            n = 0;
            throw;
        }
    }
    ~Matrix() {
        del();
    }
    Matrix& operator=(const Matrix& b) {
        if (this != &b) {
            Matrix copy(b);
            int tempN = n;
            n = copy.n;
            copy.n = tempN;
            T* tempData = data;
            data = copy.data;
            copy.data = tempData;
        }
        return *this;
    }
    T& operator()(int r, int c) {
        checkIndex(r, c);
        return data[r * n + c];
    }
    const T& operator()(int r, int c) const {
        checkIndex(r, c);
        return data[r * n + c];
    }
    Matrix operator+(const Matrix& b) const {
        checkSameSize(b);
        Matrix res(n);
        for (int i = 0; i < n * n; ++i) {
            res.data[i] = this->data[i] + b.data[i];
        }
        return res;
    }
    Matrix operator-(const Matrix& b) const {
        checkSameSize(b);
        Matrix res(n);
        for (int i = 0; i < n * n; ++i) {
            res.data[i] = this->data[i] - b.data[i];
        }
        return res;
    }
    Matrix operator*(const Matrix& b) const {
        checkSameSize(b);
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

template <typename T>
void more(Matrix<T>& a, const Matrix<T>& b) {
    Matrix<T> d = a - b;
    cout << "\nA-B:\n" << d;
    Matrix<T> e = a * b;
    cout << "\nA*B:\n" << e;
    cout << "\nA[0][0] = " << a(0, 0) << endl;
    a(0, 0) = 999;
    cout << "A sau khi sua:\n" << a;
}

void more(Matrix<string>& a, const Matrix<string>&) {
    cout << "\nA[0][0] = " << a(0, 0) << endl;
    a(0, 0) = "999";
    cout << "A sau khi sua:\n" << a;
}

void more(Matrix<char>& a, const Matrix<char>& b) {
    Matrix<char> d = a - b;
    cout << "\nA-B:\n" << d;
    Matrix<char> e = a * b;
    cout << "\nA*B:\n" << e;
    cout << "\nA[0][0] = " << a(0, 0) << endl;
    a(0, 0) = 'X';
    cout << "A sau khi sua:\n" << a;
}

template <typename T>
void run() {
    int n;
    cout<<"Nhap n: ";
    if (!(cin >> n))
        throw MatrixException("Khong doc duoc kich thuoc ma tran.");
    if (n <= 0)
        throw MatrixException("Kich thuoc ma tran phai lon hon 0.");
    Matrix<T> a(n),b(n);
    cout<<"Nhap ma tran 1:\n";
    cin>>a;
    if (!cin)
        throw MatrixException("Loi khi nhap ma tran 1.");
    cout<<"Nhap ma tran 2:\n";
    cin>>b;
    if (!cin)
        throw MatrixException("Loi khi nhap ma tran 2.");

    cout<<"\nA:\n"<<a;
    cout<<"\nB:\n"<<b;
    Matrix<T> c=a+b;
    cout<<"\nA+B:\n"<<c;
    more(a, b);
}

int main() {
    int loai;
    cout<<"1-int 2-float 3-char 4-string: ";
    try {
        if (!(cin >> loai))
            throw MatrixException("Khong doc duoc loai ma tran.");
        if (loai == 1) run<int>();
        else if (loai == 2) run<float>();
        else if (loai == 3) run<char>();
        else if (loai == 4) run<string>();
        else cout<<"Sai roi\n";
    } catch (const exception& e) {
        cerr << "Loi: " << e.what() << '\n';
        return 1;
    }
    return 0;
}