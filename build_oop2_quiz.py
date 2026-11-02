# -*- coding: utf-8 -*-
import json

questions = []

# =========================================================================
# NHÓM 1: TIẾN HÓA TỪ THỦ TỤC SANG HƯỚNG ĐỐI TƯỢNG & TÍNH TOÀN VẸN (CÂU 1 - 5)
# =========================================================================

questions.append({
    "id": 1,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Tiến Hóa Từ Thủ Tục Sang OOP & Tính Toàn Vẹn",
    "title": "Bẫy biến toàn cục chia sẻ trong Lập trình hướng thủ tục (Shared Global State)",
    "code": """#include <iostream>

int global_balance = 1000;

void withdraw(int amount) {
    if (global_balance >= amount) {
        global_balance -= amount;
    }
}

void hacker_modify() {
    global_balance = -50000; // Can thiệp trực tiếp từ bất kỳ đâu
}

int main() {
    withdraw(200);
    hacker_modify();
    std::cout << "Balance: " << global_balance << std::endl;
    return 0;
}""",
    "options": [
        "A. Lỗi biên dịch vì hàm hacker_modify không có quyền truy cập global_balance",
        "B. In ra: Balance: -50000; minh họa nhược điểm dữ liệu toàn cục bị can thiệp tự do trong lập trình hướng thủ tục",
        "C. In ra: Balance: 800",
        "D. Lỗi runtime vi phạm bộ nhớ"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong lập trình hướng thủ tục, biến toàn cục <code>global_balance</code> nằm trong Data Segment và có thể bị đọc/ghi từ bất kỳ hàm nào trong toàn bộ chương trình mà không qua kiểm soát.<br>"
                   "2. Không có cơ chế đóng gói (Encapsulation), dẫn đến việc tính bất biến dữ liệu (Data Invariants - ví dụ số dư không thể âm) bị phá vỡ hoàn toàn.<br>"
                   "3. Slide trang 13 & 16 chỉ rõ: 'Tiếp cận hướng đối tượng xuất phát từ hạn chế không quản lý được sự thay đổi dữ liệu khi có nhiều chương trình cùng thay đổi một biến chung; OOP giúp không có nguy cơ dữ liệu bị thay đổi tự do trong chương trình'.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 13 & 16: Hạn chế của Lập trình thủ tục & Ưu điểm OOP]</span>"
})

questions.append({
    "id": 2,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Tiến Hóa Từ Thủ Tục Sang OOP & Tính Toàn Vẹn",
    "title": "Vi phạm tính bất biến dữ liệu (Class Invariants) trong Struct kiểu C thuần",
    "code": """#include <iostream>

struct Date {
    int day;
    int month;
    int year;
};

void setDate(Date& d, int day, int month, int year) {
    d.day = day;
    d.month = month;
    d.year = year;
}

int main() {
    Date d;
    setDate(d, 31, 2, 2024); // Ngày 31 tháng 2 bất hợp lệ!
    d.day = 99;              // Thậm chí gán trực tiếp
    std::cout << d.day << "/" << d.month << "/" << d.year << std::endl;
    return 0;
}""",
    "options": [
        "A. Hàm setDate tự động kiểm tra tính hợp lệ và ném ngoại lệ",
        "B. Chương trình in ra 99/2/2024; struct trong C không che giấu dữ liệu nên không thể đảm bảo tính toàn vẹn (Invariants)",
        "C. Lỗi biên dịch vì struct không có hàm tạo",
        "D. Giá trị d.day tự động tràn về 1"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 7-8 phân tích trực diện ví dụ này: Nhược điểm của lập trình cấu trúc là dữ liệu thụ động, các trường <code>day</code>, <code>month</code>, <code>year</code> phơi bày hoàn toàn ra ngoài.<br>"
                   "2. Người dùng có thể truyền tham số tạo thành ngày tháng không hợp lệ hoặc gán đè trực tiếp mà không có tầng kiểm duyệt logic (Validation Layer).<br>"
                   "3. OOP giải quyết triệt để điều này bằng cách đặt dữ liệu vào phạm vi <code>private</code> và chỉ cho phép cập nhật thông qua phương thức (Member Function / Setter) có kèm kiểm tra điều kiện.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 7-8: Vấn đề tính đúng đắn và ràng buộc dữ liệu trong struct]</span>"
})

questions.append({
    "id": 3,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Tiến Hóa Từ Thủ Tục Sang OOP & Tính Toàn Vẹn",
    "title": "Sự khác biệt mặc định cốt tử giữa struct và class trong C++",
    "code": """#include <iostream>

struct StructType {
    int a;
};

class ClassType {
    int b;
};

int main() {
    StructType s;
    ClassType c;
    s.a = 10; // Dòng 1
    c.b = 20; // Dòng 2
    std::cout << s.a << std::endl;
    return 0;
}""",
    "options": [
        "A. Cả Dòng 1 và Dòng 2 đều hợp lệ",
        "B. Dòng 1 hợp lệ, Dòng 2 lỗi biên dịch: 'int ClassType::b' is private within this context",
        "C. Dòng 1 lỗi, Dòng 2 hợp lệ",
        "D. Cả hai dòng đều lỗi biên dịch"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong chuẩn C++, điểm khác biệt DUY NHẤT giữa từ khóa <code>struct</code> và <code>class</code> là quyền truy cập mặc định (Default Access Specifier):<br>"
                   "   - Trong <code>struct</code>: Các thành viên và kế thừa mặc định là <code>public</code>.<br>"
                   "   - Trong <code>class</code>: Các thành viên và kế thừa mặc định là <code>private</code>.<br>"
                   "2. Vì vậy, <code>c.b</code> là biến thành viên riêng tư của <code>ClassType</code>, việc truy cập trực tiếp từ hàm <code>main</code> bị compiler chặn và báo lỗi truy cập.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 28-29 & 36: Lớp & Tính đóng gói]</span>"
})

questions.append({
    "id": 4,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Tiến Hóa Từ Thủ Tục Sang OOP & Tính Toàn Vẹn",
    "title": "Hệ quả chi phí bảo trì khi thay đổi Cấu trúc dữ liệu trong Hướng thủ tục",
    "code": """// Phiên bản cũ:
struct Employee { char name[50]; double daily_rate; int days; };
double calcSalaryOld(const Employee& e) { return e.daily_rate * e.days; }

// Khi yêu cầu bài toán thay đổi CTDL:
struct EmployeeNew { char name[50]; double monthly_fixed_salary; double bonus; };
// Hàm calcSalaryOld hoàn toàn bị gãy và phải sửa mã nguồn ở mọi nơi sử dụng!""",
    "options": [
        "A. Lập trình hướng thủ tục có khả năng tự động thích ứng với cấu trúc dữ liệu mới",
        "B. Khi thay đổi CTDL trong hướng thủ tục, thuật toán gắn liền với CTDL cũng phải sửa đổi theo, làm chi phí phát triển tăng cao và không tái sử dụng được mã cũ",
        "C. Trong C++, struct không bao giờ thay đổi được cấu trúc",
        "D. Mã nguồn tự động tương thích ngược nhờ trình tiền xử lý"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 9-10 giải thích sâu sắc: 'Tại sao phải thay đổi cấu trúc dữ liệu? Cấu trúc dữ liệu là mô hình của bài toán, khi mô hình thực tế thay đổi, việc thay đổi CTDL dẫn đến việc sửa lại toàn bộ thuật toán tương ứng, chi phí phát triển tăng cao và không tái sử dụng được mã xử lý cũ'.<br>"
                   "2. OOP giải quyết bài toán này bằng cơ chế Che giấu cấu trúc (Data Hiding): Hàm <code>calcSalary()</code> trở thành phương thức thành viên của lớp. Bên ngoài chỉ gọi <code>emp.calcSalary()</code> mà hoàn toàn không cần biết bên trong lương được tính theo ngày hay theo tháng cố định.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 9-12: Các vấn đề khi thay đổi cấu trúc dữ liệu & Giải pháp]</span>"
})

questions.append({
    "id": 5,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Tiến Hóa Từ Thủ Tục Sang OOP & Tính Toàn Vẹn",
    "title": "Bẫy dùng memset kiểu thủ tục làm hỏng cấu trúc đối tượng C++11",
    "code": """#include <iostream>
#include <cstring>
#include <string>

class Student {
public:
    std::string name;
    int age;
    Student() : name("Default"), age(18) {}
};

int main() {
    Student s;
    std::memset(&s, 0, sizeof(Student)); // Dùng memset xóa sạch bộ nhớ
    std::cout << "Age: " << s.age << std::endl;
    // Khi thoát main, Destructor của s.name được gọi!
    return 0;
}""",
    "options": [
        "A. Chương trình in ra Age: 0 và kết thúc hoàn toàn an toàn",
        "B. Lỗi biên dịch vì memset không nhận địa chỉ đối tượng class",
        "C. Undefined Behavior / Crash: memset ghi đè 0 vào con trỏ quản lý bộ nhớ heap nội tại của std::string, gây lỗi Double Free / Corruption khi Destructor chạy",
        "D. std::string tự động khôi phục dữ liệu ban đầu"
    ],
    "correct": 2,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong lập trình hướng thủ tục C, <code>memset(&struct_var, 0, sizeof(...))</code> là cách thông dụng để reset POD (Plain Old Data).<br>"
                   "2. Trong OOP C++, một đối tượng không phải là POD thuần túy (ví dụ chứa <code>std::string</code> quản lý tài nguyên heap). Con trỏ buffer và kích thước của <code>std::string</code> nằm bên trong ô nhớ của <code>Student</code>.<br>"
                   "3. <code>memset</code> ghi đè byte 0 lên các con trỏ quản lý heap này. Khi hàm <code>main</code> kết thúc, Destructor của <code>s</code> tự động chạy và hủy <code>s.name</code>, cố gắng giải phóng con trỏ rác hoặc cấu trúc bị hỏng, dẫn tới sập chương trình (Crash).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 7 & 25: Tự động khởi tạo và hủy dữ liệu trong OOP]</span>"
})

# =========================================================================
# NHÓM 2: BẢN CHẤT ĐỐI TƯỢNG (IDENTITY, STATE, BEHAVIOR & BỐ CỤC RAM) (CÂU 6 - 12)
# =========================================================================

questions.append({
    "id": 6,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Bản Chất Đối Tượng & Bố Cục Bộ Nhớ RAM",
    "title": "Bản chất Định danh (Object Identity): Cùng Trạng Thái nhưng Khác Thực Thể",
    "code": """#include <iostream>

class Point {
public:
    int x, y;
    Point(int x, int y) : x(x), y(y) {}
};

int main() {
    Point p1(10, 20);
    Point p2(10, 20);
    
    std::cout << ((p1.x == p2.x && p1.y == p2.y) ? "EQ_STATE" : "DIFF_STATE") << " ";
    std::cout << ((&p1 == &p2) ? "SAME_ID" : "DIFF_ID") << std::endl;
    return 0;
}""",
    "options": [
        "A. EQ_STATE SAME_ID",
        "B. EQ_STATE DIFF_ID",
        "C. DIFF_STATE DIFF_ID",
        "D. Lỗi biên dịch vì không thể so sánh &p1 và &p2"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 26-27 định nghĩa 3 yếu tố cốt tử của Object: Định danh (Identity), Thuộc tính (State) và Phương thức (Behavior).<br>"
                   "2. Trạng thái (State) của <code>p1</code> và <code>p2</code> bằng nhau vì cả hai đều có <code>x=10, y=20</code>.<br>"
                   "3. Định danh (Identity) trong C++ được xác định bằng địa chỉ ô nhớ vật lý duy nhất trên Stack/Heap. Do <code>p1</code> và <code>p2</code> là hai thực thể độc lập chiếm hai vùng nhớ khác nhau, <code>&p1 != &p2</code> -> <code>DIFF_ID</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 26-27: Ba yếu tố xác định một đối tượng: Identity, State, Behavior]</span>"
})

questions.append({
    "id": 7,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Bản Chất Đối Tượng & Bố Cục Bộ Nhớ RAM",
    "title": "Kích thước của Lớp Rỗng (Empty Class Size Trap) trong C++",
    "code": """#include <iostream>

class EmptyClass {
    // Không chứa biến thành viên nào
};

int main() {
    std::cout << sizeof(EmptyClass) << " ";
    EmptyClass e1, e2;
    std::cout << (&e1 != &e2) << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: 0 0",
        "B. In ra: 1 1 (kích thước tối thiểu là 1 byte để đảm bảo tính duy nhất của Object Identity)",
        "C. In ra: 4 1",
        "D. Lỗi biên dịch vì class bắt buộc phải có ít nhất một thuộc tính"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Chuẩn C++ quy định: Không có bất kỳ đối tượng nào có kích thước bằng 0 byte.<br>"
                   "2. Nếu một lớp rỗng có kích thước 0 byte, thì trong mảng <code>EmptyClass arr[5]</code>, mọi phần tử <code>arr[0], arr[1]...</code> sẽ có cùng địa chỉ ô nhớ, làm phá vỡ nguyên lý nền tảng về Định danh đối tượng (Object Identity).<br>"
                   "3. Do đó trình biên dịch tự động cấp phát kích thước tối thiểu là <strong>1 byte</strong> cho lớp rỗng để đảm bảo hai đối tượng khác nhau luôn có địa chỉ khác nhau (<code>&e1 != &e2</code> trả về 1).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 22 & 26: Bản chất đối tượng và định danh trong hệ thống]</span>"
})

questions.append({
    "id": 8,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Bản Chất Đối Tượng & Bố Cục Bộ Nhớ RAM",
    "title": "Độn bộ nhớ (Memory Alignment & Padding) ảnh hưởng đến sizeof(Object)",
    "code": """#include <iostream>

class ClassA {
    char c1;   // 1 byte
    int x;     // 4 byte
    char c2;   // 1 byte
};

class ClassB {
    int x;     // 4 byte
    char c1;   // 1 byte
    char c2;   // 1 byte
};

int main() {
    std::cout << sizeof(ClassA) << " " << sizeof(ClassB) << std::endl;
    return 0;
}""",
    "options": [
        "A. 6 6",
        "B. 12 8 (trên kiến trúc 32-bit / 64-bit chuẩn)",
        "C. 8 8",
        "D. 12 12"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. CPU đọc bộ nhớ hiệu quả nhất khi dữ liệu được căn chỉnh (aligned) tại các địa chỉ là bội số kích thước của kiểu dữ liệu (kiểu <code>int</code> 4 byte phải căn chỉnh tại địa chỉ chia hết cho 4).<br>"
                   "2. Trong <code>ClassA</code>: <code>c1</code> (1 byte) + 3 byte padding + <code>x</code> (4 byte) + <code>c2</code> (1 byte) + 3 byte padding ở đuôi để tổng kích thước chia hết cho 4 -> Tổng = 12 bytes.<br>"
                   "3. Trong <code>ClassB</code>: <code>x</code> (4 byte) + <code>c1</code> (1 byte) + <code>c2</code> (1 byte) + 2 byte padding ở đuôi -> Tổng = 8 bytes.<br>"
                   "Thứ tự khai báo thuộc tính trong lớp ảnh hưởng trực tiếp đến bố cục bộ nhớ RAM của đối tượng.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 25 & 34: Thuộc tính của đối tượng và lưu trữ bộ nhớ]</span>"
})

questions.append({
    "id": 9,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Bản Chất Đối Tượng & Bố Cục Bộ Nhớ RAM",
    "title": "Bản chất con trỏ this và bẫy gọi hàm qua nullptr",
    "code": """#include <iostream>

class Logger {
public:
    void printHello() {
        std::cout << "Hello" << std::endl;
    }
    void printID() {
        std::cout << "ID: " << id << std::endl;
    }
private:
    int id = 42;
};

int main() {
    Logger* ptr = nullptr;
    ptr->printHello(); // Lời gọi 1
    ptr->printID();    // Lời gọi 2
    return 0;
}""",
    "options": [
        "A. Cả hai lời gọi đều crash ngay tại dòng ptr->printHello()",
        "B. Lời gọi 1 in ra 'Hello' bình thường, Lời gọi 2 gây Crash / Undefined Behavior",
        "C. Cả hai lời gọi đều in ra bình thường",
        "D. Lỗi biên dịch vì con trỏ nullptr không thể gọi hàm thành viên"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, các hàm thành viên không ảo (non-virtual) không được lưu bên trong đối tượng; mã máy của hàm nằm trong Code Segment. Lời gọi <code>ptr->printHello()</code> thực chất là <code>Logger_printHello(ptr)</code>.<br>"
                   "2. Trong <code>printHello()</code>, hàm không hề truy cập bất kỳ biến thành viên nào của đối tượng, con trỏ <code>this</code> (dù bằng <code>nullptr</code>) không bị giải tham chiếu (dereference), nên lệnh in 'Hello' chạy bình thường!<br>"
                   "3. Trong <code>printID()</code>, hàm thực hiện truy cập <code>this->id</code>. Vì <code>this == nullptr</code>, việc giải tham chiếu con trỏ 0 gây lỗi phân đoạn bộ nhớ (Segmentation Fault / Access Violation) và sập chương trình ngay lập tức.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 25 & 35: Đối tượng, phương thức và cơ chế truyền thông điệp]</span>"
})

questions.append({
    "id": 10,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Bản Chất Đối Tượng & Bố Cục Bộ Nhớ RAM",
    "title": "Tự hủy đối tượng bằng 'delete this;' và bẫy Use-After-Free",
    "code": """#include <iostream>

class SuicideObject {
public:
    int val = 10;
    void destroy() {
        delete this;
        // Dòng sau khi delete:
        std::cout << val << std::endl; 
    }
};

int main() {
    SuicideObject* obj = new SuicideObject();
    obj->destroy();
    return 0;
}""",
    "options": [
        "A. 'delete this;' là cú pháp bất hợp pháp trong C++",
        "B. 'delete this;' hợp lệ nếu đối tượng được cấp phát bằng new, nhưng truy cập 'val' sau delete là Undefined Behavior (Use-After-Free)",
        "C. Đối tượng tự động chuyển sang stack sau khi delete",
        "D. Chương trình đảm bảo an toàn 100% in ra 10"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Cú pháp <code>delete this;</code> hoàn toàn hợp lệ trong C++ với điều kiện tiên quyết: Đối tượng đó bắt buộc phải được cấp phát trên Heap bằng <code>new</code> (nếu đối tượng nằm trên Stack mà gọi <code>delete this</code> sẽ crash ngay lập tức).<br>"
                   "2. Tuy nhiên, ngay sau lệnh <code>delete this;</code>, vùng nhớ của đối tượng đã bị giải phóng và trả về cho Heap Manager.<br>"
                   "3. Việc truy cập <code>val</code> (tức là <code>this->val</code>) là lỗi nghiêm trọng <strong>Use-After-Free</strong> (Undefined Behavior), có thể in giá trị rác hoặc làm sập tiến trình.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 22 & 25: Vòng đời đối tượng và quản lý tài nguyên]</span>"
})

questions.append({
    "id": 11,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Bản Chất Đối Tượng & Bố Cục Bộ Nhớ RAM",
    "title": "Kỹ thuật Method Chaining (Fluent Interface) bằng cách trả về *this qua tham chiếu",
    "code": """#include <iostream>

class Calculator {
    int total = 0;
public:
    Calculator& add(int val) {
        total += val;
        return *this;
    }
    Calculator& mul(int val) {
        total *= val;
        return *this;
    }
    int get() const { return total; }
};

int main() {
    Calculator calc;
    calc.add(5).mul(3).add(2);
    std::cout << calc.get() << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: 17",
        "B. In ra: 21",
        "C. Lỗi biên dịch vì không thể nối tiếp nhiều dấu chấm gọi hàm liên tục",
        "D. In ra: 0 vì mỗi lần trả về tạo ra bản sao mới"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Bằng cách trả về tham chiếu đến chính đối tượng hiện tại (<code>Calculator&</code>) thông qua <code>return *this;</code>, mỗi lời gọi hàm thành viên trả về chính lvalue của đối tượng gốc <code>calc</code>.<br>"
                   "2. Chuỗi tính toán diễn ra tuần tự trên cùng một ô nhớ duy nhất: <code>add(5)</code> -> <code>total = 5</code>; tiếp tục <code>mul(3)</code> -> <code>total = 15</code>; tiếp tục <code>add(2)</code> -> <code>total = 17</code>.<br>"
                   "3. <code>calc.get()</code> trả về chính xác <code>17</code>. Đây là mẫu thiết kế Fluent Interface được dùng rất rộng rãi trong thư viện chuẩn C++ (như <code>std::cout << a << b</code>).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 35: Tương tác qua thông điệp và phương thức]</span>"
})

questions.append({
    "id": 12,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Bản Chất Đối Tượng & Bố Cục Bộ Nhớ RAM",
    "title": "Bẫy trả về *this theo giá trị (By Value) làm mất trạng thái đối tượng gốc",
    "code": """#include <iostream>

class Counter {
public:
    int count = 0;
    Counter increment() { // Bẫy: trả về by-value, không có dấu &
        count++;
        return *this;
    }
};

int main() {
    Counter c;
    c.increment().increment().increment();
    std::cout << c.count << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: 3",
        "B. In ra: 1",
        "C. In ra: 0",
        "D. Lỗi biên dịch vì không thể gọi increment trên đối tượng tạm thời"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Hãy quan sát kỹ kiểu trả về: <code>Counter</code> (by value) thay vì <code>Counter&</code> (by reference).<br>"
                   "2. Khi <code>c.increment()</code> được gọi: biến <code>c.count</code> tăng lên 1. Sau đó, hàm trả về một <strong>bản sao tạm thời (temporary copy)</strong> của <code>c</code> trên stack.<br>"
                   "3. Lời gọi <code>.increment()</code> thứ hai được thực thi trên bản sao tạm thời này (làm tăng bản sao lên 2), và lời gọi thứ ba tăng một bản sao tạm thời khác lên 3.<br>"
                   "4. Toàn bộ các bản sao tạm thời bị hủy khi kết thúc câu lệnh chấm phẩy. Đối tượng gốc <code>c</code> chỉ được tăng duy nhất một lần ở bước đầu tiên, do đó <code>c.count == 1</code>!<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 25 & 35: Thuộc tính và trạng thái đối tượng]</span>"
})

# =========================================================================
# NHÓM 3: TÍNH ĐÓNG GÓI (ENCAPSULATION) & INFORMATION HIDING (CÂU 13 - 18)
# =========================================================================

questions.append({
    "id": 13,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Tính Đóng Gói (Encapsulation) & Information Hiding",
    "title": "Bẫy phá vỡ Đóng gói (Encapsulation Breach) bằng cách trả về Con trỏ thành viên Private",
    "code": """#include <iostream>

class Vault {
private:
    int secret_code = 1234;
public:
    int* leakSecret() {
        return &secret_code; // Trả về con trỏ tới biến private
    }
    int getSecret() const { return secret_code; }
};

int main() {
    Vault v;
    int* p = v.leakSecret();
    *p = 9999; // Can thiệp trực tiếp từ bên ngoài
    std::cout << v.getSecret() << std::endl;
    return 0;
}""",
    "options": [
        "A. Lỗi biên dịch vì con trỏ không thể trỏ tới biến private",
        "B. In ra: 9999; việc trả về con trỏ/tham chiếu không hằng tới thuộc tính private làm phá hủy hoàn toàn tính đóng gói của OOP",
        "C. In ra: 1234",
        "D. Lỗi runtime vi phạm bộ nhớ"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Quyền truy cập <code>private</code> chỉ là cơ chế kiểm tra ngữ nghĩa ở tầng biên dịch (Compile-time access checking). Khi chương trình đã biên dịch ra mã máy, thuộc tính <code>secret_code</code> chỉ là một ô nhớ bình thường.<br>"
                   "2. Nếu một phương thức công khai trả về con trỏ (<code>int*</code>) hoặc tham chiếu không hằng (<code>int&</code>) trỏ trực tiếp vào ô nhớ <code>private</code> này, bên ngoài có thể giải con trỏ để ghi đè tùy tiện.<br>"
                   "3. Điều này vi phạm nghiêm trọng nguyên lý đóng gói (Encapsulation Breach). Để an toàn, phương thức getter chỉ được phép trả về theo giá trị (by value) hoặc trả về hằng tham chiếu (<code>const int&</code>).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 36-39: Tính đóng gói & Che giấu chi tiết cài đặt]</span>"
})

questions.append({
    "id": 14,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Tính Đóng Gói (Encapsulation) & Information Hiding",
    "title": "Bản chất quyền truy cập cấp Lớp (Class-Level Access, không phải Object-Level)",
    "code": """#include <iostream>

class SecretHolder {
private:
    int secret;
public:
    SecretHolder(int s) : secret(s) {}
    void stealSecret(const SecretHolder& other) {
        // Truy cập trực tiếp other.secret của một đối tượng KHÁC:
        std::cout << other.secret << std::endl;
    }
};

int main() {
    SecretHolder a(100);
    SecretHolder b(200);
    a.stealSecret(b);
    return 0;
}""",
    "options": [
        "A. Lỗi biên dịch: đối tượng 'a' không được phép truy cập trường private của đối tượng 'b'",
        "B. Hoàn toàn hợp lệ và in ra 200: trong C++, quyền truy cập private là ở cấp độ LỚP (Class-level), các đối tượng cùng một lớp có thể đọc private của nhau",
        "C. Chỉ chạy được nếu b khai báo a là friend",
        "D. Lỗi runtime vi phạm bảo mật"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Rất nhiều người học OOP hiểu nhầm rằng <code>private</code> bảo vệ riêng cho từng đối tượng độc lập (Object-level protection).<br>"
                   "2. Trong C++, quyền truy cập được kiểm soát ở <strong>CẤP ĐỘ LỚP (Class-level)</strong>, chứ không phải cấp độ đối tượng. Nghĩa là: Bất kỳ mã nguồn nào nằm bên trong phạm vi định nghĩa của lớp <code>SecretHolder</code> đều có toàn quyền truy cập vào mọi thành viên <code>private</code> của <strong>BẤT KỲ ĐỐI TƯỢNG NÀO</strong> thuộc lớp <code>SecretHolder</code>.<br>"
                   "3. Do đó, phương thức <code>stealSecret</code> của đối tượng <code>a</code> đọc <code>other.secret</code> hoàn toàn hợp lệ.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 28-29 & 36: Bản chất của Lớp và Đóng gói]</span>"
})

questions.append({
    "id": 15,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Tính Đóng Gói (Encapsulation) & Information Hiding",
    "title": "Bẫy const Member Function: Bản chất của con trỏ this trong hàm const",
    "code": """#include <iostream>

class Account {
    double balance;
public:
    Account(double b) : balance(b) {}
    
    void printBalance() const {
        // Thử thực hiện:
        // balance += 10; // Dòng 1
        std::cout << balance << std::endl; // Dòng 2
    }
};

int main() {
    Account acc(100);
    acc.printBalance();
    return 0;
}""",
    "options": [
        "A. Mở chú thích Dòng 1 chương trình vẫn chạy bình thường",
        "B. Mở chú thích Dòng 1 gây lỗi biên dịch: trong hàm const, con trỏ this có kiểu là 'const Account* const this', cấm sửa đổi thuộc tính",
        "C. Từ khóa const ở cuối hàm chỉ để chú thích cho người đọc, compiler không kiểm tra",
        "D. Hàm const chỉ được gọi bởi các đối tượng const"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong một hàm thành viên thông thường, con trỏ ẩn <code>this</code> có kiểu: <code>Account* const this</code> (hằng con trỏ trỏ tới đối tượng cho phép sửa).<br>"
                   "2. Khi thêm từ khóa <code>const</code> ở cuối hàm (<code>void printBalance() const</code>), kiểu của con trỏ <code>this</code> bị ép chuyển thành: <code>const Account* const this</code> (hằng con trỏ trỏ tới đối tượng chỉ đọc).<br>"
                   "3. Do đó mọi nỗ lực sửa đổi biến thành viên như <code>balance += 10</code> đều bị compiler phát hiện là hành vi vi phạm thuộc tính chỉ đọc và chặn ngay tại compile-time.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 34 & 36: Thuộc tính và tính toàn vẹn dữ liệu]</span>"
})

questions.append({
    "id": 16,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Tính Đóng Gói (Encapsulation) & Information Hiding",
    "title": "Từ khóa mutable: Ngoại lệ hợp lệ duy nhất trong const Member Function",
    "code": """#include <iostream>

class CacheService {
    mutable int access_count = 0;
    int data = 100;
public:
    int getData() const {
        access_count++; // Có hợp lệ trong hàm const?
        return data;
    }
    int getAccessCount() const { return access_count; }
};

int main() {
    const CacheService service;
    service.getData();
    service.getData();
    std::cout << service.getAccessCount() << std::endl;
    return 0;
}""",
    "options": [
        "A. Lỗi biên dịch vì service là const object không thể sửa access_count",
        "B. In ra: 2; từ khóa mutable cho phép thuộc tính được sửa đổi ngay cả trong const member function hoặc trên const object",
        "C. In ra: 0",
        "D. Lỗi runtime vi phạm phân vùng bộ nhớ RODATA"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Chuẩn C++ cung cấp từ khóa <code>mutable</code> để giải quyết bài toán: Tính toàn vẹn logic (Logical Constness) vs Tính toàn vẹn bit (Bitwise Constness).<br>"
                   "2. Đối tượng <code>service</code> về mặt nghiệp vụ không thay đổi dữ liệu cốt lõi (<code>data</code> vẫn nguyên vẹn), nhưng cần cập nhật bộ đếm truy vết hoặc cơ chế khóa (Mutex/Cache).<br>"
                   "3. Thuộc tính khai báo <code>mutable</code> được miễn trừ hoàn toàn khỏi sự ràng buộc của <code>const</code>. Chương trình chạy hoàn hảo và in ra <code>2</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 27 & 36: Trạng thái đối tượng và tính đóng gói]</span>"
})

questions.append({
    "id": 17,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Tính Đóng Gói (Encapsulation) & Information Hiding",
    "title": "Thành viên tĩnh static: Tách biệt khỏi không gian bộ nhớ của từng Instance",
    "code": """#include <iostream>

class InstanceCounter {
public:
    static int count;
    int id;
    InstanceCounter() { count++; }
};

int InstanceCounter::count = 0; // Định nghĩa biến static

int main() {
    InstanceCounter a, b, c;
    std::cout << sizeof(InstanceCounter) << " " << InstanceCounter::count << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: 8 3 (giả sử sizeof(int) == 4, biến static chiếm thêm 4 byte trong đối tượng)",
        "B. In ra: 4 3 (biến static KHÔNG nằm trong bộ nhớ đối tượng mà nằm trong Data/BSS Segment)",
        "C. Lỗi biên dịch vì biến static không được phép khởi tạo ngoài class",
        "D. In ra: 4 1"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Biến thành viên tĩnh (<code>static int count</code>) là thuộc tính chung của toàn bộ LỚP (Class Attribute), không thuộc về bất kỳ một đối tượng thể hiện (Object Instance) cụ thể nào.<br>"
                   "2. Trong cấu trúc bộ nhớ RAM, <code>count</code> được cấp phát trong phân vùng dữ liệu tĩnh (Data/BSS Segment). Bộ nhớ của mỗi đối tượng <code>a</code>, <code>b</code>, <code>c</code> chỉ chứa duy nhất biến thành viên phi tĩnh <code>id</code> (4 bytes). Do đó <code>sizeof(InstanceCounter) == 4</code>.<br>"
                   "3. Mỗi khi tạo một đối tượng, hàm tạo tăng biến dùng chung, in ra <code>3</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 28-29: Khái niệm Lớp và các thành viên dùng chung]</span>"
})

questions.append({
    "id": 18,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Tính Đóng Gói (Encapsulation) & Information Hiding",
    "title": "Bẫy gọi hàm thành viên thông thường từ Static Member Function",
    "code": """#include <iostream>

class Device {
    int serial = 12345;
public:
    static void resetDevice() {
        // Dòng thử nghiệm:
        // serial = 0; 
        std::cout << "Resetting..." << std::endl;
    }
};

int main() {
    Device::resetDevice();
    return 0;
}""",
    "options": [
        "A. Mở chú thích dòng 'serial = 0;' chương trình vẫn chạy bình thường",
        "B. Lỗi biên dịch: không thể truy cập thành viên phi tĩnh 'serial' từ hàm tĩnh vì static function KHÔNG CÓ con trỏ this",
        "C. Hợp lệ nếu gọi qua đối tượng: Device d; d.resetDevice()",
        "D. Hàm static tự động biến serial thành biến static"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Phương thức tĩnh (Static Member Function) được trình biên dịch tạo mã máy như một hàm tự do toàn cục thông thường, hoàn toàn <strong>KHÔNG ĐƯỢC TRUYỀN CON TRỎ ẨN <code class=\"inline-code\">this</code></strong>.<br>"
                   "2. Việc truy cập <code>serial</code> đòi hỏi phải biết địa chỉ ô nhớ của một đối tượng cụ thể (<code>this->serial</code>). Do không có <code>this</code>, trình biên dịch báo lỗi ngay lập tức: <em>cannot access non-static data member 'serial' from static member function</em>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 35: Cơ chế truyền thông điệp & phương thức]</span>"
})

# =========================================================================
# NHÓM 4: LỚP & VÒNG ĐỜI THỂ HIỆN (INSTANCE LIFECYCLE) (CÂU 19 - 25)
# =========================================================================

questions.append({
    "id": 19,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Lớp (Class) & Vòng Đời Thể Hiện (Lifecycle)",
    "title": "Bẫy thứ tự khởi tạo trong Member Initializer List (Declaration Order Rule)",
    "code": """#include <iostream>

class OrderTest {
    int a;
    int b;
public:
    // Khởi tạo: viết b trước a trong danh sách khởi tạo
    OrderTest(int val) : b(val), a(b + 5) {}
    
    void print() {
        std::cout << "a=" << a << " b=" << b << std::endl;
    }
};

int main() {
    OrderTest obj(10);
    obj.print();
    return 0;
}""",
    "options": [
        "A. Chắc chắn luôn in ra: a=15 b=10",
        "B. Hành vi không xác định (UB): 'a' luôn được khởi tạo trước 'b' theo thứ tự khai báo trong class, do đó 'a' sử dụng giá trị rác của 'b'",
        "C. Lỗi biên dịch vì b đứng trước a trong initializer list",
        "D. In ra: a=5 b=10"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Chuẩn C++ quy định một quy tắc vàng: Các biến thành viên <strong>LUÔN ĐƯỢC KHỞI TẠO THEO THỨ TỰ CHÚNG ĐƯỢC KHAI BÁO TRONG CLASS</strong>, hoàn toàn bất chấp thứ tự viết trong Member Initializer List.<br>"
                   "2. Trong <code>OrderTest</code>, <code>int a</code> được khai báo trước <code>int b</code>. Do đó <code>a</code> được khởi tạo trước bằng biểu thức <code>b + 5</code>.<br>"
                   "3. Tại thời điểm đó, <code>b</code> chưa hề được cấp giá trị (đang chứa rác trên stack). Lấy rác cộng 5 gán cho <code>a</code> dẫn tới Undefined Behavior.<br>"
                   "Trình biên dịch hiện đại (như GCC với cờ <code>-Wreorder</code>) sẽ phát cảnh báo nghiêm trọng về lỗi này.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 28-34: Khai báo lớp và khởi tạo thuộc tính]</span>"
})

questions.append({
    "id": 20,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Lớp (Class) & Vòng Đời Thể Hiện (Lifecycle)",
    "title": "Trường dữ liệu const và tham chiếu (&) bắt buộc phải dùng Initializer List",
    "code": """#include <iostream>

class SpecialClass {
    const int max_limit;
    int& ref_val;
public:
    SpecialClass(int limit, int& external) {
        // Dòng 1:
        // max_limit = limit;
        // Dòng 2:
        // ref_val = external;
    }
};""",
    "options": [
        "A. Gán trong thân constructor (Dòng 1, Dòng 2) hoàn toàn hợp lệ",
        "B. Lỗi biên dịch: biến thành viên const và tham chiếu bắt buộc phải được khởi tạo trong Member Initializer List, không thể gán trong thân Constructor",
        "C. Chỉ cần từ khóa const là phải dùng list, tham chiếu thì gán trong thân được",
        "D. Chỉ hợp lệ nếu thêm từ khóa static"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi bước vào dấu ngoặc nhọn <code>{</code> của thân Constructor, mọi biến thành viên đã được cấp phát và khởi tạo xong xuôi.<br>"
                   "2. Một biến tham chiếu (<code>int&</code>) không thể tồn tại ở trạng thái chưa khởi tạo (uninitialized reference). Một biến hằng (<code>const int</code>) không thể bị ghi đè sau khi đã hình thành.<br>"
                   "3. Phép gán trong thân Constructor là phép gán (assignment), không phải khởi tạo (initialization). Do đó, chuẩn C++ bắt buộc phải dùng Initializer List: <code>SpecialClass(...) : max_limit(limit), ref_val(external) {}</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 28-34: Định nghĩa lớp và khởi tạo]</span>"
})

questions.append({
    "id": 21,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Lớp (Class) & Vòng Đời Thể Hiện (Lifecycle)",
    "title": "Mất Constructor mặc định tự sinh (Synthesized Default Constructor)",
    "code": """#include <iostream>

class Product {
public:
    int id;
    Product(int id) : id(id) {} // Constructor có tham số
};

int main() {
    Product p1(101); // Dòng A
    Product p2;      // Dòng B
    std::cout << p1.id << std::endl;
    return 0;
}""",
    "options": [
        "A. Cả Dòng A và Dòng B đều chạy bình thường",
        "B. Dòng B lỗi biên dịch: no matching function for call to 'Product::Product()'",
        "C. Dòng B hợp lệ và id của p2 tự động bằng 0",
        "D. Dòng A lỗi biên dịch"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trình biên dịch C++ chỉ tự động sinh Constructor mặc định không tham số (Default Constructor) NẾU VÀ CHỈ NẾU lập trình viên <strong>chưa định nghĩa bất kỳ Constructor nào khác</strong>.<br>"
                   "2. Khi lập trình viên đã viết <code>Product(int id)</code>, compiler coi như lập trình viên muốn áp đặt quy tắc khởi tạo có tham số, và compiler lập tức hủy bỏ việc sinh Default Constructor.<br>"
                   "3. Lệnh <code>Product p2;</code> ở Dòng B yêu cầu gọi constructor không tham số, nhưng không tìm thấy nên gây lỗi biên dịch.<br>"
                   "Trong C++11, có thể khôi phục bằng cú pháp: <code>Product() = default;</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 29-31: Khai báo lớp và khởi tạo đối tượng]</span>"
})

questions.append({
    "id": 22,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Lớp (Class) & Vòng Đời Thể Hiện (Lifecycle)",
    "title": "Từ khóa explicit: Ngăn chặn chuyển đổi kiểu ngầm định nguy hiểm (Implicit Conversion)",
    "code": """#include <iostream>

class Buffer {
public:
    explicit Buffer(int size) {
        std::cout << "Alloc: " << size << std::endl;
    }
};

void processBuffer(Buffer b) {}

int main() {
    Buffer b1(10); // Hợp lệ
    // Buffer b2 = 20; // Thử nghiệm 1
    // processBuffer(30); // Thử nghiệm 2
    return 0;
}""",
    "options": [
        "A. Thử nghiệm 1 và 2 đều hợp lệ",
        "B. Cả Thử nghiệm 1 và 2 đều bị chặn và báo lỗi biên dịch do từ khóa explicit ngăn cản chuyển đổi ngầm định từ int sang Buffer",
        "C. Từ khóa explicit chỉ có tác dụng trong C++20",
        "D. Chương trình crash tại runtime"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, một constructor có thể gọi với 1 tham số mặc định đóng vai trò như một toán tử chuyển đổi kiểu ngầm định (Implicit Conversion Operator). Nếu không có <code>explicit</code>, lệnh <code>processBuffer(30)</code> sẽ âm thầm tạo một đối tượng Buffer kích thước 30 mà người lập trình không hề hay biết.<br>"
                   "2. Từ khóa <code>explicit</code> báo cho compiler: 'Chỉ được khởi tạo đối tượng tường minh, cấm dùng trong các phép gán ngầm định hoặc truyền tham số hàm chuyển đổi kiểu'.<br>"
                   "3. Cả <code>Buffer b2 = 20;</code> và <code>processBuffer(30);</code> đều bị compiler chặn đứng ngay lập tức.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 31-34: Khởi tạo lớp và các hàm thành viên]</span>"
})

questions.append({
    "id": 23,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Lớp (Class) & Vòng Đời Thể Hiện (Lifecycle)",
    "title": "Bẫy sao chép nông (Shallow Copy) và lỗi Double Free trong Destructor",
    "code": """#include <iostream>

class DynamicArray {
public:
    int* data;
    DynamicArray(int val) {
        data = new int(val);
    }
    ~DynamicArray() {
        delete data; // Giải phóng ô nhớ heap
    }
};

int main() {
    DynamicArray a(50);
    DynamicArray b = a; // Gọi Implicit Copy Constructor
    return 0;
}""",
    "options": [
        "A. Chương trình chạy an toàn không có lỗi",
        "B. Lỗi biên dịch vì class chứa con trỏ không thể sao chép",
        "C. Lỗi sập chương trình nghiêm trọng (Double Free Corruption): Copy Constructor mặc định chỉ sao chép nông địa chỉ con trỏ, khi thoát hàm cả a và b cùng delete một địa chỉ heap",
        "D. Hệ điều hành tự động nhân bản vùng nhớ heap"
    ],
    "correct": 2,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Copy Constructor mặc định của C++ thực hiện sao chép từng thành viên (Member-wise Copy / Shallow Copy).<br>"
                   "2. Khi gán <code>DynamicArray b = a;</code>, con trỏ <code>b.data</code> nhận đúng địa chỉ mà <code>a.data</code> đang trỏ tới. Cả hai cùng trỏ chung vào 1 ô nhớ Heap duy nhất.<br>"
                   "3. Khi hàm <code>main</code> kết thúc: <code>b</code> bị hủy trước, gọi <code>delete b.data</code> -> ô nhớ heap bị giải phóng.<br>"
                   "4. Tiếp tục <code>a</code> bị hủy, gọi <code>delete a.data</code> -> Cố gắng giải phóng một ô nhớ ĐÃ BỊ GIẢI PHÓNG. Lỗi <strong>Double Free</strong> xảy ra làm hệ điều hành terminate tiến trình ngay lập tức.<br>"
                   "Đây là quy tắc Rule of Three kinh điển của C++.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 25 & 37: Quản lý thuộc tính và tính đóng gói]</span>"
})

questions.append({
    "id": 24,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Lớp (Class) & Vòng Đời Thể Hiện (Lifecycle)",
    "title": "Kỹ thuật C++11 '= delete' để ngăn chặn hoàn toàn việc sao chép đối tượng",
    "code": """#include <iostream>

class NonCopyable {
public:
    NonCopyable() = default;
    NonCopyable(const NonCopyable&) = delete;
    NonCopyable& operator=(const NonCopyable&) = delete;
};

int main() {
    NonCopyable n1;
    // NonCopyable n2 = n1; // Dòng kiểm tra
    return 0;
}""",
    "options": [
        "A. Mở chú thích dòng kiểm tra: Lỗi biên dịch 'use of deleted function NonCopyable::NonCopyable(const NonCopyable&)'",
        "B. Vẫn sao chép được nếu ép kiểu qua static_cast",
        "C. Cú pháp = delete chỉ dùng để xóa con trỏ",
        "D. Lỗi runtime vi phạm bộ nhớ"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong các hệ thống quản lý tài nguyên độc quyền (như file handle, socket, database connection), việc sao chép đối tượng là hoàn toàn bị cấm.<br>"
                   "2. C++11 giới thiệu cú pháp <code>= delete</code>: Cho phép lập trình viên chỉ thị cho trình biên dịch xóa bỏ hoàn toàn một hàm thành viên khỏi danh sách phân giải quá tải.<br>"
                   "3. Mọi thao tác sao chép như <code>NonCopyable n2 = n1;</code> đều bị chặn đứng ngay từ lúc biên dịch.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 16 & 28: Thiết kế hướng đối tượng an toàn]</span>"
})

questions.append({
    "id": 25,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Lớp (Class) & Vòng Đời Thể Hiện (Lifecycle)",
    "title": "Khởi tạo thành viên trực tiếp trong khai báo Class (C++11 In-class Member Initializer)",
    "code": """#include <iostream>

class Widget {
public:
    int x = 10;
    int y = 20;
    Widget() {}
    Widget(int custom_x) : x(custom_x) {}
};

int main() {
    Widget w1;
    Widget w2(99);
    std::cout << w1.x << " " << w1.y << " | " << w2.x << " " << w2.y << std::endl;
    return 0;
}""",
    "options": [
        "A. 10 20 | 99 20",
        "B. 10 20 | 99 0",
        "C. Lỗi biên dịch vì C++ cấm gán giá trị tại nơi khai báo thuộc tính trong class",
        "D. 0 0 | 99 0"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trước C++11, việc gán giá trị trực tiếp <code>int x = 10;</code> trong khai báo class bị cấm.<br>"
                   "2. Từ C++11, tính năng <em>In-class member initializer</em> được chuẩn hóa: Trình biên dịch sẽ tự động chèn mã khởi tạo <code>x = 10; y = 20;</code> vào tất cả các Constructor nào không khởi tạo tường minh biến đó trong Member Initializer List.<br>"
                   "3. <code>w1</code> dùng toàn bộ giá trị mặc định: <code>10 20</code>.<br>"
                   "4. <code>w2</code> khởi tạo tường minh <code>x(99)</code> nên ghi đè 10, trong khi <code>y</code> vẫn dùng giá trị mặc định là 20. Kết quả in ra: <code>10 20 | 99 20</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 28-34: Khai báo lớp và khởi tạo]</span>"
})

# =========================================================================
# NHÓM 5: THÔNG ĐIỆP & CON TRỎ THIS (CÂU 26 - 30)
# =========================================================================

questions.append({
    "id": 26,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Truyền Thông Điệp (Message Passing) & Cơ Chế Gọi Hàm",
    "title": "Bản chất chuyển đổi Thông điệp thành Mã Máy của C++ Compiler",
    "code": """#include <iostream>

class Car {
    int speed;
public:
    Car(int s) : speed(s) {}
    void accelerate(int delta) {
        this->speed += delta;
    }
    int getSpeed() const { return speed; }
};

int main() {
    Car myCar(50);
    myCar.accelerate(20);
    std::cout << myCar.getSpeed() << std::endl;
    return 0;
}""",
    "options": [
        "A. accelerate gửi một tín hiệu broadcast qua IPC của hệ điều hành",
        "B. Lời gọi myCar.accelerate(20) được compiler hạ xuống thành lời gọi hàm mức máy tương đương Car_accelerate(&myCar, 20)",
        "C. Mã accelerate nằm trực tiếp bên trong vùng nhớ của biến myCar",
        "D. Đối tượng myCar bị nhân bản mỗi khi gọi hàm"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 35 định nghĩa: 'Thông điệp (Message) là phương tiện để đối tượng này chuyển yêu cầu tới đối tượng khác... Trong C++, thông điệp được hiện thực bằng lời gọi phương thức'.<br>"
                   "2. Ở tầng thấp (Lower level), trình biên dịch chuyển đổi phương thức thành một hàm toàn cục duy nhất kèm Name Mangling, và nạp địa chỉ của <code>myCar</code> làm đối số đầu tiên (con trỏ <code>this</code>).<br>"
                   "3. Đoạn mã máy thực tế chỉ biên dịch một lần duy nhất trong phân vùng Text/Code Segment, không hề tốn bộ nhớ lưu trữ mã lệnh trong từng đối tượng.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 35: Khái niệm Thông điệp (Message)]</span>"
})

questions.append({
    "id": 27,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Truyền Thông Điệp (Message Passing) & Cơ Chế Gọi Hàm",
    "title": "Con trỏ tới hàm thành viên (Pointer-to-Member Function) và toán tử .* / ->*",
    "code": """#include <iostream>

class MathOp {
public:
    int square(int x) { return x * x; }
    int cube(int x) { return x * x * x; }
};

int main() {
    int (MathOp::*pmf)(int) = &MathOp::square; // Con trỏ tới hàm thành viên
    MathOp op;
    std::cout << (op.*pmf)(5) << " ";
    
    pmf = &MathOp::cube;
    std::cout << (op.*pmf)(3) << std::endl;
    return 0;
}""",
    "options": [
        "A. 25 27",
        "B. Lỗi biên dịch vì C++ không hỗ trợ con trỏ tới hàm thành viên",
        "C. 5 3",
        "D. Lỗi runtime vi phạm con trỏ"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, một hàm thành viên khác với một hàm tự do vì nó cần một đối tượng để cung cấp con trỏ <code>this</code>.<br>"
                   "2. Cú pháp khai báo con trỏ tới hàm thành viên: <code>Return_Type (ClassName::*ptr_name)(Arg_Types)</code>.<br>"
                   "3. Khi gọi thông qua đối tượng, bắt buộc phải dùng toán tử đặc biệt <code>.*</code>: <code>(op.*pmf)(5)</code>, hoặc <code>(ptr->*pmf)(5)</code> nếu thông qua con trỏ đối tượng.<br>"
                   "4. Kết quả tính toán: <code>5*5 = 25</code> và <code>3*3*3 = 27</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 35: Phương thức và tương tác đối tượng]</span>"
})

questions.append({
    "id": 28,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Truyền Thông Điệp (Message Passing) & Cơ Chế Gọi Hàm",
    "title": "Đa năng hóa hàm thành viên dựa trên tính const của phương thức",
    "code": """#include <iostream>

class TextHolder {
public:
    void display() {
        std::cout << "Non-const" << std::endl;
    }
    void display() const {
        std::cout << "Const" << std::endl;
    }
};

int main() {
    TextHolder t1;
    const TextHolder t2;
    t1.display();
    t2.display();
    return 0;
}""",
    "options": [
        "A. Non-const Const",
        "B. Const Const",
        "C. Lỗi biên dịch vì hai hàm trùng tên và trùng danh sách tham số",
        "D. Non-const Non-const"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Nhiều người lầm tưởng hai hàm trên có chữ ký trùng nhau. Tuy nhiên, tham số ngầm định <code>this</code> của chúng có kiểu khác nhau:<br>"
                   "   - Bản thứ nhất: <code>display(TextHolder* const this)</code>.<br>"
                   "   - Bản thứ hai: <code>display(const TextHolder* const this)</code>.<br>"
                   "2. Khi gọi <code>t1.display()</code>: <code>t1</code> là đối tượng không hằng nên trình biên dịch ưu tiên gọi bản non-const -> in 'Non-const'.<br>"
                   "3. Khi gọi <code>t2.display()</code>: <code>t2</code> là đối tượng <code>const</code>, chỉ có thể gọi được phiên bản <code>const</code> -> in 'Const'.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 34-36: Phương thức và tính toàn vẹn trạng thái]</span>"
})

questions.append({
    "id": 29,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Truyền Thông Điệp (Message Passing) & Cơ Chế Gọi Hàm",
    "title": "Bẫy Name Hiding giữa các phạm vi lớp kế thừa",
    "code": """#include <iostream>

class Base {
public:
    void show(int x) { std::cout << "Base: " << x << std::endl; }
};

class Derived : public Base {
public:
    void show(double d) { std::cout << "Derived: " << d << std::endl; }
};

int main() {
    Derived d;
    d.show(5); // Gọi với số nguyên int
    return 0;
}""",
    "options": [
        "A. Base: 5 (vì khớp chính xác kiểu int)",
        "B. Derived: 5 (hàm trong lớp con che khuất hoàn toàn hàm cùng tên trong lớp cha, ép kiểu ngầm định int sang double)",
        "C. Lỗi biên dịch vì nhập nhằng giữa hai hàm",
        "D. Lỗi runtime tại thời điểm gọi hàm"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, quá trình tra cứu tên (Name Lookup) diễn ra trước quá trình phân giải quá tải (Overload Resolution).<br>"
                   "2. Khi gặp <code>d.show(5)</code>, trình biên dịch bắt đầu tìm kiếm định danh <code>show</code> từ phạm vi hẹp nhất là <code>Derived</code>. Nó tìm thấy <code>Derived::show(double)</code>.<br>"
                   "3. Ngay lập tức, quá trình tra cứu tên DỪNG LẠI (không tìm kiếm lên lớp <code>Base</code> nữa). Toàn bộ các hàm tên <code>show</code> của <code>Base</code> bị <strong>ẨN HOÀN TOÀN (Name Hiding)</strong>.<br>"
                   "4. Compiler ép số nguyên <code>5</code> thành số thực <code>5.0</code> để gọi <code>Derived::show(double)</code> -> in ra <code>Derived: 5</code>.<br>"
                   "Muốn giữ lại hàm của lớp cha, phải dùng chỉ thị: <code>using Base::show;</code> trong lớp con.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 40 & 43: Đặc điểm của lớp dẫn xuất trong thừa kế]</span>"
})

questions.append({
    "id": 30,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Truyền Thông Điệp (Message Passing) & Cơ Chế Gọi Hàm",
    "title": "Bẫy thay đổi cấu trúc bên trong nhưng giữ nguyên giao diện ngoài (Interface Invariance)",
    "code": """#include <iostream>

// Thiết kế cũ dùng 2 số nguyên biểu diễn Phân số:
class Fraction {
private:
    int num, den; // Cấu trúc dữ liệu nội bộ
public:
    Fraction(int n, int d) : num(n), den(d) {}
    double toDecimal() const { return (double)num / den; }
};

int main() {
    Fraction f(1, 2);
    std::cout << f.toDecimal() << std::endl;
    return 0;
}""",
    "options": [
        "A. Nếu đổi cấu trúc bên trong từ 2 biến int sang 1 biến double duy nhất, mã của hàm main không cần thay đổi",
        "B. Nếu đổi cấu trúc bên trong, toàn bộ hàm main bắt buộc phải sửa đổi",
        "C. OOP bắt buộc cấu trúc dữ liệu bên trong phải cố định vĩnh viễn",
        "D. Hàm toDecimal() bắt buộc phải trả về kiểu int"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 16 nêu bật ưu điểm của OOP: 'Khi thay đổi cấu trúc dữ liệu của một đối tượng, KHÔNG CẦN THAY ĐỔI MÃ NGUỒN của các đối tượng khác, mà chỉ cần thay đổi một số thành phần của đối tượng bị thay đổi'.<br>"
                   "2. Do hàm <code>main</code> chỉ giao tiếp với <code>Fraction</code> thông qua giao diện công khai <code>toDecimal()</code>, ta hoàn toàn có thể tái cấu trúc (refactor) bên trong thành <code>double value = 0.5;</code> mà mã nguồn bên ngoài vẫn chạy nguyên vẹn.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 16: Ưu điểm của tiếp cận hướng đối tượng]</span>"
})

# =========================================================================
# NHÓM 6: TÍNH KẾ THỪA (INHERITANCE) & IS-A VS HAS-A (CÂU 31 - 38)
# =========================================================================

questions.append({
    "id": 31,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Tính Kế Thừa (Inheritance) & IS-A vs HAS-A",
    "title": "Phân biệt bản chất quan hệ IS-A (Kế thừa) và quan hệ HAS-A (Thành phần)",
    "code": """#include <iostream>

class Engine {};

// Cách 1:
class CarA : public Engine {}; // Kế thừa IS-A

// Cách 2:
class CarB {                   // Chứa đựng HAS-A
    Engine engine;
};""",
    "options": [
        "A. CarA là thiết kế chuẩn OOP vì Ô tô là một Động cơ",
        "B. CarB là thiết kế chuẩn OOP: Car HAS-A Engine (Ô tô có một Động cơ), dùng Composition; CarA vi phạm ngữ nghĩa vì Ô tô không phải là Động cơ (Car IS-NOT-A Engine)",
        "C. Cả hai cách đều hoàn toàn tương đương nhau về mặt thiết kế kiến trúc",
        "D. CarB vi phạm tính đóng gói"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Kế thừa (Inheritance) chỉ được sử dụng khi tồn tại quan hệ bản chất <strong>IS-A (Là một)</strong>: Một lớp con là một trường hợp đặc biệt, một thể loại cụ thể của lớp cha (ví dụ: Chó là Động vật, Xe tải là Xe cơ giới).<br>"
                   "2. Khi một đối tượng là một bộ phận, thành phần cấu thành nên đối tượng khác, quan hệ đó là <strong>HAS-A (Có một / Chứa)</strong>. Ta phải dùng kỹ thuật Bao hàm / Thành phần (Composition).<br>"
                   "3. Một chiếc Ô tô 'có một' Động cơ, chứ Ô tô 'không phải là' một Động cơ. Thiết kế <code>CarA</code> là sai lầm kinh điển trong hướng đối tượng.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 40-43: Tính thừa kế trong hệ thống hướng đối tượng]</span>"
})

questions.append({
    "id": 32,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Tính Kế Thừa (Inheritance) & IS-A vs HAS-A",
    "title": "Bảng chuyển đổi quyền truy cập trong Kế thừa Public vs Protected vs Private",
    "code": """#include <iostream>

class Base {
public:
    int pub = 1;
protected:
    int pro = 2;
private:
    int pri = 3;
};

class Derived : private Base {
public:
    void check() {
        std::cout << pub << " " << pro << std::endl; // Hợp lệ không?
    }
};

int main() {
    Derived d;
    // d.pub = 10; // Dòng kiểm tra bên ngoài
    d.check();
    return 0;
}""",
    "options": [
        "A. check() in ra: 1 2; dòng d.pub lỗi biên dịch vì thừa kế private biến mọi thành viên của cha thành private trong con",
        "B. check() bị lỗi biên dịch vì không thể truy cập protected",
        "C. d.pub bên ngoài main hoàn toàn hợp lệ",
        "D. Thừa kế private cấm lớp con truy cập biến của lớp cha"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong kế thừa riêng tư (<code>private Base</code>): Toàn bộ các thành viên <code>public</code> và <code>protected</code> của lớp cha khi truyền xuống lớp con sẽ bị chuyển đổi thành phạm vi <code>private</code> của lớp con.<br>"
                   "2. Bên trong các phương thức của <code>Derived</code> (như hàm <code>check</code>), các biến <code>pub</code> và <code>pro</code> vẫn được phép truy cập tự do.<br>"
                   "3. Tuy nhiên, từ bên ngoài (như hàm <code>main</code>), <code>d.pub</code> đã trở thành thành viên <code>private</code> của <code>Derived</code>, nên việc gọi <code>d.pub = 10</code> bị compiler chặn ngay lập tức.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 40 & 43: Thừa kế và quyền truy cập thành viên]</span>"
})

questions.append({
    "id": 33,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Tính Kế Thừa (Inheritance) & IS-A vs HAS-A",
    "title": "Thứ tự gọi Constructor và Destructor trong Cây Kế Thừa Đơn",
    "code": """#include <iostream>

class Base {
public:
    Base() { std::cout << "B+ "; }
    ~Base() { std::cout << "B- "; }
};

class Derived : public Base {
public:
    Derived() { std::cout << "D+ "; }
    ~Derived() { std::cout << "D- "; }
};

int main() {
    {
        Derived d;
    }
    std::cout << std::endl;
    return 0;
}""",
    "options": [
        "A. B+ D+ D- B-",
        "B. D+ B+ B- D-",
        "C. B+ D+ B- D-",
        "D. D+ B+ D- B-"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Bố cục bộ nhớ của đối tượng <code>Derived</code> bao gồm phần cốt lõi của lớp <code>Base</code> nằm trước, sau đó mới đến phần mở rộng của <code>Derived</code>.<br>"
                   "2. Thứ tự khởi tạo (Construction Order): Nền móng phải xây trước. Constructor của <code>Base</code> bắt buộc phải hoàn tất (in <code>B+</code>) rồi mới đến Constructor của <code>Derived</code> (in <code>D+</code>).<br>"
                   "3. Thứ tự hủy (Destruction Order): Ngược lại hoàn toàn với khởi tạo (LIFO). Destructor của lớp con <code>Derived</code> phải chạy trước để dọn dẹp các tài nguyên mở rộng (in <code>D-</code>), sau đó mới tới Destructor của <code>Base</code> (in <code>B-</code>).<br>"
                   "Chuỗi in hoàn chỉnh: <code>B+ D+ D- B-</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 40-43: Thứ tự thực thi trong thừa kế]</span>"
})

questions.append({
    "id": 34,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Tính Kế Thừa (Inheritance) & IS-A vs HAS-A",
    "title": "Thứ tự khởi tạo khi Lớp con vừa Kế Thừa vừa Chứa Đối Tượng Thành Viên (Composition)",
    "code": """#include <iostream>

struct Part { Part() { std::cout << "Part "; } };
struct Base { Base() { std::cout << "Base "; } };

struct Derived : public Base {
    Part member;
    Derived() { std::cout << "Derived "; }
};

int main() {
    Derived d;
    std::cout << std::endl;
    return 0;
}""",
    "options": [
        "A. Base Part Derived",
        "B. Part Base Derived",
        "C. Derived Part Base",
        "D. Base Derived Part"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "Quy tắc khởi tạo chuẩn xác trong C++:<br>"
                   "1. Bước 1: Khởi tạo toàn bộ các lớp cơ sở (Base classes) theo thứ tự kế thừa -> in <code>Base</code>.<br>"
                   "2. Bước 2: Khởi tạo toàn bộ các biến thành viên (Member objects) theo thứ tự khai báo trong class -> in <code>Part</code>.<br>"
                   "3. Bước 3: Thực thi thân Constructor của chính lớp dẫn xuất -> in <code>Derived</code>.<br>"
                   "Kết quả: <code>Base Part Derived</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 40-43: Kế thừa và thành phần]</span>"
})

questions.append({
    "id": 35,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Tính Kế Thừa (Inheritance) & IS-A vs HAS-A",
    "title": "Bẫy cắt gọt đối tượng (Object Slicing Trap) khi gán theo Giá Trị",
    "code": """#include <iostream>

class Base {
public:
    int b = 10;
};

class Derived : public Base {
public:
    int d = 20;
};

int main() {
    Derived objD;
    objD.b = 99;
    objD.d = 88;

    Base objB = objD; // Bẫy Object Slicing
    std::cout << sizeof(objB) << " " << objB.b << std::endl;
    return 0;
}""",
    "options": [
        "A. objB chứa cả b và d, sizeof bằng sizeof(Derived)",
        "B. objB chỉ là một đối tượng Base; toàn bộ thuộc tính d của Derived bị cắt gọt (sliced off), sizeof bằng sizeof(Base) và objB.b = 99",
        "C. Lỗi biên dịch vì không thể gán đối tượng con cho biến cha",
        "D. Lỗi runtime vi phạm tràn bộ nhớ"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Biến <code>Base objB</code> được cấp phát trên Stack với kích thước chỉ đủ chứa các thuộc tính của <code>Base</code> (chỉ chứa <code>int b</code>).<br>"
                   "2. Khi thực hiện phép gán theo giá trị <code>Base objB = objD;</code>, Copy Constructor của <code>Base</code> được gọi. Nó chỉ sao chép phần dữ liệu của <code>Base</code> nằm trong <code>objD</code>.<br>"
                   "3. Toàn bộ phần dữ liệu mở rộng của <code>Derived</code> (biến <code>d</code>) hoàn toàn bị cắt bỏ (Sliced off) vì không có chỗ chứa trong <code>objB</code>.<br>"
                   "Để duy trì tính toàn vẹn đa hình, trong C++ bắt buộc phải dùng con trỏ (<code>Base*</code>) hoặc tham chiếu (<code>Base&</code>).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 40-43: Tính chất lớp dẫn xuất và lớp cơ sở]</span>"
})

questions.append({
    "id": 36,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Tính Kế Thừa (Inheritance) & IS-A vs HAS-A",
    "title": "Upcasting an toàn tuyệt đối với Con trỏ và Tham chiếu",
    "code": """#include <iostream>

class Animal {
public:
    int health = 100;
};

class Cat : public Animal {
public:
    int lives = 9;
};

int main() {
    Cat myCat;
    Animal* ptr = &myCat; // Upcast con trỏ
    Animal& ref = myCat;  // Upcast tham chiếu
    
    std::cout << ptr->health << " " << ref.health << std::endl;
    return 0;
}""",
    "options": [
        "A. Hợp lệ 100% và in ra 100 100 (Upcast trong kế thừa public là an toàn tuyệt đối và không cần ép kiểu tường minh)",
        "B. Lỗi biên dịch vì thiếu phép ép kiểu static_cast<Animal*>",
        "C. Xảy ra hiện tượng Object Slicing làm mất dữ liệu",
        "D. Gây lỗi Segmentation Fault tại runtime"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Kế thừa công khai (<code>public inheritance</code>) thiết lập mối quan hệ IS-A: Mọi con Mèo đều là một Động vật.<br>"
                   "2. Về mặt địa chỉ bộ nhớ, phần đầu của đối tượng <code>Cat</code> chính là bố cục ô nhớ của <code>Animal</code>. Do đó địa chỉ của <code>myCat</code> và địa chỉ của phần <code>Animal</code> bên trong nó là trùng khớp hoàn hảo.<br>"
                   "3. Phép Upcast chuyển đổi con trỏ/tham chiếu từ lớp con lên lớp cha là an toàn tuyệt đối (100% Type-Safe) và được trình biên dịch thực hiện ngầm định mà không cần bất kỳ cú pháp cast nào.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 40-43: Tái sử dụng mã và quan hệ kế thừa]</span>"
})

questions.append({
    "id": 37,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Tính Kế Thừa (Inheritance) & IS-A vs HAS-A",
    "title": "Gọi phương thức bị che khuất của Lớp Cha bằng toán tử định phạm vi Base::",
    "code": """#include <iostream>

class Parent {
public:
    void greet() { std::cout << "Hello from Parent" << std::endl; }
};

class Child : public Parent {
public:
    void greet() {
        Parent::greet(); // Gọi tường minh hàm lớp cha
        std::cout << "Hello from Child" << std::endl;
    }
};

int main() {
    Child c;
    c.greet();
    return 0;
}""",
    "options": [
        "A. Lặp vô tận vì hàm greet tự gọi đệ quy",
        "B. In ra: Hello from Parent, tiếp theo Hello from Child",
        "C. Lỗi biên dịch vì không được dùng Parent:: bên trong Child",
        "D. Chỉ in ra: Hello from Child"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi lớp con định nghĩa một hàm trùng tên <code>greet()</code>, nó sẽ che khuất (hide) hàm của lớp cha.<br>"
                   "2. Để tái sử dụng mã nguồn và tránh lặp mã, C++ cho phép lớp con gọi trực tiếp phương thức của lớp cha bằng toán tử định phạm vi: <code>Parent::greet();</code>.<br>"
                   "3. Trình biên dịch sẽ liên kết tĩnh trực tiếp tới địa chỉ của <code>Parent::greet</code>, thực thi in ra thông điệp của cha trước rồi đến con.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 43: Lớp dẫn xuất sử dụng lại các phương thức của lớp cơ sở]</span>"
})

questions.append({
    "id": 38,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Tính Kế Thừa (Inheritance) & IS-A vs HAS-A",
    "title": "Bẫy con trỏ Downcasting không kiểm tra (Unsafe Downcast Trap)",
    "code": """#include <iostream>

class Vehicle { public: int v = 1; };
class Airplane : public Vehicle { public: void fly() { std::cout << "Flying" << std::endl; } };

int main() {
    Vehicle car;
    // Bẫy Downcast ép từ Cha xuống Con:
    Airplane* planePtr = static_cast<Airplane*>(&car);
    planePtr->fly();
    return 0;
}""",
    "options": [
        "A. Chương trình đảm bảo an toàn tuyệt đối",
        "B. Nguy hiểm: static_cast không kiểm tra kiểu tại runtime, car thực chất chỉ là Vehicle, việc đối xử với nó như Airplane là Undefined Behavior",
        "C. Lỗi biên dịch vì static_cast không hỗ trợ downcast",
        "D. car tự động được cấp phát thêm bộ nhớ của Airplane"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <code>car</code> là một thể hiện độc lập của <code>Vehicle</code>, chỉ chiếm kích thước bộ nhớ của <code>Vehicle</code> trên stack.<br>"
                   "2. <code>static_cast<Airplane*></code> chỉ kiểm tra tại compile-time rằng giữa hai lớp có quan hệ kế thừa. Nó ép con trỏ mà không kiểm tra tại runtime xem đối tượng thực tế đằng sau là gì.<br>"
                   "3. Khi <code>planePtr</code> gọi phương thức hoặc truy cập thuộc tính mở rộng của <code>Airplane</code>, chương trình sẽ đọc/ghi vào vùng nhớ không thuộc về đối tượng, dẫn đến lỗi đổ vỡ nghiêm trọng (Undefined Behavior).<br>"
                   "Để downcast an toàn, bắt buộc lớp cơ sở phải có tính đa hình (hàm ảo) và sử dụng <code>dynamic_cast</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 40-43: Quan hệ kiểu dữ liệu trong thừa kế]</span>"
})

# =========================================================================
# NHÓM 7: TÍNH ĐA HÌNH & BẢNG ẢO VTABLE (CÂU 39 - 46)
# =========================================================================

questions.append({
    "id": 39,
    "group_id": "q-group-7",
    "group_name": "Nhóm 7: Tính Đa Hình (Polymorphism) & Liên Kết Động VTable",
    "title": "Liên kết tĩnh (Early Binding) khi hàm không có từ khóa virtual",
    "code": """#include <iostream>

class Shape {
public:
    void draw() { std::cout << "Shape" << std::endl; }
};

class Circle : public Shape {
public:
    void draw() { std::cout << "Circle" << std::endl; }
};

int main() {
    Circle c;
    Shape* s = &c;
    s->draw(); // Gọi hàm không ảo qua con trỏ lớp cơ sở
    return 0;
}""",
    "options": [
        "A. In ra: Circle (vì đối tượng thực tế là Circle)",
        "B. In ra: Shape (vì hàm không ảo sử dụng Liên kết tĩnh - Static Binding dựa trên kiểu của con trỏ Shape*)",
        "C. Lỗi biên dịch vì hàm draw bị trùng tên",
        "D. Lỗi runtime vi phạm con trỏ"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 45-48 giải thích rõ bản chất của Tính Đa Hình: Cùng một thông điệp nhưng các đối tượng phản ứng khác nhau.<br>"
                   "2. Khi một hàm thành viên KHÔNG có từ khóa <code>virtual</code>, trình biên dịch thực hiện <strong>Liên kết tĩnh (Early Binding / Static Binding)</strong> ngay tại thời điểm biên dịch.<br>"
                   "3. Trình biên dịch căn cứ vào kiểu của con trỏ lúc khai báo (ở đây <code>Shape* s</code> là con trỏ kiểu <code>Shape</code>) để chèn lệnh gọi trực tiếp tới địa chỉ của hàm <code>Shape::draw()</code>.<br>"
                   "4. Kết quả in ra: <code>Shape</code>. Tính đa hình KHÔNG hoạt động nếu thiếu từ khóa <code>virtual</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 45-48: Tính đa hình và liên kết động]</span>"
})

questions.append({
    "id": 40,
    "group_id": "q-group-7",
    "group_name": "Nhóm 7: Tính Đa Hình (Polymorphism) & Liên Kết Động VTable",
    "title": "Liên kết động (Late / Dynamic Binding) với từ khóa virtual",
    "code": """#include <iostream>

class Shape {
public:
    virtual void draw() { std::cout << "Shape" << std::endl; }
};

class Circle : public Shape {
public:
    void draw() override { std::cout << "Circle" << std::endl; }
};

int main() {
    Circle c;
    Shape* s = &c;
    s->draw(); // Gọi hàm ảo qua con trỏ lớp cơ sở
    return 0;
}""",
    "options": [
        "A. Shape",
        "B. Circle (Liên kết động tại runtime tìm đúng phiên bản của đối tượng thực sự)",
        "C. Lỗi biên dịch vì override không hợp lệ trong C++11",
        "D. Sập chương trình do lỗi bảng ảo"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi hàm được đánh dấu <code>virtual</code>, trình biên dịch chuyển cơ chế gọi hàm sang <strong>Liên kết động (Late Binding / Dynamic Binding)</strong>.<br>"
                   "2. Tại thời điểm chạy chương trình, CPU không nhảy trực tiếp tới một địa chỉ hàm cố định, mà nó thực hiện 3 bước:<br>"
                   "   - Đọc con trỏ bảng ảo <code>vptr</code> nằm trong đối tượng <code>c</code>.<br>"
                   "   - Tra cứu bảng ảo <code>VTable</code> tương ứng với lớp <code>Circle</code>.<br>"
                   "   - Lấy địa chỉ của hàm <code>Circle::draw()</code> và thực thi.<br>"
                   "3. Do đó in ra chính xác: <code>Circle</code>. Đây là hiện thân thuần khiết của Đa hình trong C++.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 45-48: Tính đa hình & Dynamic Binding]</span>"
})

questions.append({
    "id": 41,
    "group_id": "q-group-7",
    "group_name": "Nhóm 7: Tính Đa Hình (Polymorphism) & Liên Kết Động VTable",
    "title": "Chi phí bộ nhớ của Đa hình: Con trỏ bảng ảo vptr làm tăng kích thước đối tượng",
    "code": """#include <iostream>

class WithoutVirtual {
    int a;
    int b;
};

class WithVirtual {
    int a;
    int b;
    virtual void func() {}
};

int main() {
    std::cout << sizeof(WithoutVirtual) << " ";
    std::cout << sizeof(WithVirtual) << std::endl;
    return 0;
}""",
    "options": [
        "A. Trên hệ thống 64-bit in ra: 8 16 (thêm 8 byte cho con trỏ vptr)",
        "B. In ra: 8 8 (hàm virtual không tốn dung lượng bộ nhớ đối tượng)",
        "C. In ra: 8 12",
        "D. Lỗi biên dịch vì hàm virtual rỗng"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <code>WithoutVirtual</code> chỉ chứa 2 số nguyên <code>int a, b</code> -> <code>sizeof = 4 + 4 = 8</code> bytes.<br>"
                   "2. Khi một lớp có ít nhất một hàm <code>virtual</code>, trình biên dịch tự động chèn thêm một biến thành viên ẩn nằm ở đầu đối tượng: <strong>con trỏ bảng ảo (<code>vptr</code> - Virtual Pointer)</strong>.<br>"
                   "3. Trên hệ điều hành 64-bit, con trỏ có kích thước 8 bytes. Đối tượng gồm: <code>vptr</code> (8 byte) + <code>a</code> (4 byte) + <code>b</code> (4 byte) = 16 bytes.<br>"
                   "Đây là cái giá về bộ nhớ RAM (Zero-cost abstraction tradeoff) mà ta phải trả để có được tính năng Đa hình.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 45-48: Cơ chế Đa hình và liên kết động]</span>"
})

questions.append({
    "id": 42,
    "group_id": "q-group-7",
    "group_name": "Nhóm 7: Tính Đa Hình (Polymorphism) & Liên Kết Động VTable",
    "title": "Bẫy thiếu Virtual Destructor trong Lớp cơ sở (Resource Leak & UB)",
    "code": """#include <iostream>

class Base {
public:
    Base() { std::cout << "B+ "; }
    ~Base() { std::cout << "B- "; } // Bẫy: không có từ khóa virtual
};

class Derived : public Base {
    int* buffer;
public:
    Derived() {
        buffer = new int[100];
        std::cout << "D+ ";
    }
    ~Derived() {
        delete[] buffer;
        std::cout << "D- ";
    }
};

int main() {
    Base* ptr = new Derived();
    delete ptr; // Xóa đối tượng con qua con trỏ cha
    std::cout << std::endl;
    return 0;
}""",
    "options": [
        "A. B+ D+ D- B-",
        "B. B+ D+ B- (Destructor của Derived KHÔNG ĐƯỢC GỌI, gây rò rỉ bộ nhớ mảng buffer và Undefined Behavior)",
        "C. Lỗi biên dịch vì delete không nhận con trỏ Base*",
        "D. D+ B+ B- D-"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi giải phóng đối tượng qua con trỏ lớp cơ sở <code>delete ptr;</code>, nếu Destructor của <code>Base</code> không phải là <code>virtual</code>, trình biên dịch áp dụng liên kết tĩnh (Static Binding).<br>"
                   "2. CPU chỉ gọi duy nhất Destructor của lớp cơ sở <code>~Base()</code> (in <code>B-</code>), hoàn toàn bỏ qua Destructor của lớp dẫn xuất <code>~Derived()</code>.<br>"
                   "3. Hậu quả: Toàn bộ bộ nhớ heap <code>buffer</code> mà lớp con cấp phát bị rò rỉ vĩnh viễn (Memory Leak), và chuẩn C++ định nghĩa hành vi này là <strong>UNDEFINED BEHAVIOR</strong>.<br>"
                   "Quy tắc vàng của OOP C++: Bất kỳ lớp cơ sở nào có hàm ảo đều BẮT BUỘC PHẢI CÓ Virtual Destructor.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 25 & 45: Quản lý vòng đời và đa hình an toàn]</span>"
})

questions.append({
    "id": 43,
    "group_id": "q-group-7",
    "group_name": "Nhóm 7: Tính Đa Hình (Polymorphism) & Liên Kết Động VTable",
    "title": "Từ khóa C++11 'override' ngăn chặn lỗi chính tả chữ ký hàm ảo",
    "code": """#include <iostream>

class Base {
public:
    virtual void compute(int x) const {
        std::cout << "Base: " << x << std::endl;
    }
};

class Derived : public Base {
public:
    // Quên từ khóa const hoặc sai kiểu:
    void compute(int x) override { // Có từ khóa override
        std::cout << "Derived: " << x << std::endl;
    }
};""",
    "options": [
        "A. Mã biên dịch bình thường và ghi đè thành công",
        "B. Lỗi biên dịch: 'void Derived::compute(int)' marked 'override', but does not override any member function (do thiếu const nên chữ ký không khớp)",
        "C. Trình biên dịch tự động sửa chữ ký cho khớp với Base",
        "D. Chỉ sinh cảnh báo warning"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trước C++11, nếu lập trình viên viết sai dù chỉ một chữ ký nhỏ (như quên <code>const</code>, sai kiểu tham số), compiler sẽ âm thầm coi đó là một hàm mới độc lập chứ không ghi đè hàm ảo của cha. Lỗi này cực kỳ khó debug.<br>"
                   "2. C++11 bổ sung từ khóa ngữ cảnh <code>override</code>: Bắt buộc trình biên dịch phải đối chiếu nghiêm ngặt với lớp cha. Nếu không tìm thấy hàm ảo nào có chữ ký khớp 100%, compiler báo lỗi biên dịch ngay lập tức.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 45-48: Tính đa hình và ghi đè hàm]</span>"
})

questions.append({
    "id": 44,
    "group_id": "q-group-7",
    "group_name": "Nhóm 7: Tính Đa Hình (Polymorphism) & Liên Kết Động VTable",
    "title": "Từ khóa C++11 'final': Đóng băng kế thừa và cấm ghi đè phương thức",
    "code": """#include <iostream>

class SecureCore final {
    // Lớp bị khóa kế thừa
};

// class Exploit : public SecureCore {}; // Thử kế thừa

class BaseAction {
public:
    virtual void run() final {} // Cấm ghi đè ở lớp con
};

class SubAction : public BaseAction {
public:
    // void run() override {} // Thử ghi đè
};

int main() {
    std::cout << "Security enforced" << std::endl;
    return 0;
}""",
    "options": [
        "A. Cả hai dòng thử nghiệm nếu mở chú thích đều bị compiler chặn đứng và báo lỗi biên dịch do từ khóa final",
        "B. final chỉ áp dụng cho biến, không áp dụng cho lớp và phương thức",
        "C. Vẫn kế thừa được nếu dùng private inheritance",
        "D. Lỗi runtime tại thời điểm nạp lớp"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Từ khóa <code>final</code> trong C++11 có hai công dụng bảo mật kiến trúc mạnh mẽ:<br>"
                   "   - Đặt sau tên lớp (<code>class SecureCore final</code>): Cấm tuyệt đối bất kỳ lớp nào kế thừa từ nó (ngăn chặn rủi ro kế thừa bừa bãi).<br>"
                   "   - Đặt sau chữ ký hàm ảo (<code>virtual void run() final</code>): Khóa cứng phương thức này, cấm mọi lớp con phía sau ghi đè.<br>"
                   "2. Mọi vi phạm đều bị compiler phát hiện và từ chối sinh mã máy.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 40-48: Tính kế thừa và tính đa hình]</span>"
})

questions.append({
    "id": 45,
    "group_id": "q-group-7",
    "group_name": "Nhóm 7: Tính Đa Hình (Polymorphism) & Liên Kết Động VTable",
    "title": "Bẫy gọi hàm ảo bên trong Constructor (Virtual Call in Constructor Trap)",
    "code": """#include <iostream>

class Base {
public:
    Base() {
        show(); // Bẫy: gọi hàm ảo trong Constructor
    }
    virtual void show() {
        std::cout << "BaseShow ";
    }
};

class Derived : public Base {
public:
    Derived() {}
    void show() override {
        std::cout << "DerivedShow ";
    }
};

int main() {
    Derived d;
    std::cout << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: DerivedShow (vì đối tượng là Derived)",
        "B. In ra: BaseShow (trong constructor của Base, cơ chế đa hình bị vô hiệu hóa, vptr trỏ tới VTable của Base)",
        "C. Lỗi biên dịch vì cấm gọi hàm ảo trong constructor",
        "D. Chương trình crash do VTable chưa được nạp"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi tạo <code>Derived d;</code>, Constructor của <code>Base</code> được thực thi trước. Tại thời điểm này, phần của <code>Derived</code> thậm chí còn chưa được khởi tạo!<br>"
                   "2. Nếu cho phép gọi đa hình tới <code>Derived::show()</code>, phương thức đó có thể truy cập các biến thành viên của <code>Derived</code> vốn chưa được khởi tạo (chứa rác), dẫn đến sập chương trình.<br>"
                   "3. Do đó, chuẩn C++ quy định cơ chế bảo vệ: Trong suốt thời gian Constructor của <code>Base</code> đang chạy, con trỏ bảng ảo <code>vptr</code> được trỏ cố định vào <code>VTable của Base</code>. Lời gọi hàm ảo bị giáng cấp thành liên kết tĩnh tới <code>Base::show()</code> -> in ra <code>BaseShow</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 45-48: Đa hình và bản chất khởi tạo đối tượng]</span>"
})

questions.append({
    "id": 46,
    "group_id": "q-group-7",
    "group_name": "Nhóm 7: Tính Đa Hình (Polymorphism) & Liên Kết Động VTable",
    "title": "Lớp trừu tượng (Abstract Class) & Hàm thuần ảo (Pure Virtual Function)",
    "code": """#include <iostream>

class AbstractSensor {
public:
    virtual void readData() = 0; // Hàm thuần ảo
};

int main() {
    // AbstractSensor s; // Dòng 1
    AbstractSensor* ptr = nullptr; // Dòng 2
    std::cout << "Ptr OK" << std::endl;
    return 0;
}""",
    "options": [
        "A. Dòng 1 lỗi biên dịch vì không thể tạo thể hiện của lớp trừu tượng; Dòng 2 hợp lệ vì con trỏ tới lớp trừu tượng được phép tồn tại",
        "B. Cả Dòng 1 và Dòng 2 đều lỗi biên dịch",
        "C. Dòng 1 hợp lệ, Dòng 2 lỗi biên dịch",
        "D. Cú pháp = 0 chỉ có trong ngôn ngữ C"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Cú pháp <code>= 0</code> biến hàm thành hàm thuần ảo (Pure Virtual Function) và biến lớp chứa nó thành <strong>Lớp trừu tượng (Abstract Class)</strong>.<br>"
                   "2. Lớp trừu tượng đóng vai trò giao diện (Interface / Pure Contract). Compiler cấm tiệt việc khởi tạo đối tượng cụ thể <code>AbstractSensor s;</code> (Dòng 1 lỗi).<br>"
                   "3. Tuy nhiên, việc khai báo con trỏ (<code>AbstractSensor*</code>) hoặc tham chiếu (<code>AbstractSensor&</code>) là hoàn toàn hợp lệ và là nền tảng cốt lõi để triển khai đa hình runtime trong C++.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 45-48: Lớp trừu tượng và tính đa hình]</span>"
})

# =========================================================================
# NHÓM 8: KIẾN TRÚC & TỔNG HỢP 4 TRỤ CỘT (CÂU 47 - 50)
# =========================================================================

questions.append({
    "id": 47,
    "group_id": "q-group-8",
    "group_name": "Nhóm 8: Kiến Trúc & Tổng Hợp 4 Trụ Cột OOP",
    "title": "Lạm dụng hàm bạn (friend function) phá vỡ ranh giới Đóng gói",
    "code": """#include <iostream>

class BankDatabase {
private:
    double total_reserves = 1000000.0;
    friend void emergencyAudit(BankDatabase& db);
};

void emergencyAudit(BankDatabase& db) {
    db.total_reserves = 0; // Hàm tự do bên ngoài sửa trực tiếp private
    std::cout << "Audited" << std::endl;
}

int main() {
    BankDatabase db;
    emergencyAudit(db);
    return 0;
}""",
    "options": [
        "A. Hợp lệ in ra 'Audited'; từ khóa friend cho phép hàm bên ngoài xâm phạm trực tiếp private, nhưng lạm dụng friend sẽ làm suy yếu tính đóng gói",
        "B. Lỗi biên dịch vì friend chỉ được dùng giữa các class",
        "C. emergencyAudit chỉ có quyền đọc, không có quyền ghi",
        "D. Biến total_reserves tự động thành biến toàn cục"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Từ khóa <code>friend</code> là một lỗ mở chủ động trong cơ chế đóng gói: Lớp chủ động chỉ định một hàm hoặc lớp khác được quyền truy cập toàn bộ các thành viên <code>private</code> và <code>protected</code> của mình.<br>"
                   "2. Mặc dù hữu ích cho các hàm toán tử (như <code>operator<<</code>), nhưng lạm dụng <code>friend</code> tạo nên sự phụ thuộc chặt chẽ (tight coupling) và làm suy giảm khả năng kiểm soát toàn vẹn dữ liệu của đối tượng.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 36-39: Tính đóng gói và bảo vệ dữ liệu]</span>"
})

questions.append({
    "id": 48,
    "group_id": "q-group-8",
    "group_name": "Nhóm 8: Kiến Trúc & Tổng Hợp 4 Trụ Cột OOP",
    "title": "Nguyên lý thiết kế: Ưu tiên Bao hàm hơn Kế thừa (Composition over Inheritance)",
    "code": """#include <iostream>

class Logger {
public:
    void log(const char* msg) { std::cout << msg << std::endl; }
};

// Thiết kế Composition (Bao hàm):
class OrderProcessor {
    Logger logger; // HAS-A Logger
public:
    void process() {
        logger.log("Order processed successfully.");
    }
};

int main() {
    OrderProcessor op;
    op.process();
    return 0;
}""",
    "options": [
        "A. OrderProcessor nên kế thừa Logger (public Logger) để tái sử dụng mã tốt hơn",
        "B. Composition over Inheritance là nguyên lý chuẩn: Bao hàm giúp giảm sự gắn kết chặt (Loose Coupling), tránh làm phình to interface của lớp con",
        "C. Kế thừa luôn luôn tốt hơn bao hàm trong mọi trường hợp",
        "D. Composition làm chậm tốc độ thực thi gấp 10 lần"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Kế thừa (Inheritance) tạo ra sự gắn kết rất chặt (Tight Coupling / White-box reuse) và phơi bày toàn bộ phương thức của cha ra ngoài.<br>"
                   "2. Bao hàm (Composition / Black-box reuse) tuân thủ quan hệ HAS-A: <code>OrderProcessor</code> chỉ sử dụng hành vi của <code>Logger</code> thông qua giao diện rõ ràng, giấu kín bên trong thuộc tính riêng tư.<br>"
                   "3. Thiết kế này giúp dễ dàng thay đổi thành phần (thậm chí hoán đổi logger khác lúc runtime) mà không phá vỡ cây phân cấp lớp.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 15 & 40: Tái sử dụng mã nguồn và kế thừa]</span>"
})

questions.append({
    "id": 49,
    "group_id": "q-group-8",
    "group_name": "Nhóm 8: Kiến Trúc & Tổng Hợp 4 Trụ Cột OOP",
    "title": "Bẫy ném ngoại lệ trong Constructor: Destructor sẽ KHÔNG BAO GIỜ được gọi!",
    "code": """#include <iostream>
#include <stdexcept>

class MemoryTracker {
    int* ptr;
public:
    MemoryTracker() {
        ptr = new int[50];
        throw std::runtime_error("Constructor failed!");
    }
    ~MemoryTracker() {
        delete[] ptr;
        std::cout << "Cleaned up" << std::endl;
    }
};

int main() {
    try {
        MemoryTracker mt;
    } catch (const std::exception& e) {
        std::cout << e.what() << std::endl;
    }
    return 0;
}""",
    "options": [
        "A. Destructor ~MemoryTracker() được tự động gọi để giải phóng ptr",
        "B. In ra 'Constructor failed!'; Destructor KHÔNG ĐƯỢC GỌI vì đối tượng chưa hình thành hoàn chỉnh, dẫn đến rò rỉ vùng nhớ heap ptr",
        "C. Lỗi biên dịch vì cấm ném ngoại lệ trong constructor",
        "D. Hệ điều hành tự động thu hồi toàn bộ biến động"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, một đối tượng chỉ được coi là 'đã sinh ra' (fully constructed) khi Constructor của nó kết thúc thành công (chạm tới dấu ngoặc nhọn đóng).<br>"
                   "2. Nếu một ngoại lệ được ném ra từ giữa thân Constructor, runtime coi như đối tượng này chưa từng tồn tại, và <strong>DESTRUCTOR SẼ KHÔNG BAO GIỜ ĐƯỢC GỌI</strong>.<br>"
                   "3. Con trỏ thô <code>ptr</code> đã được cấp phát trước lệnh <code>throw</code> sẽ bị rò rỉ vĩnh viễn.<br>"
                   "Giải pháp C++11 chuẩn mực: Luôn dùng Smart Pointer (<code>std::unique_ptr</code>) theo chuẩn RAII để tự động giải phóng tài nguyên khi ngoại lệ xảy ra.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 25: Tự động khởi tạo và hủy dữ liệu trong OOP]</span>"
})

questions.append({
    "id": 50,
    "group_id": "q-group-8",
    "group_name": "Nhóm 8: Kiến Trúc & Tổng Hợp 4 Trụ Cột OOP",
    "title": "Toàn cảnh 4 Trụ Cột OOP: Mối quan hệ tương hỗ giải quyết bài toán phức tạp",
    "code": """#include <iostream>

// 1. Trừu tượng (Abstraction):
class Shape {
public:
    virtual double area() const = 0; // Pure Virtual
    virtual ~Shape() = default;
};

// 2. Kế thừa (Inheritance) & 3. Đóng gói (Encapsulation):
class Circle : public Shape {
private:
    double radius;
public:
    Circle(double r) : radius(r) {}
    // 4. Đa hình (Polymorphism):
    double area() const override { return 3.14159 * radius * radius; }
};

int main() {
    Shape* s = new Circle(2.0);
    std::cout << s->area() << std::endl;
    delete s;
    return 0;
}""",
    "options": [
        "A. Đoạn mã thể hiện hoàn hảo cả 4 trụ cột: Abstraction (lớp Shape thuần ảo), Encapsulation (radius private), Inheritance (Circle : Shape), Polymorphism (area override qua con trỏ Shape*)",
        "B. Đoạn mã thiếu tính Đóng gói",
        "C. Đoạn mã vi phạm tính Trừu tượng",
        "D. Lỗi biên dịch vì delete s không hợp lệ"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "Đoạn mã tổng hợp đầy đủ và chuẩn xác 4 trụ cột OOP được đúc kết từ slide trang 13-48:<br>"
                   "1. <strong>Tính Trừu Tượng (Abstraction):</strong> <code>Shape</code> phơi bày hợp đồng tính toán diện tích mà không quan tâm hình thù cụ thể.<br>"
                   "2. <strong>Tính Đóng Gói (Encapsulation):</strong> Biến <code>radius</code> được bảo vệ trong <code>private</code>, che giấu chi tiết lưu trữ.<br>"
                   "3. <strong>Tính Kế Thừa (Inheritance):</strong> <code>Circle</code> kế thừa <code>Shape</code>, tái sử dụng định nghĩa kiểu.<br>"
                   "4. <strong>Tính Đa Hình (Polymorphism):</strong> Thông qua con trỏ lớp cơ sở <code>Shape* s</code>, lời gọi <code>s->area()</code> kích hoạt liên kết động qua VTable tới đúng <code>Circle::area()</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP2-introduction_new.pdf - Trang 13-48: Tổng kết 4 trụ cột Lập trình Hướng Đối Tượng]</span>"
})

print(f"Loaded {len(questions)} questions for Chapter 2.")

# Serialize to JSON
quiz_data_json = json.dumps(questions, ensure_ascii=False, indent=2)

# Read generate_chapter2.py template
with open("c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/generate_chapter2.py", "r", encoding="utf-8") as f:
    gen_text = f.read()

template_part = gen_text.split('html_template = """')[1].split('const quizData = [\n"""')[0]

# Construct JS logic
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

with open("c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/OOP2-introduction_new.html", "w", encoding="utf-8") as f:
    f.write(full_html)

try:
    with open("c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/Bài tập/OOP2-introduction_new.html", "w", encoding="utf-8") as f:
        f.write(full_html)
except Exception:
    pass

print(f"Successfully generated Chapter 2 standalone HTML! Size: {len(full_html)} bytes.")

