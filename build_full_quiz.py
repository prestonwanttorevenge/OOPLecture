# -*- coding: utf-8 -*-
import json
import html

# We will define the 50 questions
questions = []

# =========================================================================
# NHÓM 1: TỪ KHÓA C++11, PHẠM VI BIẾN (SCOPE) & TOÁN TỬ :: (CÂU 1 - 5)
# =========================================================================

questions.append({
    "id": 1,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Từ khóa C++11, Phạm vi biến (Scope) & Toán tử ::",
    "title": "Bẫy Shadowing biến cục bộ nhiều cấp và toán tử phân giải phạm vi đơn nguyên ::",
    "code": """#include <iostream>
int x = 100;

int main() {
    int x = 50;
    {
        int x = 20;
        std::cout << x << " " << ::x << " ";
    }
    std::cout << x << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: 20 100 50",
        "B. In ra: 20 50 50",
        "C. In ra: 20 100 100",
        "D. Lỗi biên dịch vì khai báo trùng tên x trong cùng một hàm"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong khối lệnh lồng bên trong (inner block), biến <code>int x = 20</code> che khuất (shadowing) cả biến <code>x = 50</code> của <code>main</code> và biến toàn cục <code>x = 100</code>.<br>"
                   "2. Khi gọi <code>x</code> trần, trình biên dịch tra cứu bảng ký hiệu (Symbol Table) từ phạm vi hẹp nhất ra ngoài, nên tìm thấy <code>x = 20</code>.<br>"
                   "3. Toán tử phạm vi đơn nguyên <code>::x</code> (Unary Scope Resolution Operator) bắt buộc trình biên dịch bỏ qua mọi phạm vi cục bộ để truy cập trực tiếp vào Global Namespace, do đó in ra <code>100</code>.<br>"
                   "4. Ra khỏi inner block, <code>x = 20</code> bị hủy khỏi stack. Lệnh <code>std::cout << x</code> tiếp theo truy cập biến cục bộ của hàm <code>main</code> là <code>50</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 6-7: Biến cục bộ, toàn cục & Toán tử ::]</span>"
})

questions.append({
    "id": 2,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Từ khóa C++11, Phạm vi biến (Scope) & Toán tử ::",
    "title": "Phạm vi biến khai báo bên trong điều kiện của lệnh if (C++ Condition Scope)",
    "code": """#include <iostream>

int check() { return 5; }

int main() {
    if (int val = check()) {
        int val = 10; // Dòng A
        std::cout << val << " ";
    }
    std::cout << val << std::endl; // Dòng B
    return 0;
}""",
    "options": [
        "A. Chương trình in ra: 10 5",
        "B. Lỗi biên dịch tại Dòng A vì biến val đã được khai báo trong scope của if",
        "C. Lỗi biên dịch tại Dòng B vì biến val chỉ có phạm vi bên trong khối lệnh if",
        "D. Cả Dòng A và Dòng B đều gây lỗi biên dịch"
    ],
    "correct": 3,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Theo chuẩn C++ (và C++11), biến khai báo trong mệnh đề điều kiện của <code>if</code> (như <code>if (int val = check())</code>) có phạm vi bao trùm toàn bộ khối <code>then</code> và <code>else</code>.<br>"
                   "2. Tại Dòng A: Trong cùng khối lệnh trực tiếp của <code>if</code>, việc tái khai báo <code>int val = 10;</code> là vi phạm quy tắc định danh trùng lặp trong cùng một scope (redefinition of 'val'), gây lỗi biên dịch.<br>"
                   "3. Tại Dòng B: Biến <code>val</code> khai báo trong <code>if</code> có thời gian sống (lifetime) kết thúc ngay khi thoát khỏi cấu trúc <code>if</code>. Truy cập <code>val</code> ở Dòng B gây lỗi 'val was not declared in this scope'.<br>"
                   "Do đó cả hai dòng đều gây lỗi biên dịch.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 6: Vị trí khai báo & phạm vi hoạt động của biến]</span>"
})

questions.append({
    "id": 3,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Từ khóa C++11, Phạm vi biến (Scope) & Toán tử ::",
    "title": "Bẫy chú thích khối lồng nhau (Nested Multi-line Comments)",
    "code": """#include <iostream>

int main() {
    int a = 10;
    /*
        int b = 20;
        /* Chú thích bên trong */
        a = a + b;
    */
    std::cout << a << std::endl;
    return 0;
}""",
    "options": [
        "A. Chương trình in ra 10 bình thường",
        "B. Chương trình in ra 30",
        "C. Lỗi biên dịch vì C/C++ không hỗ trợ chú thích /* ... */ lồng nhau",
        "D. Chương trình gặp lỗi Undefined Behavior"
    ],
    "correct": 2,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Bộ phân tích từ vựng (Lexer) của trình biên dịch C/C++ xử lý khối chú thích <code>/*</code> theo nguyên tắc tham lam: nó sẽ tìm ký tự đóng <code>*/</code> ĐẦU TIÊN để kết thúc khối chú thích.<br>"
                   "2. Ký tự <code>*/</code> sau chữ 'Chú thích bên trong' đã đóng ngay khối chú thích mở đầu. Do đó đoạn code <code>a = a + b;</code> và ký tự thừa <code>*/</code> tiếp theo bị coi là mã C++ thông thường.<br>"
                   "3. Trình biên dịch báo lỗi cú pháp: biến <code>b</code> chưa được khai báo và ký tự <code>*/</code> đứng trơ trọi không có <code>/*</code> mở tương ứng.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 4: Chú thích trong C và C++]</span>"
})

questions.append({
    "id": 4,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Từ khóa C++11, Phạm vi biến (Scope) & Toán tử ::",
    "title": "Xung đột từ khóa C++ mới so với mã nguồn viết bằng ngôn ngữ C thuần",
    "code": """#include <iostream>

int main() {
    int class = 10;
    int new = 20;
    int template = 30;
    std::cout << class + new + template << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra 60 nếu biên dịch bằng g++",
        "B. Lỗi biên dịch vì class, new, template là các từ khóa dành riêng (reserved keywords) của C++",
        "C. Mã biên dịch được nếu dùng cờ -fpermissive",
        "D. Chương trình bị tràn số"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong ngôn ngữ C cũ, <code>class</code>, <code>new</code>, <code>template</code>, <code>friend</code>, <code>inline</code>, <code>operator</code>, <code>this</code> không phải là từ khóa, nên có thể dùng làm tên biến.<br>"
                   "2. Khi dịch bằng trình biên dịch C++, toàn bộ các từ này trở thành từ khóa cốt lõi (keywords) của ngôn ngữ theo bộ ngữ pháp chính thức.<br>"
                   "3. Slide nhấn mạnh: 'Các chương trình bằng C nào sử dụng các tên trùng với các từ khóa mới cần phải thay đổi trước khi chương trình được dịch lại bằng C++'.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 3: Từ khóa mới trong C++]</span>"
})

questions.append({
    "id": 5,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Từ khóa C++11, Phạm vi biến (Scope) & Toán tử ::",
    "title": "Khối lệnh ẩn danh (Anonymous Scope) và thứ tự hủy biến tự động trên Stack",
    "code": """#include <iostream>

struct Tracker {
    int id;
    Tracker(int i) : id(i) { std::cout << "+" << id; }
    ~Tracker() { std::cout << "-" << id; }
};

int main() {
    Tracker t1(1);
    {
        Tracker t2(2);
        Tracker t3(3);
    }
    std::cout << "M";
    return 0;
}""",
    "options": [
        "A. +1+2+3-3-2M-1",
        "B. +1+2+3-2-3M-1",
        "C. +1+2+3M-3-2-1",
        "D. +1+2+3-1-2-3M"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Các đối tượng có thời gian lưu trữ tự động (automatic storage duration) được cấp phát trên Stack theo cấu trúc LIFO (Last-In, First-Out).<br>"
                   "2. <code>t1(1)</code> được tạo trước -> in <code>+1</code>.<br>"
                   "3. Đi vào inner scope: <code>t2(2)</code> tạo in <code>+2</code>, <code>t3(3)</code> tạo in <code>+3</code>.<br>"
                   "4. Gặp dấu đóng ngoặc nhọn <code>}</code> của inner scope: các đối tượng bên trong scope bị hủy theo thứ tự ngược lại với thứ tự khởi tạo. Do đó <code>t3</code> bị hủy trước (in <code>-3</code>), rồi đến <code>t2</code> (in <code>-2</code>).<br>"
                   "5. Gặp lệnh <code>std::cout << \"M\";</code> -> in <code>M</code>.<br>"
                   "6. Hàm <code>main</code> kết thúc: <code>t1</code> bị hủy cuối cùng -> in <code>-1</code>. Chuỗi hoàn chỉnh: <code>+1+2+3-3-2M-1</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 5-6: Vùng bộ nhớ & phạm vi biến]</span>"
})

# =========================================================================
# NHÓM 2: HỆ THỐNG ÉP KIỂU (CASTING) & CONST_CAST (CÂU 6 - 10)
# =========================================================================

questions.append({
    "id": 6,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Hệ Thống Ép Kiểu & Bẫy const_cast",
    "title": "Bẫy thay đổi giá trị của biến thực sự là hằng số qua const_cast (Undefined Behavior)",
    "code": """#include <iostream>

int main() {
    const int val = 100;
    int* p = const_cast<int*>(&val);
    *p = 200;
    std::cout << val << " " << *p << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: 200 200",
        "B. In ra: 100 200",
        "C. Lỗi biên dịch tại dòng const_cast",
        "D. Lỗi thực thi hoặc hành vi không xác định (Undefined Behavior) theo chuẩn C++"
    ],
    "correct": 3,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <code>val</code> được định nghĩa ban đầu là hằng số <code>const int val = 100;</code>. Trình biên dịch có thể lưu <code>val</code> vào phân vùng bộ nhớ chỉ đọc (Read-Only Data Segment / RODATA) hoặc thực hiện gập hằng (Constant Folding) trực tiếp vào mã máy.<br>"
                   "2. <code>const_cast</code> cho phép tước bỏ thuộc tính <code>const</code> về mặt kiểu dữ liệu để vượt qua kiểm tra của trình biên dịch.<br>"
                   "3. Tuy nhiên, chuẩn C++11 (khoản §7.1.6.1) quy định rõ: Việc cố tình ghi đè (modify) một ô nhớ mà đối tượng ban đầu được khai báo là <code>const</code> là <strong>HÀNH VI KHÔNG XÁC ĐỊNH (Undefined Behavior)</strong>.<br>"
                   "4. Trên thực tế với g++, lệnh <code>std::cout << val</code> bị compiler thay thế trực tiếp hằng số 100 tại compile-time, trong khi <code>*p</code> đọc từ ô nhớ stack bị ghi đè, cho kết quả dị thường <code>100 200</code> hoặc gây lỗi đổ vỡ (Crash/Access Violation) nếu lưu trong RODATA.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 35: const_cast thay đổi tính hằng của biến]</span>"
})

questions.append({
    "id": 7,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Hệ Thống Ép Kiểu & Bẫy const_cast",
    "title": "Sự khác biệt bản chất giữa static_cast và reinterpret_cast trên con trỏ",
    "code": """#include <iostream>

int main() {
    int a = 65;
    // Dòng 1:
    char* p1 = reinterpret_cast<char*>(&a);
    // Dòng 2:
    char* p2 = static_cast<char*>(&a);

    std::cout << *p1 << std::endl;
    return 0;
}""",
    "options": [
        "A. Cả Dòng 1 và Dòng 2 đều hợp lệ và in ra 'A'",
        "B. Dòng 1 lỗi biên dịch, Dòng 2 hợp lệ",
        "C. Dòng 2 lỗi biên dịch: static_cast không cho phép ép kiểu giữa các con trỏ kiểu dữ liệu cơ bản không liên quan",
        "D. Cả hai dòng đều gây lỗi biên dịch"
    ],
    "correct": 2,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <code>static_cast</code> là toán tử ép kiểu có kiểm tra tính tương thích ngữ nghĩa tại thời điểm biên dịch. Nó chỉ cho phép chuyển đổi giữa các kiểu số, hoặc con trỏ giữa lớp cha và con, hoặc từ <code>void*</code> sang con trỏ kiểu cụ thể. Nó <strong>từ chối</strong> ép trực tiếp giữa <code>int*</code> và <code>char*</code> vì chúng là hai kiểu con trỏ không có quan hệ tương thích.<br>"
                   "2. <code>reinterpret_cast</code> thực hiện ánh xạ lại dạng nhị phân thuần túy (bitwise reinterpretation). Nó cho phép ép kiểu giữa mọi loại con trỏ bất chấp kiểu trỏ tới. Do đó Dòng 1 biên dịch được và trên máy Little-Endian, byte đầu tiên của số nguyên 65 chính là mã ASCII 65 ('A').<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 8 & 35: Phép chuyển kiểu mới trong C++]</span>"
})

questions.append({
    "id": 8,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Hệ Thống Ép Kiểu & Bẫy const_cast",
    "title": "Functional Cast vs C-style Cast và độ ưu tiên toán tử",
    "code": """#include <iostream>

int main() {
    double x = 3.7;
    double y = 2.4;
    int res1 = (int)x + y;
    int res2 = int(x + y);
    std::cout << res1 << " " << res2 << std::endl;
    return 0;
}""",
    "options": [
        "A. 5 6",
        "B. 6 6",
        "C. 5 5",
        "D. Lỗi biên dịch vì int(x + y) không phải cú pháp hợp lệ trong C++"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong biểu thức <code>(int)x + y</code>: Toán tử ép kiểu tiền tố <code>(int)</code> có độ ưu tiên cao hơn phép cộng <code>+</code>. Do đó <code>x</code> (3.7) bị ép kiểu thành <code>3</code> trước, sau đó <code>3 + 2.4 = 5.4</code>. Khi gán vào <code>int res1</code>, giá trị bị cắt phần thập phân thành <code>5</code>.<br>"
                   "2. Trong biểu thức <code>int(x + y)</code>: Đây là dạng Functional Cast đặc trưng của C++. Biểu thức trong ngoặc <code>x + y</code> được tính trước: <code>3.7 + 2.4 = 6.1</code>. Sau đó hàm ép kiểu <code>int(...)</code> chuyển 6.1 thành <code>6</code>. Khi gán vào <code>res2</code> nhận giá trị <code>6</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 8: Phép chuyển kiểu mới dạng hàm new_type(expression)]</span>"
})

questions.append({
    "id": 9,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Hệ Thống Ép Kiểu & Bẫy const_cast",
    "title": "const_cast trên biến thực tế không phải hằng (Valid Modification)",
    "code": """#include <iostream>

void modify(const int& r) {
    int& non_const_r = const_cast<int&>(r);
    non_const_r += 50;
}

int main() {
    int original = 25;
    modify(original);
    std::cout << original << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: 75",
        "B. In ra: 25",
        "C. Lỗi biên dịch tại hàm const_cast",
        "D. Gặp lỗi Undefined Behavior do vi phạm const"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Điểm mấu chốt: Biến gốc <code>original</code> được khai báo là biến bình thường (non-const), nằm trong vùng nhớ Stack có quyền đọc/ghi (read/write).<br>"
                   "2. Hàm <code>modify</code> nhận tham chiếu hằng <code>const int& r</code> để cam kết không sửa đổi qua interface.<br>"
                   "3. Khi dùng <code>const_cast<int&>(r)</code> để gỡ bỏ thuộc tính const, vì ô nhớ gốc thực chất là bộ nhớ ghi được, hành động này là <strong>HOÀN TOÀN HỢP LỆ VÀ ĐƯỢC CHUẨN C++ CHO PHÉP</strong> (Well-defined behavior).<br>"
                   "4. Biến <code>original</code> được cộng thêm 50, in ra giá trị 75.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 35: const_cast thêm hoặc loại bỏ const]</span>"
})

questions.append({
    "id": 10,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Hệ Thống Ép Kiểu & Bẫy const_cast",
    "title": "Bẫy thăng cấp số nguyên có dấu (Sign Extension Trap) khi ép kiểu",
    "code": """#include <iostream>

int main() {
    signed char c = -1;
    unsigned int u = (unsigned int)c;
    std::cout << (u > 1000 ? "LON" : "NHO") << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: NHO",
        "B. In ra: LON",
        "C. Lỗi biên dịch vì không thể ép kiểu signed char sang unsigned int",
        "D. Chương trình bị tràn bộ nhớ stack"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <code>signed char c = -1</code> có biểu diễn nhị phân bù 2 (8-bit) là <code>0xFF</code>.<br>"
                   "2. Khi ép kiểu sang kiểu có kích thước lớn hơn (<code>unsigned int</code> 32-bit), trước hết phép mở rộng có dấu (Sign Extension) diễn ra: bit dấu (bit 1) được điền vào toàn bộ các bit cao, tạo thành <code>0xFFFFFFFF</code>.<br>"
                   "3. Sau đó, <code>0xFFFFFFFF</code> được diễn giải theo kiểu không dấu là giá trị cực đại <code>UINT_MAX = 4,294,967,295</code>.<br>"
                   "4. Rõ ràng <code>4,294,967,295 > 1000</code> nên in ra 'LON'. Đây là lỗi logic kinh điển khi trộn lẫn signed và unsigned trong C/C++.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 8: Ép kiểu dữ liệu trong C/C++]</span>"
})

# =========================================================================
# NHÓM 3: HẰNG SỐ (CONST VS #DEFINE), LINKAGE & BẢNG KÝ HIỆU (CÂU 11 - 15)
# =========================================================================

questions.append({
    "id": 11,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Hằng Số (const vs #define), Linkage & Bảng Ký Hiệu",
    "title": "Bẫy thay thế chuỗi của Macro #define và thứ tự ưu tiên toán tử",
    "code": """#include <iostream>
#define SQUARE(x) x * x

int main() {
    int res = SQUARE(2 + 3);
    std::cout << res << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: 25",
        "B. In ra: 11",
        "C. In ra: 13",
        "D. Lỗi biên dịch vì tham số macro không có dấu ngoặc tròn"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Bộ tiền xử lý (Preprocessor) không hiểu cú pháp C++, nó chỉ thực hiện thay thế chuỗi thuần túy: <code>SQUARE(2 + 3)</code> được thế thành <code>2 + 3 * 2 + 3</code>.<br>"
                   "2. Phép nhân <code>*</code> có độ ưu tiên cao hơn phép cộng <code>+</code>. Biểu thức được tính toán: <code>2 + (3 * 2) + 3 = 2 + 6 + 3 = 11</code>.<br>"
                   "3. Để đúng toán học, macro phải viết là <code>#define SQUARE(x) ((x) * (x))</code>. Slide nhấn mạnh đây là lý do tại sao C++ khuyến nghị dùng <code>const</code> hoặc hàm <code>inline</code> thay vì <code>#define</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 9 & 27: Hằng số #define vs const & hàm inline]</span>"
})

questions.append({
    "id": 12,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Hằng Số (const vs #define), Linkage & Bảng Ký Hiệu",
    "title": "Bẫy hiệu ứng phụ (Side Effects) với toán tử tăng giảm trong Macro #define",
    "code": """#include <iostream>
#define MAX(a, b) ((a) > (b) ? (a) : (b))

int main() {
    int x = 5;
    int y = 3;
    int m = MAX(x++, y);
    std::cout << "m=" << m << " x=" << x << std::endl;
    return 0;
}""",
    "options": [
        "A. m=5 x=6",
        "B. m=6 x=7",
        "C. m=5 x=7",
        "D. m=6 x=6"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Biểu thức sau khi tiền xử lý thay thế: <code>((x++) > (y) ? (x++) : (y))</code>.<br>"
                   "2. Bước 1: Điều kiện <code>(x++) > y</code> được đánh giá. Giá trị cũ của <code>x</code> là 5, so sánh <code>5 > 3</code> là đúng. Sau đó hiệu ứng phụ tăng <code>x</code> lên 6.<br>"
                   "3. Bước 2: Do điều kiện đúng, nhánh <code>(x++)</code> được thực thi. Lệnh này lấy giá trị hiện tại của <code>x</code> là 6 gán cho <code>m</code> (vậy <code>m = 6</code>), rồi ngay sau đó tiếp tục tăng <code>x</code> lên 7!<br>"
                   "4. Kết quả: <code>m = 6</code> và <code>x = 7</code>. Toán tử <code>x++</code> bị chạy 2 lần ngoài ý muốn!<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 9: Khai báo hằng bằng #define]</span>"
})

questions.append({
    "id": 13,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Hằng Số (const vs #define), Linkage & Bảng Ký Hiệu",
    "title": "Bản chất Internal Linkage của const toàn cục trong C++ so với C",
    "code": """// File: test.cpp
#include <iostream>

const int GLOBAL_VAL = 42;

int main() {
    const int* p = &GLOBAL_VAL;
    std::cout << *p << std::endl;
    return 0;
}""",
    "options": [
        "A. Biến GLOBAL_VAL có External Linkage và có thể extern sang file khác mà không cần từ khóa extern",
        "B. Biến GLOBAL_VAL trong C++ mặc định có Internal Linkage (phạm vi chỉ trong Translation Unit hiện tại)",
        "C. Lỗi biên dịch vì không được phép lấy địa chỉ của hằng số toàn cục",
        "D. Trình biên dịch không cấp phát bộ nhớ cho GLOBAL_VAL trong mọi trường hợp"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong ngôn ngữ C, biến <code>const</code> toàn cục mặc định có External Linkage.<br>"
                   "2. Trong C++, biến <code>const</code> toàn cục mặc định có <strong>Internal Linkage</strong> (tương đương với việc có từ khóa <code>static</code> trong C). Điều này cho phép lập trình viên định nghĩa biến <code>const</code> trong header file mà không bị lỗi trùng ký hiệu (multiple definition error) khi include vào nhiều file .cpp.<br>"
                   "3. Muốn biến const trong C++ có external linkage, bắt buộc phải khai báo tường minh: <code>extern const int GLOBAL_VAL = 42;</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 9: Khai báo hằng bằng const]</span>"
})

questions.append({
    "id": 14,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Hằng Số (const vs #define), Linkage & Bảng Ký Hiệu",
    "title": "Bảo vệ hệ thống kiểu: Cấm gán con trỏ hằng cho con trỏ thông thường",
    "code": """#include <iostream>

int main() {
    const int num = 50;
    int* ptr = &num; // Dòng kiểm tra
    *ptr = 100;
    std::cout << num << std::endl;
    return 0;
}""",
    "options": [
        "A. Chương trình in ra: 100",
        "B. Lỗi biên dịch: invalid conversion from 'const int*' to 'int*'",
        "C. Cảnh báo biên dịch nhưng vẫn chạy ra 50",
        "D. Gây lỗi Segmentation Fault tại runtime"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <code>&num</code> có kiểu dữ liệu là <code>const int*</code> (con trỏ trỏ tới dữ liệu hằng chỉ đọc).<br>"
                   "2. Biến <code>ptr</code> có kiểu là <code>int*</code> (con trỏ trỏ tới dữ liệu cho phép ghi đè).<br>"
                   "3. Hệ thống kiểu của C++ thiết kế để bảo toàn tính an toàn bộ nhớ (Const-correctness). Nếu cho phép gán <code>int* ptr = &num</code>, trình biên dịch sẽ vô tình tạo ra một cửa sau (backdoor) để sửa đổi hằng số mà không hay biết.<br>"
                   "4. Do đó, trình biên dịch C++ bắt buộc phải phát sinh lỗi biên dịch ngay tại dòng này.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 31-32: Con trỏ hằng và gán con trỏ]</span>"
})

questions.append({
    "id": 15,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Hằng Số (const vs #define), Linkage & Bảng Ký Hiệu",
    "title": "Gập hằng số (Constant Folding) và hành vi khi lấy địa chỉ con trỏ",
    "code": """#include <iostream>

int main() {
    const int N = 10;
    int arr[N]; // Dòng 1
    const int* p = &N; // Dòng 2
    std::cout << sizeof(arr)/sizeof(arr[0]) << " " << *p << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: 10 10",
        "B. Dòng 1 lỗi biên dịch vì N không phải là literal",
        "C. Dòng 2 lỗi biên dịch vì hằng số không có địa chỉ",
        "D. Dòng 1 chỉ hợp lệ trong C99 VLA, không hợp lệ trong C++11"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, biến <code>const int N = 10;</code> khởi tạo với một hằng số được coi là một biểu thức hằng số tại thời điểm biên dịch (Compile-time constant expression / Constant folding). Vì thế, <code>arr[N]</code> hoàn toàn hợp lệ trong C++11 và kích thước mảng được ấn định là 10 ngay lúc biên dịch.<br>"
                   "2. Khi chương trình thực hiện lấy địa chỉ <code>&N</code> ở Dòng 2, trình biên dịch bắt buộc phải cấp phát một ô nhớ thật trên phân vùng Stack để chứa giá trị 10, phục vụ cho con trỏ <code>p</code> trỏ tới.<br>"
                   "3. Chương trình chạy hoàn hảo và in ra <code>10 10</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 9 & 36: Khai báo hằng và kích thước mảng]</span>"
})

# =========================================================================
# NHÓM 4: I/O STREAM & BỘ ĐỊNH DẠNG <IOMANIP> (CÂU 16 - 20)
# =========================================================================

questions.append({
    "id": 16,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Nhập Xuất Chuẩn I/O Stream & Bộ Định Dạng <iomanip>",
    "title": "Tính chất 'Sticky' của setprecision vs tính chất 'One-Shot' của setw",
    "code": """#include <iostream>
#include <iomanip>

int main() {
    std::cout << std::setw(6) << 12 << 34 << std::endl;
    std::cout << std::setprecision(3) << std::fixed << 5.6789 << " " << 1.2345 << std::endl;
    return 0;
}""",
    "options": [
        "A. Dòng 1 in ra 12 và 34 đều có độ rộng 6. Dòng 2 in 5.679 và 1.2345",
        "B. Dòng 1: '    1234'. Dòng 2: '5.679 1.235'",
        "C. Dòng 1: '12    34'. Dòng 2: '5.68 1.23'",
        "D. Lỗi biên dịch vì setw không áp dụng cho số nguyên"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <strong>Tính chất One-shot của <code class=\"inline-code\">setw(k)</code>:</strong> Slide trang 13 ghi rõ: 'Hàm này cần đặt trong toán tử xuất và nó CHỈ CÓ HIỆU LỰC CHO MỘT GIÁ TRỊ được in gần nhất. Các giá trị in ra tiếp theo sẽ có độ rộng tối thiểu mặc định là 0'. Do đó, số <code>12</code> chiếm 2 vị trí được đệm 4 khoảng trắng phía trước (tổng độ rộng 6: <code>'    12'</code>), còn số <code>34</code> in ngay sau không có đệm -> kết quả: <code>'    1234'</code>.<br>"
                   "2. <strong>Tính chất Sticky của <code class=\"inline-code\">setprecision</code> & <code class=\"inline-code\">fixed</code>:</strong> Định dạng này duy trì hiệu lực liên tục cho toàn bộ các toán tử xuất tiếp theo. Cả 5.6789 và 1.2345 đều được làm tròn tới 3 chữ số thập phân: <code>5.679</code> và <code>1.235</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 12-13: Định dạng xuất setw, setprecision, setiosflags]</span>"
})

questions.append({
    "id": 17,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Nhập Xuất Chuẩn I/O Stream & Bộ Định Dạng <iomanip>",
    "title": "Bẫy ký tự xuống dòng dư thừa trong bộ đệm khi trộn toán tử >> và getline",
    "code": """#include <iostream>
#include <string>
#include <sstream>

int main() {
    std::stringstream ss("42\\nLap Trinh C++");
    int age;
    std::string name;
    
    ss >> age;
    std::getline(ss, name);
    
    std::cout << "age=" << age << ", len=" << name.length() << std::endl;
    return 0;
}""",
    "options": [
        "A. age=42, len=13",
        "B. age=42, len=0",
        "C. age=42, len=12",
        "D. Lỗi runtime khi đọc getline"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Toán tử trích luồng <code>ss >> age</code> đọc chuỗi ký tự số <code>42</code> và dừng lại ngay trước ký tự xuống dòng <code>\\n</code>. Ký tự <code>\\n</code> vẫn còn nằm nguyên vẹn trong Stream Buffer.<br>"
                   "2. Lệnh <code>std::getline(ss, name)</code> bắt đầu đọc từ vị trí hiện tại của buffer cho đến khi gặp <code>\\n</code>. Nó lập tức gặp ngay ký tự <code>\\n</code> thừa đó, coi như đã đọc xong một dòng rỗng, và trích xuất chuỗi rỗng vào <code>name</code>!<br>"
                   "3. Do đó, <code>name.length()</code> bằng 0 (chuỗi rỗng), chuỗi 'Lap Trinh C++' vẫn chưa được đọc.<br>"
                   "Để khắc phục, cần dùng <code>cin.ignore()</code> để nuốt ký tự <code>\\n</code> trước khi gọi <code>getline</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 14: Nhập dữ liệu với cin & toán tử >>]</span>"
})

questions.append({
    "id": 18,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Nhập Xuất Chuẩn I/O Stream & Bộ Định Dạng <iomanip>",
    "title": "Bẫy thứ tự lượng giá biểu thức con trong chuỗi toán tử <<",
    "code": """#include <iostream>

int main() {
    int i = 1;
    // Xét biểu thức in có toán tử tăng:
    std::cout << i++ << " " << i++ << std::endl;
    return 0;
}""",
    "options": [
        "A. Chắc chắn luôn in ra: 1 2",
        "B. Chắc chắn luôn in ra: 2 1",
        "C. Trong C++11, thứ tự lượng giá các đối số toán tử là Unspecified/Undefined Behavior",
        "D. Lỗi biên dịch vì không được phép lặp lại toán tử ++ trong cùng một dòng cout"
    ],
    "correct": 2,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong chuẩn C++11 (trước chuẩn C++17), phép gọi <code>cout << i++ << ...</code> tương đương với các lời gọi hàm lồng nhau <code>operator<<(operator<<(cout, i++), ...)</code>.<br>"
                   "2. C++11 không quy định thứ tự lượng giá (Order of Evaluation) giữa các tham số hàm hoặc các biểu thức con giữa các Sequence Points. Trình biên dịch có quyền lượng giá <code>i++</code> bên phải trước hoặc bên trái trước tùy thuộc vào kiến trúc thanh ghi.<br>"
                   "3. Việc sửa đổi cùng một biến vô hướng nhiều lần mà không có sequence point dẫn tới <strong>Undefined Behavior</strong> (chỉ từ C++17 trở đi toán tử chèn luồng mới được chuẩn hóa lượng giá từ trái qua phải).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 11: Toán tử chèn luồng <<]</span>"
})

questions.append({
    "id": 19,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Nhập Xuất Chuẩn I/O Stream & Bộ Định Dạng <iomanip>",
    "title": "Trạng thái lỗi của luồng nhập (Stream Fail State) khi nhập sai kiểu dữ liệu",
    "code": """#include <iostream>
#include <sstream>

int main() {
    std::stringstream ss("ABC 123");
    int x = 99;
    int y = 88;
    
    ss >> x; // Nhập chuỗi "ABC" vào biến int
    ss >> y;
    
    std::cout << "x=" << x << " y=" << y << " fail=" << ss.fail() << std::endl;
    return 0;
}""",
    "options": [
        "A. x=0 y=123 fail=0",
        "B. x=0 y=88 fail=1 (trong C++11 x được gán 0 và luồng bật cờ failbit)",
        "C. Chương trình bị crash ngoại lệ std::invalid_argument",
        "D. x=99 y=123 fail=0"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi toán tử trích xuất <code>>></code> cố gắng phân tích cú pháp số nguyên từ chuỗi 'ABC', việc trích xuất thất bại.<br>"
                   "2. Trạng thái của stream bị chuyển sang <code>failbit</code> (<code>ss.fail() == true</code>). Theo chuẩn C++11, khi phép đọc số thất bại, giá trị của biến đích <code>x</code> được đặt thành 0.<br>"
                   "3. Khi một stream đã rơi vào trạng thái <code>fail</code>, mọi thao tác đọc tiếp theo (như <code>ss >> y</code>) sẽ <strong>LẬP TỨC BỊ BỎ QUA</strong> mà không làm thay đổi giá trị của <code>y</code>.<br>"
                   "4. Do đó <code>y</code> vẫn giữ nguyên giá trị khởi tạo ban đầu là <code>88</code>, và <code>ss.fail()</code> trả về 1.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 14: Nhập dữ liệu từ bàn phím bằng cin >>]</span>"
})

questions.append({
    "id": 20,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Nhập Xuất Chuẩn I/O Stream & Bộ Định Dạng <iomanip>",
    "title": "Sự khác biệt bản chất giữa '\\n' và std::endl trong I/O Performance",
    "code": """#include <iostream>

int main() {
    std::cout << "A\\n";
    std::cout << "B" << std::endl;
    return 0;
}""",
    "options": [
        "A. '\\n' và std::endl hoàn toàn giống nhau về mặt mã máy và chi phí thực thi",
        "B. std::endl vừa ghi ký tự xuống dòng '\\n' vừa gọi tường minh flush() để đẩy bộ đệm, gây suy giảm hiệu năng nếu dùng trong vòng lặp lớn",
        "C. '\\n' không thể dùng được với std::cout trong C++11",
        "D. std::endl tự động giải phóng bộ nhớ của đối tượng cout"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Lệnh <code>std::cout << '\\n'</code> chỉ đơn thuần đẩy 1 byte ký tự ASCII 10 (newline) vào buffer trong không gian người dùng (User-space Stream Buffer). Hệ điều hành chưa cần thực hiện System Call.<br>"
                   "2. <code>std::endl</code> được định nghĩa là một hàm manipulator: nó ghi <code>'\\n'</code> và ngay sau đó gọi <code>std::cout.flush()</code>. Lệnh flush ép buộc CPU thực hiện chuyển ngữ cảnh (context switch) gọi hàm hệ thống của OS (như <code>write()</code> trong POSIX) để xả đĩa hoặc terminal.<br>"
                   "3. Sử dụng <code>std::endl</code> trong các vòng lặp hàng triệu lần sẽ làm giảm tốc độ thực thi hàng chục lần so với <code>'\\n'</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 11: Sử dụng '\\n' hoặc endl để xuống dòng mới]</span>"
})

# =========================================================================
# NHÓM 5: BIẾN THAM CHIẾU (&), HẰNG THAM CHIẾU & TRẢ VỀ THAM CHIẾU (CÂU 21 - 27)
# =========================================================================

questions.append({
    "id": 21,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Biến Tham Chiếu (&), Hằng Tham Chiếu & Trả Về Tham Chiếu",
    "title": "Bẫy trả về tham chiếu đến biến cục bộ trên Stack (Dangling Reference Trap)",
    "code": """#include <iostream>

int& getLocal() {
    int temp = 50;
    return temp;
}

int main() {
    int& ref = getLocal();
    std::cout << ref << std::endl;
    return 0;
}""",
    "options": [
        "A. Luôn luôn in ra 50 an toàn",
        "B. Lỗi biên dịch: C++ cấm hàm trả về kiểu tham chiếu int&",
        "C. Hành vi không xác định (Undefined Behavior): biến temp bị hủy khi thoát hàm, ref trở thành tham chiếu rác (dangling reference)",
        "D. Giá trị của ref tự động chuyển thành biến toàn cục"
    ],
    "correct": 2,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Biến <code>temp</code> được cấp phát trên Stack Frame của hàm <code>getLocal()</code>.<br>"
                   "2. Khi gặp lệnh <code>return temp;</code>, hàm trả về địa chỉ của biến <code>temp</code> dưới dạng tham chiếu.<br>"
                   "3. Ngay khi hàm kết thúc, con trỏ Stack Pointer (ESP/RSP) được dọn dẹp, toàn bộ vùng nhớ của <code>temp</code> bị thu hồi (deallocated).<br>"
                   "4. Biến <code>ref</code> trong <code>main</code> bây giờ trỏ vào một vùng nhớ chết (Dangling Reference). Khi thực thi <code>cout << ref</code>, nếu bộ nhớ bị một hàm khác ghi đè, chương trình sẽ in số rác hoặc gây lỗi đổ vỡ (Crash/Segmentation Fault).<br>"
                   "Slide trang 24 nhấn mạnh rõ: 'Nếu trả về tham chiếu đến một biến cục bộ thì biến cục bộ này sẽ bị mất đi khi kết thúc hàm... nếu hàm trả về tham chiếu đến biến cục bộ thì biến cục bộ này NÊN khai báo static'.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 24-25: Hàm trả về là tham chiếu]</span>"
})

questions.append({
    "id": 22,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Biến Tham Chiếu (&), Hằng Tham Chiếu & Trả Về Tham Chiếu",
    "title": "Cơ chế kéo dài vòng đời đối tượng tạm thời qua Hằng Tham Chiếu (Lifetime Extension)",
    "code": """#include <iostream>

int compute() {
    return 10 + 20;
}

int main() {
    // Dòng 1:
    // int& r1 = compute(); 
    // Dòng 2:
    const int& r2 = compute();
    
    std::cout << r2 << std::endl;
    return 0;
}""",
    "options": [
        "A. Cả Dòng 1 và Dòng 2 đều hợp lệ",
        "B. Dòng 1 lỗi biên dịch (không thể bind lvalue ref vào rvalue), Dòng 2 hợp lệ và kéo dài vòng đời đối tượng tạm",
        "C. Dòng 2 cũng bị lỗi biên dịch vì compute() trả về giá trị tạm không có địa chỉ",
        "D. Chương trình crash tại Dòng 2"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Hàm <code>compute()</code> trả về một giá trị theo giá trị (by value), đây là một <strong>rvalue (giá trị tạm thời)</strong> không có định danh bộ nhớ bền vững.<br>"
                   "2. Dòng 1: Tham chiếu không hằng (<code class=\"inline-code\">int&</code>) chỉ được phép liên kết (bind) với một lvalue (biến có địa chỉ có thể gán). Cố tình bind vào rvalue gây lỗi biên dịch: 'cannot bind non-const lvalue reference of type int& to an rvalue of type int'.<br>"
                   "3. Dòng 2: Theo chuẩn C++ (và slide trang 16, 21), <strong>Hằng tham chiếu (<code class=\"inline-code\">const int&</code>)</strong> có một đặc quyền tối cao: Trình biên dịch sẽ tạo ra một đối tượng tạm thời ẩn danh trên stack để chứa giá trị 30, và <strong>KÉO DÀI VÒNG ĐỜI (Lifetime Extension)</strong> của đối tượng tạm thời này bằng đúng phạm vi của biến tham chiếu <code>r2</code>!<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 16 & 21: Hằng tham chiếu & Đối số hằng tham chiếu]</span>"
})

questions.append({
    "id": 23,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Biến Tham Chiếu (&), Hằng Tham Chiếu & Trả Về Tham Chiếu",
    "title": "Hàm trả về tham chiếu được sử dụng làm Vế Trái (Lvalue) của phép gán",
    "code": """#include <iostream>

int global_arr[3] = {10, 20, 30};

int& getElement(int index) {
    return global_arr[index];
}

int main() {
    getElement(1) = 99;
    std::cout << global_arr[0] << " " << global_arr[1] << " " << global_arr[2] << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: 10 20 30",
        "B. Lỗi biên dịch: không thể gán một giá trị cho một lời gọi hàm getElement(1)",
        "C. In ra: 10 99 30",
        "D. Lỗi runtime: vi phạm bảo vệ bộ nhớ mảng"
    ],
    "correct": 2,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C truyền thống, lời gọi hàm luôn là một rvalue, không bao giờ được đứng ở vế trái phép gán.<br>"
                   "2. Trong C++, khi một hàm có kiểu trả về là một tham chiếu lvalue (<code class=\"inline-code\">int&</code>), kết quả trả về của hàm chính là bản thân ô nhớ mà nó tham chiếu tới.<br>"
                   "3. Ở đây, <code>global_arr</code> là mảng toàn cục, vùng nhớ hoàn toàn tồn tại ổn định trong Data Segment suốt thời gian chạy chương trình.<br>"
                   "4. Lệnh <code>getElement(1) = 99;</code> tương đương trực tiếp với <code>global_arr[1] = 99;</code>. Mảng được sửa đổi và in ra: <code>10 99 30</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 24-25: Hàm trả về là tham chiếu]</span>"
})

questions.append({
    "id": 24,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Biến Tham Chiếu (&), Hằng Tham Chiếu & Trả Về Tham Chiếu",
    "title": "Bản chất không thể gán lại (Cannot Re-bind) của Biến Tham Chiếu",
    "code": """#include <iostream>

int main() {
    int a = 10;
    int b = 20;
    int& ref = a; // ref là bí danh của a
    
    ref = b; // Lệnh này làm gì?
    ref = 100;
    
    std::cout << a << " " << b << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: 10 100 (ref chuyển sang trỏ tới b)",
        "B. In ra: 100 20 (ref mãi mãi liên kết với a, phép gán gán giá trị của b vào a)",
        "C. In ra: 100 100",
        "D. Lỗi biên dịch vì không được phép gán một biến cho biến tham chiếu"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Biến tham chiếu trong C++ <strong>KHÔNG PHẢI LÀ CON TRỎ</strong>; nó là một bí danh vĩnh viễn gắn chặt với ô nhớ mà nó được khởi tạo.<br>"
                   "2. Khi thực hiện <code>ref = b;</code>, lập trình viên không làm cho <code>ref</code> trỏ tới biến <code>b</code>. Thay vào đó, nó copy giá trị của <code>b</code> (20) ghi đè vào biến mà <code>ref</code> đang đại diện (tức là biến <code>a</code>). Lúc này <code>a = 20</code>.<br>"
                   "3. Tiếp tục <code>ref = 100;</code> thì biến <code>a</code> nhận giá trị <code>100</code>.<br>"
                   "4. Biến <code>b</code> hoàn toàn không bị ảnh hưởng và giữ nguyên giá trị <code>20</code>. Kết quả in ra: <code>100 20</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 15: Biến tham chiếu dùng chung địa chỉ với biến được tham chiếu]</span>"
})

questions.append({
    "id": 25,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Biến Tham Chiếu (&), Hằng Tham Chiếu & Trả Về Tham Chiếu",
    "title": "Lý do chuẩn C++ cấm khai báo Mảng các biến tham chiếu",
    "code": """#include <iostream>

int main() {
    int x = 1, y = 2, z = 3;
    int& arr[3] = {x, y, z}; // Khai báo mảng tham chiếu
    std::cout << arr[0] << std::endl;
    return 0;
}""",
    "options": [
        "A. Hợp lệ và in ra: 1",
        "B. Lỗi biên dịch: declaration of 'arr' as array of references is not allowed",
        "C. Hợp lệ nếu thêm từ khóa const: const int& arr[3]",
        "D. Chỉ cảnh báo biên dịch và chạy bình thường"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, một mảng yêu cầu các phần tử phải là các đối tượng độc lập có kích thước xác định và có địa chỉ bộ nhớ liên tiếp nhau (contiguous memory). Phép toán chỉ số mảng dựa trên số học con trỏ: <code>arr + i * sizeof(T)</code>.<br>"
                   "2. Bản thân biến tham chiếu không phải là một đối tượng độc lập có địa chỉ riêng biệt (khi lấy <code>&ref</code> thì compiler trả về địa chỉ của biến gốc). Do đó không thể tồn tại con trỏ trỏ tới tham chiếu, và không thể xác định bước nhảy ô nhớ cho mảng tham chiếu.<br>"
                   "3. Chuẩn C++ (ISO/IEC 14882) và slide trang 15 khẳng định dứt khoát: 'Biến tham chiếu có thể tham chiếu đến một phần tử mảng, nhưng KHÔNG CHO PHÉP khai báo mảng các biến tham chiếu'.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 15: Quy tắc khai báo biến tham chiếu]</span>"
})

questions.append({
    "id": 26,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Biến Tham Chiếu (&), Hằng Tham Chiếu & Trả Về Tham Chiếu",
    "title": "Hàm trả về tham chiếu đến biến tĩnh (Static Local Reference) an toàn",
    "code": """#include <iostream>

int& counter() {
    static int count = 0;
    count++;
    return count;
}

int main() {
    counter();
    counter() = 10;
    std::cout << counter() << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: 1",
        "B. In ra: 11",
        "C. In ra: 10",
        "D. Lỗi biên dịch vì không thể gán giá trị cho hàm counter()"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Biến <code>static int count = 0</code> được cấp phát trong vùng nhớ Data/BSS Segment, có thời gian tồn tại vĩnh viễn suốt chu kỳ chạy của tiến trình (Program Lifetime), không bị hủy khi thoát hàm.<br>"
                   "2. Lần gọi 1: <code>counter();</code> -> <code>count</code> tăng từ 0 lên 1.<br>"
                   "3. Lần gọi 2: <code>counter() = 10;</code> -> hàm thực hiện <code>count++</code> (tăng từ 1 lên 2), sau đó trả về tham chiếu tới <code>count</code>. Phép gán <code>= 10</code> ghi đè giá trị 10 vào <code>count</code>.<br>"
                   "4. Lần gọi 3: <code>counter()</code> trong <code>cout</code> -> thực hiện <code>count++</code> (từ 10 tăng lên 11) và trả về tham chiếu giá trị <code>11</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 24: Tham chiếu đến biến static]</span>"
})

questions.append({
    "id": 27,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Biến Tham Chiếu (&), Hằng Tham Chiếu & Trả Về Tham Chiếu",
    "title": "Hàm trả về Hằng Tham Chiếu (Const Reference Return Value)",
    "code": """#include <iostream>

int global_val = 100;

const int& getVal() {
    return global_val;
}

int main() {
    getVal() = 200; // Dòng này có hợp lệ không?
    std::cout << global_val << std::endl;
    return 0;
}""",
    "options": [
        "A. Hợp lệ và in ra 200",
        "B. Lỗi biên dịch: assignment of read-only location",
        "C. Cảnh báo biên dịch và in ra 100",
        "D. Gây lỗi runtime Undefined Behavior"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Hàm <code>getVal()</code> trả về kiểu <code>const int&</code> (hằng tham chiếu).<br>"
                   "2. Về mặt ngữ nghĩa, từ khóa <code>const</code> ở kiểu trả về thông báo cho trình biên dịch rằng đối tượng được trả về chỉ có quyền đọc (Read-only), tuyệt đối không được phép làm vế trái (lvalue) của phép gán.<br>"
                   "3. Lệnh <code>getVal() = 200;</code> vi phạm quy tắc an toàn hằng số của C++, compiler báo lỗi ngay lập tức: <em>assignment of read-only location</em>.<br>"
                   "Đây là kỹ thuật đóng gói thường dùng trong C++ để trả về thuộc tính lớp với hiệu năng cao (tránh sao chép) nhưng vẫn ngăn không cho bên ngoài sửa đổi bừa bãi.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 26: Hàm trả về hằng tham chiếu]</span>"
})

# =========================================================================
# NHÓM 6: THAM SỐ MẶC ĐỊNH & HÀM NỘI TUYẾN (INLINE) (CÂU 28 - 32)
# =========================================================================

questions.append({
    "id": 28,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Tham Số Mặc Định & Hàm Nội Tuyến (Inline)",
    "title": "Quy tắc thứ tự khai báo tham số mặc định (Right-to-Left Rule)",
    "code": """#include <iostream>

// Khai báo hàm:
void display(int a = 10, int b, int c = 30) {
    std::cout << a + b + c << std::endl;
}

int main() {
    display(5, 5);
    return 0;
}""",
    "options": [
        "A. Chương trình in ra: 40",
        "B. Lỗi biên dịch: default argument missing for parameter 2 ('b')",
        "C. In ra: 45",
        "D. Hợp lệ nếu gọi display(5, 5, 5)"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi gọi một hàm, các đối số truyền vào luôn được ánh xạ từ trái sang phải cho các tham số hình thức tương ứng.<br>"
                   "2. Nếu cho phép tham số ở giữa không có giá trị mặc định trong khi tham số bên trái có mặc định, trình biên dịch sẽ không thể giải quyết được tính nhập nhằng khi người dùng truyền thiếu tham số (ví dụ: đối số thứ 2 truyền vào là của <code>a</code> hay của <code>b</code>?).<br>"
                   "3. Chuẩn C++ và slide trang 22 quy định bắt buộc: 'Các đối số mặc định CẦN LÀ CÁC ĐỐI SỐ CUỐI CÙNG tính từ trái qua phải'. Do <code>b</code> không có giá trị mặc định mà <code>c</code> lại có, compiler phát sinh lỗi ngay lập tức.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 22: Quy tắc đối số mặc định]</span>"
})

questions.append({
    "id": 29,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Tham Số Mặc Định & Hàm Nội Tuyến (Inline)",
    "title": "Bẫy lặp lại tham số mặc định giữa Nguyên mẫu (Prototype) và Định nghĩa (Definition)",
    "code": """#include <iostream>

// Nguyên mẫu hàm:
void printSum(int x, int y = 20);

// Định nghĩa hàm:
void printSum(int x, int y = 20) {
    std::cout << x + y << std::endl;
}

int main() {
    printSum(10);
    return 0;
}""",
    "options": [
        "A. In ra: 30 bình thường",
        "B. Lỗi biên dịch: redefinition of default argument for parameter 'y'",
        "C. Cảnh báo biên dịch nhưng vẫn chạy ra 30",
        "D. In ra: 10"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 22 nêu rõ ràng quy tắc vàng: 'Nếu chương trình sử dụng khai báo nguyên mẫu hàm thì các đối số mặc định cần được khởi gán trong nguyên mẫu hàm, KHÔNG ĐƯỢC KHỞI GÁN LẠI cho các đối số mặc định trong dòng đầu của định nghĩa hàm'.<br>"
                   "2. Trình biên dịch lưu trữ thông tin tham số mặc định trong bảng ký hiệu khi đọc prototype. Khi gặp lại định nghĩa hàm với tham số mặc định lặp lại, nó coi đây là hành vi tái định nghĩa tham số mặc định (redefinition of default argument) và báo lỗi biên dịch.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 22: Lưu ý về nguyên mẫu hàm và đối số mặc định]</span>"
})

questions.append({
    "id": 30,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Tham Số Mặc Định & Hàm Nội Tuyến (Inline)",
    "title": "Bẫy nhập nhằng (Ambiguity) giữa Đa năng hóa hàm và Tham số mặc định",
    "code": """#include <iostream>

void calc(int a) {
    std::cout << "One: " << a << std::endl;
}

void calc(int a, int b = 0) {
    std::cout << "Two: " << a + b << std::endl;
}

int main() {
    calc(10);
    return 0;
}""",
    "options": [
        "A. In ra: One: 10 (vì ưu tiên hàm khớp chính xác số tham số)",
        "B. In ra: Two: 10",
        "C. Lỗi biên dịch: call of overloaded 'calc(int)' is ambiguous",
        "D. Lỗi runtime tại thời điểm gọi hàm"
    ],
    "correct": 2,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong quá trình tìm kiếm hàm thích hợp (Overload Resolution), trình biên dịch lập danh sách các hàm ứng viên (Candidate functions) và hàm khả dĩ (Viable functions).<br>"
                   "2. Khi gọi <code>calc(10)</code>: Hàm 1 <code>calc(int)</code> hoàn toàn thỏa mãn vì nhận 1 đối số. Nhưng Hàm 2 <code>calc(int, int = 0)</code> cũng hoàn toàn thỏa mãn vì tham số thứ 2 đã có giá trị mặc định.<br>"
                   "3. Do cả hai phiên bản đều có mức độ chuyển đổi kiểu bằng nhau (Exact Match) và không có phiên bản nào chiếm ưu thế tuyệt đối theo quy tắc của chuẩn C++, trình biên dịch dừng lại và báo lỗi nhập nhằng (Ambiguity Error).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 22 & 60: Quá trình tìm kiếm hàm đa năng hóa]</span>"
})

questions.append({
    "id": 31,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Tham Số Mặc Định & Hàm Nội Tuyến (Inline)",
    "title": "Bản chất từ khóa inline: Quyền quyết định thực sự thuộc về Compiler Hint",
    "code": """#include <iostream>

inline int recursiveFactorial(int n) {
    if (n <= 1) return 1;
    return n * recursiveFactorial(n - 1);
}

int main() {
    std::cout << recursiveFactorial(5) << std::endl;
    return 0;
}""",
    "options": [
        "A. Lỗi biên dịch: C++ cấm dùng từ khóa inline cho các hàm đệ quy",
        "B. Trình biên dịch bắt buộc phải nội tuyến hóa toàn bộ các bước đệ quy tại vị trí gọi",
        "C. Từ khóa inline chỉ là một lời gợi ý (hint); trình biên dịch có toàn quyền từ chối inline và sinh mã như một hàm bình thường để tránh tràn stack/bloat",
        "D. Chương trình bị lặp vô tận tại compile-time"
    ],
    "correct": 2,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Từ khóa <code>inline</code> KHÔNG PHẢI là một mệnh lệnh bắt buộc đối với trình biên dịch; nó chỉ là một lời gợi ý tối ưu hóa (Compiler Hint / Request).<br>"
                   "2. Đối với các hàm có cấu trúc phức tạp như đệ quy không giới hạn, vòng lặp phức tạp, hoặc kích thước mã quá lớn, trình biên dịch sẽ từ chối mở rộng mã (inlining) và tự động phát sinh mã máy gọi hàm thông thường (dùng lệnh CALL / RET) để tránh hiện tượng phình to mã nguồn (Code Bloat).<br>"
                   "3. Chương trình vẫn biên dịch và chạy hoàn hảo, tính ra 120.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 27-28: Hàm nội tuyến inline]</span>"
})

questions.append({
    "id": 32,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Tham Số Mặc Định & Hàm Nội Tuyến (Inline)",
    "title": "Biến tĩnh cục bộ (Static Local) bên trong Hàm Inline tuân thủ One Definition Rule (ODR)",
    "code": """#include <iostream>

inline void tick() {
    static int count = 0;
    count++;
    std::cout << count << " ";
}

int main() {
    tick();
    tick();
    tick();
    std::cout << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: 1 1 1 (vì mỗi lần inline mã được nhân bản độc lập)",
        "B. In ra: 1 2 3 (biến static chỉ có duy nhất 1 bản sao trong toàn bộ chương trình theo luật ODR)",
        "C. Lỗi biên dịch: không được dùng biến static trong hàm inline",
        "D. In ra giá trị ngẫu nhiên do xung đột bộ nhớ"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Theo quy tắc định nghĩa duy nhất (One Definition Rule - ODR) của C++11, dù một hàm <code>inline</code> được sao chép mở rộng mã ở nhiều vị trí hoặc trên nhiều đơn vị dịch (Translation Units) khác nhau, thì mọi lời gọi hàm đó vẫn phải dùng chung <strong>DUY NHẤT MỘT THỂ HIỆN</strong> của biến cục bộ tĩnh <code>static int count</code>.<br>"
                   "2. Trình liên kết (Linker) chịu trách nhiệm hợp nhất các biểu tượng biến static này vào một địa chỉ duy nhất trong phân vùng dữ liệu tĩnh (BSS/Data Segment).<br>"
                   "3. Do đó mỗi lần <code>tick()</code> được gọi, biến tĩnh tăng tuần tự: 1, rồi 2, rồi 3.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 27-28: Cơ chế hàm inline]</span>"
})

# =========================================================================
# NHÓM 7: CON TRỎ CƠ BẢN, CON TRỎ HẰNG & HẰNG CON TRỎ (CÂU 33 - 36)
# =========================================================================

questions.append({
    "id": 33,
    "group_id": "q-group-7",
    "group_name": "Nhóm 7: Con Trỏ Cơ Bản, Con Trỏ Hằng & Hằng Con Trỏ",
    "title": "Phân biệt Con trỏ hằng (Pointer to Const) và Hằng con trỏ (Const Pointer)",
    "code": """#include <iostream>

int main() {
    int a = 10, b = 20;
    const int* p1 = &a; // Con trỏ hằng
    int* const p2 = &a; // Hằng con trỏ

    // Thử 4 thao tác:
    p1 = &b;   // Thao tác 1
    // *p1 = 30; // Thao tác 2
    *p2 = 40;  // Thao tác 3
    // p2 = &b;  // Thao tác 4

    std::cout << a << " " << *p1 << std::endl;
    return 0;
}""",
    "options": [
        "A. Cả Thao tác 1 và 3 đều hợp lệ; in ra: 40 20",
        "B. Thao tác 1 lỗi, Thao tác 3 hợp lệ",
        "C. Thao tác 1 hợp lệ, Thao tác 3 lỗi",
        "D. Cả hai thao tác đều gây lỗi biên dịch"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <code>const int* p1</code> (từ khóa <code>const</code> đứng trước <code>int</code>): <strong>Con trỏ tới hằng (Pointer to const)</strong>. Nó bảo vệ giá trị vùng nhớ không bị sửa thông qua <code>*p1</code>, nhưng bản thân địa chỉ của con trỏ <code>p1</code> là tự do thay đổi. Do đó <code>p1 = &b;</code> hoàn toàn hợp lệ! Khi đó <code>*p1</code> trỏ tới <code>b</code> (giá trị 20).<br>"
                   "2. <code>int* const p2</code> (từ khóa <code>const</code> đứng sau dấu <code>*</code>): <strong>Hằng con trỏ (Const pointer)</strong>. Bản thân con trỏ bị đóng băng địa chỉ (không thể trỏ sang biến khác như <code>p2 = &b</code>), nhưng vùng nhớ mà nó trỏ tới được phép chỉnh sửa tự do. Do đó <code>*p2 = 40;</code> sửa đổi biến <code>a</code> thành 40 hoàn toàn hợp lệ!<br>"
                   "3. Kết quả in ra: <code>40 20</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 31: Con trỏ hằng và hằng con trỏ]</span>"
})

questions.append({
    "id": 34,
    "group_id": "q-group-7",
    "group_name": "Nhóm 7: Con Trỏ Cơ Bản, Con Trỏ Hằng & Hằng Con Trỏ",
    "title": "Hằng con trỏ trỏ tới hằng (Const Pointer to Const)",
    "code": """#include <iostream>

int main() {
    int x = 100, y = 200;
    const int* const p = &x;

    // Dòng A:
    // *p = 150;
    // Dòng B:
    // p = &y;

    std::cout << *p << std::endl;
    return 0;
}""",
    "options": [
        "A. Dòng A hợp lệ, Dòng B lỗi biên dịch",
        "B. Dòng A lỗi biên dịch, Dòng B hợp lệ",
        "C. Cả Dòng A và Dòng B đều bị cấm và gây lỗi biên dịch nếu mở chú thích",
        "D. Cho phép sửa nếu ép kiểu tường minh qua static_cast"
    ],
    "correct": 2,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Cú pháp <code>const int* const p = &x;</code> có hai từ khóa <code>const</code>.<br>"
                   "2. Từ khóa <code>const</code> thứ nhất khóa giá trị ô nhớ: Cấm lệnh <code>*p = ...</code>.<br>"
                   "3. Từ khóa <code>const</code> thứ hai khóa bản thân biến con trỏ: Cấm lệnh thay đổi địa chỉ <code>p = &y</code>.<br>"
                   "4. Đây là mức độ bảo vệ nghiêm ngặt nhất (Read-only Pointer & Read-only Target). Mọi thao tác ghi đè đều bị trình biên dịch chặn lại ngay từ bước phân tích ngữ nghĩa.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 31: Khai báo con trỏ kết hợp const]</span>"
})

questions.append({
    "id": 35,
    "group_id": "q-group-7",
    "group_name": "Nhóm 7: Con Trỏ Cơ Bản, Con Trỏ Hằng & Hằng Con Trỏ",
    "title": "Bẫy con trỏ hoang (Wild Pointer) chưa được khởi tạo",
    "code": """#include <iostream>

int main() {
    int* ptr; // Con trỏ cục bộ chưa khởi tạo
    if (ptr != nullptr) { // Dòng kiểm tra
        *ptr = 10;
        std::cout << *ptr << std::endl;
    }
    return 0;
}""",
    "options": [
        "A. Chương trình luôn in ra 10 an toàn",
        "B. Khối if không bao giờ chạy vì con trỏ tự động bằng nullptr trong C++11",
        "C. Nguy hiểm cực độ: ptr chứa giá trị rác ngẫu nhiên trên stack, kiểm tra ptr != nullptr vẫn đúng nhưng ghi *ptr = 10 gây Crash hoặc ghi đè ô nhớ hệ thống",
        "D. Lỗi biên dịch vì biến ptr chưa được gán giá trị"
    ],
    "correct": 2,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, các biến cục bộ có thời gian lưu trữ tự động trên Stack <strong>KHÔNG ĐƯỢC TỰ ĐỘNG KHỞI TẠO VỀ 0</strong> (trừ khi có từ khóa <code>static</code> hoặc là biến toàn cục).<br>"
                   "2. Biến <code>ptr</code> chứa bất kỳ bit rác nào đang tồn tại sẵn tại vị trí stack đó. Do đó giá trị của <code>ptr</code> gần như chắc chắn khác <code>0</code> (khác <code>nullptr</code>).<br>"
                   "3. Điều kiện <code>if (ptr != nullptr)</code> bị đánh lừa là đúng. Khi CPU thực hiện lệnh ghi <code>*ptr = 10</code>, nó ghi vào một địa chỉ tùy ý trong không gian địa chỉ ảo, gây ra lỗi vi phạm quyền truy cập bộ nhớ (Access Violation / SIGSEGV) hoặc phá hủy dữ liệu của biến khác.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 29 & 56: Khái niệm con trỏ & con trỏ lạc]</span>"
})

questions.append({
    "id": 36,
    "group_id": "q-group-7",
    "group_name": "Nhóm 7: Con Trỏ Cơ Bản, Con Trỏ Hằng & Hằng Con Trỏ",
    "title": "Phép toán số học trừ hai con trỏ (Pointer Subtraction & ptrdiff_t)",
    "code": """#include <iostream>

int main() {
    int arr[5] = {10, 20, 30, 40, 50};
    int* p1 = &arr[1];
    int* p2 = &arr[4];
    
    std::cout << (p2 - p1) << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: 12 (vì khoảng cách là 3 số nguyên * 4 byte = 12 byte)",
        "B. In ra: 3 (số lượng phần tử kiểu int nằm giữa hai con trỏ)",
        "C. In ra địa chỉ hexa của ô nhớ",
        "D. Lỗi biên dịch vì C++ cấm trừ hai con trỏ cho nhau"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi thực hiện phép trừ giữa hai con trỏ cùng trỏ vào một mảng (<code>p2 - p1</code>), kết quả trả về không phải là độ chênh lệch số byte vật lý thô.<br>"
                   "2. Trình biên dịch tự động lấy khoảng cách byte thực tế chia cho kích thước của kiểu dữ liệu mà con trỏ trỏ tới: <code>(Byte_Address(p2) - Byte_Address(p1)) / sizeof(int)</code>.<br>"
                   "3. Khoảng cách giữa phần tử index 4 và index 1 là <code>4 - 1 = 3</code> phần tử. Kiểu trả về là số nguyên có dấu <code>ptrdiff_t</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 38: Phép toán trên con trỏ và mảng 1 chiều]</span>"
})

# =========================================================================
# NHÓM 8: CON TRỎ VÀ MẢNG (1D & 2D ARRAY DECAY & CON TRỎ MẢNG) (CÂU 37 - 41)
# =========================================================================

questions.append({
    "id": 37,
    "group_id": "q-group-8",
    "group_name": "Nhóm 8: Con Trỏ Và Mảng (1D, 2D Decay & Pointer Arithmetic)",
    "title": "Sự khác biệt bản chất giữa Tên Mảng (A), &A[0] và Địa Chỉ Toàn Mảng (&A)",
    "code": """#include <iostream>

int main() {
    int A[5] = {1, 2, 3, 4, 5};
    std::cout << sizeof(A) << " ";
    std::cout << sizeof(&A[0]) << " ";
    std::cout << sizeof(&A) << std::endl;
    return 0;
}""",
    "options": [
        "A. Trên hệ thống 64-bit in ra: 20 8 8",
        "B. Trên hệ thống 64-bit in ra: 20 20 20",
        "C. Trên hệ thống 64-bit in ra: 8 8 8",
        "D. Lỗi biên dịch vì &A là cú pháp không hợp lệ"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <code>sizeof(A)</code>: Khi đứng độc lập trong toán tử <code>sizeof</code>, <code>A</code> không bị phân rã (decay) thành con trỏ; nó đại diện cho toàn bộ đối tượng mảng 5 phần tử -> <code>5 * sizeof(int) = 20</code> bytes.<br>"
                   "2. <code>sizeof(&A[0])</code>: <code>&A[0]</code> là con trỏ trỏ tới phần tử đầu tiên, kiểu dữ liệu là <code>int*</code>. Trên hệ điều hành 64-bit, con trỏ có kích thước 8 bytes.<br>"
                   "3. <code>sizeof(&A)</code>: <code>&A</code> là con trỏ trỏ tới TOÀN BỘ MẢNG 5 phần tử, kiểu dữ liệu là <code>int(*)[5]</code>. Dù trỏ tới cả mảng nhưng bản chất nó vẫn là một con trỏ địa chỉ, do đó trên kiến trúc 64-bit kích thước của nó là 8 bytes.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 36-37: Con trỏ và mảng 1 chiều]</span>"
})

questions.append({
    "id": 38,
    "group_id": "q-group-8",
    "group_name": "Nhóm 8: Con Trỏ Và Mảng (1D, 2D Decay & Pointer Arithmetic)",
    "title": "Bẫy độ ưu tiên toán tử trong biểu thức *p++ so với (*p)++",
    "code": """#include <iostream>

int main() {
    int arr[] = {10, 20, 30};
    int* p = arr;

    int v1 = *p++;
    int v2 = (*p)++;

    std::cout << "v1=" << v1 << " v2=" << v2 << " arr[1]=" << arr[1] << std::endl;
    return 0;
}""",
    "options": [
        "A. v1=10 v2=20 arr[1]=21",
        "B. v1=11 v2=20 arr[1]=20",
        "C. v1=10 v2=21 arr[1]=21",
        "D. v1=20 v2=20 arr[1]=21"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Xét <code>*p++</code>: Toán tử hậu tố <code>++</code> có độ ưu tiên cao hơn toán tử giải tham chiếu <code>*</code>. Tuy nhiên vì là hậu tố, giá trị cũ của con trỏ <code>p</code> (địa chỉ <code>arr[0]</code>) được đưa vào toán tử <code>*</code>, lấy ra giá trị <code>10</code> gán cho <code>v1</code>. Sau đó con trỏ <code>p</code> mới dịch chuyển sang trỏ vào <code>arr[1]</code>.<br>"
                   "2. Xét <code>(*p)++</code>: Dấu ngoặc đơn ép buộc thực hiện <code>*p</code> trước (đang trỏ vào <code>arr[1]</code> có giá trị 20). Toán tử hậu tố <code>++</code> trả về giá trị cũ là 20 gán cho <code>v2</code>, sau đó giá trị trong ô nhớ <code>arr[1]</code> được tăng lên thành 21!<br>"
                   "3. Kết quả in ra: <code>v1=10 v2=20 arr[1]=21</code>.<br>"
                   "Slide trang 38 ghi chú đặc biệt: 'Nếu int* p = A thì p++ và *p++ là khác nhau: p++ thao tác trên con trỏ dịch đến phần tử tiếp theo, *p++ thao tác trên giá trị...'.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 38: Phép toán trên con trỏ và mảng]</span>"
})

questions.append({
    "id": 39,
    "group_id": "q-group-8",
    "group_name": "Nhóm 8: Con Trỏ Và Mảng (1D, 2D Decay & Pointer Arithmetic)",
    "title": "Công thức truy xuất con trỏ mảng 2 chiều *(*(A + i) + j)",
    "code": """#include <iostream>

int main() {
    int A[2][3] = {{1, 2, 3}, {4, 5, 6}};
    
    // Đọc giá trị phần tử A[1][2] qua con trỏ:
    int val = *(*(A + 1) + 2);
    
    std::cout << val << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: 6",
        "B. In ra: 5",
        "C. In ra: 4",
        "D. Lỗi biên dịch vì A là mảng 2 chiều không thể cộng số nguyên trực tiếp"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong mảng 2 chiều <code>A[2][3]</code>, <code>A</code> phân rã thành con trỏ trỏ tới hàng: <code>int (*)[3]</code>.<br>"
                   "2. <code>A + 1</code> dịch chuyển con trỏ đi 1 hàng (bước nhảy = <code>3 * sizeof(int) = 12</code> bytes), trỏ tới hàng thứ 1 <code>{4, 5, 6}</code>.<br>"
                   "3. <code>*(A + 1)</code> giải tham chiếu hàng, phân rã thành con trỏ trỏ tới phần tử đầu tiên của hàng 1 (kiểu <code>int*</code> trỏ tới số 4).<br>"
                   "4. <code>*(A + 1) + 2</code> dịch tiếp 2 phần tử kiểu int (bước nhảy = <code>2 * 4 = 8</code> bytes), trỏ tới số 6.<br>"
                   "5. Cuối cùng, <code>*(*(A + 1) + 2)</code> giải tham chiếu lấy giá trị tại ô nhớ, trả về chính xác <code>6</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 40: Địa chỉ và giá trị phần tử mảng 2 chiều]</span>"
})

questions.append({
    "id": 40,
    "group_id": "q-group-8",
    "group_name": "Nhóm 8: Con Trỏ Và Mảng (1D, 2D Decay & Pointer Arithmetic)",
    "title": "Bẫy truyền Mảng 2 chiều tĩnh vào hàm nhận con trỏ kép int**",
    "code": """#include <iostream>

void printMatrix(int** matrix, int rows, int cols) {
    std::cout << matrix[0][0] << std::endl;
}

int main() {
    int A[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    printMatrix(A, 3, 3); // Lời gọi hàm này có hợp lệ?
    return 0;
}""",
    "options": [
        "A. Hợp lệ và in ra 1",
        "B. Lỗi biên dịch: cannot convert 'int (*)[3]' to 'int**'",
        "C. Chạy được nhưng in ra giá trị rác",
        "D. Bị lỗi crash Segfault khi truy cập matrix[0][0]"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Một quan niệm sai lầm rất phổ biến là coi mảng 2 chiều tương đương với con trỏ kép <code>int**</code>.<br>"
                   "2. <code>int A[3][3]</code> là một khối 9 số nguyên liên tục trên Stack. Khi truyền vào hàm, nó phân rã thành con trỏ trỏ tới mảng 3 phần tử: <code>int (*)[3]</code>.<br>"
                   "3. Ngược lại, <code>int**</code> đòi hỏi một con trỏ trỏ tới một mảng các con trỏ (mỗi con trỏ mới lại trỏ tới một dòng rời rạc trên Heap). Hai kiểu dữ liệu này có bố cục bộ nhớ hoàn toàn khác nhau.<br>"
                   "4. Trình biên dịch C++ phát hiện sự không tương thích kiểu và chặn ngay lập tức tại compile-time.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 40-41: Con trỏ tới con trỏ và mảng 2 chiều]</span>"
})

questions.append({
    "id": 41,
    "group_id": "q-group-8",
    "group_name": "Nhóm 8: Con Trỏ Và Mảng (1D, 2D Decay & Pointer Arithmetic)",
    "title": "Bước nhảy con trỏ khi tăng (A + 1) so với (*A + 1) trong mảng 2 chiều",
    "code": """#include <iostream>

int main() {
    int A[3][4];
    uintptr_t addrA = (uintptr_t)A;
    uintptr_t stepRow = (uintptr_t)(A + 1) - addrA;
    uintptr_t stepElem = (uintptr_t)(*A + 1) - addrA;

    std::cout << stepRow << " " << stepElem << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: 16 4 (trên hệ thống sizeof(int) == 4)",
        "B. In ra: 4 4",
        "C. In ra: 12 4",
        "D. In ra: 48 4"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <code>A</code> có kiểu là <code>int (*)[4]</code> (con trỏ trỏ tới mảng 4 số nguyên). Khi tăng <code>A + 1</code>, con trỏ nhảy nguyên 1 hàng gồm 4 phần tử <code>int</code> -> độ lệch byte là <code>4 * sizeof(int) = 4 * 4 = 16</code> bytes.<br>"
                   "2. <code>*A</code> có kiểu là <code>int*</code> (con trỏ trỏ tới phần tử đơn lẻ đầu tiên của hàng 0). Khi tăng <code>*A + 1</code>, con trỏ chỉ nhảy 1 phần tử <code>int</code> -> độ lệch byte là <code>1 * sizeof(int) = 4</code> bytes.<br>"
                   "3. Kết quả in ra chính xác là <code>16 4</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 40: Địa chỉ con trỏ và mảng 2 chiều]</span>"
})

# =========================================================================
# NHÓM 9: CON TRỎ HÀM (FUNCTION POINTERS) (CÂU 42 - 45)
# =========================================================================

questions.append({
    "id": 42,
    "group_id": "q-group-9",
    "group_name": "Nhóm 9: Con Trỏ Hàm (Function Pointers)",
    "title": "Phân biệt cú pháp: Con trỏ hàm vs Hàm trả về con trỏ",
    "code": """#include <iostream>

int* func1(int a, int b);
int (*func2)(int a, int b);

int add(int a, int b) { return a + b; }

int main() {
    func2 = add;
    std::cout << func2(10, 20) << std::endl;
    return 0;
}""",
    "options": [
        "A. func1 là con trỏ hàm, func2 là hàm trả về con trỏ int*",
        "B. func1 là hàm trả về con trỏ int*, func2 là con trỏ hàm; chương trình in ra 30",
        "C. Cả hai khai báo đều là con trỏ hàm tương đương nhau",
        "D. Lỗi biên dịch vì không dùng toán tử & khi gán func2 = &add"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 43 lưu ý rất rõ: 'Dấu () bao bọc tên hàm để thông báo đó là con trỏ hàm; nếu không có dấu () thì trình biên dịch sẽ hiểu ta đang khai báo một hàm có giá trị trả về là một con trỏ'.<br>"
                   "2. Do đó <code>int* func1(...)</code> là nguyên mẫu hàm trả về con trỏ <code>int*</code>.<br>"
                   "3. Còn <code>int (*func2)(...)</code> có cặp ngoặc tròn kết hợp dấu sao <code>(*func2)</code> báo hiệu đây là một biến con trỏ chứa địa chỉ của một hàm.<br>"
                   "4. Trong C++, tên hàm <code>add</code> tự động phân rã thành địa chỉ của hàm đó, nên gán <code>func2 = add;</code> và gọi <code>func2(10, 20)</code> in ra 30 hoàn toàn chuẩn xác.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 43: Khai báo con trỏ hàm]</span>"
})

questions.append({
    "id": 43,
    "group_id": "q-group-9",
    "group_name": "Nhóm 9: Con Trỏ Hàm (Function Pointers)",
    "title": "Cơ chế Callback: Sử dụng con trỏ hàm làm đối số truyền cho thuật toán sắp xếp",
    "code": """#include <iostream>

bool ascending(int a, int b) { return a > b; }
bool descending(int a, int b) { return a < b; }

void customSort(int arr[], int n, bool (*cmp)(int, int)) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (cmp(arr[i], arr[j])) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

int main() {
    int a[] = {4, 1, 3};
    customSort(a, 3, descending);
    std::cout << a[0] << a[1] << a[2] << std::endl;
    return 0;
}""",
    "options": [
        "A. 134",
        "B. 431",
        "C. 314",
        "D. Lỗi biên dịch khi truyền tên hàm descending vào tham số con trỏ hàm"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Hàm <code>customSort</code> áp dụng mẫu thiết kế hàm gọi lại (Callback Pattern) thông qua con trỏ hàm <code>bool (*cmp)(int, int)</code>.<br>"
                   "2. Khi truyền hàm <code>descending</code> (so sánh <code>a < b</code>), mỗi khi phần tử đứng trước nhỏ hơn phần tử đứng sau (<code>arr[i] < arr[j]</code>), điều kiện đúng và hai phần tử tráo đổi vị trí.<br>"
                   "3. Thuật toán đưa các phần tử lớn nhất về phía đầu mảng, tức là sắp xếp giảm dần: <code>{4, 3, 1}</code>.<br>"
                   "Slide trang 48-49 lấy ví dụ kinh điển về việc dùng con trỏ hàm làm tiêu chí so sánh tăng dần/giảm dần.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 48-49: Sử dụng con trỏ hàm làm đối số]</span>"
})

questions.append({
    "id": 44,
    "group_id": "q-group-9",
    "group_name": "Nhóm 9: Con Trỏ Hàm (Function Pointers)",
    "title": "Con trỏ hàm làm tham số mặc định (Default Argument Function Pointer)",
    "code": """#include <iostream>

int opAdd(int a, int b) { return a + b; }
int opMul(int a, int b) { return a * b; }

// Hàm nhận con trỏ hàm làm tham số mặc định:
int execute(int x, int y, int (*op)(int, int) = opAdd) {
    return op(x, y);
}

int main() {
    std::cout << execute(3, 4) << " ";
    std::cout << execute(3, 4, opMul) << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: 7 12",
        "B. In ra: 12 12",
        "C. In ra: 7 7",
        "D. Lỗi biên dịch vì C++ không cho phép con trỏ hàm làm giá trị mặc định"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 50 nhấn mạnh điểm chú ý: 'Con trỏ hàm là đối số mặc định'. Trong C++, con trỏ hàm cũng là một biến con trỏ thông thường chứa địa chỉ mã lệnh của hàm, nên hoàn toàn có thể gán giá trị mặc định bằng địa chỉ của một hàm đã biết (như <code>opAdd</code>).<br>"
                   "2. Khi gọi <code>execute(3, 4)</code> thiếu đối số thứ ba, compiler tự động điền địa chỉ của hàm <code>opAdd</code>, trả về <code>3 + 4 = 7</code>.<br>"
                   "3. Khi gọi <code>execute(3, 4, opMul)</code>, con trỏ <code>op</code> nhận địa chỉ hàm <code>opMul</code>, trả về <code>3 * 4 = 12</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 50: Con trỏ hàm là đối số mặc định]</span>"
})

questions.append({
    "id": 45,
    "group_id": "q-group-9",
    "group_name": "Nhóm 9: Con Trỏ Hàm (Function Pointers)",
    "title": "Bảo vệ hệ thống kiểu đối với Con trỏ hàm (Type Safety Trap)",
    "code": """#include <iostream>

int compute(int a, int b) { return a + b; }
double computeDouble(double a, int b) { return a + b; }

int main() {
    int (*fp)(int, int) = compute; // Hợp lệ
    fp = computeDouble; // Dòng này có hợp lệ không?
    std::cout << fp(5, 5) << std::endl;
    return 0;
}""",
    "options": [
        "A. Hợp lệ vì trình biên dịch tự ép kiểu ngầm định tham số double thành int",
        "B. Lỗi biên dịch: không thể gán con trỏ hàm có kiểu chữ ký khác nhau",
        "C. Cảnh báo biên dịch và chạy bình thường",
        "D. Lỗi runtime tại thời điểm gọi fp(5, 5)"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Kiểu của con trỏ hàm trong C++ bao gồm toàn bộ chữ ký: Kiểu trả về và danh sách kiểu của toàn bộ các tham số.<br>"
                   "2. <code>fp</code> có kiểu chính xác là: <code>int (*)(int, int)</code>.<br>"
                   "3. Hàm <code>computeDouble</code> có kiểu: <code>double (*)(double, int)</code>.<br>"
                   "4. Slide trang 45 nêu rõ: Con trỏ hàm chỉ có thể trỏ tới các hàm có cùng kiểu tham số và kiểu trả về, KHÔNG ĐƯỢC trỏ tới các hàm khác kiểu tham số hoặc kiểu trả về. Compiler sẽ từ chối biên dịch ngay lập tức.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 45: Ví dụ về tính tương thích kiểu của con trỏ hàm]</span>"
})

# =========================================================================
# NHÓM 10: CẤP PHÁT ĐỘNG (NEW/DELETE, LEAKS & DANGLING) (CÂU 46 - 48)
# =========================================================================

questions.append({
    "id": 46,
    "group_id": "q-group-10",
    "group_name": "Nhóm 10: Cấp Phát Động (new/delete, Memory Leaks & Dangling)",
    "title": "Bẫy hủy mảng cấp phát động sai cách: new[] đi với delete thường thay vì delete[]",
    "code": """#include <iostream>

struct Sample {
    Sample() { std::cout << "C"; }
    ~Sample() { std::cout << "D"; }
};

int main() {
    Sample* p = new Sample[3];
    delete p; // Bẫy: dùng delete thay vì delete[]
    std::cout << "X";
    return 0;
}""",
    "options": [
        "A. In ra: CCCDDDX (hoạt động bình thường)",
        "B. In ra: CCCDX (chỉ phần tử đầu tiên được gọi Destructor, gây rò rỉ bộ nhớ hoặc Heap Corruption / UB)",
        "C. Lỗi biên dịch vì delete không nhận con trỏ mảng",
        "D. Chương trình tự động sửa thành delete[]"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi cấp phát mảng đối tượng <code>new Sample[3]</code>, trình biên dịch cấp phát một vùng nhớ heap kèm theo một ô nhớ phụ (Array Cookie) nằm ngay trước con trỏ trả về để lưu trữ số lượng phần tử (ở đây là 3), đồng thời gọi 3 lần Constructor (in <code>CCC</code>).<br>"
                   "2. Khi gọi toán tử <code>delete[] p</code>, runtime sẽ đọc cookie này để gọi đúng 3 lần Destructor và giải phóng toàn bộ khối heap.<br>"
                   "3. Nhưng nếu gọi <code>delete p</code> (không có ngoặc vuông), runtime coi <code>p</code> chỉ là một đối tượng đơn lẻ: nó chỉ gọi duy nhất 1 lần Destructor của phần tử đầu tiên (in <code>D</code>), bỏ qua Destructor của các phần tử còn lại, và truyền sai địa chỉ cho trình quản lý heap của OS.<br>"
                   "4. Hành vi này theo chuẩn C++11 là <strong>UNDEFINED BEHAVIOR</strong> (thường gây crash Heap Corruption). Slide trang 53 & 55 nhấn mạnh: bắt buộc phải dùng <code>delete [] biếncontrỏ</code> để hủy mảng động.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 53 & 55: Giải phóng bộ nhớ & Hủy mảng động bất hợp lệ]</span>"
})

questions.append({
    "id": 47,
    "group_id": "q-group-10",
    "group_name": "Nhóm 10: Cấp Phát Động (new/delete, Memory Leaks & Dangling)",
    "title": "Bẫy con trỏ lạc (Dangling Pointer) khi nhiều con trỏ cùng trỏ tới một vùng nhớ",
    "code": """#include <iostream>

int main() {
    int* P = new int(100);
    int* Q = P; // Q cùng trỏ vào ô nhớ của P
    
    delete P; // Giải phóng ô nhớ qua P
    P = nullptr;
    
    // Kiểm tra Q:
    if (Q != nullptr) {
        std::cout << *Q << std::endl; // Dòng nguy hiểm
    }
    return 0;
}""",
    "options": [
        "A. Luôn in ra 100 an toàn vì Q vẫn còn giữ giá trị",
        "B. Biến Q tự động được cập nhật thành nullptr khi P bị delete",
        "C. Lỗi biên dịch vì Q không thể đọc ô nhớ đã delete",
        "D. Nguy hiểm: Q trở thành con trỏ lạc (Dangling Pointer); đọc *Q dẫn đến đọc vùng nhớ rác hoặc Undefined Behavior"
    ],
    "correct": 3,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 56 giải thích trực quan: Khi thực hiện <code>delete P</code>, hệ điều hành thu hồi ô nhớ mà <code>P</code> trỏ tới để cấp phát cho việc khác.<br>"
                   "2. Việc gán <code>P = nullptr;</code> chỉ làm sạch giá trị của bản thân con trỏ <code>P</code>. Con trỏ <code>Q</code> vẫn lưu địa chỉ cũ của vùng nhớ đã bị giải phóng.<br>"
                   "3. Điều kiện <code>if (Q != nullptr)</code> vẫn thỏa mãn, nhưng việc truy cập <code>*Q</code> (Use-After-Free) là hành vi không xác định (Undefined Behavior), có thể in ra số rác hoặc gây đổ vỡ chương trình.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 56: Con trỏ lạc (Dangling pointer)]</span>"
})

questions.append({
    "id": 48,
    "group_id": "q-group-10",
    "group_name": "Nhóm 10: Cấp Phát Động (new/delete, Memory Leaks & Dangling)",
    "title": "Bẫy rò rỉ bộ nhớ (Memory Leak) khi hủy mảng 2 chiều cấp phát động",
    "code": """#include <iostream>

int main() {
    int rows = 3, cols = 4;
    // Cấp phát mảng 2 chiều:
    int** arr = new int*[rows];
    for (int i = 0; i < rows; i++) {
        arr[i] = new int[cols];
    }

    // Giải phóng bộ nhớ:
    delete[] arr; // Bẫy: chỉ giải phóng mảng con trỏ

    std::cout << "Done" << std::endl;
    return 0;
}""",
    "options": [
        "A. Hoàn toàn sạch bộ nhớ, không rò rỉ",
        "B. Rò rỉ bộ nhớ nghiêm trọng (Memory Leak): toàn bộ 3 mảng con arr[i] chứa các phần tử số nguyên bị mất dấu vĩnh viễn trên Heap",
        "C. Lỗi biên dịch vì arr là con trỏ kép không dùng được delete[]",
        "D. Lỗi runtime crash ngay tại dòng delete[] arr"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Cấp phát mảng 2 chiều động bằng con trỏ kép thực chất là cấp phát 1 mảng các con trỏ (kích thước <code>rows</code>), và mỗi con trỏ này lại trỏ tới 1 khối nhớ độc lập trên Heap (kích thước <code>cols</code>). Tổng cộng có <code>rows + 1</code> block nhớ độc lập được cấp phát.<br>"
                   "2. Nếu lập trình viên chỉ gọi <code>delete[] arr;</code>, runtime chỉ giải phóng mảng con trỏ chứa các địa chỉ. Toàn bộ <code>rows</code> khối nhớ dữ liệu thực tế vẫn nằm trên Heap nhưng đã mất hoàn toàn địa chỉ truy cập (con trỏ lưu địa chỉ bị xóa).<br>"
                   "3. Vùng nhớ này không bao giờ có thể thu hồi được cho đến khi tiến trình kết thúc (Rò rỉ bộ nhớ - Memory Leak).<br>"
                   "4. Quy tắc đúng: Phải duyệt vòng lặp giải phóng từng <code>delete[] arr[i];</code> trước, sau đó mới giải phóng <code>delete[] arr;</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 54 & 57: Cấp phát động mảng đa chiều & Rò rỉ bộ nhớ]</span>"
})

# =========================================================================
# NHÓM 11: ĐA NĂNG HÓA HÀM & ĐA NĂNG HÓA TOÁN TỬ CƠ BẢN (CÂU 49 - 50)
# =========================================================================

questions.append({
    "id": 49,
    "group_id": "q-group-11",
    "group_name": "Nhóm 11: Đa Năng Hóa Hàm & Đa Năng Hóa Toán Tử Cơ Bản",
    "title": "Bẫy chuyển đổi ngầm định gây Ambiguity trong Phân giải Đa năng hóa hàm (Overload Resolution)",
    "code": """#include <iostream>

void printVal(int a) {
    std::cout << "Int: " << a << std::endl;
}

void printVal(double a) {
    std::cout << "Double: " << a << std::endl;
}

int main() {
    float f = 3.14f;
    // printVal(f); // Dòng A
    printVal('A');  // Dòng B
    return 0;
}""",
    "options": [
        "A. Dòng B in ra: Int: 65 (do ký tự char được nguyên số hóa thăng cấp nguyên vẹn - Integral Promotion lên int)",
        "B. Cả hai dòng đều gây lỗi nhập nhằng (Ambiguity Error)",
        "C. Dòng B in ra: Double: 65",
        "D. Lỗi biên dịch vì không có hàm printVal(char)"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Phân giải nạp chồng hàm (Overload Resolution) trong C++11 tuân thủ thứ tự ưu tiên chặt chẽ:<br>"
                   "   - Ưu tiên 1: Khớp chính xác (Exact Match).<br>"
                   "   - Ưu tiên 2: Thăng cấp chuẩn (Promotion): ví dụ <code>char</code>, <code>short</code> thăng cấp lên <code>int</code>; <code>float</code> thăng cấp lên <code>double</code>.<br>"
                   "   - Ưu tiên 3: Chuyển đổi chuẩn (Standard Conversion): ví dụ <code>int</code> sang <code>double</code>, hoặc ngược lại.<br>"
                   "2. Tại Dòng B: Đối số truyền vào là <code>'A'</code> (kiểu <code>char</code>). Phép thăng cấp số nguyên (Integral Promotion) tự động biến <code>char</code> thành <code>int</code> với mã ASCII 65. Đây là mức Promotion (ưu tiên 2), hoàn toàn áp đảo việc chuyển đổi sang <code>double</code> (mức Conversion - ưu tiên 3). Do đó hàm <code>printVal(int)</code> được chọn dứt khoát -> in <code>Int: 65</code>.<br>"
                   "3. Lưu ý: Nếu mở Dòng A với <code>float f</code>, vì có <code>float</code> thăng cấp lên <code>double</code> nên hàm <code>printVal(double)</code> sẽ được chọn an toàn.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 59-60: Quá trình tìm hàm đa năng hóa]</span>"
})

questions.append({
    "id": 50,
    "group_id": "q-group-11",
    "group_name": "Nhóm 11: Đa Năng Hóa Hàm & Đa Năng Hóa Toán Tử Cơ Bản",
    "title": "Các giới hạn bất khả xâm phạm của Đa năng hóa toán tử trong C++",
    "code": """#include <iostream>

struct Vector2D {
    float x, y;
    
    // Thử định nghĩa các toán tử:
    // Toán tử 1:
    Vector2D operator+(const Vector2D& o) const { return {x + o.x, y + o.y}; }
    
    // Toán tử 2:
    // float operator::(int a);
    
    // Toán tử 3:
    // Vector2D operator**(int exp);
    
    // Toán tử 4:
    // int operatorsizeof();
};

int main() {
    Vector2D v1{1.0f, 2.0f}, v2{3.0f, 4.0f};
    Vector2D v3 = v1 + v2;
    std::cout << v3.x << " " << v3.y << std::endl;
    return 0;
}""",
    "options": [
        "A. Hợp lệ in ra 4.0 6.0; C++ cấm đa năng hóa ::, sizeof, và không cho phép tạo toán tử mới như **",
        "B. C++ cho phép định nghĩa mọi toán tử mới kể cả ** nếu viết hàm thành viên",
        "C. Toán tử + chỉ được phép overload dưới dạng hàm tự do bên ngoài struct",
        "D. Toán tử :: có thể đa năng hóa được trong chuẩn C++11"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "Slide trang 64 liệt kê chính xác các quy tắc thép của Operator Overloading trong C++:<br>"
                   "1. <strong>Không thể định nghĩa các toán tử mới:</strong> Ký hiệu <code>**</code> không tồn tại trong tập toán tử của C++, do đó không thể tự chế ra nó.<br>"
                   "2. <strong>Danh sách các toán tử CẤM ĐA NĂNG HÓA:</strong><br>"
                   "   - <code>::</code> : Toán tử định phạm vi (Scope Resolution).<br>"
                   "   - <code>.</code> : Truy cập trường struct / thành viên class trực tiếp.<br>"
                   "   - <code>.*</code> : Truy cập thành viên thông qua con trỏ thành viên.<br>"
                   "   - <code>?:</code> : Toán tử điều kiện ba ngôi.<br>"
                   "   - <code>sizeof</code> : Toán tử tính kích thước bộ nhớ.<br>"
                   "   - <code>typeid</code> : Toán tử xác định kiểu RTTI.<br>"
                   "3. Do đó chỉ có Toán tử 1 (<code>operator+</code>) là hợp lệ, in ra <code>4 6</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP1-C to C++-New.pdf - Trang 64: Các giới hạn của đa năng hóa toán tử]</span>"
})

print(f"Loaded {len(questions)} high-quality C++11 code trap questions.")

# Now let's serialize questions to JSON for embedding into JavaScript
quiz_data_json = json.dumps(questions, ensure_ascii=False, indent=2)

# Now read html_template and construct the full HTML file
with open("c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/generate_chapter1.py", "r", encoding="utf-8") as f:
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
                // If new group, render group header
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

                // Render Question Card
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
            if (userAnswers[qId] !== undefined) return; // already answered

            const q = quizData.find(item => item.id === qId);
            userAnswers[qId] = selectedIdx;

            const isCorrect = (selectedIdx === q.correct);
            if (isCorrect) {{
                score++;
            }}

            // Update score & count
            updateScoreDisplay();

            // Disable all buttons in this question
            q.options.forEach((_, idx) => {{
                const btn = document.getElementById(`btn-${{qId}}-${{idx}}`);
                btn.disabled = true;

                if (idx === q.correct) {{
                    btn.classList.add('show-correct');
                }}
            }});

            // Mark clicked button
            const clickedBtn = document.getElementById(`btn-${{qId}}-${{selectedIdx}}`);
            if (isCorrect) {{
                clickedBtn.classList.remove('show-correct');
                clickedBtn.classList.add('selected-correct');
            }} else {{
                clickedBtn.classList.add('selected-wrong');
            }}

            // Update status badge
            const statusBadge = document.getElementById(`badge-status-${{qId}}`);
            if (isCorrect) {{
                statusBadge.innerHTML = '<span class="text-emerald-700 font-bold"><i class="fa-solid fa-check"></i> Đúng</span>';
            }} else {{
                statusBadge.innerHTML = '<span class="text-rose-700 font-bold"><i class="fa-solid fa-xmark"></i> Sai</span>';
            }}

            // Show answer explanation block
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

        // Initialize on DOM Ready
        document.addEventListener('DOMContentLoaded', () => {{
            renderQuiz();
            updateScoreDisplay();
        }});
    </script>
</body>
</html>
"""

full_html = template_part + js_logic

with open("c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/OOP1-C_to_C++.html", "w", encoding="utf-8") as f:
    f.write(full_html)

# Also write to 'Bài tập' directory if desired
try:
    with open("c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/Bài tập/OOP1-C_to_C++.html", "w", encoding="utf-8") as f:
        f.write(full_html)
except Exception as e:
    pass

print(f"Successfully generated standalone HTML! Size: {len(full_html)} bytes.")

