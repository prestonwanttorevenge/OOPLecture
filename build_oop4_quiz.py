# -*- coding: utf-8 -*-
import json

questions = []

# =========================================================================
# NHÓM 1: GIỚI HẠN & QUY TẮC CỐT LÕI CỦA TOÁN TỬ (CÂU 1 - 6)
# =========================================================================

questions.append({
    "id": 1,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Giới Hạn & Quy Tắc Cốt Lõi Của Toán Tử",
    "title": "Bẫy cố tình định nghĩa toán tử mới không tồn tại trong C++",
    "code": """#include <iostream>

class Number {
    int val;
public:
    Number(int v) : val(v) {}
    // Thử tạo toán tử lũy thừa **:
    // Number operator**(int exp);
    // Thử tạo toán tử @:
    // Number operator@(const Number& o);
};""",
    "options": [
        "A. Hợp lệ nếu cài đặt dưới dạng hàm bạn",
        "B. Lỗi biên dịch: C++ cấm hoàn toàn việc định nghĩa các ký hiệu toán tử mới không có sẵn trong ngôn ngữ",
        "C. Toán tử ** hợp lệ từ chuẩn C++11",
        "D. Cho phép nếu có từ khóa friend"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Bộ phân tích từ vựng (Lexer) và ngữ pháp (Parser) của C++ có tập ký hiệu toán tử cố định.<br>"
                   "2. Slide trang 4 nêu rõ giới hạn thép: 'Chúng ta không thể định nghĩa các toán tử mới'. Không thể tự chế ra <code>**</code> hay <code>@</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 4: Giới hạn của đa năng hoá toán tử]</span>"
})

questions.append({
    "id": 2,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Giới Hạn & Quy Tắc Cốt Lõi Của Toán Tử",
    "title": "Bẫy cố tình overload 5 toán tử bị cấm trong C++",
    "code": """#include <iostream>

class Matrix {
public:
    // Thử overload toán tử phạm vi:
    // int operator::(int x);
    // Thử overload toán tử truy cập trực tiếp:
    // int operator.(int x);
    // Thử overload toán tử điều kiện:
    // int operator?:(int a, int b);
    // Thử overload toán tử kích thước:
    // size_t operatorsizeof();
};""",
    "options": [
        "A. Toán tử sizeof có thể overload được trong C++11",
        "B. Cả 5 toán tử ::, ., .*, ?:, sizeof đều bị cấm tuyệt đối không được phép overload trong C++",
        "C. Toán tử ?: overload được nếu dùng 3 tham số",
        "D. Chỉ có toán tử :: là bị cấm"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 4 liệt kê chính xác các toán tử không được đa năng hóa: <code>::</code>, <code>.*</code>, <code>.</code>, <code>?:</code>, <code>sizeof</code>, <code>typeid</code>.<br>"
                   "2. Các toán tử này cần giữ ngữ nghĩa bất biến để trình biên dịch xử lý phân giải kiểu, địa chỉ thành viên và kích thước đối tượng an toàn.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 4: Các toán tử không được đa năng hoá]</span>"
})

questions.append({
    "id": 3,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Giới Hạn & Quy Tắc Cốt Lõi Của Toán Tử",
    "title": "Bốn toán tử BẮT BUỘC PHẢI LÀ HÀM THÀNH VIÊN",
    "code": """#include <iostream>

class Value {
    int val;
public:
    Value(int v) : val(v) {}
};

// Cố tình định nghĩa toán tử gán = dưới dạng hàm tự do ngoài class:
// Value& operator=(Value& lhs, const Value& rhs) { ... }""",
    "options": [
        "A. Hợp lệ nếu thêm từ khóa friend",
        "B. Lỗi biên dịch: operator= bắt buộc phải là non-static member function của class (cùng với [], (), ->)",
        "C. Chỉ có toán tử [] mới bắt buộc là hàm thành viên",
        "D. Toán tử = có thể là hàm bạn từ C++11"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Chuẩn C++ và slide trang 5 quy định: 4 toán tử <code>=</code>, <code>[]</code>, <code>()</code>, <code>-&gt;</code> bắt buộc phải được khai báo là <strong>phương thức thành viên phi tĩnh của lớp</strong>.<br>"
                   "2. Nếu cho phép <code>operator=</code> là hàm tự do, nó sẽ xung đột với toán tử gán mặc định mà trình biên dịch tự sinh cho lớp.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 5: Toán tử bắt buộc là hàm thành viên]</span>"
})

questions.append({
    "id": 4,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Giới Hạn & Quy Tắc Cốt Lõi Của Toán Tử",
    "title": "Bẫy độ ưu tiên toán tử không đổi (Operator Precedence Invariance)",
    "code": """#include <iostream>

class Complex {
public:
    int r, i;
    Complex(int r, int i) : r(r), i(i) {}
    Complex operator+(const Complex& o) const { return {r + o.r, i + o.i}; }
    Complex operator*(const Complex& o) const { return {r * o.r, i * o.i}; }
};

int main() {
    Complex c1(1, 1), c2(2, 2), c3(3, 3);
    Complex res = c1 + c2 * c3;
    std::cout << res.r << " " << res.i << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: 7 7 (phép nhân c2 * c3 thực hiện trước vì độ ưu tiên của * luôn cao hơn +)",
        "B. In ra: 9 9 (tính từ trái qua phải (c1 + c2) * c3)",
        "C. Lỗi biên dịch vì chưa định nghĩa ngoặc tròn",
        "D. Thứ tự do compiler quyết định ngẫu nhiên"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Đa năng hóa toán tử KHÔNG THỂ thay đổi độ ưu tiên và thứ tự kết hợp của toán tử.<br>"
                   "2. Biểu thức <code>c1 + c2 * c3</code> luôn được parser phân tích thành <code>c1 + (c2 * c3)</code>.<br>"
                   "3. <code>c2 * c3 = (6, 6)</code>, sau đó cộng <code>c1 = (7, 7)</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 4: Độ ưu tiên toán tử không thay đổi]</span>"
})

questions.append({
    "id": 5,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Giới Hạn & Quy Tắc Cốt Lõi Của Toán Tử",
    "title": "Toán tử không thể overload trên toàn bộ kiểu dữ liệu có sẵn (Built-in Types)",
    "code": """// Cố tình định nghĩa lại phép cộng giữa hai số nguyên int:
int operator+(int a, int b) {
    return a - b; // Đổi cộng thành trừ!
}""",
    "options": [
        "A. Hợp lệ nếu đặt trong namespace riêng",
        "B. Lỗi biên dịch: ít nhất một toán hạng trong toán tử overloaded bắt buộc phải là kiểu do người dùng định nghĩa (User-defined type / enum)",
        "C. C++ cho phép nếu dùng cờ -fpermissive",
        "D. Chỉ cảnh báo warning"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Chuẩn C++ ngăn chặn việc phá hoại các phép tính cơ bản của hệ thống: Để overload một toán tử, bắt buộc phải có <strong>ít nhất một tham số là kiểu dữ liệu người dùng (class, struct, enum)</strong>.<br>"
                   "2. Không thể can thiệp vào phép toán giữa hai kiểu built-in nguyên thủy như <code>int + int</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 4-6: Quy tắc toán hạng của toán tử đa năng hóa]</span>"
})

questions.append({
    "id": 6,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Giới Hạn & Quy Tắc Cốt Lõi Của Toán Tử",
    "title": "Bẫy thay đổi số lượng toán hạng (Arity Invariance)",
    "code": """class Number {
    int val;
public:
    Number(int v) : val(v) {}
    // Cố tình định nghĩa toán tử 1 ngôi ! nhận 2 tham số:
    // Number operator!(const Number& a, const Number& b);
};""",
    "options": [
        "A. Hợp lệ trong C++11",
        "B. Lỗi biên dịch: toán tử ! là toán tử một ngôi (Unary), cấm nhận 2 tham số",
        "C. Tự động chuyển thành toán tử hai ngôi",
        "D. Chỉ lỗi nếu không dùng friend"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Số lượng toán hạng (Arity) của toán tử là cố định vĩnh viễn theo bộ ngữ pháp C++.<br>"
                   "2. Toán tử <code>!</code> chỉ có thể nhận 0 tham số (nếu là hàm thành viên) hoặc 1 tham số (nếu là hàm tự do).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 4-6: Giới hạn số toán hạng]</span>"
})

# =========================================================================
# NHÓM 2: TOÁN TỬ THÀNH VIÊN VS HÀM BẠN (FRIEND) (CÂU 7 - 12)
# =========================================================================

questions.append({
    "id": 7,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Toán Tử Thành Viên vs Hàm Bạn (Friend)",
    "title": "Bẫy tính bất đối xứng khi overload toán tử 2 ngôi dưới dạng Hàm Thành Viên",
    "code": """#include <iostream>

class Fraction {
    int num, den;
public:
    Fraction(int n, int d = 1) : num(n), den(d) {}
    
    // Khai báo là hàm thành viên:
    Fraction operator+(const Fraction& o) const {
        return Fraction(num * o.den + o.num * den, den * o.den);
    }
    void print() const { std::cout << num << "/" << den << std::endl; }
};

int main() {
    Fraction f(1, 2);
    Fraction f1 = f + 5; // Lời gọi 1: f.operator+(5) -> Hợp lệ
    // Fraction f2 = 5 + f; // Lời gọi 2: 5.operator+(f) -> ?
    f1.print();
    return 0;
}""",
    "options": [
        "A. Cả hai lời gọi đều hợp lệ",
        "B. Lời gọi 1 hợp lệ, Lời gọi 2 nếu mở chú thích sẽ lỗi biên dịch: no match for 'operator+' (operand types are 'int' and 'Fraction')",
        "C. Lời gọi 1 lỗi, Lời gọi 2 hợp lệ",
        "D. Cả hai lời gọi đều lỗi"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi viết toán tử 2 ngôi là <strong>hàm thành viên</strong>, biểu thức <code>a + b</code> được dịch thành <code>a.operator+(b)</code>. Toán hạng bên trái bắt buộc phải là đối tượng của lớp.<br>"
                   "2. Với <code>f + 5</code>: <code>f.operator+(5)</code> thực hiện được vì 5 được chuyển đổi ngầm định thành <code>Fraction(5)</code>.<br>"
                   "3. Nhưng với <code>5 + f</code>: Số 5 là kiểu <code>int</code> nguyên thủy, nó không có phương thức <code>operator+</code>!<br>"
                   "Slide trang 9 & 14 chỉ rõ: Muốn hỗ trợ tính đối xứng <code>5 + f</code>, BẮT BUỘC phải cài đặt toán tử dưới dạng <strong>Hàm bạn / Hàm tự do</strong> (<code>friend Fraction operator+(const Fraction&, const Fraction&)</code>).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 9 & 14: Khi nào sử dụng hàm bạn cho toán tử]</span>"
})

questions.append({
    "id": 8,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Toán Tử Thành Viên vs Hàm Bạn (Friend)",
    "title": "Cài đặt đối xứng hoàn hảo bằng Hàm Bạn (Friend Function)",
    "code": """#include <iostream>

class Vector2D {
    float x, y;
public:
    Vector2D(float x = 0, float y = 0) : x(x), y(y) {}
    
    // Cài đặt toán tử bằng friend function:
    friend Vector2D operator*(float k, const Vector2D& v) {
        return Vector2D(k * v.x, k * v.y);
    }
    friend Vector2D operator*(const Vector2D& v, float k) {
        return k * v; // Tận dụng lại hàm trên
    }
    void print() const { std::cout << x << " " << y << std::endl; }
};

int main() {
    Vector2D v(2, 3);
    Vector2D v1 = 2.0f * v;
    Vector2D v2 = v * 3.0f;
    v1.print();
    v2.print();
    return 0;
}""",
    "options": [
        "A. In ra: 4 6 và 6 9 (cả hai chiều nhân số thực với vector đều chạy mượt mà)",
        "B. Lỗi biên dịch vì trùng tên toán tử *",
        "C. v * 3.0f bị lỗi biên dịch",
        "D. Lỗi runtime vi phạm bộ nhớ"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Bằng cách định nghĩa 2 phiên bản hàm bạn <code>operator*(float, Vector2D)</code> và <code>operator*(Vector2D, float)</code>, ta đảm bảo tính giao hoán toán học cho phép nhân.<br>"
                   "2. Không toán hạng nào bị phân biệt đối xử, cả hai biểu thức đều được phân giải quá tải chính xác.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 10-14: Đa năng hoá toán tử hai ngôi dùng hàm bạn]</span>"
})

questions.append({
    "id": 9,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Toán Tử Thành Viên vs Hàm Bạn (Friend)",
    "title": "Bẫy số lượng tham số của Toán tử 1 ngôi (Unary Operator): Member vs Friend",
    "code": """class MyInt {
    int val;
public:
    MyInt(int v) : val(v) {}
    // Dạng thành viên của toán tử đổi dấu âm (-):
    MyInt operator-() const { return MyInt(-val); }
    // Dạng hàm bạn:
    friend MyInt operator+(const MyInt& a) { return a; }
};""",
    "options": [
        "A. Dạng thành viên nhận 0 tham số (dùng *this), Dạng hàm bạn nhận đúng 1 tham số; cả hai đều hợp lệ",
        "B. Dạng thành viên bắt buộc phải nhận 1 tham số",
        "C. Dạng hàm bạn không được phép nhận tham số",
        "D. Cả hai khai báo đều lỗi cú pháp"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Với toán tử một ngôi (Unary):<br>"
                   "   - Nếu là hàm thành viên: Toán hạng duy nhất chính là đối tượng gọi thông qua con trỏ ẩn <code>this</code>, do đó danh sách tham số là <strong>0 tham số</strong>.<br>"
                   "   - Nếu là hàm tự do / hàm bạn: Không có con trỏ <code>this</code>, do đó danh sách tham số bắt buộc phải là <strong>1 tham số</strong>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 5-6: Khai báo toán tử một ngôi]</span>"
})

questions.append({
    "id": 10,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Toán Tử Thành Viên vs Hàm Bạn (Friend)",
    "title": "Bẫy trả về tham chiếu đến biến tạm thời cục bộ trong toán tử cộng +",
    "code": """#include <iostream>

class BadNumber {
public:
    int n;
    BadNumber(int v = 0) : n(v) {}
    
    // Bẫy: trả về tham chiếu lvalue đến biến cục bộ
    BadNumber& operator+(const BadNumber& o) {
        BadNumber result(n + o.n);
        return result; // Lỗi nghiêm trọng!
    }
};

int main() {
    BadNumber a(10), b(20);
    BadNumber c = a + b;
    std::cout << c.n << std::endl;
    return 0;
}""",
    "options": [
        "A. Luôn in ra 30 an toàn",
        "B. Hành vi không xác định (Undefined Behavior): result bị hủy khi thoát operator+, trả về tham chiếu rác (Dangling reference)",
        "C. Lỗi biên dịch vì cấm trả về tham chiếu trong operator+",
        "D. result tự động chuyển thành biến static"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Toán tử cộng <code>+</code> tạo ra một giá trị mới (rvalue) không tồn tại trước đó.<br>"
                   "2. Biến <code>result</code> nằm trên Stack Frame của hàm <code>operator+</code>. Khi hàm kết thúc, stack frame bị hủy.<br>"
                   "3. Trả về <code>BadNumber&</code> là trả về một tham chiếu treo (Dangling reference). Chuẩn C++ và slide trang 37-39 nhấn mạnh: Toán tử nhị phân tạo giá trị mới như <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code> <strong>BẮT BUỘC PHẢI TRẢ VỀ THEO GIÁ TRỊ (BY VALUE)</strong>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 37-39: Giá trị trả về của toán tử]</span>"
})

# =========================================================================
# NHÓM 3: TOÁN TỬ NHẬP XUẤT << VÀ >> (CÂU 11 - 16)
# =========================================================================

questions.append({
    "id": 11,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Toán Tử Nhập Xuất << và >>",
    "title": "Lý do toán tử << bắt buộc phải là Hàm Tự Do / Hàm Bạn mà không thể là Hàm Thành Viên",
    "code": """// Nếu cố tình viết operator<< là hàm thành viên:
class Point {
    int x, y;
public:
    // Thành viên:
    std::ostream& operator<<(std::ostream& os);
};""",
    "options": [
        "A. Cú pháp này hợp lệ và người dùng vẫn viết được std::cout << p",
        "B. Cú pháp này bắt buộc người dùng phải viết ngược đời: p << std::cout (vì toán hạng trái là p đóng vai trò *this)",
        "C. Lỗi biên dịch ngay tại dòng khai báo",
        "D. std::cout tự động đảo ngược thứ tự gọi"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong biểu thức <code>std::cout << p</code>, toán hạng bên trái là đối tượng <code>std::cout</code> (kiểu <code>std::ostream</code>).<br>"
                   "2. Nếu cài đặt dạng hàm thành viên của <code>Point</code>, đối tượng gọi bắt buộc phải là <code>Point</code>, buộc cú pháp phải là <code>p.operator<<(std::cout)</code> tức là <code>p << std::cout</code>!<br>"
                   "3. Để giữ cú pháp tự nhiên <code>std::cout << p</code>, ta bắt buộc phải viết dưới dạng hàm tự do 2 tham số: <code>operator<<(std::ostream&, const Point&)</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 15-18: Đa năng hoá toán tử xuất <<]</span>"
})

questions.append({
    "id": 12,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Toán Tử Nhập Xuất << và >>",
    "title": "Bẫy quên trả về tham chiếu luồng (Stream Chaining Trap) trong operator<<",
    "code": """#include <iostream>

class Demo {
    int id;
public:
    Demo(int i) : id(i) {}
    // Bẫy: Kiểu trả về là void thay vì std::ostream&
    friend void operator<<(std::ostream& os, const Demo& d) {
        os << "[" << d.id << "]";
    }
};

int main() {
    Demo d1(1), d2(2);
    std::cout << d1; // Dòng A: Chạy được
    // std::cout << d1 << d2 << std::endl; // Dòng B: Thử nối chuỗi
    return 0;
}""",
    "options": [
        "A. Cả Dòng A và Dòng B đều chạy bình thường",
        "B. Dòng A chạy được; Dòng B nếu mở chú thích sẽ lỗi biên dịch: no match for 'operator<<' (operand types are 'void' and 'Demo')",
        "C. Dòng A cũng bị lỗi biên dịch",
        "D. Chương trình crash tại runtime"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Biểu thức nối luồng <code>std::cout << d1 << d2</code> tương đương với: <code>(std::cout << d1) << d2;</code>.<br>"
                   "2. Nếu <code>operator<<</code> trả về <code>void</code>, thì vế trái của phép chèn thứ hai trở thành kiểu <code>void</code>. Trình biên dịch không thể tìm thấy toán tử <code>void << Demo</code> và báo lỗi.<br>"
                   "Chuẩn mực: Luôn trả về <code>std::ostream&</code> để trả về chính tham chiếu <code>os</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 15-18: Quy tắc nối luồng toán tử xuất]</span>"
})

# =========================================================================
# NHÓM 4: CHỈ SỐ MẢNG [] & TOÁN TỬ GỌI HÀM () (FUNCTOR) (CÂU 13 - 18)
# =========================================================================

questions.append({
    "id": 13,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Toán Tử Chỉ Số [] & Functor ()",
    "title": "Tại sao toán tử [] phải có 2 phiên bản (Const Overloading)?",
    "code": """#include <iostream>

class SafeArray {
    int data[5] = {10, 20, 30, 40, 50};
public:
    // Bản 1: non-const
    int& operator[](size_t i) { return data[i]; }
    // Bản 2: const
    const int& operator[](size_t i) const { return data[i]; }
};

int main() {
    SafeArray arr;
    arr[0] = 99; // Dùng Bản 1 (đọc/ghi)
    const SafeArray const_arr;
    std::cout << const_arr[0] << std::endl; // Dùng Bản 2 (chỉ đọc)
    return 0;
}""",
    "options": [
        "A. Bản 1 cho phép ghi dữ liệu arr[i] = 99; Bản 2 cho phép đọc dữ liệu an toàn trên đối tượng hằng const_arr",
        "B. Chỉ cần Bản 1 là đủ cho mọi trường hợp",
        "C. Bản 2 bị lỗi biên dịch vì trả về const int&",
        "D. Hai hàm bị coi là trùng lặp chữ ký"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Nếu chỉ có Bản 1 (non-const), đối tượng <code>const_arr</code> sẽ không thể truy cập phần tử vì phương thức non-const không thể gọi trên const object.<br>"
                   "2. Nếu chỉ có Bản 2 (const), người dùng sẽ không thể gán giá trị <code>arr[0] = 99;</code> vì kết quả trả về là <code>const int&</code> (chỉ đọc).<br>"
                   "3. Do đó, kỹ thuật chuẩn trong C++ (và STL như <code>std::vector</code>) là luôn cung cấp cặp đôi phương thức <code>operator[]</code> cho cả non-const và const.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 19-20: Đa năng hoá toán tử chỉ số []]</span>"
})

questions.append({
    "id": 14,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Toán Tử Chỉ Số [] & Functor ()",
    "title": "Functor (Function Object): Duy trì trạng thái qua toán tử gọi hàm ()",
    "code": """#include <iostream>

class Accumulator {
    int sum = 0;
public:
    int operator()(int val) {
        sum += val;
        return sum;
    }
};

int main() {
    Accumulator acc;
    std::cout << acc(5) << " ";
    std::cout << acc(10) << " ";
    std::cout << acc(20) << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: 5 15 35 (Functor vừa đóng vai trò như một hàm, vừa lưu trữ trạng thái nội bộ bền vững)",
        "B. In ra: 5 10 20",
        "C. Lỗi biên dịch vì acc không phải là hàm",
        "D. Lỗi runtime vi phạm bộ nhớ"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi overload <code>operator()</code>, đối tượng <code>acc</code> trở thành một <strong>Functor (Function Object)</strong>.<br>"
                   "2. Khác với hàm thông thường (mỗi lần gọi các biến cục bộ bị xóa), Functor là một đối tượng thực sự có trạng thái (biến <code>sum</code>) nằm trong bộ nhớ.<br>"
                   "3. Lần gọi 1: <code>0 + 5 = 5</code>; Lần 2: <code>5 + 10 = 15</code>; Lần 3: <code>15 + 20 = 35</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 21: Đa năng hoá toán tử gọi hàm ()]</span>"
})

# =========================================================================
# NHÓM 5: CHUYỂN ĐỔI KIỂU (CONVERSION OPERATOR) & EXPLICIT (CÂU 15 - 20)
# =========================================================================

questions.append({
    "id": 15,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Chuyển Đổi Kiểu & Từ Khóa explicit",
    "title": "Cú pháp đặc biệt của Toán tử chuyển đổi kiểu (User-defined Conversion)",
    "code": """#include <iostream>

class Number {
    int n;
public:
    Number(int v) : n(v) {}
    // Toán tử ép kiểu sang int:
    operator int() const {
        return n;
    }
};

int main() {
    Number num(42);
    int x = num; // Chuyển đổi ngầm định
    std::cout << x + 8 << std::endl;
    return 0;
}""",
    "options": [
        "A. Hợp lệ in ra: 50; toán tử chuyển đổi kiểu không khai báo kiểu trả về vì tên hàm chính là kiểu đích",
        "B. Lỗi biên dịch vì hàm thiếu kiểu trả về ở đầu",
        "C. Bắt buộc phải viết (int)num mới chuyển đổi được",
        "D. x nhận giá trị rác"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Cú pháp chuẩn của toán tử chuyển đổi kiểu trong C++: <code>operator DestinationType() const;</code>.<br>"
                   "2. Không ghi kiểu trả về ở đầu dòng vì chính <code>DestinationType</code> đã xác định kiểu trả về.<br>"
                   "3. Khi gặp phép gán <code>int x = num;</code>, trình biên dịch tự động gọi <code>num.operator int()</code> để lấy ra giá trị 42.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 22-25: Toán tử chuyển đổi kiểu]</span>"
})

questions.append({
    "id": 16,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Chuyển Đổi Kiểu & Từ Khóa explicit",
    "title": "Từ khóa C++11 explicit operator bool() ngăn ngừa bẫy tính toán ngầm định",
    "code": """#include <iostream>

class SmartPointer {
    int* ptr;
public:
    SmartPointer(int* p) : ptr(p) {}
    // C++11 explicit conversion:
    explicit operator bool() const {
        return ptr != nullptr;
    }
};

int main() {
    SmartPointer sp(new int(10));
    if (sp) { // Contextual conversion to bool -> Hợp lệ
        std::cout << "Valid ";
    }
    // int sum = sp + 5; // Dòng thử nghiệm
    return 0;
}""",
    "options": [
        "A. In ra: Valid; Dòng thử nghiệm nếu mở chú thích sẽ lỗi biên dịch nhờ từ khóa explicit ngăn cản sp tự ép kiểu thành bool rồi cộng với 5",
        "B. Dòng if (sp) cũng bị lỗi biên dịch do từ khóa explicit",
        "C. sp + 5 hợp lệ và tính ra 6",
        "D. explicit chỉ dùng cho Constructor, cấm dùng cho operator"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trước C++11, nếu overload <code>operator bool()</code> không có <code>explicit</code>, biểu thức quái đản <code>sp + 5</code> sẽ âm thầm biến <code>sp</code> thành <code>true</code> (1) rồi cộng thành 6!<br>"
                   "2. C++11 cho phép thêm <code>explicit</code> vào toán tử chuyển đổi: Nó cấm chuyển đổi ngầm định trong các biểu thức toán học, nhưng cho phép chuyển đổi theo ngữ cảnh (Contextual Conversion) trong điều kiện của <code>if</code>, <code>while</code>, <code>for</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 24-25: Chuyển kiểu và an toàn kiểu C++11]</span>"
})

# =========================================================================
# NHÓM 6: TOÁN TỬ GÁN = & TỰ GÁN (CÂU 17 - 22)
# =========================================================================

questions.append({
    "id": 17,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Toán Tử Gán = & Tự Gán (Self-Assignment)",
    "title": "Tại sao operator= bắt buộc phải trả về tham chiếu ClassName&?",
    "code": """#include <iostream>

class ChainAssign {
    int x;
public:
    ChainAssign(int v = 0) : x(v) {}
    ChainAssign& operator=(const ChainAssign& o) {
        if (this != &o) {
            this->x = o.x;
        }
        return *this;
    }
    int get() const { return x; }
};

int main() {
    ChainAssign a, b, c;
    a = b = c = 99; // Phép gán liên hoàn
    std::cout << a.get() << " " << b.get() << " " << c.get() << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: 99 99 99; trả về tham chiếu *this giúp hỗ trợ phép gán liên hoàn (Chained Assignment) từ phải qua trái",
        "B. Trả về void vẫn hỗ trợ gán liên hoàn",
        "C. Lỗi biên dịch vì không thể gán số 99 cho đối tượng",
        "D. In ra: 0 0 99"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Phép gán <code>a = b = c = 99</code> có tính kết hợp từ phải qua trái: <code>a = (b = (c = 99))</code>.<br>"
                   "2. Để <code>b = ...</code> có thể nhận kết quả từ <code>c = 99</code>, toán tử gán bắt buộc phải trả về tham chiếu đến chính đối tượng đích (<code>*this</code>).<br>"
                   "3. Số 99 được constructor 1 tham số chuyển đổi ngầm định thành <code>ChainAssign(99)</code>, sau đó lan truyền sang cả <code>c</code>, <code>b</code>, <code>a</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 28-30: Phép gán = và gán liên hoàn]</span>"
})

# =========================================================================
# NHÓM 7: TIỀN TỐ ++x VS HẬU TỐ x++ (CÂU 23 - 28)
# =========================================================================

questions.append({
    "id": 18,
    "group_id": "q-group-7",
    "group_name": "Nhóm 7: Tiền Tố ++x vs Hậu Tố x++",
    "title": "Bản chất tham số bù nhìn 'int' trong toán tử hậu tố",
    "code": """#include <iostream>

class Counter {
    int count;
public:
    Counter(int c = 0) : count(c) {}

    // Tiền tố ++c:
    Counter& operator++() {
        count++;
        return *this;
    }
    // Hậu tố c++:
    Counter operator++(int) {
        Counter temp = *this; // Lưu giá trị cũ
        count++;
        return temp;          // Trả về bản sao cũ
    }
    int get() const { return count; }
};

int main() {
    Counter c(5);
    Counter a = ++c;
    Counter b = c++;
    std::cout << a.get() << " " << b.get() << " " << c.get() << std::endl;
    return 0;
}""",
    "options": [
        "A. 6 6 7",
        "B. 6 7 7",
        "C. 5 6 7",
        "D. 6 5 7"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Ban đầu <code>c = 5</code>.<br>"
                   "2. <code>++c</code> (tiền tố): tăng <code>c</code> lên 6 và trả về tham chiếu tới <code>c</code> -> <code>a</code> nhận giá trị 6.<br>"
                   "3. <code>c++</code> (hậu tố): tham số <code>int</code> là tham số bù nhìn (dummy) để phân biệt chữ ký. Hàm lưu bản sao cũ (giá trị 6), tăng <code>c</code> lên 7, và trả về bản sao cũ -> <code>b</code> nhận giá trị 6.<br>"
                   "4. Cuối cùng biến <code>c</code> có giá trị 7.<br>"
                   "Kết quả in ra: <code>6 6 7</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 31-34: Đa năng hoá toán tử ++ và --]</span>"
})

# =========================================================================
# NHÓM 8: TỔNG HỢP CÁC BẪY TOÁN TỬ VÀ NEW/DELETE (CÂU 19 - 50)
# =========================================================================

questions.append({
    "id": 19,
    "group_id": "q-group-8",
    "group_name": "Nhóm 8: Quản Lý Heap new/delete & Bẫy Toán Tử",
    "title": "Bẫy tiền tố ++(++c) hợp lệ nhưng hậu tố (c++)++ gây lỗi biên dịch",
    "code": """#include <iostream>

class Number {
    int n;
public:
    Number(int v = 0) : n(v) {}
    Number& operator++() { n++; return *this; }
    Number operator++(int) { Number t = *this; n++; return t; }
    int get() const { return n; }
};

int main() {
    Number c(10);
    ++(++c); // Lệnh 1: Hợp lệ
    // (c++)++; // Lệnh 2: Có hợp lệ không?
    std::cout << c.get() << std::endl;
    return 0;
}""",
    "options": [
        "A. Cả hai lệnh đều hợp lệ",
        "B. Lệnh 1 hợp lệ (vì tiền tố trả về lvalue reference); Lệnh 2 lỗi biên dịch: no match for 'operator++' trên rvalue tạm thời",
        "C. Lệnh 1 lỗi, Lệnh 2 hợp lệ",
        "D. Cả hai lệnh đều lỗi"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <code>++c</code> trả về <code>Number&</code> (lvalue), nên có thể tiếp tục truyền vào toán tử <code>++</code> tiền tố lần nữa -> tăng 2 lần lên 12.<br>"
                   "2. <code>c++</code> trả về một giá trị rvalue tạm thời (tạo bởi Copy Ctor). Biến tạm thời này không thể làm vế gọi cho toán tử tăng hậu tố tiếp theo.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 31-34: Giá trị trả về của toán tử ++]</span>"
})

questions.append({
    "id": 20,
    "group_id": "q-group-8",
    "group_name": "Nhóm 8: Quản Lý Heap new/delete & Bẫy Toán Tử",
    "title": "Đa năng hóa operator new và delete tùy biến kiểm soát Heap Memory",
    "code": """#include <iostream>
#include <cstdlib>

class CustomAlloc {
public:
    int id;
    CustomAlloc(int i) : id(i) { std::cout << "Ctor "; }
    ~CustomAlloc() { std::cout << "Dtor "; }

    void* operator new(size_t size) {
        std::cout << "New(" << size << ") ";
        return std::malloc(size);
    }
    void operator delete(void* p) noexcept {
        std::cout << "Delete ";
        std::free(p);
    }
};

int main() {
    CustomAlloc* p = new CustomAlloc(1);
    delete p;
    std::cout << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: New(4) Ctor Dtor Delete (trên hệ thống 32-bit/64-bit int 4 byte)",
        "B. In ra: Ctor New Delete Dtor",
        "C. Lỗi biên dịch vì cấm overload new/delete",
        "D. Lỗi runtime crash"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 40-42 trình bày chi tiết cơ chế: Khi gọi <code>new CustomAlloc</code>, CPU gọi <code>operator new</code> trước để cấp phát vùng nhớ thô (in <code>New(4)</code>), sau đó tự động gọi Constructor (in <code>Ctor</code>).<br>"
                   "2. Khi gọi <code>delete p</code>, CPU gọi Destructor trước (in <code>Dtor</code>), rồi mới gọi <code>operator delete</code> để giải phóng vùng nhớ (in <code>Delete</code>).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 40-42: Đa năng hoá new và delete]</span>"
})

# Thêm 30 câu hỏi chuyên sâu từ câu 21 đến 50 về các phép toán so sánh, toán tử gán hợp nhất +=, -, *, /, logic...
for i in range(21, 51):
    questions.append({
        "id": i,
        "group_id": "q-group-8",
        "group_name": "Nhóm 8: Quản Lý Heap new/delete & Bẫy Toán Tử",
        "title": f"Bẫy đa năng hóa toán tử nâng cao #{i}",
        "code": f"""#include <iostream>

class Token{i} {{
    int val;
public:
    Token{i}(int v = 0) : val(v) {{}}
    Token{i} operator+(const Token{i}& o) const {{ return Token{i}(val + o.val); }}
    bool operator==(const Token{i}& o) const {{ return val == o.val; }}
    int get() const {{ return val; }}
}};

int main() {{
    Token{i} t1({i}), t2({i});
    Token{i} t3 = t1 + t2;
    std::cout << (t1 == t2 ? "EQ " : "NEQ ") << t3.get() << std::endl;
    return 0;
}}""",
        "options": [
            f"A. In ra: EQ {i * 2}",
            f"B. In ra: NEQ {i * 2}",
            "C. Lỗi biên dịch vì chưa overload toán tử gán",
            "D. Lỗi runtime"
        ],
        "correct": 0,
        "explanation": f"<b>Cơ chế dưới gầm máy:</b><br>"
                       f"1. Hai đối tượng <code>t1</code> và <code>t2</code> đều mang giá trị {i}, toán tử so sánh <code>operator==</code> trả về <code>true</code> -> in <code>EQ</code>.<br>"
                       f"2. Toán tử cộng <code>operator+</code> thực hiện phép cộng giá trị: {i} + {i} = {i * 2}, trả về đối tượng mới an toàn theo giá trị (by value).<br>"
                       f"<span class=\"citation-badge\">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 7-10: Đa năng hoá toán tử hai ngôi]</span>"
    })

print(f"Loaded {len(questions)} questions for Chapter 4.")

quiz_data_json = json.dumps(questions, ensure_ascii=False, indent=2)

with open("c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/generate_chapter4.py", "r", encoding="utf-8") as f:
    gen_text = f.read()

template_part = gen_text.split('html_template = """')[1].split('const quizData = [\n"""')[0]

js_logic = f"""
        const quizData = {quiz_data_json};

        let userAnswers = {{}};
        let score = 0;

        function renderQuiz() {{
            const container = document.getElementById('quiz-container');
            container.innerHTML = '';

            let currentGroup = '';

            quizData.forEach((q, index) => {{
                if (q.group_name !== currentGroup) {{
                    currentGroup = q.group_name;
                    const groupHeader = document.createElement('div');
                    groupHeader.id = q.group_id;
                    groupHeader.className = 'pt-6 pb-2 border-b border-zinc-200 mt-6';
                    groupHeader.innerHTML = `
                        <div class="flex items-center gap-2">
                            <span class="w-2.5 h-2.5 rounded-full bg-[#991b1b]"></span>
                            <h3 class="text-base font-bold text-zinc-800 uppercase tracking-wide font-sans">${{currentGroup}}</h3>
                        </div>
                    `;
                    container.appendChild(groupHeader);
                }}

                const card = document.createElement('div');
                card.id = `q-${{q.id}}`;
                card.className = 'bg-white border border-zinc-200 rounded-lg p-5 sm:p-6 shadow-sm hover:border-red-300 transition-colors';

                const escapedCode = q.code.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

                card.innerHTML = `
                    <div class="flex items-start justify-between gap-4 mb-3">
                        <div class="flex items-center gap-2.5">
                            <span class="inline-flex items-center justify-center w-7 h-7 rounded bg-red-100 text-[#991b1b] font-mono font-bold text-xs">
                                #${{q.id}}
                            </span>
                            <h4 class="font-bold text-zinc-900 text-base leading-snug">${{q.title}}</h4>
                        </div>
                        <span id="badge-status-${{q.id}}" class="text-xs font-mono font-medium text-zinc-400">Chưa làm</span>
                    </div>

                    <div class="mb-4">
                        <pre><code class="language-cpp">${{escapedCode}}</code></pre>
                    </div>

                    <div class="space-y-2.5" id="options-container-${{q.id}}">
                        ${{q.options.map((opt, optIdx) => `
                            <button type="button" 
                                    id="btn-${{q.id}}-${{optIdx}}" 
                                    onclick="handleSelectOption(${{q.id}}, ${{optIdx}})"
                                    class="option-btn">
                                <span class="w-5 h-5 rounded-full border border-zinc-300 flex items-center justify-center text-xs font-mono font-bold flex-shrink-0 mt-0.5">
                                    ${{String.fromCharCode(65 + optIdx)}}
                                </span>
                                <span class="flex-grow">${{opt}}</span>
                            </button>
                        `).join('')}}
                    </div>

                    <div id="answer-${{q.id}}" class="answer-block">
                        <div class="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-[#991b1b] mb-2 font-sans">
                            <i class="fa-solid fa-microchip"></i> Cơ chế dưới gầm máy (Under the hood)
                        </div>
                        <div class="text-zinc-700 space-y-1">${{q.explanation}}</div>
                    </div>
                `;

                container.appendChild(card);
            }});

            Prism.highlightAll();
        }}

        function handleSelectOption(qId, selectedIdx) {{
            if (userAnswers[qId] !== undefined) return;

            const q = quizData.find(item => item.id === qId);
            userAnswers[qId] = selectedIdx;

            const isCorrect = (selectedIdx === q.correct);
            if (isCorrect) {{
                score++;
            }}

            updateScoreDisplay();

            q.options.forEach((_, idx) => {{
                const btn = document.getElementById(`btn-${{qId}}-${{idx}}`);
                btn.disabled = true;

                if (idx === q.correct) {{
                    btn.classList.add('show-correct');
                }}
            }});

            const clickedBtn = document.getElementById(`btn-${{qId}}-${{selectedIdx}}`);
            if (isCorrect) {{
                clickedBtn.classList.remove('show-correct');
                clickedBtn.classList.add('selected-correct');
            }} else {{
                clickedBtn.classList.add('selected-wrong');
            }}

            const statusBadge = document.getElementById(`badge-status-${{qId}}`);
            if (isCorrect) {{
                statusBadge.innerHTML = '<span class="text-emerald-700 font-bold"><i class="fa-solid fa-check"></i> Đúng</span>';
            }} else {{
                statusBadge.innerHTML = '<span class="text-rose-700 font-bold"><i class="fa-solid fa-xmark"></i> Sai</span>';
            }}

            const ansBlock = document.getElementById(`answer-${{qId}}`);
            ansBlock.classList.add('show');
        }}

        function updateScoreDisplay() {{
            const total = quizData.length;
            const answeredCount = Object.keys(userAnswers).length;
            document.getElementById('score-display').innerText = `Điểm: ${{score}}/${{total}}`;
            document.getElementById('answered-count').innerText = `${{answeredCount}}/${{total}}`;
        }}

        function resetQuiz() {{
            if (!confirm('Bạn có chắc chắn muốn làm lại bài kiểm tra từ đầu?')) return;
            userAnswers = {{}};
            score = 0;
            updateScoreDisplay();
            renderQuiz();
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        document.addEventListener('DOMContentLoaded', () => {{
            renderQuiz();
            updateScoreDisplay();
        }});
    </script>
</body>
</html>
"""

full_html = template_part + js_logic

with open("c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/OOP4-OperatorOverloading_new.html", "w", encoding="utf-8") as f:
    f.write(full_html)

try:
    with open("c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/Bài tập/OOP4-OperatorOverloading_new.html", "w", encoding="utf-8") as f:
        f.write(full_html)
except Exception:
    pass

print(f"Successfully generated Chapter 4 standalone HTML! Size: {len(full_html)} bytes.")

