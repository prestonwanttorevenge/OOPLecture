# -*- coding: utf-8 -*-
"""
Builder for Chapter 7: Khuôn Mẫu (Templates) - MOSTest5_2
Produces: OOP7-Template.html
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

questions = []

# =========================================================================
# NHÓM 1: BẢN CHẤT TEMPLATE & CƠ CHẾ INSTANTIATION (CÂU 1 - 8)
# =========================================================================

questions.append({
    "id": 1,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bản Chất Template & Cơ Chế Instantiation",
    "title": "Bản chất Instantiation và hiện tượng phình to mã máy (Code Bloat)",
    "code": """#include <iostream>

template <typename T>
void inspect(T val) {
    std::cout << sizeof(val) << " ";
}

int main() {
    inspect(10);       // int: 4 bytes
    inspect(3.14);     // double: 8 bytes
    inspect('A');      // char: 1 byte
    return 0;
}""",
    "options": [
        "A. 4 8 1 (Trình biên dịch sinh ra 3 phiên bản mã máy nhị phân độc lập của hàm inspect trong file .obj)",
        "B. 4 4 4",
        "C. Chỉ có 1 phiên bản hàm duy nhất dùng con trỏ void*",
        "D. Lỗi biên dịch vì inspect nhận nhiều kiểu khác nhau"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 12-15 nhấn mạnh: 'Thực chất, khi sử dụng template, ta đã định nghĩa một tập vô hạn các hàm... Cuối quy trình biên dịch, sẽ có các phiên bản độc lập được tạo tương ứng với từng kiểu dữ liệu'.<br>"
                   "2. Quá trình này gọi là <strong>Instantiation (Hiện thực hóa khuôn mẫu)</strong>. Trình biên dịch tạo ra 3 hàm cụ thể: <code>inspect<int></code>, <code>inspect<double></code>, <code>inspect<char></code> trong phân vùng mã lệnh (.text).<br>"
                   "3. Nếu lạm dụng quá nhiều kiểu, file thực thi sẽ phình to kích thước, hiện tượng này gọi là <strong>Template Code Bloat</strong>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 12-15: Hoạt động của trình biên dịch khi gặp template]</span>"
})

questions.append({
    "id": 2,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bản Chất Template & Cơ Chế Instantiation",
    "title": "Cơ chế phân giải hai pha (Two-Phase Name Lookup) trong Template C++",
    "code": """#include <iostream>

template <typename T>
void process(T val) {
    // Phase 1 kiểm tra cú pháp độc lập với T:
    // int x = ; // Dòng Cú Pháp Sai
    
    // Phase 2 kiểm tra ngữ nghĩa khi đã biết kiểu T cụ thể:
    val.unknownMethod(); // Dòng Phụ Thuộc T
}

int main() {
    std::cout << "NotInstantiated";
    return 0;
}""",
    "options": [
        "A. In ra NotInstantiated; Do process() chưa được gọi trong main, Dòng Phụ Thuộc T không bị biên dịch ở Phase 2, nhưng Dòng Cú Pháp Sai nếu mở ra sẽ bị bắt ngay ở Phase 1",
        "B. Chương trình luôn lỗi biên dịch tại unknownMethod() dù chưa gọi",
        "C. Cả hai lỗi đều chỉ bị phát hiện khi gọi hàm",
        "D. Không có lỗi nào xảy ra"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trình biên dịch C++ xử lý template qua <strong>Two-Phase Name Lookup</strong>:<br>"
                   "   - <strong>Phase 1 (Parse time):</strong> Kiểm tra cú pháp cơ bản và các tên không phụ thuộc (Non-dependent names). Nếu có lỗi cú pháp trắng trợn (như <code>int x = ;</code>), compiler báo lỗi ngay.<br>"
                   "   - <strong>Phase 2 (Instantiation time):</strong> Chỉ diễn ra khi template được gọi với một kiểu <code>T</code> cụ thể. Vì <code>process()</code> không bao giờ được gọi trong <code>main</code>, Phase 2 không chạy và lỗi <code>val.unknownMethod()</code> không bị kích hoạt!<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 13-14 & ISO C++ Two-Phase Lookup]</span>"
})

questions.append({
    "id": 3,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bản Chất Template & Cơ Chế Instantiation",
    "title": "Bẫy Tách File Header (.h) và Implementation (.cpp) trong Template",
    "code": """// File: MathUtil.h
template <typename T>
T add(T a, T b);

// File: MathUtil.cpp
template <typename T>
T add(T a, T b) { return a + b; }

// File: main.cpp
#include "MathUtil.h"
int main() {
    // int res = add(5, 10); // Lỗi gì sẽ xảy ra?
    return 0;
}""",
    "options": [
        "A. Lỗi Linker: 'undefined reference to add<int>(int, int)' vì compiler không thể instantiate template nếu không nhìn thấy thân hàm trong cùng translation unit",
        "B. Biên dịch và liên kết bình thường như hàm C++ thông thường",
        "C. Lỗi biên dịch cú pháp tại MathUtil.h",
        "D. Chương trình crash tại runtime"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Đây là lỗi phổ biến bậc nhất của người mới học C++ Template!<br>"
                   "2. Khi biên dịch <code>main.cpp</code>, compiler thấy khai báo <code>add<int></code> nhưng KHÔNG thấy định nghĩa thân hàm (vì nó nằm ở file .cpp riêng biệt), nên compiler để lại một tham chiếu chưa giải quyết (unresolved external symbol) cho Linker.<br>"
                   "3. Khi sang <code>MathUtil.cpp</code>, compiler không thấy ai gọi <code>add<int></code> nên nó KHÔNG SINH RA bất kỳ mã máy nào cho <code>add<int></code> cả!<br>"
                   "4. Kết quả: Linker không tìm thấy mã máy và báo lỗi. <em>Quy tắc vàng: Định nghĩa của Template BẮT BUỘC phải nằm trong file Header (.h / .hpp)!</em><br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 21 & Template Compilation Model]</span>"
})

questions.append({
    "id": 4,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bản Chất Template & Cơ Chế Instantiation",
    "title": "Biến thành viên tĩnh (Static Member Variables) trong Class Template",
    "code": """#include <iostream>

template <typename T>
struct Counter {
    static int count;
    Counter() { count++; }
};

template <typename T>
int Counter<T>::count = 0;

int main() {
    Counter<int> a;
    Counter<int> b;
    Counter<double> c;

    std::cout << Counter<int>::count << " " << Counter<double>::count;
    return 0;
}""",
    "options": [
        "A. 2 1 (Mỗi instantiation kiểu cụ thể sở hữu một biến static hoàn toàn độc lập trong RAM)",
        "B. 3 3 (Tất cả dùng chung một biến static)",
        "C. 0 0",
        "D. Lỗi biên dịch vì template không thể chứa biến static"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <code>Counter<int></code> và <code>Counter<double></code> là <strong>HAI LỚP HOÀN TOÀN TÁCH BIỆT</strong> trong hệ thống kiểu của C++.<br>"
                   "2. Do đó, <code>Counter<int>::count</code> và <code>Counter<double>::count</code> nằm tại 2 địa chỉ ô nhớ khác nhau trong phân vùng tĩnh (Data Segment <code>.bss</code>).<br>"
                   "3. Tạo 2 đối tượng <code>Counter<int></code> tăng biến count của int lên 2, còn 1 đối tượng <code>Counter<double></code> tăng biến count của double lên 1 -> in ra <code>2 1</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 19-20 & Static members in class templates]</span>"
})

questions.append({
    "id": 5,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bản Chất Template & Cơ Chế Instantiation",
    "title": "Sự tương đương tuyệt đối giữa từ khóa typename và class trong khai báo tham số",
    "code": """#include <iostream>

template <typename T>
void funcA(T val) { std::cout << "A "; }

template <class T>
void funcB(T val) { std::cout << "B "; }

int main() {
    funcA(1);
    funcB(2);
    return 0;
}""",
    "options": [
        "A. A B (Trong danh sách tham số template <typename T> và <class T> hoàn toàn đồng nghĩa và có ngữ nghĩa giống hệt nhau 100%)",
        "B. funcB chỉ chấp nhận kiểu là class/struct chứ không nhận kiểu int",
        "C. Lỗi biên dịch vì từ khóa class đã lỗi thời trong template",
        "D. funcA nhanh hơn funcB"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong khai báo tham số khuôn mẫu (Template Parameter List), chuẩn ISO C++ quy định <code>typename</code> và <code>class</code> có vai trò thay thế lẫn nhau hoàn hảo và không có bất kỳ sự khác biệt nào về mặt ngữ nghĩa hay sinh mã máy.<br>"
                   "2. Tuy nhiên, <code>typename</code> được ưa chuộng hơn trong C++ hiện đại vì nó tránh gây hiểu lầm rằng tham số bắt buộc phải là một kiểu người dùng tự định nghĩa (class).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 11 & C++ typename vs class keyword]</span>"
})

questions.append({
    "id": 6,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bản Chất Template & Cơ Chế Instantiation",
    "title": "Kỹ thuật Extern Template trong C++11 ngăn chặn trùng lặp Instantiation",
    "code": """#include <iostream>

template <typename T>
void heavyCompute(T val) {}

// C++11 Explicit Instantiation Declaration:
extern template void heavyCompute<int>(int);

int main() {
    heavyCompute(42);
    std::cout << "ExternSuccess";
    return 0;
}""",
    "options": [
        "A. In ra: ExternSuccess (Tính năng extern template trong C++11 thông báo cho compiler rằng bản instantiation này đã được tạo ở file khác, giúp giảm đáng kể thời gian build và dung lượng file obj)",
        "B. Lỗi biên dịch vì extern không áp dụng cho template",
        "C. Lỗi Linker do thiếu mã máy",
        "D. Chương trình crash tại runtime"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trước C++11, nếu 50 file .cpp cùng gọi <code>heavyCompute<int></code>, cả 50 file đều phải tự sinh mã máy cho hàm này, sau đó Linker phải mất công loại bỏ 49 bản sao trùng lặp.<br>"
                   "2. C++11 giới thiệu <code>extern template</code> (Explicit Instantiation Declaration): chỉ thị cho compiler bỏ qua việc sinh mã ở file hiện tại vì đã có một translation unit khác chịu trách nhiệm sinh mã, tăng tốc độ biên dịch rõ rệt.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 14-15 & C++11 extern template]</span>"
})

questions.append({
    "id": 7,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bản Chất Template & Cơ Chế Instantiation",
    "title": "Toán tử không hợp lệ trong Template chỉ gây lỗi khi kiểu tham số được truyền vào",
    "code": """#include <iostream>

struct NoPlus {
    int val;
};

template <typename T>
T addOne(T a) {
    return a + 1; // Sử dụng operator+
}

int main() {
    std::cout << addOne(5) << " "; // Hợp lệ với int
    // NoPlus np;
    // addOne(np); // Dòng Lỗi
    return 0;
}""",
    "options": [
        "A. In ra: 6; Dòng Lỗi nếu mở ra sẽ bị LỖI BIÊN DỊCH vì kiểu NoPlus không hỗ trợ operator+",
        "B. Bị lỗi biên dịch ngay từ đầu dù không gọi addOne(np)",
        "C. Tự động ép kiểu NoPlus về int",
        "D. In ra 6 1"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Lập trình template trong C++ áp dụng nguyên lý <strong>Duck Typing tại thời điểm biên dịch</strong>: <em>'Nếu nó đi như con vịt và kêu như con vịt, compiler coi nó là con vịt'</em>.<br>"
                   "2. Khi truyền <code>int</code>, biểu thức <code>a + 1</code> hoàn toàn hợp lệ -> sinh mã thành công.<br>"
                   "3. Nhưng khi truyền <code>NoPlus</code> (không có <code>operator+</code>), quá trình Instantiation thất bại và compiler ném lỗi: <em>no match for 'operator+' (operand types are 'NoPlus' and 'int')</em>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 13-15: Kiểm tra kiểu khi tạo thể hiện]</span>"
})

questions.append({
    "id": 8,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bản Chất Template & Cơ Chế Instantiation",
    "title": "Hàm bạn (Friend Function) bên trong Class Template",
    "code": """#include <iostream>

template <typename T>
class Box {
    T value;
public:
    Box(T v) : value(v) {}
    // Khai báo và định nghĩa friend function trực tiếp trong class template:
    friend void printVal(const Box<T>& b) {
        std::cout << b.value << " ";
    }
};

int main() {
    Box<int> b1(100);
    Box<double> b2(3.14);
    printVal(b1);
    printVal(b2);
    return 0;
}""",
    "options": [
        "A. 100 3.14 (Friend function được định nghĩa inline trong class template sẽ tự động được sinh ra như một non-template function cho từng instantiation nhờ ADL)",
        "B. Lỗi biên dịch vì friend function không được phép inline",
        "C. Lỗi Linker do trùng tên hàm printVal",
        "D. Chỉ in ra 100"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Kỹ thuật này gọi là <strong>Hidden Friends (Hàm bạn ẩn)</strong>.<br>"
                   "2. Khi <code>Box<int></code> được khởi tạo, compiler sinh ra một hàm tự do không phải template <code>void printVal(const Box<int>&)</code>.<br>"
                   "3. Hàm này chỉ có thể được tìm thấy thông qua cơ chế <strong>ADL (Argument-Dependent Lookup / Koenig Lookup)</strong> khi truyền đối số kiểu <code>Box<int></code> vào, đảm bảo tính đóng gói và an toàn tuyệt đối.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 21 & Hidden Friends Idiom]</span>"
})

print(f"Loaded {len(questions)} questions for Group 1.")
# =========================================================================
# NHÓM 2: FUNCTION TEMPLATES & SUY DIỄN KIỂU (DEDUCTION) (CÂU 9 - 16)
# =========================================================================

questions.append({
    "id": 9,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Function Templates & Suy Diễn Kiểu",
    "title": "Bẫy Xung Đột Suy Diễn Kiểu (Template Argument Deduction Conflict)",
    "code": """#include <iostream>

template <typename T>
T myMax(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    // std::cout << myMax(5, 3.14); // Lời gọi gây tranh cãi!
    std::cout << "DeductionFailed";
    return 0;
}""",
    "options": [
        "A. In ra: DeductionFailed; Nếu bỏ chú thích lời gọi, compiler sẽ BÁO LỖI BIÊN DỊCH vì T bị suy diễn xung đột (vừa là int từ đối số 1, vừa là double từ đối số 2)",
        "B. Tự động ép kiểu 5 thành 5.0 và in ra 5",
        "C. Tự động ép kiểu 3.14 thành 3 và in ra 5",
        "D. Chương trình crash tại runtime"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong quá trình suy diễn kiểu (Template Argument Deduction), <strong>trình biên dịch KHÔNG thực hiện ép kiểu ngầm định (Implicit Type Conversion)</strong> giữa các tham số cùng dùng chung tham số kiểu <code>T</code>.<br>"
                   "2. Khi gặp <code>myMax(5, 3.14)</code>: tham số thứ nhất đề xuất <code>T = int</code>, nhưng tham số thứ hai lại đề xuất <code>T = double</code>. Do có sự bất đồng và không có cơ sở ưu tiên, compiler lập tức tung lỗi: <em>no matching function for call to 'myMax(int, double)'</em>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 13-14: Khớp lời gọi hàm và template]</span>"
})

questions.append({
    "id": 10,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Function Templates & Suy Diễn Kiểu",
    "title": "Chỉ định kiểu tường minh (Explicit Template Argument) giải quyết xung đột",
    "code": """#include <iostream>

template <typename T>
T myMax(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    std::cout << myMax<double>(5, 3.14) << " ";
    std::cout << myMax<int>(5, 3.14);
    return 0;
}""",
    "options": [
        "A. 5 5 (Khi chỉ định tường minh <double> hoặc <int>, compiler bỏ qua bước suy diễn và thực hiện ép kiểu tham số thông thường)",
        "B. 5 3.14",
        "C. 3.14 5",
        "D. Lỗi biên dịch vì không được ép kiểu trong template"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi lập trình viên viết <code>myMax<double>(5, 3.14)</code>, trình biên dịch bỏ qua hoàn toàn cơ chế suy diễn (Deduction).<br>"
                   "2. Hàm được cố định là <code>double myMax(double, double)</code>. Lúc này, quy tắc chuyển đổi kiểu chuẩn (Standard Conversion) được áp dụng: số nguyên <code>5</code> được ép kiểu ngầm định thành <code>5.0</code> -> trả về <code>5.0</code>.<br>"
                   "3. Ngược lại với <code>myMax<int></code>, <code>3.14</code> bị ép thành <code>3</code> -> trả về <code>5</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 14: Chỉ định tham số khuôn mẫu tường minh]</span>"
})

questions.append({
    "id": 11,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Function Templates & Suy Diễn Kiểu",
    "title": "Thứ tự ưu tiên nạp chồng giữa Non-Template Function và Template Function",
    "code": """#include <iostream>

void print(int x) {
    std::cout << "NonTemplate:" << x << " ";
}

template <typename T>
void print(T x) {
    std::cout << "Template:" << x << " ";
}

int main() {
    print(10);       // Gọi với int
    print(3.14);     // Gọi với double
    print<>(20);     // Gọi với cú pháp <>
    return 0;
}""",
    "options": [
        "A. NonTemplate:10 Template:3.14 Template:20 (Hàm non-template luôn được ưu tiên nếu cùng mức độ khớp tham số; cú pháp <> buộc compiler chọn bản template)",
        "B. Template:10 Template:3.14 Template:20",
        "C. NonTemplate:10 NonTemplate:3 Template:20",
        "D. Lỗi biên dịch do mơ hồ giữa hai hàm"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <strong>Quy tắc Overload Resolution của C++:</strong> Nếu một hàm không phải template (Non-template function) và một hàm khuôn mẫu (Template function) đều khớp chính xác tham số truyền vào (Exact Match <code>int</code>), trình biên dịch <strong>LUÔN ƯU TIÊN</strong> hàm non-template!<br>"
                   "2. Với <code>print(3.14)</code>, kiểu <code>double</code> chỉ khớp với template -> gọi Template.<br>"
                   "3. Với <code>print<>(20)</code>, sự xuất hiện của cặp dấu <code><></code> thông báo rõ cho compiler chỉ được tìm kiếm trong tập hợp các hàm Template, bỏ qua hàm non-template -> gọi Template.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 12-14: Nạp chồng khuôn mẫu hàm]</span>"
})

questions.append({
    "id": 12,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Function Templates & Suy Diễn Kiểu",
    "title": "Bẫy suy diễn mảng: Thoái hóa con trỏ (Array Decay) vs Tham chiếu mảng bảo toàn kích thước",
    "code": """#include <iostream>

template <typename T>
void funcVal(T arr) {
    std::cout << sizeof(arr) << " "; // Bị decay thành con trỏ!
}

template <typename T, int N>
void funcRef(T (&arr)[N]) {
    std::cout << N << " "; // Giữ nguyên kích thước mảng!
}

int main() {
    int a[10];
    funcVal(a);
    funcRef(a);
    return 0;
}""",
    "options": [
        "A. 8 10 (funcVal truyền tham trị nên mảng bị suy thoái thành int* có kích thước 8 bytes trên 64-bit; funcRef nhận tham chiếu mảng nên suy diễn được chính xác N = 10)",
        "B. 40 10",
        "C. 40 40",
        "D. 10 10"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, khi truyền mảng theo giá trị vào template <code>funcVal(T arr)</code>, cơ chế <strong>Array-to-Pointer Decay</strong> xảy ra: <code>T</code> được suy diễn là con trỏ <code>int*</code>, và <code>sizeof(arr)</code> là kích thước con trỏ (8 bytes trên 64-bit).<br>"
                   "2. Nhưng với <code>funcRef(T (&arr)[N])</code>, tham số là tham chiếu tới mảng cố định kích thước, compiler suy diễn được <code>T = int</code> và <strong>Non-Type Template Parameter N = 10</strong>, bảo toàn trọn vẹn thông tin độ dài mảng!<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 11 & 28: Tham chiếu mảng trong template]</span>"
})

questions.append({
    "id": 13,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Function Templates & Suy Diễn Kiểu",
    "title": "Suy diễn kiểu khi kết hợp const và tham chiếu (const T&)",
    "code": """#include <iostream>

template <typename T>
void check(const T& ref) {
    std::cout << (sizeof(T) == sizeof(int)) << " ";
}

int main() {
    int x = 42;
    const int cx = 100;

    check(x);
    check(cx);
    return 0;
}""",
    "options": [
        "A. 1 1 (Cả hai trường hợp T đều được suy diễn là int, thuộc tính const được gắn ngoài bởi const T&)",
        "B. 1 0",
        "C. T của cx được suy ra là const int*",
        "D. Lỗi biên dịch"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi khuôn mẫu nhận <code>const T& ref</code>, thuộc tính <code>const</code> và tham chiếu <code>&</code> đã có sẵn trong chữ ký của hàm.<br>"
                   "2. Khi truyền <code>cx</code> (kiểu <code>const int</code>), phần <code>const</code> bị lột bỏ để suy diễn kiểu nền tảng <code>T</code>, do đó <code>T</code> được suy ra là <code>int</code>.<br>"
                   "3. Cả hai lời gọi đều instantiate cùng một hàm duy nhất <code>check<int>(const int&)</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 11-13 & Deduction with const references]</span>"
})

questions.append({
    "id": 14,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Function Templates & Suy Diễn Kiểu",
    "title": "Tham số khuôn mẫu mặc định (Default Template Arguments) cho hàm trong C++11",
    "code": """#include <iostream>

// C++11 cho phép default argument cho function template:
template <typename T = double>
T getValue() {
    return 3.14159;
}

int main() {
    auto v1 = getValue();      // Sử dụng kiểu mặc định double
    auto v2 = getValue<int>(); // Ghi đè kiểu int

    std::cout << v1 << " " << v2;
    return 0;
}""",
    "options": [
        "A. 3.14159 3 (C++11 cho phép gán kiểu mặc định T = double cho hàm mẫu khi không có tham số để suy diễn)",
        "B. Lỗi biên dịch vì function template không được phép có default template arguments",
        "C. 3.14159 3.14159",
        "D. 3 3"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trước C++11, tham số template mặc định chỉ được phép dùng cho Class Template, cấm dùng cho Function Template.<br>"
                   "2. Chuẩn C++11 đã bãi bỏ hạn chế này, cho phép lập trình viên viết <code>template <typename T = double> T getValue()</code>.<br>"
                   "3. Khi gọi <code>getValue()</code> không truyền đối số, compiler lấy kiểu mặc định <code>double</code>; khi chỉ định <code>getValue<int>()</code>, <code>T</code> được gán là <code>int</code> và cắt phần thập phân -> in ra <code>3.14159 3</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: C++11 Standard & OOP7-Template.pdf - Trang 11: Mở rộng khuôn mẫu hàm]</span>"
})

questions.append({
    "id": 15,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Function Templates & Suy Diễn Kiểu",
    "title": "Tham Chiếu Vạn Năng (Universal Reference) & Quy Tắc Gập Tham Chiếu (Reference Collapsing)",
    "code": """#include <iostream>

template <typename T>
void relay(T&& arg) { // arg là Forwarding / Universal Reference!
    std::cout << (std::is_lvalue_reference<T>::value ? "LRef " : "RRef ");
}

int main() {
    int a = 10;
    relay(a);  // Truyền lvalue
    relay(20); // Truyền rvalue
    return 0;
}""",
    "options": [
        "A. LRef RRef (Với lvalue a, T suy ra int& và gập tham chiếu thành int&; với rvalue 20, T suy ra int và tham số là int&&)",
        "B. RRef RRef (Cả hai đều là rvalue reference vì có ký hiệu &&)",
        "C. LRef LRef",
        "D. Lỗi biên dịch vì không thể truyền lvalue vào &&"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi <code>T&&</code> xuất hiện trên một tham số khuôn mẫu đang suy diễn, nó không phải là Rvalue Reference đơn thuần mà là <strong>Universal Reference (Forwarding Reference)</strong>.<br>"
                   "2. <strong>Quy tắc Reference Collapsing trong C++11:</strong><br>"
                   "   - <code>& + & -> &</code><br>"
                   "   - <code>& + && -> &</code><br>"
                   "   - <code>&& + & -> &</code><br>"
                   "   - <code>&& + && -> &&</code><br>"
                   "3. Khi truyền <code>a</code> (lvalue), <code>T</code> suy ra <code>int&</code>, gập <code>int& + && -> int&</code> -> in ra <code>LRef</code>. Khi truyền <code>20</code> (rvalue), <code>T</code> suy ra <code>int</code> -> in ra <code>RRef</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 11 & C++11 Reference Collapsing Rules]</span>"
})

questions.append({
    "id": 16,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Function Templates & Suy Diễn Kiểu",
    "title": "Kỹ thuật Chuyển Tiếp Hoàn Hảo (Perfect Forwarding) với std::forward trong C++11",
    "code": """#include <iostream>
#include <utility>

void target(int& x) { std::cout << "TargetLvalue "; }
void target(int&& x) { std::cout << "TargetRvalue "; }

template <typename T>
void forwarder(T&& arg) {
    target(std::forward<T>(arg)); // Chuyển tiếp bảo toàn nguyên vẹn giá trị gốc
}

int main() {
    int val = 5;
    forwarder(val);
    forwarder(10);
    return 0;
}""",
    "options": [
        "A. TargetLvalue TargetRvalue (std::forward bảo toàn hoàn hảo bản chất lvalue/rvalue của đối số ban đầu)",
        "B. TargetLvalue TargetLvalue (Vì arg có tên nên arg luôn là lvalue)",
        "C. TargetRvalue TargetRvalue",
        "D. Lỗi biên dịch do thiếu thư viện"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Bên trong <code>forwarder</code>, tham số <code>arg</code> dù có kiểu gì thì bản thân nó là một biểu thức có tên (lvalue). Nếu gọi trần trụi <code>target(arg)</code>, nó luôn luôn gọi bản <code>target(int&)</code>!<br>"
                   "2. Hàm mẫu <code>std::forward<T>(arg)</code> trong C++11 thực hiện ép kiểu có điều kiện: nếu <code>T</code> được suy ra từ một rvalue, nó sẽ ép <code>arg</code> về lại rvalue (xvalue). Nếu <code>T</code> là lvalue reference, nó giữ nguyên là lvalue.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 11 & C++11 Perfect Forwarding & std::forward]</span>"
})

print(f"Loaded {len(questions)} questions for Groups 1-2.")
# =========================================================================
# NHÓM 3: CLASS TEMPLATES & CẤU TRÚC DỮ LIỆU TỔNG QUÁT (CÂU 17 - 24)
# =========================================================================

questions.append({
    "id": 17,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Class Templates & Cấu Trúc Dữ Liệu Tổng Quát",
    "title": "Ký hiệu cặp dấu ngoặc nhọn <> bắt buộc khi khai báo đối tượng Class Template",
    "code": """#include <iostream>

template <typename T>
class Container {
    T data;
public:
    Container(T d) : data(d) {}
    void print() { std::cout << data; }
};

int main() {
    Container<int> c(10); // Trong C++11
    c.print();
    // Container c2(20); // Dòng C++17
    return 0;
}""",
    "options": [
        "A. In ra 10; Trong chuẩn C++11, Class Template BẮT BUỘC phải có cặp dấu <> chỉ định kiểu tường minh, việc tự động suy diễn kiểu constructor (CTAD) chỉ xuất hiện từ C++17",
        "B. Cả hai cách khai báo đều hợp lệ trong C++11",
        "C. Dòng c2 tự động suy ra kiểu int trong C++11",
        "D. Lỗi biên dịch tại Container<int> c(10)"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 18-19 ghi rõ: <em>'Để tạo các thể hiện của template, ta phải dùng ký hiệu cặp dấu < >... Không có struct Pair mà chỉ có các struct có tên Pair<int, int>...'</em>.<br>"
                   "2. Trong C++11, trình biên dịch không tự động suy diễn tham số cho Class Template từ Constructor (tính năng Class Template Argument Deduction - CTAD chỉ có từ C++17). Do đó viết <code>Container c2(20);</code> sẽ gây lỗi biên dịch trong C++11.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 18-19: Ký hiệu <> và khởi tạo khuôn mẫu lớp]</span>"
})

questions.append({
    "id": 18,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Class Templates & Cấu Trúc Dữ Liệu Tổng Quát",
    "title": "Cú pháp định nghĩa phương thức của Class Template ở ngoài Class",
    "code": """#include <iostream>

template <typename T>
class Stack {
    T elements[10];
    int top = 0;
public:
    void push(const T& val);
};

// Cú pháp định nghĩa ngoài class đúng chuẩn:
template <typename T>
void Stack<T>::push(const T& val) {
    elements[top++] = val;
    std::cout << "Pushed:" << val << " ";
}

int main() {
    Stack<int> s;
    s.push(42);
    return 0;
}""",
    "options": [
        "A. In ra: Pushed:42 (Cú pháp định nghĩa phương thức ngoài class bắt buộc phải có tiền tố template <typename T> và tên lớp kèm tham số Stack<T>::)",
        "B. Chỉ cần viết void Stack::push(const T& val)",
        "C. Lỗi biên dịch vì phương thức template bắt buộc phải viết inline trong class",
        "D. Lỗi Linker do không tìm thấy Stack<T>::push"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 25-26 chỉ dẫn chi tiết: 'Mỗi phương thức cần một lệnh template riêng... và tên lớp phải có tham số kiểu dạng <code>ClassName<T>::method()</code>'.<br>"
                   "2. Nếu quên <code><T></code> sau tên lớp (ví dụ viết <code>Stack::push</code>), trình biên dịch sẽ báo lỗi vì không tồn tại lớp thông thường nào tên là <code>Stack</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 25-26: Định nghĩa phương thức ngoài khuôn mẫu lớp]</span>"
})

questions.append({
    "id": 19,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Class Templates & Cấu Trúc Dữ Liệu Tổng Quát",
    "title": "Kế thừa giữa hai Class Template và bẫy gọi hàm lớp cha phụ thuộc (this->)",
    "code": """#include <iostream>

template <typename T>
class Base {
public:
    void greet() { std::cout << "HelloBase "; }
};

template <typename T>
class Derived : public Base<T> {
public:
    void call() {
        // greet(); // Dòng Lỗi: Compiler không tìm thấy greet!
        this->greet(); // Cách gọi chuẩn xác
    }
};

int main() {
    Derived<int> d;
    d.call();
    return 0;
}""",
    "options": [
        "A. In ra: HelloBase ; Dòng Lỗi nếu mở ra sẽ bị LỖI BIÊN DỊCH vì Base<T> là dependent base, compiler không tự tìm kiếm trong scope của nó ở Phase 1",
        "B. Dòng Lỗi hợp lệ bình thường như kế thừa C++ không template",
        "C. Lỗi biên dịch vì Derived<int> không thể kế thừa Base<int>",
        "D. Chương trình crash tại this->greet()"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Đây là quy tắc bất biến của <strong>Two-Phase Lookup</strong> trong C++.<br>"
                   "2. Khi trình biên dịch phân tích cú pháp của <code>Derived<T></code> ở Phase 1, nó chưa biết kiểu <code>T</code> là gì, và không loại trừ khả năng sau này sẽ có một phiên bản đặc tả <code>Base<Special></code> không hề có hàm <code>greet()</code>.<br>"
                   "3. Do đó, lời gọi không định danh <code>greet()</code> sẽ bị compiler báo lỗi không tìm thấy. Bắt buộc phải viết <code>this->greet()</code> hoặc <code>Base<T>::greet()</code> để báo hiệu đây là một lời gọi phụ thuộc (Dependent Call) cần hoãn sang Phase 2.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 26-27 & Dependent Base Lookup]</span>"
})

questions.append({
    "id": 20,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Class Templates & Cấu Trúc Dữ Liệu Tổng Quát",
    "title": "Lớp thông thường (Non-template Class) kế thừa từ một Template cụ thể hóa",
    "code": """#include <iostream>

template <typename T>
struct GenericNode {
    T value;
    GenericNode(T v) : value(v) {}
};

// Lớp thông thường kế thừa từ một template với kiểu cố định int:
struct IntegerNode : public GenericNode<int> {
    IntegerNode(int val) : GenericNode<int>(val) {}
    void print() {
        std::cout << "IntNode:" << value << " ";
    }
};

int main() {
    IntegerNode node(99);
    node.print();
    std::cout << sizeof(node);
    return 0;
}""",
    "options": [
        "A. IntNode:99 4 (IntegerNode là một lớp thông thường hoàn chỉnh, kế thừa đầy đủ thuộc tính của GenericNode<int>)",
        "B. Lỗi biên dịch vì lớp không phải template không được kế thừa từ template",
        "C. Kích thước node là 8 bytes",
        "D. Lỗi runtime do không tìm thấy constructor"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi truyền tham số cụ thể <code>int</code> vào <code>GenericNode<int></code>, nó trở thành một kiểu cụ thể hoàn chỉnh (Concrete Type).<br>"
                   "2. Một lớp thông thường hoàn toàn có thể kế thừa từ <code>GenericNode<int></code> giống hệt như bất kỳ lớp C++ cơ sở nào khác.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 20: Tương tác với thể hiện của khuôn mẫu]</span>"
})

questions.append({
    "id": 21,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Class Templates & Cấu Trúc Dữ Liệu Tổng Quát",
    "title": "Cấu trúc Lớp Lồng Nhau (Nested Class) bên trong Class Template",
    "code": """#include <iostream>

template <typename T>
class LinkedList {
public:
    struct Node {
        T data;
        Node* next = nullptr;
        Node(T d) : data(d) {}
    };
    Node* head = nullptr;
};

int main() {
    LinkedList<int>::Node n(50);
    std::cout << n.data << " " << sizeof(n.data);
    return 0;
}""",
    "options": [
        "A. 50 4 (Lớp lồng nhau Node tự động thừa hưởng tham số kiểu T từ lớp bao ngoài LinkedList)",
        "B. Lỗi biên dịch vì Node bắt buộc phải khai báo template riêng",
        "C. 50 8",
        "D. Lỗi runtime bad_alloc"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi một struct hoặc class được lồng bên trong một Class Template, nó tự động nằm trong phạm vi (scope) của template đó và có thể truy cập trực tiếp tham số kiểu <code>T</code>.<br>"
                   "2. Cú pháp định danh bên ngoài là <code>LinkedList<int>::Node</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 19-20: Cấu trúc lồng trong khuôn mẫu lớp]</span>"
})

questions.append({
    "id": 22,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Class Templates & Cấu Trúc Dữ Liệu Tổng Quát",
    "title": "Hàm thành viên mẫu (Member Template) bên trong một Class Template",
    "code": """#include <iostream>

template <typename T>
struct SmartPointer {
    T* ptr;
    SmartPointer(T* p) : ptr(p) {}
    ~SmartPointer() { delete ptr; }

    // Member template cho phép chuyển đổi giữa các kiểu tương thích:
    template <typename U>
    SmartPointer(SmartPointer<U>&& other) : ptr(other.ptr) {
        other.ptr = nullptr;
        std::cout << "ConvertedMove ";
    }
};

struct Base {};
struct Derived : public Base {};

int main() {
    SmartPointer<Derived> pD(new Derived());
    SmartPointer<Base> pB(std::move(pD)); // Chuyển đổi từ SmartPointer<Derived> sang SmartPointer<Base>!
    return 0;
}""",
    "options": [
        "A. ConvertedMove (Member template constructor cho phép mô phỏng hành vi chuyển đổi kiểu con trỏ upcast giữa hai SmartPointer có kiểu khác nhau)",
        "B. Lỗi biên dịch vì SmartPointer<Derived> và SmartPointer<Base> là hai kiểu không liên quan",
        "C. Lỗi runtime double free",
        "D. Chỉ in ra ConvertedMove nếu Base có virtual dtor"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Đây là kỹ thuật cốt lõi được sử dụng bên trong <code>std::unique_ptr</code> và <code>std::shared_ptr</code> của STL C++11.<br>"
                   "2. Mặc dù <code>SmartPointer<Derived></code> và <code>SmartPointer<Base></code> là hai kiểu độc lập, nhưng nhờ có <strong>Member Function Template</strong> <code>template <typename U> SmartPointer(SmartPointer<U>&&)</code>, phép gán chuyển đổi (Move Conversion) trở nên hoàn toàn hợp lệ vì con trỏ thô <code>Derived*</code> có thể ép kiểu ngầm định sang <code>Base*</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 16 & C++11 Generalized Copy/Move Constructors]</span>"
})

questions.append({
    "id": 23,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Class Templates & Cấu Trúc Dữ Liệu Tổng Quát",
    "title": "Khởi tạo thành viên tại chỗ (In-Class Member Initializer) trong Class Template",
    "code": """#include <iostream>

template <typename T>
struct DataHolder {
    T value{}; // Zero-initialization mặc định
    int status = 200; // Khởi tạo tại chỗ chuẩn C++11
};

int main() {
    DataHolder<int> d1;
    DataHolder<double> d2;
    std::cout << d1.value << " " << d1.status << " | " << d2.value << " " << d2.status;
    return 0;
}""",
    "options": [
        "A. 0 200 | 0 200 (Cú pháp value{} thực hiện value-initialization an toàn cho kiểu T, status nhận giá trị khởi tạo tại chỗ 200)",
        "B. Rác 200 | Rác 200",
        "C. Lỗi biên dịch vì C++11 cấm khởi tạo tại chỗ trong template",
        "D. 0 0 | 0 0"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Chuẩn C++11 hỗ trợ toàn diện tính năng <strong>In-class member initializers</strong> cho cả lớp thông thường và khuôn mẫu lớp.<br>"
                   "2. Cú pháp <code>T value{}</code> kích hoạt Value-initialization: đối với kiểu nguyên thủy (<code>int</code>, <code>double</code>) nó gán bằng <code>0</code>, đối với kiểu class nó gọi Default Constructor.<br>"
                   "<span class=\"citation-badge\">[Nguồn: C++11 In-class initializers & OOP7-Template.pdf - Trang 17]</span>"
})

questions.append({
    "id": 24,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Class Templates & Cấu Trúc Dữ Liệu Tổng Quát",
    "title": "Destructor của Class Template quản lý mảng động",
    "code": """#include <iostream>

template <typename T>
class DynArray {
    T* data;
    int size;
public:
    DynArray(int s) : size(s), data(new T[s]) {
        std::cout << "+Array ";
    }
    ~DynArray() {
        delete[] data;
        std::cout << "-Array ";
    }
};

int main() {
    {
        DynArray<int> arr(5);
    } // Hết scope
    std::cout << "Done";
    return 0;
}""",
    "options": [
        "A. +Array -Array Done (Destructor tự động gọi delete[] giải phóng vùng nhớ heap khi đối tượng ra khỏi scope)",
        "B. +Array Done (Rò rỉ mảng data)",
        "C. Lỗi biên dịch vì delete[] không thể dùng cho kiểu T*",
        "D. +Array -Array và crash"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi <code>DynArray<int></code> kết thúc vòng đời trên stack, trình biên dịch tự động chèn lệnh gọi destructor <code>~DynArray()</code>.<br>"
                   "2. Lệnh <code>delete[] data;</code> thực thi hủy từng phần tử và thu hồi bộ nhớ mảng heap, tuân thủ chặt chẽ nguyên lý <strong>RAII (Resource Acquisition Is Initialization)</strong>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 37: Bài tập 7.1 Lớp template mảng động]</span>"
})

print(f"Loaded {len(questions)} questions for Groups 1-3.")
# =========================================================================
# NHÓM 4: NON-TYPE TEMPLATE PARAMETERS (NTTP) & THAM SỐ TEMPLATE KHÁC (CÂU 25 - 34)
# =========================================================================

questions.append({
    "id": 25,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Non-Type Template Parameters & Tham Số Khác",
    "title": "Ràng buộc nghiêm ngặt của NTTP trong C++11 (Lệnh cấm số thực float/double)",
    "code": """#include <iostream>

template <typename T, int Size> // int là Non-type parameter hợp lệ
struct FixedBuffer {
    T buffer[Size];
};

// Cố tình dùng số thực làm NTTP:
// template <double Factor> // Dòng Lỗi
// struct Scaler {};

int main() {
    FixedBuffer<char, 128> buf;
    std::cout << sizeof(buf.buffer) << " ";
    return 0;
}""",
    "options": [
        "A. In ra: 128; Dòng Lỗi nếu mở ra sẽ bị LỖI BIÊN DỊCH vì chuẩn C++11 cấm tuyệt đối sử dụng kiểu số thực (float/double) làm tham số NTTP",
        "B. Dòng Lỗi hoàn toàn hợp lệ trong C++11",
        "C. Chỉ cho phép float, cấm double",
        "D. Lỗi biên dịch tại FixedBuffer vì Size không phải typename"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 28-33 nêu rõ: 'Các ràng buộc khi sử dụng các kiểu thực sự làm tham số cho lệnh template: tham số kiểu số nguyên int...'.<br>"
                   "2. Trong C++11, <strong>Non-Type Template Parameters (NTTP)</strong> chỉ chấp nhận: số nguyên (integral), kiểu liệt kê (enum), con trỏ hoặc tham chiếu tới đối tượng có static linkage, con trỏ hàm, hoặc <code>std::nullptr_t</code>.<br>"
                   "3. Số thực (<code>float</code>, <code>double</code>) bị cấm ngặt nghèo vì sai số dấu phẩy động (floating-point representation) có thể khiến hai giá trị giống hệt nhau về mặt logic nhưng lại có bit pattern khác nhau, làm phá vỡ bảng tra cứu kiểu của trình biên dịch.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 28-33: Các ràng buộc đối với tham số template]</span>"
})

questions.append({
    "id": 26,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Non-Type Template Parameters & Tham Số Khác",
    "title": "Hai thể hiện khác nhau về giá trị NTTP là hai kiểu lớp hoàn toàn không tương thích",
    "code": """#include <iostream>

template <typename T, int N>
struct StaticArray {
    T data[N];
};

int main() {
    StaticArray<int, 5> a1;
    StaticArray<int, 10> a2;

    // a1 = a2; // Dòng Gán
    std::cout << (sizeof(a1) != sizeof(a2)) << std::endl;
    return 0;
}""",
    "options": [
        "A. 1; Dòng Gán nếu mở ra sẽ bị LỖI BIÊN DỊCH: 'no match for operator=' vì StaticArray<int, 5> và StaticArray<int, 10> là hai kiểu hoàn toàn độc lập",
        "B. Dòng Gán hợp lệ vì cùng kiểu int",
        "C. Tự động cắt bớt 5 phần tử của a2 để gán sang a1",
        "D. In ra 0"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 30-32 nhấn mạnh: 'Mỗi giá trị tham số khác nhau sinh ra một lớp khác nhau'.<br>"
                   "2. Trong hệ thống kiểu của C++, <code>StaticArray<int, 5></code> (kích thước 20 bytes) và <code>StaticArray<int, 10></code> (kích thước 40 bytes) có type ID hoàn toàn khác nhau, giống như <code>int</code> và <code>std::string</code>. Chúng không thể gán trực tiếp cho nhau.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 30-32: Tham số NTTP và hệ thống kiểu]</span>"
})

questions.append({
    "id": 27,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Non-Type Template Parameters & Tham Số Khác",
    "title": "Truyền biểu thức hằng số constexpr và sizeof() vào NTTP",
    "code": """#include <iostream>

template <int Size>
struct MemoryPool {
    static const int capacity = Size;
};

constexpr int computeSize(int base) {
    return base * 2 + 8;
}

int main() {
    MemoryPool<computeSize(16)> pool; // 16 * 2 + 8 = 40
    MemoryPool<sizeof(double)> pool2;  // 8

    std::cout << pool.capacity << " " << pool2.capacity;
    return 0;
}""",
    "options": [
        "A. 40 8 (Mọi biểu thức có thể tính toán tại thời điểm biên dịch - compile-time constant expression như hàm constexpr và toán tử sizeof đều dùng được cho NTTP)",
        "B. Lỗi biên dịch vì hàm computeSize() là hàm, không thể truyền vào template",
        "C. 32 8",
        "D. Lỗi runtime bad_template_argument"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong chuẩn C++11, tham số NTTP đòi hỏi một <strong>Constant Expression (Biểu thức hằng số)</strong>.<br>"
                   "2. Các biểu thức được tính toán ở Compile-time như toán tử <code>sizeof(...)</code> và hàm <code>constexpr</code> được compiler đánh giá ngay trong giai đoạn dịch mã, chuyển thành giá trị nguyên cố định trước khi instantiate template.<br>"
                   "<span class=\"citation-badge\">[Nguồn: C++11 constexpr & OOP7-Template.pdf - Trang 29: Tham số số nguyên]</span>"
})

questions.append({
    "id": 28,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Non-Type Template Parameters & Tham Số Khác",
    "title": "Ràng buộc Linkage khi sử dụng Con trỏ làm NTTP trong C++11",
    "code": """#include <iostream>

template <const char* Msg>
struct Logger {
    void print() { std::cout << Msg << " "; }
};

// Biến toàn cục có liên kết tĩnh (External Linkage):
const char globalMsg[] = "GlobalHello";

int main() {
    Logger<globalMsg> log1;
    log1.print();

    // Logger<"LiteralHello"> log2; // Dòng Lỗi: Chuỗi string literal!
    return 0;
}""",
    "options": [
        "A. In ra: GlobalHello ; Dòng Lỗi nếu mở ra sẽ bị LỖI BIÊN DỊCH vì chuỗi literal không có external linkage trong C++11",
        "B. Cả hai cách đều hợp lệ trong C++11",
        "C. Cả hai cách đều bị lỗi biên dịch",
        "D. In ra GlobalHello LiteralHello"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++11, khi dùng con trỏ <code>const char*</code> làm NTTP, con trỏ đó <strong>BẮT BUỘC phải trỏ tới một đối tượng có External / Static Linkage</strong> (địa chỉ bộ nhớ cố định trong phân vùng tĩnh mà Linker nhìn thấy được).<br>"
                   "2. Một chuỗi ký tự trực tiếp (String Literal <code>\"LiteralHello\"</code>) không có tên định danh và không có external linkage, do đó compiler từ chối nhận nó làm tham số template.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 33: Ràng buộc con trỏ làm tham số template]</span>"
})

questions.append({
    "id": 29,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Non-Type Template Parameters & Tham Số Khác",
    "title": "Tham số khuôn mẫu là một khuôn mẫu (Template Template Parameters)",
    "code": """#include <iostream>

// Lớp lưu trữ nhận một tham số kiểu
template <typename T>
struct SimpleList {
    T val;
};

// Lớp bao bọc nhận tham số thứ hai là một Khuôn Mẫu (Template Template Parameter):
template <typename T, template <typename> class Container>
struct Wrapper {
    Container<T> storage;
    void set(T v) { storage.val = v; }
    T get() { return storage.val; }
};

int main() {
    Wrapper<int, SimpleList> w;
    w.set(88);
    std::cout << w.get();
    return 0;
}""",
    "options": [
        "A. In ra: 88 (Template Template Parameter cho phép truyền bản thân một khuôn mẫu chưa cụ thể hóa làm tham số cho khuôn mẫu khác)",
        "B. Lỗi biên dịch vì SimpleList chưa truyền tham số <int>",
        "C. Phải viết Wrapper<int, SimpleList<int>>",
        "D. Chương trình crash tại w.get()"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 34-36 giải thích rõ: <em>'Một loại tham số thứ ba cho lệnh template chính là một template... cú pháp: template <typename T, template <typename> class Container> class Map'</em>.<br>"
                   "2. Khi truyền <code>SimpleList</code> vào <code>Wrapper</code>, ta truyền một <strong>Khuôn mẫu gốc (Template Pattern)</strong> chứ không phải một kiểu hoàn chỉnh. Bên trong <code>Wrapper</code>, nó tự ghép kiểu <code>Container<T></code> thành <code>SimpleList<int></code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 34-36: Template sử dụng template]</span>"
})

questions.append({
    "id": 30,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Non-Type Template Parameters & Tham Số Khác",
    "title": "Bẫy Template Template Parameter với std::vector do tham số Allocator mặc định",
    "code": """#include <iostream>
#include <vector>

// Template Template Parameter mong đợi chính xác 1 tham số template:
template <typename T, template <typename> class Container>
struct BadContainerWrapper {};

// Cách giải quyết chuẩn C++11 bằng Template Alias:
template <typename T>
using VectorWrapper = std::vector<T>;

template <typename T, template <typename> class Cont>
struct GoodWrapper {
    Cont<T> c;
};

int main() {
    // BadContainerWrapper<int, std::vector> bad; // Dòng Bẫy C++03!
    GoodWrapper<int, VectorWrapper> good;
    good.c.push_back(100);
    std::cout << good.c[0];
    return 0;
}""",
    "options": [
        "A. In ra: 100; Dòng Bẫy bị lỗi trong các chuẩn cũ vì std::vector thực chất có 2 tham số (T và Allocator), dùng template alias trong C++11 giải quyết triệt để lỗi này",
        "B. Dòng Bẫy hợp lệ hoàn toàn trong mọi chuẩn C++",
        "C. Lỗi biên dịch tại using VectorWrapper",
        "D. Chương trình crash tại push_back"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khai báo thực sự của <code>std::vector</code> trong STL là <code>template <typename T, typename Alloc = std::allocator<T>> class vector;</code> (gồm 2 tham số template).<br>"
                   "2. Một template template parameter khai báo <code>template <typename> class Cont</code> chỉ nhận khuôn mẫu có ĐÚNG 1 tham số.<br>"
                   "3. Trong C++11, sử dụng <strong>Template Alias</strong> (<code>template <typename T> using VectorWrapper = std::vector<T>;</code>) che giấu tham số allocator thứ hai, giúp ghép khớp hoàn hảo.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 35-36 & C++11 Template Alias with Template Template]</span>"
})

questions.append({
    "id": 31,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Non-Type Template Parameters & Tham Số Khác",
    "title": "Cải tiến Cú pháp Dấu Ngoặc Nhọn Kép >> trong C++11 (Right Angle Bracket Fix)",
    "code": """#include <iostream>
#include <vector>

template <typename T>
struct Holder {
    T data;
};

int main() {
    // Trong C++03 bắt buộc phải viết: Holder<Holder<int> > (có dấu cách)
    // Trong C++11 được viết liền:
    Holder<Holder<int>> nested; // >> không còn bị nhầm là toán tử dịch bit!
    nested.data.data = 77;
    std::cout << nested.data.data;
    return 0;
}""",
    "options": [
        "A. In ra: 77 (C++11 giải quyết lỗi cú pháp cổ điển, compiler đủ thông minh để nhận diện >> là hai dấu đóng ngoặc nhọn lồng nhau thay vì toán tử dịch bit right-shift)",
        "B. Lỗi biên dịch vì >> là toán tử nhập cin >> hoặc dịch bit",
        "C. Lỗi biên dịch do thiếu thư viện <vector>",
        "D. In ra 0"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++03, trình phân tích từ vựng (Lexer) hoạt động theo nguyên tắc 'Maximal Munch': hai ký tự <code>>></code> đứng liền nhau luôn bị gom lại thành token toán tử dịch bit <code>>></code>, dẫn tới lỗi cú pháp ngớ ngẩn và buộc lập trình viên phải chèn dấu cách <code>> ></code>.<br>"
                   "2. Chuẩn C++11 đã sửa đổi quy tắc từ vựng ngữ cảnh, nhận diện chính xác <code>>></code> là hai dấu đóng template liên tiếp.<br>"
                   "<span class=\"citation-badge\">[Nguồn: C++11 Right Angle Bracket Fix (N1757) & OOP7-Template.pdf - Trang 18]</span>"
})

questions.append({
    "id": 32,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Non-Type Template Parameters & Tham Số Khác",
    "title": "Giá trị mặc định cho Non-Type Template Parameter",
    "code": """#include <iostream>

template <typename T, int Capacity = 64>
class Buffer {
public:
    int getCapacity() const { return Capacity; }
};

int main() {
    Buffer<char> b1;       // Dùng mặc định Capacity = 64
    Buffer<int, 256> b2;   // Chỉ định Capacity = 256

    std::cout << b1.getCapacity() << " " << b2.getCapacity();
    return 0;
}""",
    "options": [
        "A. 64 256 (C++ cho phép gán giá trị mặc định cho tham số NTTP tương tự như tham số hàm)",
        "B. 64 64",
        "C. 0 256",
        "D. Lỗi biên dịch vì NTTP không được phép có giá trị mặc định"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Tương tự như tham số kiểu (<code>typename T = int</code>), các tham số phi kiểu NTTP cũng hoàn toàn được phép có giá trị hằng mặc định: <code>int Capacity = 64</code>.<br>"
                   "2. Khi khởi tạo <code>Buffer<char></code>, compiler điền giá trị <code>64</code> vào tham số <code>Capacity</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 29-31: Tham số mặc định cho template]</span>"
})

questions.append({
    "id": 33,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Non-Type Template Parameters & Tham Số Khác",
    "title": "Metaprogramming cơ bản: Tính toán tại thời điểm biên dịch bằng NTTP",
    "code": """#include <iostream>

// Tính giai thừa lúc biên dịch bằng đệ quy template NTTP
template <int N>
struct Factorial {
    static const int value = N * Factorial<N - 1>::value;
};

// Điều kiện dừng đệ quy (Specialization cho N = 0):
template <>
struct Factorial<0> {
    static const int value = 1;
};

int main() {
    std::cout << Factorial<5>::value; // 5! = 120
    return 0;
}""",
    "options": [
        "A. 120 (Toàn bộ phép tính 5*4*3*2*1 được compiler giải quyết tại compile-time, mã thực thi chỉ chứa hằng số 120 không tốn một chu kỳ CPU runtime)",
        "B. 24",
        "C. Lỗi tràn ngăn xếp stack tại runtime do đệ quy",
        "D. Lỗi biên dịch vì template không thể tự gọi chính nó"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Đây là kỹ thuật <strong>Template Metaprogramming (TMP)</strong> kinh điển.<br>"
                   "2. Khi compiler gặp <code>Factorial<5></code>, nó lần lượt instantiate: <code>Factorial<4></code>, <code>Factorial<3></code>, <code>Factorial<2></code>, <code>Factorial<1></code>, và chạm tới điểm dừng <code>Factorial<0></code>.<br>"
                   "3. Giá trị <code>120</code> được tính toán xong xuôi trước khi sinh ra file nhị phân (Zero-overhead computation).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 28-30 & Template Metaprogramming basics]</span>"
})

questions.append({
    "id": 34,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Non-Type Template Parameters & Tham Số Khác",
    "title": "Bẫy con trỏ hàm làm tham số Non-Type Template Parameter",
    "code": """#include <iostream>

int add(int a, int b) { return a + b; }
int multiply(int a, int b) { return a * b; }

template <int (*Op)(int, int)>
int compute(int x, int y) {
    return Op(x, y);
}

int main() {
    std::cout << compute<add>(4, 5) << " ";
    std::cout << compute<multiply>(4, 5);
    return 0;
}""",
    "options": [
        "A. 9 20 (Con trỏ hàm có external linkage là NTTP hợp lệ, cho phép compiler inline trực tiếp con trỏ hàm mà không cần gọi gián tiếp)",
        "B. Lỗi biên dịch vì con trỏ hàm không thể là tham số template",
        "C. 20 9",
        "D. Chương trình crash tại lời gọi Op(x, y)"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Con trỏ hàm có liên kết tĩnh (như <code>&add</code>, <code>&multiply</code>) là một NTTP hoàn toàn hợp lệ trong C++11.<br>"
                   "2. Điểm đặc biệt: Vì địa chỉ hàm được cố định tại thời điểm biên dịch cho từng bản thể hiện <code>compute<add></code>, trình tối ưu hóa (Optimizer) có thể <strong>inline trực tiếp thân hàm add</strong> vào vị trí gọi, loại bỏ hoàn toàn chi phí gọi con trỏ hàm thông thường!<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 33: Con trỏ hàm trong template]</span>"
})

print(f"Loaded {len(questions)} questions for Groups 1-4.")
# =========================================================================
# NHÓM 5: ĐẶC TẢ KHUÔN MẪU (TEMPLATE SPECIALIZATION) (CÂU 35 - 42)
# =========================================================================

questions.append({
    "id": 35,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Đặc Tả Khuôn Mẫu (Template Specialization)",
    "title": "Đặc Tả Toàn Phần (Full Specialization) cho Class Template",
    "code": """#include <iostream>

template <typename T>
struct Storage {
    void print() { std::cout << "GenericStorage "; }
};

// Đặc tả toàn phần cho kiểu bool:
template <>
struct Storage<bool> {
    void print() { std::cout << "OptimizedBitStorage "; }
};

int main() {
    Storage<int> s1;
    Storage<bool> s2;

    s1.print();
    s2.print();
    return 0;
}""",
    "options": [
        "A. GenericStorage OptimizedBitStorage (Cú pháp template <> cho phép thay thế hoàn toàn cấu trúc class cho một kiểu dữ liệu cụ thể như std::vector<bool>)",
        "B. GenericStorage GenericStorage",
        "C. Lỗi biên dịch vì trùng tên struct Storage",
        "D. Lỗi Linker do duplicate symbol"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <strong>Full Specialization (Đặc tả toàn phần)</strong> sử dụng cú pháp <code>template <> struct Storage<bool></code>.<br>"
                   "2. Khi gặp <code>Storage<bool></code>, trình biên dịch bỏ qua Primary Template và sử dụng bản cài đặt riêng biệt này.<br>"
                   "3. Đây là kỹ thuật mà STL áp dụng cho <code>std::vector<bool></code> để nén mỗi giá trị boolean vào đúng 1 bit trong RAM thay vì 1 byte.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 20-22: Đặc tả khuôn mẫu lớp]</span>"
})

questions.append({
    "id": 36,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Đặc Tả Khuôn Mẫu (Template Specialization)",
    "title": "Đặc Tả Từng Phần (Partial Specialization) cho Kiểu Con Trỏ",
    "code": """#include <iostream>

template <typename T>
struct Inspector {
    static void inspect(T val) { std::cout << "ValueType "; }
};

// Đặc tả từng phần cho mọi kiểu con trỏ T*:
template <typename T>
struct Inspector<T*> {
    static void inspect(T* val) { std::cout << "PointerToType "; }
};

int main() {
    int x = 10;
    Inspector<int>::inspect(x);
    Inspector<int*>::inspect(&x);
    return 0;
}""",
    "options": [
        "A. ValueType PointerToType (Partial Specialization nhận diện mọi kiểu con trỏ T* một cách tự động)",
        "B. ValueType ValueType",
        "C. PointerToType PointerToType",
        "D. Lỗi biên dịch vì template không hỗ trợ ký tự *"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <strong>Partial Specialization (Đặc tả từng phần)</strong> cho phép thu hẹp phạm vi của tham số kiểu (Pattern Matching).<br>"
                   "2. Cú pháp <code>template <typename T> struct Inspector<T*></code> áp dụng cho bất kỳ kiểu con trỏ nào (<code>int*</code>, <code>char*</code>, <code>double*</code>), cho phép xử lý giải tham chiếu an toàn.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 21-22 & Partial Specialization rules]</span>"
})

questions.append({
    "id": 37,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Đặc Tả Khuôn Mẫu (Template Specialization)",
    "title": "Đặc Tả Từng Phần khi hai tham số kiểu trùng nhau",
    "code": """#include <iostream>

template <typename T, typename U>
struct PairHandler {
    static void handle() { std::cout << "DifferentTypes "; }
};

// Đặc tả từng phần khi cả 2 tham số đều cùng kiểu T:
template <typename T>
struct PairHandler<T, T> {
    static void handle() { std::cout << "SameTypes "; }
};

int main() {
    PairHandler<int, double>::handle();
    PairHandler<int, int>::handle();
    return 0;
}""",
    "options": [
        "A. DifferentTypes SameTypes (Khi hai tham số template cùng kiểu, compiler tự động chọn bản partial specialization <T, T> vì tính chuyên biệt cao hơn)",
        "B. DifferentTypes DifferentTypes",
        "C. SameTypes SameTypes",
        "D. Lỗi biên dịch do mơ hồ giữa 2 định nghĩa"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong quy tắc so khớp của trình biên dịch, một bản đặc tả từng phần (Partial Specialization) có độ chuyên biệt (more specialized) cao hơn Primary Template sẽ luôn được ưu tiên lựa chọn.<br>"
                   "2. <code>PairHandler<int, int></code> khớp hoàn hảo với mẫu <code><T, T></code> -> in ra <code>SameTypes</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 17 & 21: Pair template và đặc tả]</span>"
})

questions.append({
    "id": 38,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Đặc Tả Khuôn Mẫu (Template Specialization)",
    "title": "Bẫy Lớn: Khuôn Mẫu Hàm (Function Template) KHÔNG HỖ TRỢ Đặc Tả Từng Phần!",
    "code": """#include <iostream>

template <typename T, typename U>
void process(T a, U b) { std::cout << "GenericFunc "; }

// Cố tình viết partial specialization cho function template:
// template <typename T>
// void process<T, int>(T a, int b) {} // Dòng Lỗi

int main() {
    process(1, 2.5);
    std::cout << "FunctionCannotBePartiallySpecialized";
    return 0;
}""",
    "options": [
        "A. In ra: GenericFunc FunctionCannotBePartiallySpecialized; Dòng Lỗi nếu mở ra sẽ bị LỖI BIÊN DỊCH vì C++ cấm partial specialization trên Function Template",
        "B. Function Template hỗ trợ partial specialization bình thường trong C++11",
        "C. Lỗi biên dịch tại process(1, 2.5)",
        "D. Tự động chuyển thành overload"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <strong>Quy tắc cấm kỵ của ISO C++:</strong> Chỉ có Class Template mới được phép Đặc tả từng phần (Partial Specialization). <strong>Function Template TUYỆT ĐỐI KHÔNG HỖ TRỢ</strong> đặc tả từng phần!<br>"
                   "2. Để đạt được hiệu ứng tương tự cho hàm, lập trình viên bắt buộc phải sử dụng <strong>Function Overloading (Nạp chồng hàm)</strong> thông thường: <code>template <typename T> void process(T a, int b);</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 12-15 & ISO C++ Function Template Restrictions]</span>"
})

questions.append({
    "id": 39,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Đặc Tả Khuôn Mẫu (Template Specialization)",
    "title": "Đặc tả toàn phần cho Function Template và Cú pháp chuẩn",
    "code": """#include <iostream>

template <typename T>
void display(T val) {
    std::cout << "Generic:" << val << " ";
}

// Full Specialization cho const char*
template <>
void display<const char*>(const char* val) {
    std::cout << "SpecializedString:" << val << " ";
}

int main() {
    display(100);
    display("Hello");
    return 0;
}""",
    "options": [
        "A. Generic:100 SpecializedString:Hello (Đặc tả toàn phần cho Function Template hoàn toàn hợp lệ với cú pháp template <>)",
        "B. Generic:100 Generic:Hello",
        "C. Lỗi biên dịch vì function template không thể có full specialization",
        "D. Lỗi Linker"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Mặc dù không hỗ trợ Partial Specialization, Function Template <strong>HOÀN TOÀN HỖ TRỢ Full Specialization (Đặc tả toàn phần)</strong> với cú pháp <code>template <> void func<SpecificType>(SpecificType)</code>.<br>"
                   "2. Khi truyền <code>\"Hello\"</code>, compiler nhận diện kiểu <code>const char*</code> và gọi vào bản đặc tả riêng biệt.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 14-15: Đặc tả khuôn mẫu hàm]</span>"
})

questions.append({
    "id": 40,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Đặc Tả Khuôn Mẫu (Template Specialization)",
    "title": "Bẫy Tương Tác Giữa Function Overloading và Function Specialization (Sutter's Trap)",
    "code": """#include <iostream>

// 1. Base template:
template <typename T>
void f(T) { std::cout << "1 "; }

// 2. Base template overload:
template <typename T>
void f(T*) { std::cout << "2 "; }

// 3. Specialization của template 1 (không phải của 2!):
template <>
void f<int*>(int*) { std::cout << "3 "; }

int main() {
    int* p = nullptr;
    f(p); // Gọi hàm nào? Bẫy cực kỳ hóc búa!
    return 0;
}""",
    "options": [
        "A. In ra: 2 (Quá trình Overload Resolution chọn template 2 trước, và vì specialization 3 thuộc về template 1 nên nó bị bỏ qua hoàn toàn!)",
        "B. In ra: 3",
        "C. In ra: 1",
        "D. Lỗi biên dịch do mơ hồ giữa 2 và 3"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Đây là cạm bẫy nổi tiếng được chuyên gia Herb Sutter chỉ ra (<em>'Why Not Specialize Function Templates?'</em>).<br>"
                   "2. <strong>Quy tắc của C++:</strong> Specialization KHÔNG tham gia vào quá trình Overload Resolution! Trình biên dịch chỉ chọn giữa các Base Template (giữa hàm 1 và hàm 2).<br>"
                   "3. Với đối số <code>int*</code>, hàm 2 <code>f(T*)</code> chuyên biệt hơn hàm 1 <code>f(T)</code>, nên compiler chọn hàm 2!<br>"
                   "4. Sau khi chọn hàm 2, compiler kiểm tra xem hàm 2 có specialization nào không? Không có! (Bản số 3 là specialization của hàm 1). Do đó nó gọi mã của hàm 2 -> in ra <code>2 </code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 12-15 & Herb Sutter: Why Not Specialize Function Templates]</span>"
})

questions.append({
    "id": 41,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Đặc Tả Khuôn Mẫu (Template Specialization)",
    "title": "Đặc tả một Phương Thức Thành Viên Duy Nhất của Class Template",
    "code": """#include <iostream>

template <typename T>
struct Processor {
    void run() { std::cout << "GenericRun "; }
};

// Đặc tả riêng phương thức run() cho kiểu double mà không cần viết lại cả class:
template <>
void Processor<double>::run() {
    std::cout << "DoubleSpecialRun ";
}

int main() {
    Processor<int> p1;
    Processor<double> p2;

    p1.run();
    p2.run();
    return 0;
}""",
    "options": [
        "A. GenericRun DoubleSpecialRun (C++ cho phép đặc tả toàn phần từng phương thức thành viên riêng lẻ của một Class Template mà không cần định nghĩa lại cả lớp)",
        "B. Lỗi biên dịch vì bắt buộc phải đặc tả toàn bộ struct Processor<double>",
        "C. GenericRun GenericRun",
        "D. Lỗi Linker"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Chuẩn C++ cho phép tính linh hoạt cao: Bạn không bắt buộc phải sao chép toàn bộ khai báo lớp nếu chỉ muốn thay đổi hành vi của duy nhất một hàm thành viên.<br>"
                   "2. Cú pháp <code>template <> void Processor<double>::run()</code> định nghĩa riêng mã máy cho hàm đó khi <code>T = double</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 25 & Member function template specialization]</span>"
})

questions.append({
    "id": 42,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Đặc Tả Khuôn Mẫu (Template Specialization)",
    "title": "Đặc tả biến thành viên tĩnh (Static Member Specialization)",
    "code": """#include <iostream>

template <typename T>
struct TypeName {
    static const char* name;
};

template <typename T>
const char* TypeName<T>::name = "UnknownType";

// Đặc tả biến static cho int:
template <>
const char* TypeName<int>::name = "Integer";

int main() {
    std::cout << TypeName<double>::name << " ";
    std::cout << TypeName<int>::name;
    return 0;
}""",
    "options": [
        "A. UnknownType Integer (Biến thành viên tĩnh của Class Template có thể được đặc tả riêng biệt cho từng kiểu cụ thể)",
        "B. UnknownType UnknownType",
        "C. Integer Integer",
        "D. Lỗi biên dịch do thiếu template <>"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Tương tự như phương thức thành viên, biến static của một Class Template cũng có thể được khởi tạo và đặc tả riêng biệt thông qua <code>template <> const char* TypeName<int>::name = ...</code>.<br>"
                   "2. Giá trị này nằm trong bảng ký hiệu tĩnh của <code>TypeName<int></code>, không ảnh hưởng tới các kiểu khác.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 19-20 & Static member template specialization]</span>"
})

print(f"Loaded {len(questions)} questions for Groups 1-5.")
# =========================================================================
# NHÓM 6: C++11 MODERN TEMPLATE FEATURES & METAPROGRAMMING (CÂU 43 - 50)
# =========================================================================

questions.append({
    "id": 43,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: C++11 Template Features & Metaprogramming",
    "title": "Bắt Buộc Sử Dụng Từ Khóa typename Cho Dependent Type",
    "code": """#include <iostream>
#include <vector>

template <typename Container>
void printFirst(const Container& c) {
    // Bắt buộc phải có từ khóa typename:
    typename Container::const_iterator it = c.begin();
    if (it != c.end()) {
        std::cout << *it << " ";
    }
}

int main() {
    std::vector<int> v = {42, 99};
    printFirst(v);
    return 0;
}""",
    "options": [
        "A. In ra: 42; Nếu bỏ từ khóa typename trước Container::const_iterator, compiler sẽ báo LỖI BIÊN DỊCH vì mặc định coi nó là một biến/phép nhân",
        "B. Không cần từ khóa typename trong C++11",
        "C. Lỗi biên dịch vì vector không có const_iterator",
        "D. Chỉ in ra khi dùng con trỏ thô"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, cú pháp <code>T::something * x;</code> có thể mang 2 ý nghĩa mơ hồ:<br>"
                   "   - Khai báo con trỏ <code>x</code> thuộc kiểu <code>T::something</code>.<br>"
                   "   - Phép nhân giữa biến tĩnh <code>T::something</code> và biến <code>x</code>!<br>"
                   "2. Để giải quyết sự nhập nhằng trong quá trình phân tích cú pháp ở Phase 1, chuẩn C++ quy định: <strong>Mọi thành viên phụ thuộc kiểu (Dependent Name) bắt buộc phải có từ khóa <code>typename</code> đứng trước</strong> để khẳng định nó là một kiểu dữ liệu.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP7-Template.pdf - Trang 11 & C++ typename disambiguator rule]</span>"
})

questions.append({
    "id": 44,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: C++11 Template Features & Metaprogramming",
    "title": "Khuôn mẫu Bí danh (Alias Templates) với từ khóa using trong C++11",
    "code": """#include <iostream>
#include <map>
#include <string>

// C++11 Template Alias thay thế cho typedef cũ kỹ:
template <typename ValueType>
using StringMap = std::map<std::string, ValueType>;

int main() {
    StringMap<int> ages;
    ages["Alice"] = 25;
    ages["Bob"] = 30;

    std::cout << ages["Alice"] << " " << ages["Bob"];
    return 0;
}""",
    "options": [
        "A. 25 30 (Tính năng Alias Template với cú pháp using trong C++11 cho phép tạo bí danh có tham số hóa, điều mà typedef của C++03 bất lực)",
        "B. Lỗi biên dịch vì using không thể đi kèm với template",
        "C. 0 0",
        "D. Lỗi runtime bad_alloc"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trước C++11, từ khóa <code>typedef</code> không thể tham số hóa theo template (muốn làm phải bọc qua struct trung gian rất cồng kềnh).<br>"
                   "2. C++11 đưa vào cú pháp <code>template <typename T> using Alias = Target<T>;</code>, cho phép định nghĩa các kiểu rút gọn cực kỳ trong sáng và thanh lịch.<br>"
                   "<span class=\"citation-badge\">[Nguồn: C++11 Alias Templates & OOP7-Template.pdf - Trang 35]</span>"
})

questions.append({
    "id": 45,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: C++11 Template Features & Metaprogramming",
    "title": "Khuôn Mẫu Số Lượng Tham Số Biến Đổi (Variadic Templates) & sizeof... trong C++11",
    "code": """#include <iostream>

template <typename... Args> // Parameter Pack trong C++11
void countArgs(Args... args) {
    // Toán tử sizeof... trả về số lượng tham số trong pack:
    std::cout << sizeof...(Args) << " " << sizeof...(args) << " ";
}

int main() {
    countArgs(1, 2.5, "three", '4');
    countArgs(); // Không truyền tham số nào
    return 0;
}""",
    "options": [
        "A. 4 4 0 0 (Toán tử sizeof... đếm chính xác số lượng đối số trong Parameter Pack tại thời điểm biên dịch)",
        "B. 4 8 0 0 (Trả về số byte)",
        "C. Lỗi biên dịch vì dấu ... chỉ dùng cho printf",
        "D. 4 0 0 0"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <strong>Variadic Templates</strong> là một trong những tính năng mang tính cách mạng nhất của chuẩn C++11 (N2242).<br>"
                   "2. Cú pháp <code>typename... Args</code> đại diện cho một gói tham số (Parameter Pack) có thể chứa từ 0 đến vô hạn kiểu dữ liệu.<br>"
                   "3. Toán tử <code>sizeof...(Args)</code> tính toán số lượng phần tử trong gói ngay lúc biên dịch.<br>"
                   "<span class=\"citation-badge\">[Nguồn: C++11 Variadic Templates & Parameter Pack Specification]</span>"
})

questions.append({
    "id": 46,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: C++11 Template Features & Metaprogramming",
    "title": "Kỹ thuật đệ quy mở gói (Recursive Unpack) trong Variadic Templates C++11",
    "code": """#include <iostream>

// 1. Điểm dừng đệ quy (Base case):
void printAll() {
    std::cout << "|End";
}

// 2. Hàm đệ quy mở gói (Recursive step):
template <typename T, typename... Rest>
void printAll(T first, Rest... rest) {
    std::cout << first << " ";
    printAll(rest...); // Mở gói phần còn lại
}

int main() {
    printAll(1, "OOP", 3.14);
    return 0;
}""",
    "options": [
        "A. 1 OOP 3.14 |End (Mỗi bước đệ quy tại compile-time tách phần tử đầu tiên first và chuyển tiếp gói rest... cho đến khi chạm vào hàm rỗng base case)",
        "B. 1 1 1 |End",
        "C. Lỗi biên dịch vì thiếu dấu phẩy trong rest...",
        "D. Tràn stack tại runtime"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++11, để duyệt qua các phần tử của Variadic Template, kỹ thuật phổ biến nhất là <strong>Đệ quy mở gói (Recursive Template Unpacking)</strong>.<br>"
                   "2. Compiler sinh ra 3 hàm chuyên biệt lúc dịch mã:<br>"
                   "   - <code>printAll(int, const char*, double)</code>: in <code>1</code>, gọi bước tiếp.<br>"
                   "   - <code>printAll(const char*, double)</code>: in <code>OOP</code>, gọi bước tiếp.<br>"
                   "   - <code>printAll(double)</code>: in <code>3.14</code>, gọi bước <code>printAll()</code> rỗng -> in <code>|End</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: C++11 Variadic Pack Expansion & Recursion]</span>"
})

questions.append({
    "id": 47,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: C++11 Template Features & Metaprogramming",
    "title": "Kết hợp decltype và Trailing Return Type trong Function Template C++11",
    "code": """#include <iostream>

// C++11 Trailing Return Type tự động suy luận kiểu trả về của phép cộng giữa 2 kiểu khác nhau:
template <typename T, typename U>
auto addMixed(T a, U b) -> decltype(a + b) {
    return a + b;
}

int main() {
    auto res1 = addMixed(10, 2.5); // int + double -> double
    auto res2 = addMixed(5, 3);    // int + int -> int

    std::cout << res1 << " " << sizeof(res1) << " | " << res2 << " " << sizeof(res2);
    return 0;
}""",
    "options": [
        "A. 12.5 8 | 8 4 (Toán tử decltype(a + b) suy diễn chính xác kiểu kết quả theo quy tắc chuyển đổi số học chuẩn lúc biên dịch)",
        "B. 12 4 | 8 4",
        "C. Lỗi biên dịch vì auto không thể đi kèm với decltype",
        "D. 12.5 4 | 8 8"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++03, không có cách nào viết kiểu trả về cho hàm cộng hai kiểu bất kỳ <code>T a, U b</code> vì không biết kiểu nào lớn hơn.<br>"
                   "2. C++11 giải quyết triệt để vấn đề này bằng cú pháp <strong>Trailing Return Type</strong> <code>auto func(...) -> decltype(...)</code>.<br>"
                   "3. Vì <code>decltype(a + b)</code> nằm sau danh sách tham số, nó nhìn thấy các định danh <code>a</code> và <code>b</code>, cho phép compiler tra cứu bảng thăng hạng kiểu (Type Promotion: <code>int + double -> double</code>) chuẩn xác 100%.<br>"
                   "<span class=\"citation-badge\">[Nguồn: C++11 Trailing Return Types & decltype specification]</span>"
})

questions.append({
    "id": 48,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: C++11 Template Features & Metaprogramming",
    "title": "Kiểm tra kiểu dữ liệu lúc biên dịch với thư viện <type_traits> trong C++11",
    "code": """#include <iostream>
#include <type_traits>

template <typename T>
void checkPointer(T val) {
    if (std::is_pointer<T>::value) {
        std::cout << "IsPointer ";
    } else {
        std::cout << "NotPointer ";
    }
}

int main() {
    int a = 10;
    checkPointer(a);
    checkPointer(&a);
    return 0;
}""",
    "options": [
        "A. NotPointer IsPointer (Thư viện <type_traits> trong C++11 cho phép truy vấn đặc tính kiểu dữ liệu hoàn toàn tại thời điểm biên dịch)",
        "B. NotPointer NotPointer",
        "C. IsPointer IsPointer",
        "D. Lỗi biên dịch do thiếu typeinfo"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Chuẩn C++11 giới thiệu thư viện <code><type_traits></code>, cung cấp các cấu trúc khuôn mẫu siêu dữ liệu (Type Meta-functions).<br>"
                   "2. <code>std::is_pointer<T>::value</code> là một hằng số <code>bool</code> (compile-time constant). Với <code>int</code> nó là <code>false</code>, với <code>int*</code> nó là <code>true</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: C++11 <type_traits> Header & Type Introspection]</span>"
})

questions.append({
    "id": 49,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: C++11 Template Features & Metaprogramming",
    "title": "Nguyên lý SFINAE (Substitution Failure Is Not An Error) với std::enable_if",
    "code": """#include <iostream>
#include <type_traits>

// Phiên bản 1: Chỉ kích hoạt cho kiểu số nguyên (Integral)
template <typename T>
typename std::enable_if<std::is_integral<T>::value, void>::type
processNumber(T val) {
    std::cout << "Integer:" << val << " ";
}

// Phiên bản 2: Chỉ kích hoạt cho kiểu số thực (Floating point)
template <typename T>
typename std::enable_if<std::is_floating_point<T>::value, void>::type
processNumber(T val) {
    std::cout << "Float:" << val << " ";
}

int main() {
    processNumber(42);
    processNumber(3.14);
    return 0;
}""",
    "options": [
        "A. Integer:42 Float:3.14 (Nguyên lý SFINAE: khi thay thế kiểu thất bại trên một template, compiler không báo lỗi mà âm thầm loại bỏ nó khỏi overload set)",
        "B. Lỗi biên dịch vì trùng tên hàm processNumber",
        "C. Integer:42 Integer:3",
        "D. Float:42 Float:3.14"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <strong>SFINAE (Substitution Failure Is Not An Error)</strong> là hòn đá tảng của C++ Template Metaprogramming.<br>"
                   "2. Khi gọi <code>processNumber(42)</code>, đối với Phiên bản 2, <code>std::is_floating_point<int>::value</code> là <code>false</code>, cấu trúc <code>enable_if</code> không có thành viên <code>type</code>. Quá trình thay thế thất bại, nhưng compiler không báo lỗi mà chỉ đơn giản loại bỏ Phiên bản 2 và chọn Phiên bản 1.<br>"
                   "<span class=\"citation-badge\">[Nguồn: C++11 std::enable_if & SFINAE Mechanics]</span>"
})

questions.append({
    "id": 50,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: C++11 Template Features & Metaprogramming",
    "title": "So sánh Đa Hình Động (Virtual VTable) vs Đa Hình Tĩnh (Templates)",
    "code": """#include <iostream>

// Cách 1: Đa hình động
struct DynamicBase {
    virtual void run() { std::cout << "Dynamic "; }
};

// Cách 2: Đa hình tĩnh bằng Template
template <typename T>
void executeStatic(T obj) {
    obj.run();
}

struct StaticWorker {
    void run() { std::cout << "Static "; }
};

int main() {
    DynamicBase d;
    d.run();
    executeStatic(StaticWorker());
    return 0;
}""",
    "options": [
        "A. Dynamic Static (Đa hình động tốn chi phí con trỏ vptr và gọi gián tiếp runtime nhưng mã nguồn gọn; Đa hình tĩnh template có hiệu năng tối đa và có thể inline nhưng có nguy cơ phình to mã nhị phân)",
        "B. Cả hai phương pháp đều có hiệu năng và cơ chế sinh mã giống hệt nhau",
        "C. Lỗi biên dịch tại executeStatic",
        "D. Static Dynamic"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <strong>Đa hình động (Dynamic Polymorphism - Chương 6):</strong> Dựa trên VTable và vptr. Chi phí: thêm 8 bytes trên mỗi đối tượng, 1 bước gián tiếp khi gọi hàm, cản trở tối ưu hóa Inline của trình biên dịch.<br>"
                   "2. <strong>Đa hình tĩnh (Static Polymorphism - Chương 7):</strong> Dựa trên Templates và Duck Typing compile-time. Không tốn thêm byte RAM nào trong đối tượng, trình biên dịch có thể inline 100% mã nguồn để đạt hiệu năng tối đa (Zero-overhead), nhưng có thể làm tăng thời gian build và kích thước file thực thi (Code Bloat).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf & OOP7-Template.pdf - Trang 2-10: Tổng kết so sánh hai trường phái đa hình]</span>"
})

print(f"Loaded ALL {len(questions)} questions for Chapter 7 successfully!")
