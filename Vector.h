#ifndef VECTOR_H
#define VECTOR_H
#include <iostream>
class Vector {
private:
    int n;          
    double* data;   

public:
    Vector(int dim = 0, double initValue = 0.0);
    Vector(const Vector& other);
    ~Vector();
    int GetDim() const;
    Vector& operator=(const Vector& other);
    void input();
    void print() const;
    friend std::istream& operator>>(std::istream& is, Vector& v);
    friend std::ostream& operator<<(std::ostream& os, const Vector& v);
    Vector operator+(const Vector& other) const;
    Vector operator-(const Vector& other) const;
    double dot(const Vector& other) const;
    double operator*(const Vector& other) const;
    double& operator[](int index);
    const double& operator[](int index) const;
};
#endif 