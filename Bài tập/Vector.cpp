#include "Vector.h"
using namespace std;
Vector::Vector(int dim, double initValue) {
    if (dim < 0) {
        cout << "Loi: So chieu khong the am!\n";
        dim = 0;
    }
    n = dim;
    if (n > 0) {
        data = new double[n];
        for (int i = 0; i < n; ++i) {
            data[i] = initValue;
        }
    } else {
        data = nullptr;
    }
}
Vector::Vector(const Vector& other) {
    n = other.n;
    if (n > 0) {
        data = new double[n];
        for (int i = 0; i < n; ++i) {
            data[i] = other.data[i];
        }
    } else {
        data = nullptr;
    }
}
Vector::~Vector() {
    delete[] data;
    data = nullptr;
}
int Vector::GetDim() const {
    return n;
}
Vector& Vector::operator=(const Vector& other) {
    if (this != &other) {
        delete[] data;
        n = other.n;
        if (n > 0) {
            data = new double[n];
            for (int i = 0; i < n; ++i) {
                data[i] = other.data[i];
            }
        } else {
            data = nullptr;
        }
    }
    return *this;
}
void Vector::input() {
    cout << "Nhap so chieu n: ";
    cin >> n;
    delete[] data;
    if (n > 0) {
        data = new double[n];
        cout << "Nhap " << n << " toa do: ";
        for (int i = 0; i < n; ++i) {
            cin >> data[i];
        }
    } else {
        data = nullptr;
    }
}
void Vector::print() const {
    cout << "(";
    for (int i = 0; i < n; ++i) {
        cout << data[i];
        if (i < n - 1) cout << ", ";
    }
    cout << ")";
}
istream& operator>>(istream& is, Vector& v) {
    cout << "Nhap so chieu n: ";
    is >> v.n;
    delete[] v.data;
    if (v.n > 0) {
        v.data = new double[v.n];
        cout << "Nhap " << v.n << " toa do: ";
        for (int i = 0; i < v.n; ++i) {
            is >> v.data[i];
        }
    } else {
        v.data = nullptr;
    }
    return is;
}
ostream& operator<<(ostream& os, const Vector& v) {
    os << "(";
    for (int i = 0; i < v.n; ++i) {
        os << v.data[i];
        if (i < v.n - 1) os << ", ";
    }
    os << ")";
    return os;
}
Vector Vector::operator+(const Vector& other) const {
    if (n != other.n) {
        cout << "Loi: Hai vecto khong cung chieu!\n";
        return Vector();
    }
    Vector result(n);
    for (int i = 0; i < n; ++i) {
        result.data[i] = data[i] + other.data[i];
    }
    return result;
}
Vector Vector::operator-(const Vector& other) const {
    if (n != other.n) {
        cout << "Loi: Hai vecto khong cung chieu!\n";
        return Vector(); 
    }
    Vector result(n);
    for (int i = 0; i < n; ++i) {
        result.data[i] = data[i] - other.data[i];
    }
    return result;
}
double Vector::dot(const Vector& other) const {
    if (n != other.n) {
        cout << "Loi: Hai vecto khong cung chieu!\n";
        return 0.0;
    }
    double result = 0.0;
    for (int i = 0; i < n; ++i) {
        result += data[i] * other.data[i];
    }
    return result;
}
double Vector::operator*(const Vector& other) const {
    return dot(other);
}
double& Vector::operator[](int index) {
    if (index < 0 || index >= n) {
        cout << "Loi: Chi so vuot qua pham vi!\n";
        return data[0];
    }
    return data[index];
}
const double& Vector::operator[](int index) const {
    if (index < 0 || index >= n) {
        cout << "Loi: Chi so vuot qua pham vi!\n";
        return data[0];
    }
    return data[index];
}