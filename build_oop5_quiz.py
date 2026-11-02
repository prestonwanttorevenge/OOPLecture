# -*- coding: utf-8 -*-
"""
Builder for Chapter 5: Kế Thừa (Inheritance) - MOSTest5_2
Produces: OOP5-Inheritance_new.html
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

questions = []

# =========================================================================
# NHÓM 1: CƠ CHẾ BỐ CỤC BỘ NHỚ & VÒNG ĐỜI CONSTRUCTOR / DESTRUCTOR (CÂU 1 - 8)
# =========================================================================

questions.append({
    "id": 1,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bố Cục Bộ Nhớ & Vòng Đời Ctor / Dtor",
    "title": "Thứ tự gọi Constructor và Destructor trong đơn kế thừa (LIFO)",
    "code": """#include <iostream>

struct Base {
    Base() { std::cout << "B1 "; }
    ~Base() { std::cout << "B2 "; }
};

struct Derived : public Base {
    Derived() { std::cout << "D1 "; }
    ~Derived() { std::cout << "D2 "; }
};

int main() {
    {
        Derived d;
    }
    return 0;
}""",
    "options": [
        "A. B1 D1 D2 B2 (Lớp cơ sở xây trước, lớp dẫn xuất hủy trước)",
        "B. D1 B1 B2 D2",
        "C. B1 D1 B2 D2",
        "D. D1 B1 D2 B2"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, đối tượng lớp dẫn xuất chứa một đối tượng con của lớp cơ sở (Base subobject). Để xây dựng được <code>Derived</code>, hệ thống bắt buộc phải xây dựng nền tảng <code>Base</code> trước -> in ra <code>B1</code>, sau đó thân constructor của <code>Derived</code> mới thực thi -> in ra <code>D1</code>.<br>"
                   "2. Khi hết phạm vi (scope), quá trình giải phóng tuân theo nguyên tắc ngăn xếp LIFO (Last-In First-Out): phần mở rộng của <code>Derived</code> được hủy trước -> in ra <code>D2</code>, sau đó đến subobject của <code>Base</code> -> in ra <code>B2</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 29-30: Hàm dựng và hàm hủy trong kế thừa]</span>"
})

questions.append({
    "id": 2,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bố Cục Bộ Nhớ & Vòng Đời Ctor / Dtor",
    "title": "Thứ tự khởi tạo giữa Base Subobject và Member Object",
    "code": """#include <iostream>

struct Member {
    Member(const char* name) { std::cout << name << " "; }
};

struct Base {
    Member m1;
    Base() : m1("M1") { std::cout << "Base "; }
};

struct Derived : public Base {
    Member m2;
    Derived() : m2("M2") { std::cout << "Derived "; }
};

int main() {
    Derived d;
    return 0;
}""",
    "options": [
        "A. M2 Derived M1 Base",
        "B. M1 Base M2 Derived (Khởi tạo toàn bộ Base gồm thành viên của Base, rồi mới tới thành viên và thân Derived)",
        "C. Base M1 Derived M2",
        "D. M1 M2 Base Derived"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "Thứ tự khởi tạo được chuẩn hóa nghiêm ngặt bởi C++:<br>"
                   "1. Khởi tạo Base class subobject trước tiên. Trong Base, thành viên <code>m1</code> được khởi tạo trước thân Base -> in <code>M1 Base </code>.<br>"
                   "2. Tiếp theo khởi tạo các thành viên của Derived theo thứ tự khai báo: <code>m2</code> được tạo -> in <code>M2 </code>.<br>"
                   "3. Cuối cùng thực thi thân constructor của Derived -> in <code>Derived </code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 30: Trình tự khởi tạo các thành phần]</span>"
})

questions.append({
    "id": 3,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bố Cục Bộ Nhớ & Vòng Đời Ctor / Dtor",
    "title": "Bẫy Side-effect post-increment trong Constructor Chaining (Bài tập Slide)",
    "code": """#include <iostream>

class X {
public:
    X() { std::cout << "X "; }
};

class Y : public X {
public:
    Y(int i) { std::cout << "Y(" << i << ") "; }
};

class Z : public Y {
public:
    Z(int i) : Y(i++) { std::cout << "Z(" << i << ") "; }
};

int main() {
    Z obj(5);
    return 0;
}""",
    "options": [
        "A. X Y(5) Z(6)",
        "B. X Y(6) Z(6)",
        "C. Y(5) X Z(6)",
        "D. Lỗi biên dịch vì không thể truyền biểu thức i++ vào danh sách khởi tạo"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khởi tạo <code>Z</code> bắt đầu bằng khởi tạo lớp cha <code>Y</code>, và <code>Y</code> lại bắt đầu bằng khởi tạo <code>X</code> (in ra <code>X </code>).<br>"
                   "2. Biểu thức <code>Y(i++)</code>: toán tử hậu tố <code>i++</code> trả về giá trị cũ là <code>5</code> để truyền vào constructor của <code>Y</code> -> in ra <code>Y(5) </code>.<br>"
                   "3. Sau điểm sequence point đó, biến <code>i</code> của <code>Z</code> tăng lên thành <code>6</code>. Thân constructor của <code>Z</code> in ra <code>Z(6) </code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_Baitap.pdf - Trang 2: Bài tập 1 - Thứ tự gọi hàm dựng với i++]</span>"
})

questions.append({
    "id": 4,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bố Cục Bộ Nhớ & Vòng Đời Ctor / Dtor",
    "title": "Bẫy Custom Copy Constructor quên gọi Base Copy Constructor",
    "code": """#include <iostream>

struct Base {
    int x;
    Base(int val = 10) : x(val) {}
    Base(const Base& other) : x(other.x) { std::cout << "BaseCopy "; }
};

struct Derived : public Base {
    int y;
    Derived(int vx, int vy) : Base(vx), y(vy) {}
    // Custom Copy Constructor nhưng không gọi Base(other) trong init list
    Derived(const Derived& other) : y(other.y) {
        std::cout << "DerivedCopy ";
    }
};

int main() {
    Derived d1(100, 200);
    Derived d2 = d1;
    std::cout << "| x=" << d2.x << ", y=" << d2.y << std::endl;
    return 0;
}""",
    "options": [
        "A. DerivedCopy | x=100, y=200",
        "B. BaseCopy DerivedCopy | x=100, y=200",
        "C. DerivedCopy | x=10, y=200 (Subobject Base bị khởi tạo bằng default constructor Base())",
        "D. Lỗi biên dịch vì Derived bắt buộc phải gọi Base copy constructor"
    ],
    "correct": 2,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Nếu bạn tự viết Copy Constructor cho lớp dẫn xuất mà KHÔNG tường minh gọi <code>Base(other)</code> trong danh sách khởi tạo, trình biên dịch sẽ tự động gọi <strong>Default Constructor</strong> <code>Base()</code> cho phần Base subobject!<br>"
                   "2. Kết quả là <code>d2.x</code> nhận giá trị mặc định là <code>10</code> (chứ không phải <code>100</code> được sao chép từ <code>d1</code>). Đây là một bẫy rò rỉ logic cực kỳ phổ biến trong C++.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 29 & OOP5-Inheritance_Baitap.pdf - Trang 2: Copy constructor trong kế thừa]</span>"
})

questions.append({
    "id": 5,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bố Cục Bộ Nhớ & Vòng Đời Ctor / Dtor",
    "title": "Bẫy Toán tử gán operator= trong lớp dẫn xuất",
    "code": """#include <iostream>

struct Base {
    int val = 0;
    Base& operator=(const Base& rhs) {
        val = rhs.val + 10;
        return *this;
    }
};

struct Derived : public Base {
    int extra = 0;
    Derived& operator=(const Derived& rhs) {
        extra = rhs.extra;
        // Quên gọi Base::operator=(rhs);
        return *this;
    }
};

int main() {
    Derived d1, d2;
    d1.val = 5; d1.extra = 20;
    d2 = d1;
    std::cout << "val=" << d2.val << ", extra=" << d2.extra << std::endl;
    return 0;
}""",
    "options": [
        "A. val=15, extra=20",
        "B. val=5, extra=20",
        "C. val=0, extra=20 (Phần Base subobject không hề được cập nhật vì toán tử gán không tự động gọi lên cha)",
        "D. Lỗi biên dịch vì Derived::operator= che khuất Base::operator="
    ],
    "correct": 2,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Không giống như Constructor và Destructor (tự động chuỗi hóa lên Base), toán tử gán <code>operator=</code> của lớp dẫn xuất một khi đã tự định nghĩa thì <strong>KHÔNG tự động gọi</strong> <code>operator=</code> của Base.<br>"
                   "2. Vì lập trình viên quên gọi <code>Base::operator=(rhs);</code>, vùng nhớ của Base trong <code>d2</code> giữ nguyên giá trị ban đầu (<code>val = 0</code>).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 75: Tái định nghĩa toán tử trong lớp dẫn xuất]</span>"
})

questions.append({
    "id": 6,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bố Cục Bộ Nhớ & Vòng Đời Ctor / Dtor",
    "title": "Tối ưu hóa lớp cơ sở rỗng (Empty Base Optimization - EBO)",
    "code": """#include <iostream>

struct EmptyBase {};

struct Derived1 : public EmptyBase {
    int a;
};

struct NonDerived {
    EmptyBase eb;
    int a;
};

int main() {
    std::cout << sizeof(Derived1) << " " << (sizeof(NonDerived) > sizeof(Derived1)) << std::endl;
    return 0;
}""",
    "options": [
        "A. 4 1 (Nhờ EBO, EmptyBase không tốn thêm byte nào trong Derived1, trong khi cấu trúc composition NonDerived tốn thêm byte padding)",
        "B. 8 0",
        "C. 5 0",
        "D. 4 0"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Một struct rỗng độc lập có kích thước ít nhất 1 byte để đảm bảo mỗi đối tượng có địa chỉ riêng biệt.<br>"
                   "2. Tuy nhiên, khi kế thừa (<code>Derived1 : public EmptyBase</code>), chuẩn C++ cho phép cơ chế <strong>Empty Base Optimization (EBO)</strong>: Base subobject rỗng có kích thước hiệu dụng là 0 byte bên trong Derived1, do đó <code>sizeof(Derived1) == sizeof(int) == 4</code>.<br>"
                   "3. Ngược lại, khi nhúng làm thành viên (<code>NonDerived</code>), <code>eb</code> chiếm 1 byte + 3 byte padding căn lề (alignment) trước <code>int a</code> -> <code>sizeof(NonDerived) == 8</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 10-15: Bố cục bộ nhớ đối tượng]</span>"
})

questions.append({
    "id": 7,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bố Cục Bộ Nhớ & Vòng Đời Ctor / Dtor",
    "title": "Ngoại lệ văng ra từ Constructor lớp dẫn xuất và thứ tự dtor của Base",
    "code": """#include <iostream>

struct Base {
    Base() { std::cout << "+B "; }
    ~Base() { std::cout << "-B "; }
};

struct Derived : public Base {
    Derived() {
        std::cout << "+D ";
        throw 1;
    }
    ~Derived() { std::cout << "-D "; }
};

int main() {
    try {
        Derived d;
    } catch (...) {
        std::cout << "Caught";
    }
    return 0;
}""",
    "options": [
        "A. +B +D -D -B Caught",
        "B. +B +D -B Caught (Destructor của Derived KHÔNG chạy, nhưng Destructor của Base đã hoàn thành nên PHẢI được giải phóng)",
        "C. +B +D Caught (Không có destructor nào chạy)",
        "D. +B +D -B -D Caught"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, destructor của một lớp chỉ được gọi nếu constructor của nó đã chạy XONG trọn vẹn. Vì constructor của <code>Derived</code> ném ngoại lệ giữa chừng, đối tượng <code>Derived</code> coi như chưa từng tồn tại, nên <code>~Derived()</code> <strong>KHÔNG ĐƯỢC GỌI</strong>.<br>"
                   "2. Tuy nhiên, <code>Base</code> subobject đã hoàn thành constructor thành công trước đó, do đó quá trình Stack Unwinding sẽ tự động gọi <code>~Base()</code> để thu dọn phần base -> in ra <code>+B +D -B Caught</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 29 & OOP8-Exception.pdf - Trang 43: Constructor failure & Stack unwinding]</span>"
})

questions.append({
    "id": 8,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bố Cục Bộ Nhớ & Vòng Đời Ctor / Dtor",
    "title": "Lỗi biên dịch khi Base thiếu Default Constructor",
    "code": """#include <iostream>

class Base {
public:
    Base(int x) {}
};

class Derived : public Base {
public:
    Derived() {} // Không khai báo khởi tạo cho Base
};

int main() {
    Derived d;
    return 0;
}""",
    "options": [
        "A. Biên dịch thành công, Base::x được gán giá trị rác",
        "B. Lỗi biên dịch: không có default constructor hợp lệ cho lớp Base",
        "C. Biên dịch thành công, compiler tự động sinh Base::Base() rỗng",
        "D. Chương trình crash tại runtime"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Do <code>Base</code> đã tự định nghĩa một constructor có tham số <code>Base(int)</code>, trình biên dịch <strong>KHÔNG</strong> tự động sinh default constructor <code>Base()</code> nữa.<br>"
                   "2. Constructor của <code>Derived()</code> cố gắng ngầm định gọi <code>Base()</code> nhưng không tồn tại, dẫn tới lỗi biên dịch ngay lập tức. Để sửa, lập trình viên phải viết tường minh <code>Derived() : Base(0) {}</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 29: Ràng buộc constructor mặc định]</span>"
})

print(f"Loaded {len(questions)} questions for Group 1.")
# =========================================================================
# NHÓM 2: QUYỀN TRUY CẬP PUBLIC, PROTECTED, PRIVATE (CÂU 9 - 16)
# =========================================================================

questions.append({
    "id": 9,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Quyền Truy Cập public, protected, private",
    "title": "Truy cập protected member từ hàm main thông qua thể hiện Derived",
    "code": """#include <iostream>

class Vehicle {
protected:
    int speed = 60;
};

class Car : public Vehicle {
public:
    void printSpeed() {
        std::cout << speed << " ";
    }
};

int main() {
    Car c;
    c.printSpeed();
    // std::cout << c.speed; // Dòng A
    return 0;
}""",
    "options": [
        "A. c.printSpeed() in ra 60; Dòng A nếu bỏ chú thích sẽ gây lỗi biên dịch vì speed là protected đối với bên ngoài lớp",
        "B. Dòng A hợp lệ vì Car kế thừa public từ Vehicle",
        "C. Cả c.printSpeed() và Dòng A đều gây lỗi biên dịch",
        "D. speed tự động biến thành public trong Car"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Quyền <code>protected</code> cho phép các hàm thành viên của lớp dẫn xuất (<code>Car::printSpeed()</code>) truy cập trực tiếp.<br>"
                   "2. Tuy nhiên, đối với người dùng bên ngoài (như hàm <code>main()</code>), thành viên <code>protected</code> vẫn hoàn toàn bị che giấu như <code>private</code>. Truy cập trực tiếp <code>c.speed</code> là vi phạm kiểm tra access control của compiler.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 36-37: Từ khóa protected và quyền truy nhập]</span>"
})

questions.append({
    "id": 10,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Quyền Truy Cập public, protected, private",
    "title": "Thừa kế private biến mọi thành viên thành private của lớp con",
    "code": """#include <iostream>

class Engine {
public:
    void start() { std::cout << "EngineStarted "; }
};

class Airplane : private Engine {
public:
    void fly() {
        start(); // Truy cập nội bộ hợp lệ
    }
};

class Jet : public Airplane {
public:
    void test() {
        // start(); // Dòng B
    }
};

int main() {
    Airplane a;
    a.fly();
    // a.start(); // Dòng C
    return 0;
}""",
    "options": [
        "A. In ra EngineStarted; Cả Dòng B và Dòng C nếu mở ra đều gây lỗi biên dịch",
        "B. Dòng C lỗi nhưng Dòng B hợp lệ",
        "C. In ra EngineStarted; Cả Dòng B và Dòng C đều hợp lệ",
        "D. Lỗi biên dịch ngay từ dòng Airplane : private Engine"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Với <code>private inheritance</code>, mọi thành viên public/protected của <code>Engine</code> sẽ trở thành <code>private</code> trong <code>Airplane</code>.<br>"
                   "2. Do đó, chỉ riêng các phương thức của chính <code>Airplane</code> mới gọi được <code>start()</code>.<br>"
                   "3. Lớp con kế tiếp là <code>Jet</code> không thể thấy <code>start()</code> (Dòng B lỗi), và người dùng bên ngoài cũng không thể gọi <code>a.start()</code> (Dòng C lỗi).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 33-35: Thừa kế private và hệ quả]</span>"
})

questions.append({
    "id": 11,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Quyền Truy Cập public, protected, private",
    "title": "Bẫy Upcasting với Private / Protected Inheritance",
    "code": """#include <iostream>

class Base {};
class Derived : private Base {};

void test(Base* b) {}

int main() {
    Derived d;
    // test(&d); // Dòng X
    return 0;
}""",
    "options": [
        "A. Hợp lệ vì con trỏ Derived luôn luôn ép kiểu ngầm định được về Base*",
        "B. Lỗi biên dịch tại Dòng X: 'Base' is an inaccessible base of 'Derived' (Upcast chỉ hợp lệ với public inheritance bên ngoài lớp)",
        "C. Lỗi runtime phân mảnh bộ nhớ",
        "D. Trình biên dịch sinh cảnh báo nhưng vẫn chạy được"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Upcasting ngầm định từ <code>Derived*</code> về <code>Base*</code> thể hiện mối quan hệ 'IS-A'.<br>"
                   "2. Nhưng với <code>private</code> hoặc <code>protected</code> inheritance, quan hệ IS-A bị ẩn với thế giới bên ngoài. Trình biên dịch coi Base là không thể truy cập (inaccessible), do đó từ chối phép upcasting này tại Dòng X.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 58 & 72: Điều kiện thực hiện phép Upcast]</span>"
})

questions.append({
    "id": 12,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Quyền Truy Cập public, protected, private",
    "title": "Sử dụng từ khóa using để khôi phục quyền truy cập public trong Derived",
    "code": """#include <iostream>

class Base {
protected:
    void secret() { std::cout << "Unlocked "; }
};

class Derived : public Base {
public:
    using Base::secret; // Đưa phương thức protected lên public
};

int main() {
    Derived d;
    d.secret();
    return 0;
}""",
    "options": [
        "A. In ra: Unlocked (C++ cho phép dùng cú pháp using để thăng hạng quyền truy cập từ protected lên public)",
        "B. Lỗi biên dịch vì derived class không thể thay đổi quyền truy cập của base class",
        "C. Lỗi runtime Access Violation",
        "D. Chỉ in ra khi chạy ở chế độ debug"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, một lớp con có quyền truy cập vào thành viên <code>protected</code> của lớp cha, và nó có quyền dùng từ khóa <code>using Base::secret;</code> đặt trong phần <code>public:</code> của mình để công khai phương thức đó cho đối tượng bên ngoài gọi trực tiếp.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 38-40: Điều chỉnh quyền truy cập thành viên]</span>"
})

questions.append({
    "id": 13,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Quyền Truy Cập public, protected, private",
    "title": "Khác biệt mặc định về kiểu kế thừa giữa struct và class",
    "code": """#include <iostream>

class A {
public:
    int x = 10;
};

struct B : A {}; // Kiểu thừa kế mặc định là gì?
class C : A {};  // Kiểu thừa kế mặc định là gì?

int main() {
    B b;
    std::cout << b.x << " ";
    C c;
    // std::cout << c.x; // Dòng Z
    return 0;
}""",
    "options": [
        "A. In ra: 10; B mặc định là public inheritance, còn C mặc định là private inheritance",
        "B. Cả B và C đều mặc định là public inheritance",
        "C. Cả B và C đều mặc định là private inheritance",
        "D. In ra: 10 10; Không có sự khác biệt giữa struct và class"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, nếu không ghi rõ từ khóa kế thừa: đối với <code>struct</code> mặc định là <code>public</code>, còn đối với <code>class</code> mặc định là <code>private</code>.<br>"
                   "2. Do đó <code>b.x</code> truy cập công khai bình thường, trong khi <code>c.x</code> là private đối với bên ngoài (Dòng Z sẽ báo lỗi biên dịch).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 32-33: Kiểu thừa kế mặc định của struct và class]</span>"
})

questions.append({
    "id": 14,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Quyền Truy Cập public, protected, private",
    "title": "Bẫy truy cập protected member trên một đối tượng Base khác",
    "code": """#include <iostream>

class Base {
protected:
    int val = 42;
};

class Derived : public Base {
public:
    void hack(Base& b) {
        // std::cout << b.val; // Dòng L
    }
    void accessSelf() {
        std::cout << this->val << " ";
    }
};

int main() {
    Derived d;
    d.accessSelf();
    return 0;
}""",
    "options": [
        "A. d.accessSelf() in ra 42; Dòng L nếu mở ra sẽ bị LỖI BIÊN DỊCH (Lớp con chỉ được truy cập protected trên chính nó hoặc đối tượng cùng kiểu dẫn xuất)",
        "B. Cả Dòng L và d.accessSelf() đều hợp lệ vì Derived kế thừa Base",
        "C. d.accessSelf() gây lỗi biên dịch",
        "D. val bị ẩn hoàn toàn đối với Derived"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Chuẩn C++ quy định nghiêm ngặt: Lớp dẫn xuất <code>Derived</code> chỉ được truy cập thành viên <code>protected</code> thông qua con trỏ hoặc tham chiếu có kiểu thuộc cây dẫn xuất của nó (như <code>Derived*</code> hoặc <code>this</code>).<br>"
                   "2. Nó KHÔNG được phép truy cập thành viên protected của một đối tượng <code>Base</code> độc lập ngẫu nhiên (như tham số <code>Base& b</code> ở Dòng L) để bảo vệ tính đóng gói.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 36-37: Ràng buộc truy cập protected]</span>"
})

questions.append({
    "id": 15,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Quyền Truy Cập public, protected, private",
    "title": "Tính chất quan hệ bạn bè (Friendship) trong thừa kế",
    "code": """#include <iostream>

class Base {
private:
    int secret = 99;
    friend void reveal(Base& b);
};

class Derived : public Base {
private:
    int dSecret = 88;
};

void reveal(Base& b) {
    std::cout << b.secret << " ";
    // Derived* d = (Derived*)&b;
    // std::cout << d->dSecret; // Dòng F
}

int main() {
    Base b;
    reveal(b);
    return 0;
}""",
    "options": [
        "A. In ra 99; Quan hệ friend KHÔNG được kế thừa (Friendship is not inherited)",
        "B. In ra 99 88",
        "C. Lỗi biên dịch vì friend function không thể truy cập private của Base",
        "D. reveal tự động trở thành friend của Derived"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Câu thần chú bất biến của C++: <em>'Friendship is neither inherited nor transitive'</em> (Quan hệ bạn bè không được thừa kế và không có tính bắc cầu).<br>"
                   "2. Hàm <code>reveal</code> là bạn của <code>Base</code> nên truy cập được <code>b.secret</code>, nhưng nó KHÔNG phải là bạn của <code>Derived</code>. Nếu mở Dòng F, compiler sẽ báo lỗi <code>dSecret is private</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf & OOP5-Inheritance_new.pdf - Trang 36: Hàm bạn và quyền kế thừa]</span>"
})

questions.append({
    "id": 16,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Quyền Truy Cập public, protected, private",
    "title": "Ma trận biến đổi quyền truy cập trong Protected Inheritance",
    "code": """#include <iostream>

class GrandParent {
public:
    int pub = 1;
protected:
    int pro = 2;
private:
    int pri = 3;
};

class Parent : protected GrandParent {
    // pub và pro trở thành protected trong Parent
};

class Child : public Parent {
public:
    void print() {
        std::cout << pub << " " << pro << " ";
    }
};

int main() {
    Child c;
    c.print();
    return 0;
}""",
    "options": [
        "A. In ra: 1 2 (Trong protected inheritance, cả public và protected của lớp cơ sở đều chuyển thành protected, do đó Child vẫn truy cập được)",
        "B. Lỗi biên dịch vì pub bị biến thành private trong Parent",
        "C. Lỗi biên dịch vì pro không thể kế thừa qua 2 cấp",
        "D. In ra: 1 2 3"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong <code>protected inheritance</code>:<br>"
                   "   - <code>public</code> của cha -> trở thành <code>protected</code> của con.<br>"
                   "   - <code>protected</code> của cha -> trở thành <code>protected</code> của con.<br>"
                   "   - <code>private</code> của cha -> không thể truy cập.<br>"
                   "2. Do <code>Parent</code> sở hữu <code>pub</code> và <code>pro</code> dưới dạng <code>protected</code>, nên lớp cháu <code>Child</code> (kế thừa public từ Parent) hoàn toàn có quyền truy cập chúng.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 37-38: Ma trận quyền truy cập]</span>"
})

print(f"Loaded {len(questions)} questions for Groups 1-2.")
# =========================================================================
# NHÓM 3: HIỆN TƯỢNG CHE KHUẤT TÊN (NAME HIDING) VS TÁI ĐỊNH NGHĨA (CÂU 17 - 24)
# =========================================================================

questions.append({
    "id": 17,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Che Khuất Tên (Name Hiding) & Tái Định Nghĩa",
    "title": "Bẫy Name Hiding kinh điển khi khác danh sách tham số giữa Base và Derived",
    "code": """#include <iostream>

struct Base {
    void func(int x) { std::cout << "Base::int=" << x << " "; }
};

struct Derived : public Base {
    void func(double d) { std::cout << "Derived::double=" << d << " "; }
};

int main() {
    Derived d;
    d.func(10); // Truyền số nguyên 10
    return 0;
}""",
    "options": [
        "A. Base::int=10 (Trình biên dịch tự tìm overload phù hợp nhất ở Base)",
        "B. Derived::double=10 (Hàm func ở Derived che khuất toàn bộ hàm func ở Base; 10 bị ép kiểu ngầm định thành 10.0)",
        "C. Lỗi biên dịch vì mơ hồ giữa hai phiên bản",
        "D. Lỗi runtime do mismatch tham số"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, quy trình tìm kiếm tên (<strong>Name Lookup</strong>) diễn ra TRƯỚC quy trình chọn hàm nạp chồng (<strong>Overload Resolution</strong>).<br>"
                   "2. Khi gọi <code>d.func(...)</code>, trình biên dịch tìm kiếm tên <code>func</code> trong scope của <code>Derived</code>. Do đã tìm thấy <code>Derived::func</code>, quá trình Name Lookup <strong>DỪNG LẠI NGAY LẬP TỨC</strong> và hoàn toàn bỏ qua scope của <code>Base</code>.<br>"
                   "3. Số nguyên <code>10</code> sau đó bị ép kiểu ngầm định thành <code>double</code> và gọi vào <code>Derived::func</code>!<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 41-43: Hiện tượng che khuất tên & Overriding]</span>"
})

questions.append({
    "id": 18,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Che Khuất Tên (Name Hiding) & Tái Định Nghĩa",
    "title": "Dùng từ khóa using để unhide các overload của Base trong Derived",
    "code": """#include <iostream>

struct Base {
    void show(int x) { std::cout << "B_int "; }
};

struct Derived : public Base {
    using Base::show; // Đưa show(int) vào overload set của Derived
    void show(double d) { std::cout << "D_double "; }
};

int main() {
    Derived d;
    d.show(5);
    d.show(3.14);
    return 0;
}""",
    "options": [
        "A. B_int D_double (Nhờ chỉ thị using, show(int) của Base được đưa vào bộ nạp chồng của Derived)",
        "B. D_double D_double",
        "C. Lỗi biên dịch vì trùng tên hàm show",
        "D. B_int B_int"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Chỉ thị <code>using Base::show;</code> chỉ đạo trình biên dịch nạp tất cả các phiên bản của <code>show</code> từ lớp cha vào phạm vi nạp chồng (overload set) của lớp con <code>Derived</code>.<br>"
                   "2. Do đó khi gọi <code>d.show(5)</code>, phiên bản nhận <code>int</code> là exact match tốt nhất, nên gọi <code>Base::show</code> -> in ra <code>B_int D_double</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 43-44: Nạp lại bộ hàm bị che khuất]</span>"
})

questions.append({
    "id": 19,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Che Khuất Tên (Name Hiding) & Tái Định Nghĩa",
    "title": "Che khuất biến thành viên (Shadowing Member Variables)",
    "code": """#include <iostream>

struct Base {
    int value = 10;
};

struct Derived : public Base {
    int value = 20; // Trùng tên biến với Base
    void print() {
        std::cout << value << " " << Base::value << " ";
    }
};

int main() {
    Derived d;
    d.print();
    std::cout << sizeof(d) / sizeof(int);
    return 0;
}""",
    "options": [
        "A. In ra: 20 10 2 (Derived chứa CẢ HAI biến value độc lập trong bộ nhớ, sizeof(d) là 8 byte)",
        "B. In ra: 20 20 1",
        "C. Lỗi biên dịch do khai báo biến trùng tên trong lớp kế thừa",
        "D. In ra: 10 20 2"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Biến thành viên trong lớp dẫn xuất <strong>KHÔNG GHI ĐÈ</strong> vùng nhớ của lớp cha mà chỉ CHE KHUẤT (shadow) nó.<br>"
                   "2. Trong RAM, đối tượng <code>d</code> sở hữu 2 ô nhớ kiểu <code>int</code> tách biệt: <code>Base::value</code> (offset 0) và <code>Derived::value</code> (offset 4).<br>"
                   "3. Tổng kích thước là 8 bytes, tương đương 2 biến <code>int</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 12-14: Bộ nhớ chứa các trường trùng tên]</span>"
})

questions.append({
    "id": 20,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Che Khuất Tên (Name Hiding) & Tái Định Nghĩa",
    "title": "Gọi hàm non-virtual bị che khuất qua con trỏ Base (Static Binding)",
    "code": """#include <iostream>

struct Base {
    void say() { std::cout << "BaseSay "; }
};

struct Derived : public Base {
    void say() { std::cout << "DerivedSay "; }
};

int main() {
    Derived d;
    Base* ptr = &d;
    ptr->say(); // Gọi qua con trỏ Base
    d.say();    // Gọi qua đối tượng Derived
    return 0;
}""",
    "options": [
        "A. DerivedSay DerivedSay",
        "B. BaseSay DerivedSay (Hàm không ảo dùng liên kết tĩnh Static Binding dựa trên kiểu của con trỏ tại thời điểm biên dịch)",
        "C. BaseSay BaseSay",
        "D. Lỗi biên dịch vì say bị định nghĩa lại"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Vì phương thức <code>say()</code> không có từ khóa <code>virtual</code>, trình biên dịch sử dụng <strong>Liên kết tĩnh (Static Binding)</strong>.<br>"
                   "2. Khi gọi <code>ptr->say()</code>, kiểu tĩnh của con trỏ là <code>Base*</code>, nên compiler cố định mã máy trỏ thẳng tới địa chỉ của <code>Base::say</code>.<br>"
                   "3. Ngược lại, <code>d.say()</code> có kiểu tĩnh là <code>Derived</code>, gọi thẳng <code>Derived::say</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 41 & 61: Upcast và liên kết tĩnh]</span>"
})

questions.append({
    "id": 21,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Che Khuất Tên (Name Hiding) & Tái Định Nghĩa",
    "title": "Tái định nghĩa hàm Static trong lớp dẫn xuất",
    "code": """#include <iostream>

struct Base {
    static void hello() { std::cout << "StaticBase "; }
};

struct Derived : public Base {
    static void hello() { std::cout << "StaticDerived "; }
};

int main() {
    Derived d;
    Base* p = &d;
    p->hello();
    Derived::hello();
    return 0;
}""",
    "options": [
        "A. StaticDerived StaticDerived",
        "B. StaticBase StaticDerived (Hàm static không thể có tính đa hình động, gọi qua con trỏ Base* luôn gọi bản static của Base)",
        "C. Lỗi biên dịch vì hàm static không được phép thừa kế",
        "D. StaticBase StaticBase"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Hàm <code>static</code> thuộc về phạm vi của class, không liên kết với con trỏ <code>this</code> và không có bảng ảo VTable.<br>"
                   "2. Biểu thức <code>p->hello()</code> thực chất chỉ dùng kiểu tĩnh của <code>p</code> (tức <code>Base</code>) để phân giải tên lúc biên dịch, tương đương với <code>Base::hello()</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 42 & OOP3-Class&Objec_new.pdf: Phương thức static trong kế thừa]</span>"
})

questions.append({
    "id": 22,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Che Khuất Tên (Name Hiding) & Tái Định Nghĩa",
    "title": "Từ khóa final ngăn chặn kế thừa lớp trong C++11",
    "code": """#include <iostream>

class FinalClass final {
public:
    int x = 5;
};

// class SubClass : public FinalClass {}; // Dòng K

int main() {
    FinalClass fc;
    std::cout << fc.x;
    return 0;
}""",
    "options": [
        "A. In ra 5; Dòng K nếu mở ra sẽ gây LỖI BIÊN DỊCH vì từ khóa final trong C++11 cấm bất kỳ lớp nào kế thừa từ FinalClass",
        "B. Dòng K hợp lệ nếu dùng private inheritance",
        "C. Lỗi biên dịch vì từ khóa final chỉ được dùng cho hàm ảo chứ không được dùng cho class",
        "D. In ra 5 và sinh cảnh báo compiler"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong chuẩn C++11, từ khóa <code>final</code> khi đặt sau tên lớp (<code>class FinalClass final</code>) sẽ cấm tuyệt đối mọi hành vi kế thừa từ lớp này.<br>"
                   "2. Mọi nỗ lực <code>class SubClass : public FinalClass</code> sẽ bị trình biên dịch chặn lại ngay lập tức với lỗi: <em>cannot derive from 'final' base</em>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 15 & C++11 Standard: final specifier]</span>"
})

questions.append({
    "id": 23,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Che Khuất Tên (Name Hiding) & Tái Định Nghĩa",
    "title": "Bẫy đệ quy vô hạn khi ghi đè phương thức mà quên scope Base::",
    "code": """#include <iostream>

struct Base {
    void log() { std::cout << "BaseLog "; }
};

struct Derived : public Base {
    void log() {
        // Dự định gọi hàm cha trước khi in tiếp:
        // log(); // Dòng R: Quên viết Base::log();
        std::cout << "DerivedLog ";
    }
};

int main() {
    Derived d;
    d.log();
    return 0;
}""",
    "options": [
        "A. In ra DerivedLog; Nếu mở Dòng R sẽ gây tràn ngăn xếp (Stack Overflow) do đệ quy vô hạn chính nó",
        "B. Nếu mở Dòng R sẽ in ra: BaseLog DerivedLog",
        "C. Trình biên dịch tự động đoán lập trình viên muốn gọi Base::log()",
        "D. Lỗi biên dịch tại Dòng R do gọi hàm trùng tên"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong thân hàm <code>Derived::log()</code>, việc gọi <code>log()</code> không có tiền tố phạm vi sẽ kích hoạt tìm kiếm tên tại chính scope của <code>Derived</code>.<br>"
                   "2. Nó sẽ liên tục gọi chính nó (self-recursion) mãi mãi mà không có điểm dừng, dẫn đến cạn kiệt bộ nhớ stack và sinh lỗi sập chương trình nghiêm trọng (SIGSEGV / Stack Overflow). Phải viết tường minh <code>Base::log();</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 45-46: Lời gọi hàm lớp cơ sở từ lớp dẫn xuất]</span>"
})

questions.append({
    "id": 24,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Che Khuất Tên (Name Hiding) & Tái Định Nghĩa",
    "title": "Bẫy giá trị mặc định của tham số (Default Arguments) khi gọi qua con trỏ",
    "code": """#include <iostream>

struct Base {
    virtual void show(int x = 10) {
        std::cout << "Base:" << x << " ";
    }
};

struct Derived : public Base {
    void show(int x = 20) override {
        std::cout << "Derived:" << x << " ";
    }
};

int main() {
    Derived d;
    Base* p = &d;
    p->show(); // Bẫy cực kỳ kinh điển!
    return 0;
}""",
    "options": [
        "A. Derived:20",
        "B. Base:10",
        "C. Derived:10 (Thực thi thân hàm ảo của Derived, nhưng tham số mặc định được liên kết tĩnh theo kiểu Base* lúc biên dịch)",
        "D. Lỗi biên dịch vì tham số mặc định khác nhau giữa Base và Derived"
    ],
    "correct": 2,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <strong>Quy tắc vàng của C++:</strong> Hàm ảo được phân giải động tại runtime (Dynamic Binding), nhưng <em>Tham số mặc định (Default Argument) được nạp tĩnh tại thời điểm biên dịch (Static Binding)</em> dựa trên kiểu của con trỏ gọi hàm!<br>"
                   "2. Con trỏ <code>p</code> có kiểu <code>Base*</code>, nên trình biên dịch gắn tham số mặc định <code>x = 10</code> vào lời gọi hàm lúc sinh mã.<br>"
                   "3. Tại runtime, con trỏ vptr trỏ vào <code>Derived::show</code>, nhận giá trị <code>x = 10</code> truyền vào -> in ra <code>Derived:10</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 61 & OOP6-Polymorphism_new.pdf: Default arguments in virtual functions]</span>"
})

print(f"Loaded {len(questions)} questions for Groups 1-3.")
# =========================================================================
# NHÓM 4: UPCASTING, DOWNCASTING & BẪY CẮT XÉN ĐỐI TƯỢNG (OBJECT SLICING) (CÂU 25 - 34)
# =========================================================================

questions.append({
    "id": 25,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Upcast, Downcast & Object Slicing",
    "title": "Hiện tượng Cắt Xén Đối Tượng (Object Slicing) khi truyền tham trị",
    "code": """#include <iostream>

struct Base {
    virtual void print() const { std::cout << "Base "; }
};

struct Derived : public Base {
    void print() const override { std::cout << "Derived "; }
};

void callByValue(Base b) {
    b.print();
}

void callByRef(const Base& b) {
    b.print();
}

int main() {
    Derived d;
    callByValue(d); // Truyền tham trị
    callByRef(d);   // Truyền tham chiếu
    return 0;
}""",
    "options": [
        "A. Derived Derived",
        "B. Base Derived (callByValue gây ra Object Slicing: chỉ phần Base subobject được copy, vptr trỏ về Base)",
        "C. Base Base",
        "D. Lỗi biên dịch khi truyền đối tượng Derived vào tham số kiểu Base"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong <code>callByValue(Base b)</code>, biến <code>b</code> là một đối tượng độc lập kiểu <code>Base</code> được cấp phát trên stack frame. Trình biên dịch gọi copy constructor của <code>Base</code>, chỉ sao chép phần Base subobject từ <code>d</code>.<br>"
                   "2. Mọi thông tin mở rộng của <code>Derived</code> (kể cả bảng vptr trỏ tới Derived) bị <strong>CẮT BỎ HOÀN TOÀN (Sliced away)</strong>. Biến <code>b</code> trở thành một thể hiện Base thuần túy, do đó gọi <code>Base::print</code>.<br>"
                   "3. Trong khi đó <code>callByRef(const Base& b)</code> chỉ là bí danh (alias) của chính đối tượng <code>d</code> trong bộ nhớ, vptr của nó vẫn trỏ tới VTable của <code>Derived</code>, gọi đúng <code>Derived::print</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 63-66: Hiện tượng Slicing]</span>"
})

questions.append({
    "id": 26,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Upcast, Downcast & Object Slicing",
    "title": "Bẫy Slicing trong mảng các đối tượng Base thô",
    "code": """#include <iostream>

struct Base {
    int id = 1;
};

struct Derived : public Base {
    int extra = 99;
};

int main() {
    Derived d;
    d.id = 5;
    d.extra = 77;

    Base list[2];
    list[0] = d; // Gán đối tượng Derived vào mảng kiểu Base

    std::cout << list[0].id << " " << sizeof(list[0]);
    return 0;
}""",
    "options": [
        "A. 5 4 (Chỉ trường id của Base được copy vào mảng, sizeof của phần tử trong mảng cố định là sizeof(Base))",
        "B. 5 8",
        "C. 77 4",
        "D. Lỗi biên dịch vì không thể gán Derived vào phần tử mảng Base"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Mảng <code>Base list[2]</code> được cấp phát tĩnh trong RAM với kích thước mỗi ô nhớ chính xác bằng <code>sizeof(Base) = 4 bytes</code>.<br>"
                   "2. Phép gán <code>list[0] = d</code> gọi <code>Base::operator=(const Base&)</code>, chỉ sao chép trường <code>id = 5</code>, trường <code>extra</code> bị cắt bỏ không dấu vết.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 64-65: Gán đối tượng và kích thước mảng]</span>"
})

questions.append({
    "id": 27,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Upcast, Downcast & Object Slicing",
    "title": "Nguy cơ Undefined Behavior khi Downcast bừa bãi bằng static_cast",
    "code": """#include <iostream>

struct Base {
    int x = 10;
};

struct Derived : public Base {
    int y = 20;
    void show() { std::cout << x << " " << y; }
};

int main() {
    Base b; // Đối tượng Base THẬT
    Derived* p = static_cast<Derived*>(&b); // Downcast liều lĩnh!
    p->show(); // Bẫy truy cập vùng nhớ rác!
    return 0;
}""",
    "options": [
        "A. Luôn in ra 10 20 an toàn",
        "B. static_cast kiểm tra runtime và ném ngoại lệ std::bad_cast",
        "C. Hành vi không xác định (Undefined Behavior): y truy cập vào vùng nhớ ngoài phạm vi của đối tượng Base",
        "D. Lỗi biên dịch: static_cast không cho phép downcast"
    ],
    "correct": 2,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <code>static_cast</code> là phép ép kiểu tại THỜI ĐIỂM BIÊN DỊCH. Trình biên dịch tin tưởng lập trình viên và dịch chuyển con trỏ mà KHÔNG có bất kỳ kiểm tra runtime nào.<br>"
                   "2. Đối tượng <code>b</code> trong RAM chỉ được cấp phát 4 bytes cho <code>x</code>. Khi gọi <code>p->show()</code>, phương thức cố đọc <code>this->y</code> (ở offset 4 byte tiếp theo), đọc vào dữ liệu rác trên stack hoặc gây lỗi truy cập bộ nhớ bất hợp pháp (Segmentation fault).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 67-69: Nguy cơ Downcast & static_cast]</span>"
})

questions.append({
    "id": 28,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Upcast, Downcast & Object Slicing",
    "title": "Yêu cầu tính Đa Hình của dynamic_cast (Polymorphic Class Requirement)",
    "code": """#include <iostream>

struct Base {
    // Không có hàm virtual nào!
    void dummy() {}
};

struct Derived : public Base {
    void dummy() {}
};

int main() {
    Base* b = new Derived();
    // Derived* d = dynamic_cast<Derived*>(b); // Dòng D
    return 0;
}""",
    "options": [
        "A. Hợp lệ và d nhận địa chỉ hợp lệ của Derived",
        "B. Lỗi biên dịch tại Dòng D: 'Base' is not polymorphic (dynamic_cast bắt buộc lớp cơ sở phải có ít nhất 1 hàm ảo để sinh thông tin RTTI)",
        "C. Dòng D trả về nullptr tại runtime",
        "D. Lỗi runtime bad_cast"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <code>dynamic_cast</code> hoạt động dựa trên cơ chế <strong>RTTI (Run-Time Type Information)</strong> được lưu trữ trong con trỏ VTable của đối tượng.<br>"
                   "2. Nếu một lớp không chứa bất kỳ hàm ảo (virtual function) nào, trình biên dịch sẽ không tạo bảng ảo (VTable) và cấu trúc RTTI cho nó.<br>"
                   "3. Do đó, việc gọi <code>dynamic_cast</code> trên một kiểu không đa hình (non-polymorphic) sẽ bị trình biên dịch từ chối ngay lập tức.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 68 & OOP6-Polymorphism_new.pdf: RTTI và hàm ảo]</span>"
})

questions.append({
    "id": 29,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Upcast, Downcast & Object Slicing",
    "title": "Cơ chế xử lý lỗi của dynamic_cast trên Con trỏ vs trên Tham chiếu",
    "code": """#include <iostream>

struct Base {
    virtual ~Base() = default;
};

struct Derived : public Base {};
struct Other : public Base {};

int main() {
    Derived d;
    Base& ref = d;

    try {
        Other& o = dynamic_cast<Other&>(ref); // Ép kiểu tham chiếu thất bại
        std::cout << "Success ";
    } catch (const std::bad_cast& e) {
        std::cout << "CaughtBadCast ";
    }

    Base* ptr = &d;
    Other* oPtr = dynamic_cast<Other*>(ptr); // Ép kiểu con trỏ thất bại
    if (oPtr == nullptr) {
        std::cout << "NullPtr";
    }
    return 0;
}""",
    "options": [
        "A. CaughtBadCast NullPtr (Con trỏ thất bại trả về nullptr, tham chiếu thất bại không thể có 'null reference' nên bắt buộc ném std::bad_cast)",
        "B. Success NullPtr",
        "C. CaughtBadCast CaughtBadCast",
        "D. Chương trình crash tại dynamic_cast con trỏ"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Với con trỏ (pointer), khi <code>dynamic_cast</code> thất bại, nó báo lỗi một cách nhẹ nhàng bằng cách trả về <code>nullptr</code>.<br>"
                   "2. Với tham chiếu (reference), vì C++ không tồn tại khái niệm tham chiếu null (null reference), cơ chế duy nhất để báo lỗi an toàn là ném ra ngoại lệ <code>std::bad_cast</code> thuộc thư viện <code><typeinfo></code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 67-69 & C++11 RTTI Specification]</span>"
})

questions.append({
    "id": 30,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Upcast, Downcast & Object Slicing",
    "title": "Hiểm họa khi truy cập mảng Derived thông qua con trỏ Base* (Array Stride Mismatch)",
    "code": """#include <iostream>

struct Base {
    int b = 1;
};

struct Derived : public Base {
    int d = 2; // Derived lớn hơn Base (8 bytes vs 4 bytes)
};

void printArray(Base* arr, int n) {
    for (int i = 0; i < n; ++i) {
        std::cout << arr[i].b << " "; // Bẫy tính toán con trỏ pointer arithmetic!
    }
}

int main() {
    Derived arr[3];
    arr[0].b = 10; arr[1].b = 20; arr[2].b = 30;
    printArray(arr, 3);
    return 0;
}""",
    "options": [
        "A. 10 20 30",
        "B. Kết quả sai lệch hoặc rác bộ nhớ (arr[i] nhảy theo bước sizeof(Base)=4 thay vì sizeof(Derived)=8)",
        "C. Lỗi biên dịch vì không thể truyền Derived[] vào Base*",
        "D. 10 2 20"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, đa hình không áp dụng cho phép toán con trỏ mảng (Pointer Arithmetic).<br>"
                   "2. Biểu thức <code>arr[i]</code> tương đương với <code>*(arr + i)</code>, tức là nhảy một đoạn bộ nhớ có kích thước <code>i * sizeof(Base) = i * 4 bytes</code>.<br>"
                   "3. Nhưng thực tế các phần tử <code>Derived</code> trong mảng cách nhau <code>8 bytes</code>! Do đó <code>arr[1]</code> sẽ đọc nhầm vào trường <code>d</code> của phần tử 0 thay vì phần tử 1. Đây là lỗi cực kỳ nguy hiểm trong kiến trúc C++.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 62-63: Upcast mảng và bẫy con trỏ]</span>"
})

questions.append({
    "id": 31,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Upcast, Downcast & Object Slicing",
    "title": "Bẫy Slicing khi hàm trả về đối tượng theo giá trị (Return by Value)",
    "code": """#include <iostream>

struct Base {
    virtual const char* name() const { return "Base"; }
};

struct Derived : public Base {
    const char* name() const override { return "Derived"; }
};

Base getObject() {
    Derived d;
    return d; // Trả về theo giá trị kiểu Base
}

int main() {
    Base b = getObject();
    std::cout << b.name();
    return 0;
}""",
    "options": [
        "A. Derived",
        "B. Base (getObject trả về đối tượng tạm kiểu Base bằng copy ctor, cắt bỏ hoàn toàn bản sắc Derived)",
        "C. Lỗi biên dịch do mismatch kiểu trả về",
        "D. Chương trình crash vì con trỏ cục bộ d bị hủy"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Kiểu trả về của hàm là <code>Base</code>. Khi thực hiện <code>return d;</code>, đối tượng tạm trả về được khởi tạo bằng <code>Base(const Base&)</code>.<br>"
                   "2. Toàn bộ phần <code>Derived</code> bị cắt bỏ ngay tại lệnh return. Đối tượng <code>b</code> trong <code>main</code> là một Base thuần túy, vptr trỏ vào Base VTable -> in ra <code>Base</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 64: Slicing khi return đối tượng]</span>"
})

questions.append({
    "id": 32,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Upcast, Downcast & Object Slicing",
    "title": "Upcasting qua nhiều tầng thừa kế và tính an toàn tuyệt đối",
    "code": """#include <iostream>

struct A { int a = 1; };
struct B : public A { int b = 2; };
struct C : public B { int c = 3; };

void inspect(A* ptr) {
    std::cout << ptr->a << " ";
}

int main() {
    C obj;
    inspect(&obj); // Upcast từ C* thẳng lên A*
    B* bPtr = &obj; // Upcast C* lên B*
    inspect(bPtr);  // Upcast B* lên A*
    return 0;
}""",
    "options": [
        "A. 1 1 (Upcast qua nhiều thế hệ hoàn toàn ngầm định và bảo toàn tính đúng đắn của offset địa chỉ)",
        "B. Lỗi biên dịch vì C không kế thừa trực tiếp từ A",
        "C. 3 2",
        "D. 1 2"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Kế thừa là mối quan hệ có tính bắc cầu: Nếu C là con của B, và B là con của A, thì C cũng là một loại A (C IS-A A).<br>"
                   "2. Trong đơn kế thừa, subobject của A nằm ngay tại offset 0 của B, và subobject của B nằm ngay tại offset 0 của C. Do đó <code>&obj</code>, <code>bPtr</code> và <code>(A*)&obj</code> đều cùng chỉ tới một địa chỉ bộ nhớ.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 58-60: Upcasting nhiều cấp]</span>"
})

questions.append({
    "id": 33,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Upcast, Downcast & Object Slicing",
    "title": "Chuyển đổi con trỏ hàm thành viên trong cây kế thừa (Contravariance)",
    "code": """#include <iostream>

struct Base {
    void speak() { std::cout << "BaseSpeak "; }
};

struct Derived : public Base {
    void shout() { std::cout << "DerivedShout "; }
};

int main() {
    void (Derived::*funcPtr)() = &Base::speak; // Trỏ hàm của Base bằng con trỏ hàm của Derived
    Derived d;
    (d.*funcPtr)();
    return 0;
}""",
    "options": [
        "A. In ra: BaseSpeak (Con trỏ hàm thành viên có tính nghịch biến - Contravariance: con trỏ hàm Base có thể gán cho con trỏ hàm Derived)",
        "B. Lỗi biên dịch: không thể gán con trỏ hàm Base cho con trỏ hàm Derived",
        "C. Lỗi runtime do sai lệch con trỏ this",
        "D. In ra: DerivedShout"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <strong>Quy tắc nghịch biến của con trỏ hàm thành viên:</strong> Một con trỏ hàm nhận đối tượng <code>Derived</code> có thể an toàn gọi một hàm của <code>Base</code> (vì mọi <code>Derived</code> đều có phần <code>Base</code> bên trong).<br>"
                   "2. Do đó phép gán <code>void (Derived::*funcPtr)() = &Base::speak;</code> là hoàn toàn hợp lệ theo chuẩn C++.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 61 & C++11 Member Function Pointer rules]</span>"
})

questions.append({
    "id": 34,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Upcast, Downcast & Object Slicing",
    "title": "Hiểm họa giải phóng đối tượng Upcast khi Base thiếu Virtual Destructor",
    "code": """#include <iostream>
#include <memory>

struct Base {
    ~Base() { std::cout << "~Base "; } // Không có virtual!
};

struct Derived : public Base {
    int* buffer;
    Derived() : buffer(new int[100]) {}
    ~Derived() {
        delete[] buffer;
        std::cout << "~Derived ";
    }
};

int main() {
    Base* p = new Derived();
    delete p; // Bẫy cực kỳ nguy hiểm!
    return 0;
}""",
    "options": [
        "A. ~Derived ~Base (Giải phóng bình thường)",
        "B. Chỉ in ra ~Base (Destructor của Derived bị bỏ qua hoàn toàn, rò rỉ bộ nhớ mảng buffer và gây Undefined Behavior)",
        "C. Lỗi biên dịch tại delete p",
        "D. Chương trình crash với ngoại lệ std::bad_alloc"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Chuẩn C++ (§5.3.5/3) quy định: Nếu kiểu tĩnh của con trỏ được truyền vào lệnh <code>delete</code> khác với kiểu động của đối tượng thực sự và lớp cơ sở <strong>KHÔNG CÓ VIRTUAL DESTRUCTOR</strong> thì hành vi là <strong>UNDEFINED BEHAVIOR (UB)</strong>!<br>"
                   "2. Trong hầu hết các trình biên dịch, nó chỉ liên kết tĩnh tới <code>Base::~Base()</code>, thân hàm <code>Derived::~Derived()</code> không bao giờ được chạy, dẫn tới rò rỉ toàn bộ tài nguyên heap (100 phần tử int) mà Derived nắm giữ.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 30 & OOP6-Polymorphism_new.pdf - Trang 27-30: Destructor ảo]</span>"
})

print(f"Loaded {len(questions)} questions for Groups 1-4.")
# =========================================================================
# NHÓM 5: ĐA KẾ THỪA, SỰ MƠ HỒ & KẾ THỪA ẢO (DIAMOND PROBLEM) (CÂU 35 - 44)
# =========================================================================

questions.append({
    "id": 35,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Đa Kế Thừa & Kế Thừa Ảo (Diamond Problem)",
    "title": "Sự mơ hồ (Ambiguity) khi đa kế thừa từ hai lớp có phương thức trùng tên",
    "code": """#include <iostream>

struct Printer {
    void print() { std::cout << "Printing "; }
};

struct Scanner {
    void print() { std::cout << "ScanningPreview "; }
};

struct MultiFunctionPrinter : public Printer, public Scanner {
    // Không định nghĩa lại print()
};

int main() {
    MultiFunctionPrinter mfp;
    // mfp.print(); // Dòng A: Bẫy mơ hồ!
    mfp.Printer::print(); // Dòng B
    return 0;
}""",
    "options": [
        "A. Dòng B in ra 'Printing '; Dòng A nếu mở ra sẽ bị LỖI BIÊN DỊCH do trình biên dịch không thể quyết định gọi print() của Printer hay Scanner",
        "B. Dòng A tự động ưu tiên lớp khai báo trước (Printer)",
        "C. Cả Dòng A và Dòng B đều bị lỗi biên dịch",
        "D. Dòng A in ra cả hai chuỗi"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong đa kế thừa, khi hai lớp cha độc lập có phương thức cùng tên, việc gọi <code>mfp.print()</code> tạo ra một tình huống <strong>Mơ hồ (Ambiguity)</strong> trong quá trình Name Lookup.<br>"
                   "2. Trình biên dịch không được phép tự ý thiên vị lớp nào, do đó nó báo lỗi biên dịch ngay lập tức.<br>"
                   "3. Để giải quyết, lập trình viên bắt buộc phải dùng toán tử phân giải phạm vi tường minh như <code>mfp.Printer::print()</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 71-72: Đa thừa kế và Sự mơ hồ]</span>"
})

questions.append({
    "id": 36,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Đa Kế Thừa & Kế Thừa Ảo (Diamond Problem)",
    "title": "Bẫy nhân bản lớp cơ sở trong cấu trúc hình thoi (Diamond Problem) không có virtual",
    "code": """#include <iostream>

struct Device {
    int id = 100;
};

struct Phone : public Device {};
struct Computer : public Device {};

struct SmartPhone : public Phone, public Computer {};

int main() {
    SmartPhone sp;
    // std::cout << sp.id; // Dòng X
    std::cout << sp.Phone::id << " " << sp.Computer::id << " | Size=" << sizeof(sp);
    return 0;
}""",
    "options": [
        "A. In ra: 100 100 | Size=8 (sp chứa HAI bản sao riêng biệt của Device, Dòng X bị lỗi biên dịch do ambiguous)",
        "B. In ra: 100 100 | Size=4",
        "C. Dòng X in ra 100 bình thường",
        "D. Lỗi biên dịch vì không được phép kế thừa kiểu hình thoi"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi không có từ khóa <code>virtual</code>, <code>Phone</code> sở hữu 1 bản sao <code>Device</code> (4 bytes) và <code>Computer</code> sở hữu 1 bản sao <code>Device</code> độc lập khác (4 bytes).<br>"
                   "2. Đối tượng <code>SmartPhone</code> chứa cả 2 nhánh, dẫn đến kích thước <code>sizeof(sp) = 8 bytes</code>.<br>"
                   "3. Lệnh <code>sp.id</code> tại Dòng X không thể biết lấy <code>id</code> của nhánh Phone hay nhánh Computer -> Lỗi biên dịch mơ hồ.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 72-74: Cấu trúc hình thoi & Sự mơ hồ]</span>"
})

questions.append({
    "id": 37,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Đa Kế Thừa & Kế Thừa Ảo (Diamond Problem)",
    "title": "Thứ tự gọi Constructor trong Đa kế thừa phụ thuộc vào thứ tự khai báo class",
    "code": """#include <iostream>

struct A { A() { std::cout << "A "; } };
struct B { B() { std::cout << "B "; } };
struct C { C() { std::cout << "C "; } };

// Thứ tự khai báo trong định nghĩa class: B, rồi tới A, rồi tới C
struct Derived : public B, public A, public C {
    // Thứ tự trong Member Init List cố tình đảo ngược: C, A, B
    Derived() : C(), A(), B() {
        std::cout << "Derived ";
    }
};

int main() {
    Derived d;
    return 0;
}""",
    "options": [
        "A. C A B Derived (Theo thứ tự trong member init list)",
        "B. B A C Derived (Thứ tự thực thi constructor của các Base HOÀN TOÀN phụ thuộc thứ tự khai báo ở đầu class)",
        "C. A B C Derived (Theo thứ tự bảng chữ cái)",
        "D. Lỗi biên dịch vì thứ tự trong danh sách khởi tạo không khớp thứ tự khai báo"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Chuẩn C++ (§12.6.2) quy định: Thứ tự khởi tạo các lớp cơ sở luôn luôn và tuyệt đối tuân theo <strong>thứ tự xuất hiện trong danh sách dẫn xuất của khai báo lớp</strong> (ở đây là <code>public B, public A, public C</code>).<br>"
                   "2. Bất kỳ thứ tự nào bạn viết trong Member Initializer List của constructor đều bị trình biên dịch bỏ qua về mặt thứ tự thực thi -> luôn in ra <code>B A C Derived </code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 70-71: Thứ tự khởi tạo trong đa thừa kế]</span>"
})

questions.append({
    "id": 38,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Đa Kế Thừa & Kế Thừa Ảo (Diamond Problem)",
    "title": "Kế thừa ảo (Virtual Inheritance) giải quyết triệt để vấn đề nhân bản subobject",
    "code": """#include <iostream>

struct Device {
    int id = 42;
};

// Kế thừa ảo (virtual public)
struct Phone : virtual public Device {};
struct Computer : virtual public Device {};

struct SmartPhone : public Phone, public Computer {};

int main() {
    SmartPhone sp;
    sp.id = 99; // Truy cập trực tiếp không còn mơ hồ!
    std::cout << sp.Phone::id << " " << sp.Computer::id << " " << sp.id;
    return 0;
}""",
    "options": [
        "A. 99 99 99 (Chỉ có duy nhất một thể hiện Device dùng chung cho toàn bộ cấu trúc hình thoi)",
        "B. 42 42 99",
        "C. Lỗi biên dịch vì vẫn tồn tại 2 biến id",
        "D. 99 42 99"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Với <code>virtual public Device</code>, trình biên dịch đảm bảo trong đối tượng <code>SmartPhone</code> chỉ tồn tại duy nhất <strong>MỘT subobject Device chia sẻ chung</strong>.<br>"
                   "2. Khi thay đổi <code>sp.id = 99</code>, cả hai góc nhìn <code>sp.Phone::id</code> và <code>sp.Computer::id</code> đều trỏ vào cùng một ô nhớ duy nhất đó, cho ra giá trị đồng nhất <code>99 99 99</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 74-75: Lớp cơ sở ảo và giải quyết đa thừa kế]</span>"
})

questions.append({
    "id": 39,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Đa Kế Thừa & Kế Thừa Ảo (Diamond Problem)",
    "title": "Quy tắc đặc quyền của Most-Derived Class khi khởi tạo Virtual Base",
    "code": """#include <iostream>

struct Base {
    Base(int val) { std::cout << "Base(" << val << ") "; }
};

struct Left : virtual public Base {
    Left() : Base(10) { std::cout << "Left "; }
};

struct Right : virtual public Base {
    Right() : Base(20) { std::cout << "Right "; }
};

struct Bottom : public Left, public Right {
    // Bottom là Most-Derived Class, nó trực tiếp chỉ định constructor của Base!
    Bottom() : Base(30), Left(), Right() {
        std::cout << "Bottom ";
    }
};

int main() {
    Bottom b;
    return 0;
}""",
    "options": [
        "A. Base(10) Left Base(20) Right Bottom",
        "B. Base(30) Left Right Bottom (Lớp dẫn xuất xa nhất Bottom trực tiếp khởi tạo Virtual Base, các lời gọi Base từ Left và Right bị bỏ qua hoàn toàn)",
        "C. Base(10) Left Right Bottom",
        "D. Lỗi biên dịch vì Base được gọi 3 lần"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <strong>Quy tắc Virtual Base Constructor:</strong> Đối với một lớp cơ sở ảo, trách nhiệm gọi constructor của nó thuộc về <strong>Lớp dẫn xuất xa nhất (Most-Derived Class - ở đây là <code>Bottom</code>)</strong>.<br>"
                   "2. Lời gọi <code>Base(10)</code> trong <code>Left</code> và <code>Base(20)</code> trong <code>Right</code> hoàn toàn bị trình biên dịch <strong>BỎ QUA</strong> khi đối tượng <code>Bottom</code> được khởi tạo.<br>"
                   "3. <code>Base(30)</code> được thực thi đầu tiên trước tất cả, sau đó đến Left, Right và Bottom -> in ra <code>Base(30) Left Right Bottom </code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 74-75: Thứ tự khởi tạo lớp cơ sở ảo]</span>"
})

questions.append({
    "id": 40,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Đa Kế Thừa & Kế Thừa Ảo (Diamond Problem)",
    "title": "Bẫy biên dịch khi Most-Derived Class không khởi tạo Virtual Base thiếu Default Ctor",
    "code": """#include <iostream>

struct Base {
    Base(int x) {} // Không có default ctor!
};

struct BranchA : virtual public Base {
    BranchA() : Base(1) {}
};

struct BranchB : virtual public Base {
    BranchB() : Base(2) {}
};

struct FinalDerived : public BranchA, public BranchB {
    // Quên gọi Base(val) trong danh sách khởi tạo!
    FinalDerived() : BranchA(), BranchB() {}
};

int main() {
    // FinalDerived obj; // Dòng Err
    return 0;
}""",
    "options": [
        "A. Biên dịch thành công vì BranchA đã gọi Base(1)",
        "B. Lỗi biên dịch tại FinalDerived: no matching function for call to 'Base::Base()' (Most-Derived class bắt buộc phải tự gọi Base(int) vì Base không có default constructor)",
        "C. Lỗi runtime bad_initialization",
        "D. Tự động lấy Base(1) của BranchA"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Vì <code>FinalDerived</code> là most-derived class, nó chịu trách nhiệm khởi tạo <code>Base</code> ảo.<br>"
                   "2. Do nó không gọi tường minh constructor có tham số của <code>Base</code>, compiler cố gắng gọi ngầm định <code>Base::Base()</code>.<br>"
                   "3. Nhưng <code>Base</code> không có default constructor, dẫn đến lỗi biên dịch ngay lập tức dù cho cả <code>BranchA</code> và <code>BranchB</code> đều có gọi <code>Base</code> trong code của chúng!<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 74: Trách nhiệm khởi tạo Virtual Base]</span>"
})

questions.append({
    "id": 41,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Đa Kế Thừa & Kế Thừa Ảo (Diamond Problem)",
    "title": "Độ lệch con trỏ (Pointer Offset Adjustment) khi ép kiểu trong Đa kế thừa",
    "code": """#include <iostream>

struct BaseA {
    int a;
};

struct BaseB {
    int b;
};

struct Derived : public BaseA, public BaseB {
    int c;
};

int main() {
    Derived d;
    BaseA* pA = &d;
    BaseB* pB = &d;

    std::cout << (void*)pA << " ";
    std::cout << (void*)pB << " ";
    std::cout << (pA == (BaseA*)pB ? "Same" : "Different");
    return 0;
}""",
    "options": [
        "A. pA và pB luôn cùng địa chỉ byte 0",
        "B. Địa chỉ pB lệch so với pA chính xác một khoảng bằng sizeof(BaseA) (Pointer Adjustment để trỏ đúng vào subobject BaseB)",
        "C. Lỗi biên dịch vì không thể gán &d cho BaseB*",
        "D. pB luôn có giá trị nullptr"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong bố cục RAM của <code>Derived</code>, subobject <code>BaseA</code> nằm ở offset 0. Nhưng subobject <code>BaseB</code> nằm ngay sau <code>BaseA</code> (tại offset +4 bytes).<br>"
                   "2. Khi thực hiện <code>BaseB* pB = &d;</code>, trình biên dịch thực hiện phép tính <strong>Pointer Adjustment</strong>: lấy địa chỉ <code>&d</code> cộng thêm <code>sizeof(BaseA)</code> (4 bytes).<br>"
                   "3. Do đó, địa chỉ raw của <code>pA</code> và <code>pB</code> là khác nhau hoàn toàn trong bộ nhớ!<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 71: Bố cục bộ nhớ đa thừa kế]</span>"
})

questions.append({
    "id": 42,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Đa Kế Thừa & Kế Thừa Ảo (Diamond Problem)",
    "title": "Bẫy con trỏ cơ sở ảo (vbptr) và sự phình to kích thước đối tượng",
    "code": """#include <iostream>

struct EmptyBase {};

struct VDerived1 : virtual public EmptyBase {};
struct VDerived2 : virtual public EmptyBase {};

struct Bottom : public VDerived1, public VDerived2 {};

int main() {
    // Trên hệ điều hành 64-bit, con trỏ có kích thước 8 bytes
    std::cout << (sizeof(VDerived1) >= sizeof(void*)) << " ";
    std::cout << (sizeof(Bottom) >= sizeof(void*)) << std::endl;
    return 0;
}""",
    "options": [
        "A. 1 1 (Kế thừa ảo đòi hỏi lưu trữ con trỏ vbptr - Virtual Base Pointer để định vị subobject động tại runtime, làm tăng kích thước đối tượng)",
        "B. 0 0 (Empty Base Optimization làm cho kích thước bằng 0)",
        "C. 0 1",
        "D. Lỗi biên dịch"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi kế thừa ảo, vị trí của Virtual Base Subobject không còn cố định ở một offset tĩnh đơn giản. Lớp dẫn xuất phải chèn thêm một con trỏ cơ sở ảo (<strong>vbptr</strong>) hoặc mở rộng bảng ảo VTable để chứa bảng độ lệch (offset table).<br>"
                   "2. Do đó, dù <code>EmptyBase</code> rỗng hoàn toàn, <code>VDerived1</code> và <code>Bottom</code> vẫn phình to ít nhất bằng kích thước của 1-2 con trỏ (8 đến 16 bytes trên nền tảng 64-bit).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 74: Chi phí bộ nhớ của lớp cơ sở ảo]</span>"
})

questions.append({
    "id": 43,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Đa Kế Thừa & Kế Thừa Ảo (Diamond Problem)",
    "title": "Lỗi biên dịch Upcast mơ hồ trong mô hình hình thoi không ảo",
    "code": """#include <iostream>

struct Base {};
struct Mid1 : public Base {};
struct Mid2 : public Base {};
struct Final : public Mid1, public Mid2 {};

int main() {
    Final f;
    // Base* p = &f; // Dòng U: Bẫy ép kiểu Upcast!
    Base* p1 = (Mid1*)&f; // Dòng U1
    return 0;
}""",
    "options": [
        "A. Dòng U1 hợp lệ; Dòng U bị LỖI BIÊN DỊCH: 'Base' is an ambiguous base of 'Final' (Có 2 subobject Base khác nhau, compiler không biết trỏ vào đâu)",
        "B. Cả Dòng U và U1 đều hợp lệ",
        "C. Dòng U tự động chọn nhánh Mid1",
        "D. Cả hai dòng đều bị lỗi biên dịch"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong bộ nhớ của <code>Final</code>, tồn tại 2 subobject <code>Base</code> riêng biệt: một nằm trong <code>Mid1</code> và một nằm trong <code>Mid2</code>.<br>"
                   "2. Khi viết <code>Base* p = &f;</code>, trình biên dịch không thể quyết định dịch chuyển con trỏ tới subobject nào -> sinh lỗi <em>ambiguous base class</em>.<br>"
                   "3. Ở Dòng U1, lập trình viên chỉ rõ thông qua nhánh <code>(Mid1*)&f</code> nên trình biên dịch xác định được chính xác địa chỉ.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 72: Mơ hồ khi upcast hình thoi]</span>"
})

questions.append({
    "id": 44,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Đa Kế Thừa & Kế Thừa Ảo (Diamond Problem)",
    "title": "Cross-casting giữa hai nhánh độc lập bằng dynamic_cast",
    "code": """#include <iostream>

struct IA {
    virtual void funcA() = 0;
    virtual ~IA() = default;
};

struct IB {
    virtual void funcB() = 0;
    virtual ~IB() = default;
};

struct Service : public IA, public IB {
    void funcA() override { std::cout << "A "; }
    void funcB() override { std::cout << "B "; }
};

int main() {
    IA* pA = new Service();
    IB* pB = dynamic_cast<IB*>(pA); // Cross-cast ngang giữa 2 interface!
    if (pB != nullptr) {
        pB->funcB();
    }
    delete pA;
    return 0;
}""",
    "options": [
        "A. In ra: B (dynamic_cast tra cứu bảng RTTI tại runtime và dịch con trỏ ngang qua nhánh IB thành công)",
        "B. Lỗi biên dịch vì IA và IB không có quan hệ cha con",
        "C. dynamic_cast trả về nullptr",
        "D. Chương trình crash do sai lệch VTable"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Mặc dù <code>IA</code> và <code>IB</code> không hề kế thừa lẫn nhau, nhưng đối tượng thực tế đằng sau là <code>Service</code> (kế thừa cả hai).<br>"
                   "2. Tại runtime, <code>dynamic_cast</code> kiểm tra bảng RTTI của đối tượng <code>Service</code>, nhận diện rằng đối tượng hoàn chỉnh có cài đặt <code>IB</code>, và tự động điều chỉnh con trỏ (<strong>Cross-Cast</strong>) từ subobject <code>IA</code> sang subobject <code>IB</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 68 & 70: Ép kiểu ngang trong đa kế thừa]</span>"
})

print(f"Loaded {len(questions)} questions for Groups 1-5.")
# =========================================================================
# NHÓM 6: BÀI TẬP THỰC TẾ, BẪY NÂNG CAO & C++11 FEATURES (CÂU 45 - 50)
# =========================================================================

questions.append({
    "id": 45,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Bài Tập Thực Tế & C++11 Features",
    "title": "Kế thừa toàn bộ Constructor của lớp cha bằng using Base::Base trong C++11",
    "code": """#include <iostream>

class Base {
public:
    Base(int a) { std::cout << "B(" << a << ") "; }
    Base(double d) { std::cout << "B(" << d << ") "; }
};

class Derived : public Base {
public:
    using Base::Base; // Kế thừa toàn bộ constructors của Base trong C++11!
};

int main() {
    Derived d1(42);
    Derived d2(3.14);
    return 0;
}""",
    "options": [
        "A. B(42) B(3.14) (C++11 cho phép importing constructors của lớp cơ sở thông qua cú pháp using Base::Base)",
        "B. Lỗi biên dịch vì Derived không tự định nghĩa constructor nào",
        "C. Chỉ có Base(int) được kế thừa",
        "D. Constructors của Base bị biến thành private trong Derived"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trước C++11, lớp dẫn xuất phải viết lại toàn bộ các constructor chuyển tiếp (forwarding constructors) cho từng overload của lớp cha.<br>"
                   "2. Chuẩn C++11 giới thiệu tính năng <strong>Inheriting Constructors</strong>: chỉ thị <code>using Base::Base;</code> yêu cầu trình biên dịch tự động sinh tất cả các hàm tạo tương ứng trong <code>Derived</code> để chuyển tiếp tham số lên <code>Base</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: C++11 Standard & OOP5-Inheritance_new.pdf - Trang 29: Kế thừa hàm dựng]</span>"
})

questions.append({
    "id": 46,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Bài Tập Thực Tế & C++11 Features",
    "title": "Bẫy giá trị rác khi dùng using Base::Base nhưng Derived có thành viên riêng",
    "code": """#include <iostream>

struct Base {
    Base(int x) {}
};

struct Derived : public Base {
    using Base::Base;
    int extra; // Thành viên riêng không có in-class initializer!
};

int main() {
    Derived d(10);
    // extra nhận giá trị gì?
    std::cout << (sizeof(d.extra) == sizeof(int)) << std::endl;
    return 0;
}""",
    "options": [
        "A. d.extra luôn tự động bằng 0",
        "B. 1 (d.extra không được khởi tạo và nhận giá trị rác ngẫu nhiên trên stack; C++11 khuyến nghị dùng in-class initializer: int extra = 0;)",
        "C. Lỗi biên dịch vì Derived có thành viên chưa được khởi tạo",
        "D. Chương trình ném ngoại lệ uninitialized_memory"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi sử dụng <code>using Base::Base;</code>, constructor được sinh tự động bởi trình biên dịch chỉ khởi tạo <code>Base</code> subobject.<br>"
                   "2. Các thành viên riêng của <code>Derived</code> (như <code>extra</code>) nếu không có khởi tạo mặc định tại chỗ (in-class member initializer <code>int extra = 0;</code>) sẽ bị bỏ mặc với <strong>giá trị rác (uninitialized memory)</strong>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 30 & C++11 Inheriting Constructor Caveats]</span>"
})

questions.append({
    "id": 47,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Bài Tập Thực Tế & C++11 Features",
    "title": "Bẫy Two-Phase Name Lookup khi kế thừa từ Template Base Class",
    "code": """#include <iostream>

template <typename T>
struct Base {
    int data = 100;
};

template <typename T>
struct Derived : public Base<T> {
    void print() {
        // std::cout << data; // Dòng Lỗi: Trình biên dịch không tìm thấy 'data'!
        std::cout << this->data << " "; // Cách giải quyết chuẩn
    }
};

int main() {
    Derived<int> d;
    d.print();
    return 0;
}""",
    "options": [
        "A. In ra 100; Ở template C++, tên thành viên của base class phụ thuộc vào tham số kiểu T (Dependent Name) nên bắt buộc phải dùng this->data hoặc Base<T>::data",
        "B. Trình biên dịch luôn tự tìm thấy data mà không cần this->",
        "C. Lỗi biên dịch tại Derived<int> d;",
        "D. d.print() in ra giá trị 0"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong lập trình Template C++, cơ chế <strong>Two-Phase Name Lookup</strong> quy định: Ở Phase 1 (khi phân tích cú pháp template), trình biên dịch không biết kiểu <code>Base<T></code> có những thành viên nào (vì có thể có Specialization sau này).<br>"
                   "2. Một tên không phụ thuộc như <code>data</code> sẽ không được tìm kiếm bên trong base class mẫu. Do đó nếu viết trần trụi <code>data</code>, compiler báo lỗi <em>'data' was not declared in this scope</em>.<br>"
                   "3. Viết <code>this->data</code> biến nó thành một Dependent Name, hoãn việc tra cứu sang Phase 2 (khi đã khởi tạo kiểu cụ thể).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf & C++11 Two-Phase Lookup Rules]</span>"
})

questions.append({
    "id": 48,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Bài Tập Thực Tế & C++11 Features",
    "title": "Kỹ thuật an toàn khi xử lý Tự gán (Self-Assignment) trong Kế thừa",
    "code": """#include <iostream>

struct Base {
    int* p;
    Base(int val = 0) : p(new int(val)) {}
    virtual ~Base() { delete p; }
    Base& operator=(const Base& rhs) {
        if (this != &rhs) { // Kiểm tra tự gán
            *p = *rhs.p;
        }
        return *this;
    }
};

struct Derived : public Base {
    int* extra;
    Derived(int v1, int v2) : Base(v1), extra(new int(v2)) {}
    ~Derived() { delete extra; }
    Derived& operator=(const Derived& rhs) {
        if (this != &rhs) {
            Base::operator=(rhs); // Chuyển giao phần Base
            *extra = *rhs.extra;
        }
        return *this;
    }
};

int main() {
    Derived d1(10, 20);
    d1 = d1; // Tự gán (Self-assignment)
    std::cout << *d1.p << " " << *d1.extra;
    return 0;
}""",
    "options": [
        "A. 10 20 (An toàn vì cả hai lớp đều có cơ chế kiểm tra self-assignment this != &rhs)",
        "B. Lỗi runtime phân mảnh bộ nhớ do delete trúng ô nhớ đang dùng",
        "C. 0 0",
        "D. Lỗi biên dịch vì toán tử gán không được kế thừa"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong kế thừa, việc quản lý tài nguyên thô qua toán tử gán đòi hỏi sự phối hợp nhịp nhàng giữa lớp con và lớp cha.<br>"
                   "2. Lớp con <code>Derived</code> kiểm tra <code>this != &rhs</code>, sau đó gọi <code>Base::operator=(rhs);</code> để lớp cha xử lý phần subobject của nó.<br>"
                   "3. Nhờ cơ chế kiểm tra địa chỉ con trỏ <code>this</code>, lệnh tự gán <code>d1 = d1;</code> kết thúc an toàn mà không làm hủy hoại dữ liệu vùng nhớ heap.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP4-OperatorOverloading_new.pdf & OOP5-Inheritance_new.pdf - Trang 75: Toán tử gán trong kế thừa]</span>"
})

questions.append({
    "id": 49,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Bài Tập Thực Tế & C++11 Features",
    "title": "Private Inheritance mô phỏng quan hệ HAS-A (Composition)",
    "code": """#include <iostream>

class Engine {
public:
    void ignite() { std::cout << "Vroom "; }
};

// Sử dụng private inheritance thay cho việc nhúng biến thành viên
class Car : private Engine {
public:
    void drive() {
        ignite(); // Sử dụng cài đặt của Engine
        std::cout << "Driving ";
    }
};

int main() {
    Car c;
    c.drive();
    // Engine* p = &c; // Dòng E
    return 0;
}""",
    "options": [
        "A. In ra: Vroom Driving; Dòng E bị LỖI BIÊN DỊCH vì quan hệ private inheritance thể hiện 'is-implemented-in-terms-of' chứ không phải IS-A công khai",
        "B. Dòng E hợp lệ",
        "C. In ra Driving Vroom",
        "D. Lỗi biên dịch tại ignite() trong thân Car"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Thiết kế phần mềm C++ kinh điển quy định: <code>public inheritance</code> biểu thị quan hệ <strong>IS-A</strong> (Xe ô tô là phương tiện), trong khi <code>private inheritance</code> biểu thị quan hệ <strong>'is-implemented-in-terms-of'</strong> (được cài đặt dựa trên).<br>"
                   "2. Private inheritance cho phép lớp con tái sử dụng mã nguồn và ghi đè hàm ảo của Engine nhưng che giấu hoàn toàn giao diện Engine đối với người dùng (Dòng E sẽ lỗi biên dịch).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 33-35 & 47-49: Quan hệ IS-A vs HAS-A]</span>"
})

questions.append({
    "id": 50,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Bài Tập Thực Tế & C++11 Features",
    "title": "Bẫy Move Constructor trong Kế thừa: Quên dùng std::move cho Base Subobject",
    "code": """#include <iostream>
#include <utility>

struct Base {
    Base() = default;
    Base(const Base&) { std::cout << "BaseCopy "; }
    Base(Base&&) noexcept { std::cout << "BaseMove "; }
};

struct Derived : public Base {
    Derived() = default;
    Derived(const Derived& other) : Base(other) {}
    // Bẫy Move Constructor: Truyền 'other' thay vì 'std::move(other)'
    Derived(Derived&& other) noexcept : Base(other) {
        std::cout << "DerivedMove ";
    }
};

int main() {
    Derived d1;
    Derived d2 = std::move(d1); // Kích hoạt Move Constructor
    return 0;
}""",
    "options": [
        "A. BaseMove DerivedMove",
        "B. BaseCopy DerivedMove (Vì tham số 'other' có tên nên nó là một lvalue, Base(other) vô tình gọi Base Copy Ctor thay vì Move Ctor!)",
        "C. DerivedMove DerivedMove",
        "D. Lỗi biên dịch vì không thể truyền Derived rvalue vào Base"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <strong>Quy tắc giá trị C++11 (Value Category):</strong> Dù tham số có kiểu rvalue reference <code>Derived&& other</code>, nhưng bản thân biểu thức định danh <code>other</code> là một <strong>LVALUE</strong> (vì nó có tên và có địa chỉ bộ nhớ cố định).<br>"
                   "2. Khi truyền <code>Base(other)</code>, trình biên dịch thấy <code>other</code> là lvalue nên nó sẽ chọn <strong>Copy Constructor</strong> <code>Base(const Base&)</code> thay vì Move Constructor!<br>"
                   "3. Để di chuyển thực sự, lập trình viên bắt buộc phải viết: <code>Base(std::move(other))</code> để ép <code>other</code> về rvalue (xvalue). Đây là một trong những bẫy hiệu năng tinh vi nhất trong lập trình C++11 hiện đại.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP5-Inheritance_new.pdf - Trang 30 & C++11 Move Semantics & Rvalue references]</span>"
})

print(f"Loaded ALL {len(questions)} questions for Chapter 5 successfully!")
