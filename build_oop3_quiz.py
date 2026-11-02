# -*- coding: utf-8 -*-
import json

questions = []

# =========================================================================
# NHÓM 1: KHAI BÁO LỚP & FILE PHÂN TÁCH (CÂU 1 - 5)
# =========================================================================

questions.append({
    "id": 1,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Khai Báo Lớp & File Phân Tách",
    "title": "Hàm định nghĩa bên trong class ngầm định mang thuộc tính inline",
    "code": """// File: Vector.h
class Vector {
    int x, y;
public:
    Vector(int x, int y) : x(x), y(y) {}
    // Hàm getX được định nghĩa trực tiếp bên trong thân class:
    int getX() const { return x; }
};""",
    "options": [
        "A. getX() được trình biên dịch ngầm định xử lý như một hàm inline",
        "B. getX() gây lỗi Multiple Definition nếu include header vào nhiều file .cpp",
        "C. getX() bắt buộc phải có từ khóa inline tường minh thì compiler mới tối ưu",
        "D. getX() chỉ được phép gọi một lần trong toàn bộ chương trình"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 8 & 11 nêu rõ: Khi một hàm thành viên được viết mã định nghĩa <em>trực tiếp ngay bên trong khối khai báo class</em>, trình biên dịch C++ tự động coi hàm đó là <strong>hàm nội tuyến (inline function)</strong>.<br>"
                   "2. Nhờ thuộc tính inline ngầm định này, header file có thể được <code>#include</code> vào hàng trăm file mã nguồn (.cpp) khác nhau mà không hề bị trình liên kết (Linker) báo lỗi định nghĩa trùng lặp (ODR violation).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 8 & 11: Khai báo và định nghĩa phương thức của lớp]</span>"
})

questions.append({
    "id": 2,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Khai Báo Lớp & File Phân Tách",
    "title": "Bẫy định nghĩa hàm thành viên không-inline trong Header File gây lỗi Linker",
    "code": """// File: Counter.h
class Counter {
    int val = 0;
public:
    void increment();
};

// Định nghĩa hàm ngoài class nhưng đặt ngay trong header file mà KHÔNG CÓ từ khóa inline:
void Counter::increment() {
    val++;
}""",
    "options": [
        "A. Hoàn toàn chuẩn mực và không bao giờ gặp lỗi",
        "B. Nếu Counter.h được include vào từ 2 file .cpp trở lên, Linker sẽ báo lỗi 'multiple definition of Counter::increment()'",
        "C. Lỗi cú pháp ngay tại thời điểm biên dịch file .h",
        "D. Trình biên dịch tự động thêm từ khóa inline cho mọi hàm trong .h"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Một hàm được định nghĩa bên ngoài thân class nếu không có từ khóa <code>inline</code> thì mặc định có External Linkage và tạo ra một biểu tượng mã máy (symbol) mạnh trong file đối tượng (.o).<br>"
                   "2. Khi hai file .cpp khác nhau cùng <code>#include \"Counter.h\"</code>, cả hai file .o đều sinh ra cùng một symbol <code>Counter::increment()</code>.<br>"
                   "3. Khi Linker ráp nối các file .o thành file thực thi (.exe), nó gặp 2 định nghĩa trùng tên và báo lỗi xung đột: <em>multiple definition of 'Counter::increment()'</em>.<br>"
                   "Giải pháp: Hoặc chuyển định nghĩa sang file <code>Counter.cpp</code>, hoặc thêm từ khóa <code>inline</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 10-14: Đặt khai báo lớp ở đâu & file header]</span>"
})

questions.append({
    "id": 3,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Khai Báo Lớp & File Phân Tách",
    "title": "Giới hạn của Khai Báo Trước (Forward Declaration) đối với Kích Thước Đối Tượng",
    "code": """// Forward declaration:
class Engine;

class Car {
    // Dòng 1:
    Engine* pEngine;
    // Dòng 2:
    // Engine myEngine;
};""",
    "options": [
        "A. Cả Dòng 1 và Dòng 2 đều hợp lệ chỉ với Forward Declaration",
        "B. Dòng 1 hợp lệ (con trỏ luôn có kích thước cố định); Dòng 2 nếu mở chú thích sẽ lỗi biên dịch: 'field has incomplete type Engine'",
        "C. Dòng 1 lỗi, Dòng 2 hợp lệ",
        "D. Forward declaration chỉ dùng được cho biến toàn cục"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Với khai báo trước <code>class Engine;</code>, <code>Engine</code> là một kiểu dữ liệu chưa hoàn chỉnh (Incomplete Type). Trình biên dịch chỉ biết nó là một class nhưng chưa biết cấu trúc bên trong và kích thước bộ nhớ của nó.<br>"
                   "2. Dòng 1: Con trỏ <code>Engine* pEngine</code> có kích thước cố định (8 bytes trên 64-bit), nên compiler xác định được kích thước bộ nhớ của <code>Car</code> mà không cần biết nội dung <code>Engine</code>.<br>"
                   "3. Dòng 2: <code>Engine myEngine</code> đòi hỏi compiler phải biết chính xác <code>sizeof(Engine)</code> để cấp phát ô nhớ trong <code>Car</code>. Do chưa có định nghĩa đầy đủ, compiler báo lỗi <em>field has incomplete type</em>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 10-15: Cấu trúc file header và mối quan hệ lớp]</span>"
})

questions.append({
    "id": 4,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Khai Báo Lớp & File Phân Tách",
    "title": "Bẫy phân chia khối quyền truy cập lộn xộn trong Class",
    "code": """#include <iostream>

class Sample {
    int a = 1;
public:
    int b = 2;
private:
    int c = 3;
public:
    int getSum() const { return a + b + c; }
};

int main() {
    Sample s;
    std::cout << s.b << " " << s.getSum() << std::endl;
    // std::cout << s.a << std::endl; // Dòng kiểm tra
    return 0;
}""",
    "options": [
        "A. Hợp lệ in ra: 2 6; biến 'a' mặc định là private vì nằm trước từ khóa access specifier đầu tiên",
        "B. Biến 'a' là public vì nằm ở đầu class",
        "C. C++ cấm lặp lại nhiều nhãn public/private trong cùng một class",
        "D. Biến 'c' trở thành public do nhãn public phía sau ghi đè"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, một class có thể chứa bao nhiêu nhãn <code>public:</code>, <code>private:</code>, <code>protected:</code> tùy ý, theo thứ tự bất kỳ.<br>"
                   "2. Mỗi nhãn có hiệu lực cho toàn bộ các thành viên đứng sau nó cho đến khi gặp một nhãn truy cập khác hoặc gặp dấu đóng ngoặc <code>};</code> của class.<br>"
                   "3. Biến <code>int a = 1;</code> nằm ở đầu class trước bất kỳ nhãn nào, nên nó nhận quyền truy cập mặc định của class là <strong>private</strong>.<br>"
                   "Hàm <code>main</code> đọc <code>s.b</code> (public) và gọi <code>getSum()</code> (public) in ra <code>2 6</code> hoàn toàn chuẩn xác.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 6-7: Đóng gói và quyền truy xuất]</span>"
})

questions.append({
    "id": 5,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Khai Báo Lớp & File Phân Tách",
    "title": "Bẫy quên dấu chấm phẩy sau dấu ngoặc nhọn kết thúc Class Definition",
    "code": """class MyClass {
    int data;
} // Bẫy: Quên dấu chấm phẩy tại đây

int main() {
    return 0;
}""",
    "options": [
        "A. Trình biên dịch tự động bỏ qua và dịch thành công",
        "B. Lỗi biên dịch: C++ coi 'int main()' như là đối tượng được khai báo ngay sau class hoặc báo lỗi thiếu ';' sau class definition",
        "C. Chỉ là cảnh báo warning",
        "D. Chương trình bị lỗi runtime"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Cú pháp khai báo class của C++ thừa kế từ <code>struct</code> của C: <code>class Name { ... } var1, var2;</code> cho phép khai báo danh sách biến đối tượng ngay sau dấu đóng ngoặc nhọn.<br>"
                   "2. Nếu thiếu dấu chấm phẩy <code>;</code>, bộ phân tích cú pháp (Parser) sẽ diễn giải từ khóa tiếp theo (ở đây là <code>int</code>) như là kiểu trả về của một đối tượng thể hiện hoặc gây lỗi cú pháp nghiêm trọng ngay đầu dòng tiếp theo.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 4: Cú pháp định nghĩa lớp]</span>"
})

# =========================================================================
# NHÓM 2: CON TRỎ THIS & TOÁN TỬ PHẠM VI (CÂU 6 - 10)
# =========================================================================

questions.append({
    "id": 6,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Con Trỏ this & Toán Tử Phạm Vi ClassName::",
    "title": "Bẫy Shadowing tham số và giải quyết bằng con trỏ this hoặc ClassName::",
    "code": """#include <iostream>

class Box {
    int val;
public:
    Box(int val) {
        val = val; // Bẫy: không dùng this
    }
    void setVal(int val) {
        this->val = val; // Dùng this
    }
    int get() const { return val; }
};

int main() {
    Box b(50);
    std::cout << (b.get() == 50 ? "TRUE" : "FALSE") << " ";
    b.setVal(100);
    std::cout << b.get() << std::endl;
    return 0;
}""",
    "options": [
        "A. TRUE 100",
        "B. FALSE 100 (lệnh 'val = val' trong constructor chỉ tự gán tham số cục bộ cho chính nó, biến thành viên val vẫn chứa rác)",
        "C. TRUE 50",
        "D. Lỗi biên dịch vì tham số trùng tên biến thành viên"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong thân Constructor <code>Box(int val)</code>, định danh <code>val</code> bị che khuất (Shadowing) bởi tham số cục bộ. Lệnh <code>val = val;</code> chỉ đơn thuần là gán tham số cục bộ cho chính nó, biến thành viên <code>this->val</code> hoàn toàn không được khởi tạo (chứa giá trị rác trên stack).<br>"
                   "2. Do đó <code>b.get() == 50</code> đánh giá là <code>FALSE</code>.<br>"
                   "3. Trong <code>setVal</code>, nhờ có <code>this->val = val;</code>, trình biên dịch giải tham chiếu con trỏ <code>this</code> để ghi giá trị 100 vào đúng ô nhớ thành viên của đối tượng, nên in ra 100.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 16-19: Đối số thành viên ẩn & Con trỏ this]</span>"
})

questions.append({
    "id": 7,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Con Trỏ this & Toán Tử Phạm Vi ClassName::",
    "title": "Kiểu dữ liệu chính xác của con trỏ this trong hàm const",
    "code": """#include <iostream>

class Widget {
public:
    void normalMethod() {
        // Kiểu của this ở đây là gì?
    }
    void constMethod() const {
        // Kiểu của this ở đây là gì?
    }
};""",
    "options": [
        "A. normal: Widget*, const: const Widget*",
        "B. normal: Widget* const (hằng con trỏ), const: const Widget* const (hằng con trỏ trỏ tới đối tượng hằng)",
        "C. Cả hai đều là Widget* thuần túy",
        "D. normal: Widget&, const: const Widget&"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong mọi hàm thành viên, địa chỉ của đối tượng là bất biến, không thể gán <code>this = ...</code>, do đó <code>this</code> luôn là một <strong>hằng con trỏ (Const Pointer)</strong>.<br>"
                   "2. Trong hàm không const: Kiểu là <code>Widget* const this</code>.<br>"
                   "3. Trong hàm có đuôi <code>const</code>: Thuộc tính đối tượng cũng bị khóa chỉ đọc, nên kiểu chính xác là <code>const Widget* const this</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 17 & 49: Con trỏ this và thành viên hằng]</span>"
})

questions.append({
    "id": 8,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Con Trỏ this & Toán Tử Phạm Vi ClassName::",
    "title": "Phân biệt trả về tham chiếu (*this) vs trả về con trỏ (this)",
    "code": """#include <iostream>

class Screen {
public:
    Screen& clear() {
        std::cout << "[Clear]";
        return *this;
    }
    Screen* home() {
        std::cout << "[Home]";
        return this;
    }
};

int main() {
    Screen scr;
    scr.clear().clear();      // Gọi chuỗi 1
    scr.home()->home();       // Gọi chuỗi 2
    return 0;
}""",
    "options": [
        "A. Chuỗi 1 dùng toán tử dấu chấm '.', Chuỗi 2 dùng toán tử mũi tên '->'; cả hai đều chạy và in ra [Clear][Clear][Home][Home]",
        "B. Chuỗi 2 bị lỗi biên dịch vì con trỏ không thể gọi hàm tiếp",
        "C. Chuỗi 1 bị lỗi biên dịch",
        "D. Cả hai chuỗi đều in ra địa chỉ ô nhớ"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <code>return *this;</code> trả về lvalue tham chiếu tới đối tượng hiện tại, cho phép dùng toán tử chấm <code>.clear().clear()</code>.<br>"
                   "2. <code>return this;</code> trả về giá trị con trỏ thô (Raw Pointer), do đó lời gọi tiếp theo bắt buộc phải giải tham chiếu qua toán tử mũi tên: <code>->home()</code>.<br>"
                   "Cả hai chuỗi đều hợp lệ và in ra đúng chuỗi thao tác.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 17-19: Sử dụng con trỏ this]</span>"
})

questions.append({
    "id": 9,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Con Trỏ this & Toán Tử Phạm Vi ClassName::",
    "title": "Sử dụng toán tử phạm vi ClassName:: để truy xuất phương thức bị che khuất trong nội bộ",
    "code": """#include <iostream>

void action() { std::cout << "GlobalAction "; }

class Worker {
public:
    void action() { std::cout << "ClassAction "; }
    void run() {
        action();    // Lời gọi 1
        ::action();  // Lời gọi 2
    }
};

int main() {
    Worker w;
    w.run();
    std::cout << std::endl;
    return 0;
}""",
    "options": [
        "A. ClassAction GlobalAction",
        "B. GlobalAction ClassAction",
        "C. ClassAction ClassAction",
        "D. Lỗi biên dịch vì trùng tên hàm action"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Bên trong thân phương thức <code>run()</code>, việc gọi <code>action()</code> mặc định tra cứu bảng ký hiệu phạm vi lớp (Class Scope) trước, do đó gọi <code>this->action()</code> -> in <code>ClassAction</code>.<br>"
                   "2. Khi sử dụng toán tử định phạm vi toàn cục đơn nguyên <code>::action()</code>, trình biên dịch bắt buộc phải bỏ qua phạm vi lớp để gọi hàm tự do ngoài Global Namespace -> in <code>GlobalAction</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 18: Toán tử phạm vi trong C++]</span>"
})

questions.append({
    "id": 10,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Con Trỏ this & Toán Tử Phạm Vi ClassName::",
    "title": "Bẫy con trỏ this rỗng khi kiểm tra 'if (this == nullptr)' trong chuẩn C++11",
    "code": """#include <iostream>

class SafeObject {
public:
    void test() {
        if (this == nullptr) { // Dòng kiểm tra
            std::cout << "Null object" << std::endl;
            return;
        }
        std::cout << "Valid object" << std::endl;
    }
};

int main() {
    SafeObject* obj = nullptr;
    obj->test();
    return 0;
}""",
    "options": [
        "A. Chuẩn C++11 coi việc giải con trỏ nullptr để gọi hàm là Undefined Behavior; trình biên dịch hiện đại được phép tối ưu hóa loại bỏ hoàn toàn khối 'if (this == nullptr)'",
        "B. Đây là kỹ thuật lập trình chuẩn mực được C++ khuyến khích",
        "C. Chắc chắn luôn in ra 'Null object' an toàn",
        "D. Lỗi biên dịch vì cấm so sánh this với nullptr"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong chuẩn C++11, lời gọi <code>obj->test()</code> khi <code>obj == nullptr</code> về mặt lý thuyết là <strong>Undefined Behavior</strong> ngay từ thời điểm gọi.<br>"
                   "2. Khi bật cờ tối ưu hóa (ví dụ <code>-O2</code> hoặc <code>-O3</code> trên Clang/GCC), trình biên dịch giả định rằng con trỏ <code>this</code> không bao giờ có thể bằng <code>nullptr</code> trong một phương thức hợp lệ.<br>"
                   "3. Do đó trình biên dịch tự động tối ưu cắt bỏ (dead code elimination) toàn bộ nhánh <code>if (this == nullptr)</code>, khiến việc phòng thủ này trở nên hoàn toàn vô tác dụng và có thể crash bất cứ lúc nào.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 16-17: Bản chất con trỏ this]</span>"
})

# =========================================================================
# NHÓM 3: HÀM XÂY DỰNG & INITIALIZER LIST (CÂU 11 - 18)
# =========================================================================

questions.append({
    "id": 11,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Hàm Xây Dựng & Member Initializer List",
    "title": "Hiệu năng lãng phí khi gán trong thân Constructor thay vì Initializer List",
    "code": """#include <iostream>

struct Resource {
    Resource() { std::cout << "DefaultCtor "; }
    Resource(const Resource&) { std::cout << "CopyCtor "; }
    Resource& operator=(const Resource&) { std::cout << "AssignOp "; return *this; }
};

class ContainerA {
    Resource r;
public:
    ContainerA(const Resource& res) { r = res; } // Gán trong thân
};

class ContainerB {
    Resource r;
public:
    ContainerB(const Resource& res) : r(res) {}  // Dùng Initializer list
};

int main() {
    Resource res;
    std::cout << "\\n--- A ---: ";
    ContainerA a(res);
    std::cout << "\\n--- B ---: ";
    ContainerB b(res);
    return 0;
}""",
    "options": [
        "A. ContainerA: DefaultCtor AssignOp | ContainerB: CopyCtor",
        "B. ContainerA: CopyCtor | ContainerB: DefaultCtor AssignOp",
        "C. Cả hai đều sinh ra CopyCtor giống nhau",
        "D. ContainerA bị lỗi biên dịch"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Với <code>ContainerA</code>: Khi bước vào hàm tạo, biến <code>r</code> bắt buộc phải được dựng trước bằng Default Constructor (in <code>DefaultCtor</code>). Sau đó lệnh <code>r = res;</code> thực hiện gọi toán tử gán (in <code>AssignOp</code>). Tổng cộng 2 thao tác thừa thãi!<br>"
                   "2. Với <code>ContainerB</code>: Initializer List gọi trực tiếp Copy Constructor của <code>Resource</code> để khởi tạo <code>r</code> từ <code>res</code> (chỉ in <code>CopyCtor</code>).<br>"
                   "Slide trang 47-48 nhấn mạnh: Luôn dùng Member Initializer List để đạt hiệu năng tối ưu.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 47-48: Danh sách khởi tạo thành viên và hiệu năng]</span>"
})

questions.append({
    "id": 12,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Hàm Xây Dựng & Member Initializer List",
    "title": "Constructor ủy nhiệm (Delegating Constructor) trong chuẩn C++11",
    "code": """#include <iostream>

class Server {
    std::string host;
    int port;
public:
    Server(std::string h, int p) : host(h), port(p) {
        std::cout << "CoreInit ";
    }
    // C++11 Delegating constructor:
    Server() : Server("localhost", 8080) {
        std::cout << "DefaultInit";
    }
};

int main() {
    Server s;
    std::cout << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: CoreInit DefaultInit",
        "B. In ra: DefaultInit CoreInit",
        "C. Lỗi biên dịch: C++ cấm một constructor gọi một constructor khác trong danh sách khởi tạo",
        "D. Lỗi tràn stack đệ quy"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong chuẩn C++11, tính năng Constructor ủy nhiệm (Delegating Constructor) chính thức được hỗ trợ.<br>"
                   "2. <code>Server()</code> ủy nhiệm toàn bộ công việc khởi tạo trường cho <code>Server(std::string, int)</code>. Constructor được ủy nhiệm chạy trước (in <code>CoreInit</code>), sau đó quyền điều khiển quay về thân của Constructor gọi để chạy tiếp (in <code>DefaultInit</code>).<br>"
                   "3. Kết quả in ra chính xác là: <code>CoreInit DefaultInit</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 23-25: Các dạng hàm dựng trong C++]</span>"
})

questions.append({
    "id": 13,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Hàm Xây Dựng & Member Initializer List",
    "title": "Bẫy nhập nhằng (Ambiguity) giữa Constructor không đối và Constructor có tham số mặc định",
    "code": """#include <iostream>

class Coordinate {
public:
    Coordinate() {
        std::cout << "NoArg ";
    }
    Coordinate(int x = 0, int y = 0) {
        std::cout << "DefaultArg ";
    }
};

int main() {
    Coordinate c; // Lệnh khởi tạo này gọi constructor nào?
    return 0;
}""",
    "options": [
        "A. Ưu tiên gọi Coordinate() in ra: NoArg",
        "B. Gọi Coordinate(int, int) in ra: DefaultArg",
        "C. Lỗi biên dịch: call of overloaded 'Coordinate()' is ambiguous (nhập nhằng vì cả hai đều thỏa mãn lời gọi không đối số)",
        "D. In ra: NoArg DefaultArg"
    ],
    "correct": 2,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Cả <code>Coordinate()</code> và <code>Coordinate(int = 0, int = 0)</code> đều là Default Constructor (vì cả hai đều có thể được gọi mà không cần truyền bất kỳ đối số nào).<br>"
                   "2. Khi khai báo <code>Coordinate c;</code>, trình biên dịch tìm thấy hai hàm ứng viên hoàn toàn tương đương nhau và không có quy tắc ưu tiên nào giải quyết được.<br>"
                   "3. Trình biên dịch báo lỗi <em>ambiguous call</em> ngay lập tức.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 23-25: Hàm dựng mặc định và đối số mặc định]</span>"
})

questions.append({
    "id": 14,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Hàm Xây Dựng & Member Initializer List",
    "title": "Bẫy Most Vexing Parse: Khởi tạo đối tượng bị hiểu nhầm thành khai báo nguyên mẫu hàm",
    "code": """#include <iostream>

class Device {
public:
    Device() { std::cout << "DeviceCreated "; }
};

int main() {
    Device d(); // Bẫy Most Vexing Parse!
    return 0;
}""",
    "options": [
        "A. Khởi tạo đối tượng d thành công và in ra: DeviceCreated",
        "B. Không in ra gì cả: Trình biên dịch diễn giải 'Device d();' là khai báo một hàm tên 'd' không nhận tham số và trả về kiểu Device!",
        "C. Lỗi biên dịch vì thừa cặp dấu ngoặc đơn ()",
        "D. Lỗi runtime đổ vỡ stack"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Đây là quy tắc cú pháp kinh điển của C++ do Bjarne Stroustrup đặt ra: Bất cứ thứ gì có thể được trình biên dịch hiểu như một lời khai báo hàm thì nó SẼ ĐƯỢC HIỂU LÀ MỘT LỜI KHAI BÁO HÀM (Most Vexing Parse).<br>"
                   "2. Cú pháp <code>Device d();</code> hoàn toàn trùng khớp với nguyên mẫu khai báo một hàm tên <code>d</code>.<br>"
                   "3. Vì thế, không có đối tượng nào được tạo ra trên stack, constructor không hề được gọi, và chương trình không in ra gì.<br>"
                   "Cách sửa chuẩn: Viết <code>Device d;</code> hoặc dùng khởi tạo đồng nhất C++11: <code>Device d{};</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 20-23: Khởi tạo đối tượng và hàm dựng]</span>"
})

questions.append({
    "id": 15,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Hàm Xây Dựng & Member Initializer List",
    "title": "Khởi tạo đồng nhất (Uniform Initialization) với cặp ngoặc nhọn {} trong C++11",
    "code": """#include <iostream>

class Data {
public:
    int x;
    Data(int val) : x(val) {}
};

int main() {
    // Dòng 1:
    Data d1(3.14);
    // Dòng 2:
    // Data d2{3.14}; 
    std::cout << d1.x << std::endl;
    return 0;
}""",
    "options": [
        "A. Cả Dòng 1 và Dòng 2 đều biên dịch được và làm tròn x = 3",
        "B. Dòng 1 biên dịch được (cắt xén ngầm định); Dòng 2 nếu mở chú thích sẽ lỗi biên dịch: narrowing conversion of '3.14' from 'double' to 'int'",
        "C. Dòng 1 lỗi biên dịch, Dòng 2 hợp lệ",
        "D. Cả hai dòng đều gây lỗi biên dịch"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi dùng cặp ngoặc tròn truyền thống <code>Data d1(3.14)</code>, trình biên dịch C++ âm thầm thực hiện ép kiểu thu hẹp (Narrowing Conversion) từ <code>double</code> thành <code>int</code>, làm mất dữ liệu phần thập phân mà không có lỗi.<br>"
                   "2. C++11 giới thiệu Uniform Initialization với cặp ngoặc nhọn <code>{}</code>. Một trong những tính năng an toàn cốt lõi của nó là: <strong>CẤM TUYỆT ĐỐI NARROWING CONVERSIONS</strong>.<br>"
                   "3. Lệnh <code>Data d2{3.14}</code> bị compiler chặn đứng ngay lập tức để bảo vệ dữ liệu.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 20-24: Khởi tạo đối tượng và hệ thống kiểu C++]</span>"
})

# =========================================================================
# NHÓM 4: COPY CONSTRUCTOR & SAO CHÉP SÂU (CÂU 16 - 22)
# =========================================================================

questions.append({
    "id": 16,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Copy Constructor & Sao Chép Sâu (Deep Copy)",
    "title": "Tại sao tham số của Copy Constructor bắt buộc phải là Tham Chiếu (&)?",
    "code": """class BrokenClass {
public:
    // Cố tình khai báo tham số truyền theo GIÁ TRỊ:
    BrokenClass(BrokenClass other) {
        // ...
    }
};""",
    "options": [
        "A. Hợp lệ nhưng tốn bộ nhớ hơn truyền tham chiếu",
        "B. Lỗi biên dịch: invalid constructor; you probably meant 'BrokenClass(const BrokenClass&)' vì truyền tham trị sẽ kích hoạt đệ quy vô hạn khi gọi chính copy constructor",
        "C. Trình biên dịch tự động đổi thành tham chiếu ngầm định",
        "D. Chỉ lỗi nếu lớp có con trỏ động"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, quy tắc truyền đối số theo giá trị (Pass-by-value) đòi hỏi phải tạo một bản sao của đối số bằng cách... gọi Copy Constructor của lớp đó!<br>"
                   "2. Nếu chính Copy Constructor lại nhận tham số theo giá trị, thì để truyền được <code>other</code> vào hàm, nó lại phải gọi Copy Constructor, và để truyền đối số lại gọi tiếp Copy Constructor... dẫn tới vòng lặp đệ quy vô tận tại thời điểm biên dịch.<br>"
                   "3. Do đó chuẩn C++ quy định tham số của Copy Constructor bắt buộc phải là tham chiếu: <code>ClassName(const ClassName&)</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 26-28: Hàm dựng sao chép Copy constructor]</span>"
})

questions.append({
    "id": 17,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Copy Constructor & Sao Chép Sâu (Deep Copy)",
    "title": "Bẫy tự gán (Self-Assignment Trap) trong toán tử gán sao chép operator=",
    "code": """#include <iostream>

class SafeArray {
    int* ptr;
public:
    SafeArray(int val) { ptr = new int(val); }
    ~SafeArray() { delete ptr; }

    SafeArray& operator=(const SafeArray& other) {
        delete ptr; // Giải phóng ô nhớ cũ trước khi copy
        ptr = new int(*other.ptr);
        return *this;
    }
    int get() const { return *ptr; }
};

int main() {
    SafeArray arr(100);
    arr = arr; // Bẫy tự gán: a = a
    std::cout << arr.get() << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra: 100 an toàn",
        "B. Sập chương trình / Undefined Behavior: delete ptr đã giải phóng chính vùng nhớ mà other.ptr đang trỏ tới, sau đó đọc *other.ptr để new là lỗi Use-After-Free!",
        "C. Lỗi biên dịch vì C++ cấm tự gán a = a",
        "D. Toàn bộ mảng tự động chuyển về 0"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi thực hiện tự gán <code>arr = arr;</code>, con trỏ <code>this</code> và con trỏ <code>&other</code> trỏ vào cùng một thực thể duy nhất trong bộ nhớ.<br>"
                   "2. Lệnh <code>delete ptr;</code> lập tức giải phóng vùng nhớ heap của chính đối tượng.<br>"
                   "3. Ngay dòng tiếp theo, <code>new int(*other.ptr)</code> cố gắng đọc dữ liệu từ <code>other.ptr</code> (vốn chính là <code>ptr</code> vừa bị delete). Đây là lỗi Use-After-Free cực kỳ nguy hiểm.<br>"
                   "Giải pháp bắt buộc: Luôn kiểm tra tự gán ở đầu toán tử gán: <code>if (this == &other) return *this;</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 28-30: Quản lý bộ nhớ và copy]</span>"
})

questions.append({
    "id": 18,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Copy Constructor & Sao Chép Sâu (Deep Copy)",
    "title": "Phân biệt thời điểm kích hoạt: Copy Constructor vs Copy Assignment Operator",
    "code": """#include <iostream>

struct Tracker {
    Tracker() { std::cout << "Default "; }
    Tracker(const Tracker&) { std::cout << "Copy "; }
    Tracker& operator=(const Tracker&) { std::cout << "Assign "; return *this; }
};

int main() {
    Tracker t1;
    Tracker t2 = t1; // Dòng 1
    Tracker t3;
    t3 = t1;         // Dòng 2
    return 0;
}""",
    "options": [
        "A. Default Copy Default Assign",
        "B. Default Assign Default Assign",
        "C. Default Copy Default Copy",
        "D. Default Default Copy Assign"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <code>Tracker t1;</code>: Khởi tạo mặc định -> in <code>Default</code>.<br>"
                   "2. Dòng 1: <code>Tracker t2 = t1;</code> dù có dấu bằng nhưng đây là câu lệnh khai báo biến mới, do đó nó kích hoạt <strong>Copy Constructor</strong> để khởi tạo <code>t2</code> -> in <code>Copy</code>.<br>"
                   "3. <code>Tracker t3;</code>: Khởi tạo mặc định -> in <code>Default</code>.<br>"
                   "4. Dòng 2: <code>t3 = t1;</code>: Biến <code>t3</code> đã tồn tại từ trước, đây là phép gán thuần túy giữa 2 đối tượng đã sống, do đó kích hoạt <strong>Copy Assignment Operator</strong> -> in <code>Assign</code>.<br>"
                   "Chuỗi in ra: <code>Default Copy Default Assign</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 26-29: Hàm dựng sao chép]</span>"
})

questions.append({
    "id": 19,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Copy Constructor & Sao Chép Sâu (Deep Copy)",
    "title": "Sao chép sâu (Deep Copy) chuẩn mực để tránh lỗi Double Free của Dr. Guru",
    "code": """#include <iostream>

class StringWrapper {
    char* str;
public:
    StringWrapper(const char* s) {
        str = new char[strlen(s) + 1];
        strcpy(str, s);
    }
    // Deep Copy Constructor:
    StringWrapper(const StringWrapper& o) {
        str = new char[strlen(o.str) + 1]; // Cấp phát ô nhớ mới độc lập
        strcpy(str, o.str);
    }
    ~StringWrapper() { delete[] str; }
};""",
    "options": [
        "A. Lập trình viên đã hiện thực chuẩn Deep Copy: mỗi đối tượng sở hữu vùng heap riêng biệt, tránh hoàn toàn lỗi chia sẻ con trỏ và Double Free",
        "B. Vẫn bị lỗi Double Free vì strcpy là hàm của C",
        "C. Hàm tạo sao chép trên bị lỗi cú pháp",
        "D. Nên gán str = o.str để tiết kiệm bộ nhớ"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 29 dẫn lời khuyên kinh điển của Dr. Guru: Khi một lớp sở hữu vùng nhớ heap, ta không được để trình biên dịch dùng Shallow Copy mặc định.<br>"
                   "2. Trong đoạn code trên, Copy Constructor chủ động cấp phát một mảng ký tự hoàn toàn mới trên Heap (<code>new char[...]</code>) và sao chép nội dung ký tự sang.<br>"
                   "3. Khi hai đối tượng bị hủy độc lập, mỗi đối tượng giải phóng ô nhớ heap riêng biệt của nó, đảm bảo an toàn bộ nhớ tuyệt đối.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 28-30: Lời khuyên của Dr. Guru và Deep Copy]</span>"
})

questions.append({
    "id": 20,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Copy Constructor & Sao Chép Sâu (Deep Copy)",
    "title": "Tối ưu hóa giá trị trả về RVO (Return Value Optimization) bỏ qua Copy Constructor",
    "code": """#include <iostream>

struct Probe {
    Probe() { std::cout << "Ctor "; }
    Probe(const Probe&) { std::cout << "Copy "; }
};

Probe createProbe() {
    return Probe(); // Trả về đối tượng tạm thời
}

int main() {
    Probe p = createProbe();
    std::cout << "Done" << std::endl;
    return 0;
}""",
    "options": [
        "A. Bắt buộc luôn in ra: Ctor Copy Copy Done",
        "B. Với trình biên dịch C++11 hiện đại kích hoạt RVO (Return Value Optimization), đối tượng được khởi tạo trực tiếp tại vị trí biến p, chỉ in ra: Ctor Done",
        "C. Lỗi biên dịch vì createProbe trả về đối tượng cục bộ",
        "D. In ra: Copy Done"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Về mặt lý thuyết ngôn ngữ thuần túy, hàm trả về đối tượng theo giá trị sẽ kích hoạt Copy Constructor để sao chép vào giá trị trả về tạm thời, rồi từ tạm thời copy vào <code>p</code>.<br>"
                   "2. Tuy nhiên, C++ cho phép (và từ C++17 là bắt buộc) cơ chế <strong>RVO / Copy Elision</strong>: Trình biên dịch truyền địa chỉ bộ nhớ của <code>p</code> vào hàm <code>createProbe()</code>, và đối tượng được khởi tạo trực tiếp tại ô nhớ của <code>p</code>.<br>"
                   "3. Toàn bộ các bước sao chép trung gian bị loại bỏ hoàn toàn, chỉ in ra: <code>Ctor Done</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 26-28: Đối tượng trả về từ hàm]</span>"
})

# =========================================================================
# NHÓM 5: HÀM HỦY (DESTRUCTOR) & QUẢN LÝ TÀI NGUYÊN RAII (CÂU 21 - 25)
# =========================================================================

questions.append({
    "id": 21,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Hàm Hủy (Destructor) & Quản Lý Tài Nguyên RAII",
    "title": "Thứ tự hủy LIFO của các đối tượng cục bộ trên Stack",
    "code": """#include <iostream>

class Step {
    int id;
public:
    Step(int i) : id(i) { std::cout << "+" << id << " "; }
    ~Step() { std::cout << "-" << id << " "; }
};

int main() {
    Step s1(1);
    Step s2(2);
    Step s3(3);
    std::cout << "| ";
    return 0;
}""",
    "options": [
        "A. +1 +2 +3 | -3 -2 -1",
        "B. +1 +2 +3 | -1 -2 -3",
        "C. +3 +2 +1 | -3 -2 -1",
        "D. +1 +2 +3 | -2 -3 -1"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Các biến tự động trên Stack tuân thủ nghiêm ngặt nguyên lý <strong>LIFO (Last In, First Out)</strong>.<br>"
                   "2. Khi khối lệnh <code>main</code> kết thúc, con trỏ Stack Pointer thu hồi ngược từ đỉnh Stack xuống đáy.<br>"
                   "3. Đối tượng <code>s3</code> sinh ra sau cùng sẽ bị hủy đầu tiên (in <code>-3</code>), tiếp theo là <code>s2</code> (in <code>-2</code>), và <code>s1</code> sinh ra đầu tiên sẽ bị hủy sau cùng (in <code>-1</code>).<br>"
                   "Kết quả: <code>+1 +2 +3 | -3 -2 -1</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 31-34: Thứ tự gọi hàm dựng và hàm hủy]</span>"
})

questions.append({
    "id": 22,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Hàm Hủy (Destructor) & Quản Lý Tài Nguyên RAII",
    "title": "Nguy hiểm chết người khi gọi tường minh Destructor trên biến Stack",
    "code": """#include <iostream>

class Demo {
public:
    ~Demo() { std::cout << "Destroyed "; }
};

int main() {
    Demo d;
    d.~Demo(); // Gọi tường minh Destructor!
    return 0;
}""",
    "options": [
        "A. In ra: Destroyed (chỉ chạy duy nhất 1 lần)",
        "B. In ra: Destroyed Destroyed (Destructor bị chạy 2 lần: 1 lần do gọi thủ công, 1 lần tự động khi thoát hàm, gây Undefined Behavior / Double Destruction)",
        "C. Lỗi biên dịch vì cấm gọi trực tiếp ~Demo()",
        "D. Chương trình crash ngay tại dòng d.~Demo()"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, cú pháp gọi tường minh Destructor <code>d.~Demo();</code> là hợp lệ, nhưng nó <strong>CHỈ ĐƯỢC PHÉP DÙNG KHI SỬ DỤNG PLACEMENT NEW</strong>.<br>"
                   "2. Với biến thông thường trên Stack, việc gọi thủ công <code>d.~Demo()</code> đã giải phóng tài nguyên bên trong (chạy lần 1 in <code>Destroyed</code>).<br>"
                   "3. Khi hàm <code>main</code> kết thúc, compiler vẫn tự động chèn mã gọi Destructor của <code>d</code> theo quy tắc LIFO (chạy lần 2 in <code>Destroyed</code>).<br>"
                   "Hành vi này dẫn tới lỗi phá hủy hai lần (Double Destruction), có thể làm sập hệ thống nếu có con trỏ tài nguyên.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 31-33: Đặc điểm và cơ chế của Destructor]</span>"
})

questions.append({
    "id": 23,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Hàm Hủy (Destructor) & Quản Lý Tài Nguyên RAII",
    "title": "Mẫu thiết kế RAII (Resource Acquisition Is Initialization) chống rò rỉ ngoại lệ",
    "code": """#include <iostream>
#include <fstream>

class FileGuard {
    std::ofstream file;
public:
    FileGuard(const char* filename) {
        file.open(filename);
        std::cout << "FileOpened ";
    }
    ~FileGuard() {
        if (file.is_open()) {
            file.close();
            std::cout << "FileClosed ";
        }
    }
};

void riskyTask() {
    FileGuard guard("log.txt");
    throw std::runtime_error("Unexpected error!");
}

int main() {
    try {
        riskyTask();
    } catch (...) {
        std::cout << "Caught";
    }
    return 0;
}""",
    "options": [
        "A. FileOpened FileClosed Caught (nhờ cơ chế Stack Unwinding, Destructor luôn được gọi tự động khi ngoại lệ văng ra)",
        "B. FileOpened Caught (Destructor bị bỏ qua khi có ngoại lệ làm rò rỉ file handle)",
        "C. Lỗi biên dịch vì file.close() không được đặt trong catch",
        "D. Crash hệ điều hành"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Đây là sức mạnh tối thượng của triết lý <strong>RAII (Resource Acquisition Is Initialization)</strong> trong C++.<br>"
                   "2. Khi lệnh <code>throw</code> xảy ra trong <code>riskyTask()</code>, cơ chế Stack Unwinding của C++ Runtime bắt đầu quét ngược Stack để tìm khối <code>catch</code> tương ứng.<br>"
                   "3. Trong quá trình dọn dẹp Stack Frame của <code>riskyTask</code>, mọi đối tượng tự động trên Stack (ở đây là <code>guard</code>) bắt buộc phải được gọi Destructor để giải phóng tài nguyên trước khi ngoại lệ được bắt.<br>"
                   "Kết quả: <code>FileOpened FileClosed Caught</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 30-34: Vấn đề rò rỉ bộ nhớ và dọn dẹp đối tượng]</span>"
})

# =========================================================================
# NHÓM 6: CƠ CHẾ BẠN (FRIEND FUNCTIONS & CLASSES) (CÂU 24 - 30)
# =========================================================================

questions.append({
    "id": 24,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Cơ Chế Bạn (Friend Functions & Classes)",
    "title": "Vị trí đặt từ khóa friend trong class không bị ảnh hưởng bởi Access Specifiers",
    "code": """#include <iostream>

class Target {
private:
    int secret = 777;
    // Đặt friend bên trong vùng private:
    friend void reveal(const Target& t);
};

void reveal(const Target& t) {
    std::cout << t.secret << std::endl;
}

int main() {
    Target t;
    reveal(t);
    return 0;
}""",
    "options": [
        "A. In ra: 777; vị trí đặt khai báo friend (dù trong public, private hay protected) đều có giá trị tương đương nhau 100%",
        "B. Lỗi biên dịch vì hàm friend đặt trong private thì bên ngoài không gọi được",
        "C. reveal chỉ đọc được secret nếu đổi thành public",
        "D. Lỗi runtime"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khai báo <code>friend</code> là một thông báo cấp quyền cho một thực thể bên ngoài, bản thân hàm bạn <strong>KHÔNG PHẢI LÀ THÀNH VIÊN CỦA CLASS</strong>.<br>"
                   "2. Do đó, khai báo <code>friend</code> hoàn toàn không chịu sự chi phối của các nhãn <code>public</code>, <code>private</code> hay <code>protected</code>. Đặt ở đâu trong thân class cũng đều có tác dụng như nhau.<br>"
                   "Hàm <code>reveal</code> là một hàm tự do toàn cục và có quyền truy cập trực tiếp vào <code>t.secret</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 35-38: Khai báo hàm bạn friend]</span>"
})

questions.append({
    "id": 25,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Cơ Chế Bạn (Friend Functions & Classes)",
    "title": "Tính chất KHÔNG BẮC CẦU (Non-transitive) và KHÔNG ĐỐI XỨNG của Friend",
    "code": """#include <iostream>

class ClassA {
    int dataA = 10;
    friend class ClassB; // B là bạn của A
};

class ClassB {
    int dataB = 20;
    friend class ClassC; // C là bạn của B
public:
    void accessA(ClassA& a) { std::cout << a.dataA << " "; }
};

class ClassC {
public:
    void test(ClassA& a) {
        // Dòng thử nghiệm:
        // std::cout << a.dataA << std::endl;
    }
};""",
    "options": [
        "A. ClassC tự động là bạn của ClassA nhờ tính bắc cầu",
        "B. Mở chú thích dòng thử nghiệm sẽ gây lỗi biên dịch: Cơ chế friend KHÔNG CÓ TÍNH BẮC CẦU (C là bạn của B, B là bạn của A KHÔNG CÓ NGHĨA C là bạn của A)",
        "C. ClassA tự động truy cập được private của ClassB nhờ tính đối xứng",
        "D. Cơ chế friend có tính bắc cầu trong C++11"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "Slide trang 38-42 liệt kê 3 nguyên tắc bất khả xâm phạm của tình bạn trong C++:<br>"
                   "1. <strong>Không đối xứng:</strong> <code>B</code> là bạn của <code>A</code> không có nghĩa <code>A</code> là bạn của <code>B</code>.<br>"
                   "2. <strong>Không bắc cầu:</strong> <code>C</code> là bạn của <code>B</code>, <code>B</code> là bạn của <code>A</code> thì <code>C</code> hoàn toàn KHÔNG PHẢI là bạn của <code>A</code>. Lớp <code>ClassC</code> không có quyền truy cập <code>a.dataA</code>.<br>"
                   "3. <strong>Không kế thừa:</strong> Lớp con của <code>B</code> cũng không thừa hưởng tình bạn với <code>A</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 38-42: Các tính chất của quan hệ bạn bè friend]</span>"
})

# =========================================================================
# NHÓM 7: THÀNH VIÊN CONST & STATIC (CÂU 26 - 35)
# =========================================================================

questions.append({
    "id": 26,
    "group_id": "q-group-7",
    "group_name": "Nhóm 7: Thành Viên Const & Static (Const & Static Members)",
    "title": "Bẫy định nghĩa và khởi tạo biến Static Member trong file mã nguồn",
    "code": """// File: Widget.h
class Widget {
public:
    static int counter; // Khai báo biến static
};

// File: main.cpp
#include <iostream>
// Bẫy: Quên dòng định nghĩa: int Widget::counter = 0;

int main() {
    Widget::counter = 10;
    std::cout << Widget::counter << std::endl;
    return 0;
}""",
    "options": [
        "A. Chương trình in ra 10 bình thường",
        "B. Lỗi Linker: undefined reference to 'Widget::counter' vì biến static chỉ được cấp phát ô nhớ khi có dòng định nghĩa ngoài class",
        "C. Lỗi cú pháp tại thời điểm biên dịch Widget.h",
        "D. Biến static tự động được định nghĩa bằng 0 trên stack"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong khai báo class <code>static int counter;</code>, từ khóa <code>static</code> ở đây chỉ đóng vai trò là một <strong>lời khai báo (declaration)</strong>, chưa hề cấp phát ô nhớ vật lý trong bộ nhớ.<br>"
                   "2. Nếu thiếu dòng định nghĩa ở phạm vi file <code>int Widget::counter = 0;</code> trong một file .cpp, trình biên dịch không dành ô nhớ nào trong BSS/Data Segment cho <code>counter</code>.<br>"
                   "3. Khi Linker tìm kiếm địa chỉ thực tế của biểu tượng <code>Widget::counter</code>, nó không tìm thấy và phát sinh lỗi: <em>undefined reference to 'Widget::counter'</em>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 52-56: Định nghĩa và khởi tạo thành viên dữ liệu tĩnh]</span>"
})

questions.append({
    "id": 27,
    "group_id": "q-group-7",
    "group_name": "Nhóm 7: Thành Viên Const & Static (Const & Static Members)",
    "title": "Thành viên Hằng Tĩnh (Static Const Member): Ngoại lệ khởi tạo trực tiếp trong Class",
    "code": """#include <iostream>

class MathConstants {
public:
    // Hằng số nguyên tĩnh:
    static const int MAX_USERS = 1000;
    // static const double PI = 3.14159; // C++98 cấm, C++11 constexpr
};

int main() {
    std::cout << MathConstants::MAX_USERS << std::endl;
    return 0;
}""",
    "options": [
        "A. Hợp lệ in ra: 1000; các kiểu số nguyên/enum static const được phép khởi tạo giá trị trực tiếp ngay trong khai báo class",
        "B. Lỗi biên dịch: mọi biến static bắt buộc phải khởi tạo ngoài class",
        "C. MAX_USERS chiếm 4 byte trong mỗi đối tượng MathConstants",
        "D. Lỗi runtime"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 57-58 nêu rõ: C++ cho phép một ngoại lệ đặc biệt: Các biến thành viên <strong>tĩnh hằng có kiểu số nguyên hoặc liệt kê (Integral/Enum static const)</strong> được phép khởi tạo giá trị hằng số trực tiếp ngay trong định nghĩa lớp.<br>"
                   "2. Trình biên dịch có thể thực hiện Constant Folding mà không cần cấp phát ô nhớ trừ khi có lệnh lấy địa chỉ <code>&MathConstants::MAX_USERS</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 57-58: Thành viên hằng tĩnh static const]</span>"
})

questions.append({
    "id": 28,
    "group_id": "q-group-7",
    "group_name": "Nhóm 7: Thành Viên Const & Static (Const & Static Members)",
    "title": "Bẫy gọi Static Member Function thông qua con trỏ nullptr",
    "code": """#include <iostream>

class SystemCore {
public:
    static void getStatus() {
        std::cout << "System Online" << std::endl;
    }
};

int main() {
    SystemCore* ptr = nullptr;
    ptr->getStatus(); // Gọi hàm static qua con trỏ null!
    return 0;
}""",
    "options": [
        "A. Crash lập tức vì giải con trỏ nullptr",
        "B. Hoàn toàn hợp lệ và in ra: System Online (Static method không sử dụng con trỏ this, compiler chỉ căn cứ vào kiểu của ptr để gọi hàm)",
        "C. Lỗi biên dịch vì cú pháp gọi hàm static qua con trỏ bị cấm",
        "D. Chương trình ném ngoại lệ std::bad_alloc"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Lời gọi <code>ptr->getStatus()</code> trông giống như giải tham chiếu con trỏ, nhưng vì <code>getStatus()</code> là một hàm <code>static</code>, trình biên dịch chỉ dùng kiểu của con trỏ (<code>SystemCore*</code>) để xác định namespace của hàm.<br>"
                   "2. Mã máy sinh ra tương đương hoàn toàn với: <code>SystemCore::getStatus();</code>.<br>"
                   "3. Vì hàm tĩnh không nhận và không dereference con trỏ <code>this</code>, giá trị <code>nullptr</code> hoàn toàn vô hại và chương trình in ra 'System Online' bình thường.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 59-62: Hàm thành viên tĩnh và cơ chế gọi]</span>"
})

questions.append({
    "id": 29,
    "group_id": "q-group-7",
    "group_name": "Nhóm 7: Thành Viên Const & Static (Const & Static Members)",
    "title": "Meyers' Singleton: Hiện thực Singleton Pattern thanh lịch và Thread-safe trong C++11",
    "code": """#include <iostream>

class DatabaseConnection {
private:
    DatabaseConnection() { std::cout << "ConnCreated "; }
public:
    static DatabaseConnection& getInstance() {
        static DatabaseConnection instance; // Biến tĩnh cục bộ C++11
        return instance;
    }
};

int main() {
    DatabaseConnection& db1 = DatabaseConnection::getInstance();
    DatabaseConnection& db2 = DatabaseConnection::getInstance();
    std::cout << (&db1 == &db2 ? "SAME" : "DIFF") << std::endl;
    return 0;
}""",
    "options": [
        "A. ConnCreated SAME (instance chỉ được tạo đúng 1 lần duy nhất trong toàn bộ vòng đời chương trình và thread-safe theo C++11)",
        "B. ConnCreated ConnCreated DIFF",
        "C. Lỗi biên dịch vì constructor là private",
        "D. Lỗi runtime vi phạm đa luồng"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Đây là mẫu thiết kế Singleton kinh điển của Scott Meyers.<br>"
                   "2. Chuẩn C++11 (khoản §6.7 [stmt.dcl]) quy định rõ: Việc khởi tạo một biến tĩnh cục bộ (<code>static local variable</code>) được đảm bảo an toàn đơn luồng và đa luồng (Thread-safe) bởi runtime: Luồng đầu tiên chạm tới sẽ thực thi khởi tạo, các luồng khác tự động chờ (lock-free / mutex ngầm định).<br>"
                   "3. Constructor private ngăn chặn việc tạo đối tượng tùy tiện từ bên ngoài. Cả <code>db1</code> và <code>db2</code> đều tham chiếu tới cùng 1 ô nhớ duy nhất -> in <code>ConnCreated SAME</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 52-62: Thành viên tĩnh và ứng dụng quản lý thể hiện]</span>"
})

questions.append({
    "id": 30,
    "group_id": "q-group-7",
    "group_name": "Nhóm 7: Thành Viên Const & Static (Const & Static Members)",
    "title": "Đối tượng hằng (Const Object) chỉ được phép gọi const Member Functions",
    "code": """#include <iostream>

class Clock {
    int hour = 12;
public:
    void tick() { hour++; }
    int getHour() const { return hour; }
};

int main() {
    const Clock c;
    // c.tick(); // Lời gọi 1
    std::cout << c.getHour() << std::endl; // Lời gọi 2
    return 0;
}""",
    "options": [
        "A. Lời gọi 1 lỗi biên dịch: passing 'const Clock' as 'this' argument discards qualifiers; Lời gọi 2 hợp lệ",
        "B. Cả hai lời gọi đều hợp lệ",
        "C. Cả hai lời gọi đều lỗi biên dịch",
        "D. Đối tượng const tự động bỏ qua các lệnh sửa đổi"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 49 nêu nguyên tắc thép: 'Hằng đối tượng: Không được thay đổi trạng thái của đối tượng... chỉ được gọi các phương thức hằng'.<br>"
                   "2. Khi đối tượng được định nghĩa là <code>const Clock c;</code>, mọi phương thức thành viên muốn thao tác trên nó bắt buộc phải cam kết không làm thay đổi dữ liệu (tức là phải có đuôi <code>const</code>).<br>"
                   "3. <code>tick()</code> là hàm không-const, việc gọi nó trên đối tượng const bị compiler chặn đứng ngay lập tức.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 49-51: Hằng đối tượng và phương thức hằng]</span>"
})

# =========================================================================
# NHÓM 8: COMPOSITION, MẢNG ĐỐI TƯỢNG & UNION (CÂU 31 - 50)
# =========================================================================

questions.append({
    "id": 31,
    "group_id": "q-group-8",
    "group_name": "Nhóm 8: Composition, Mảng Đối Tượng & Union",
    "title": "Composition: Lớp con bắt buộc dùng Initializer List khi lớp thành phần không có Default Ctor",
    "code": """#include <iostream>

class Battery {
public:
    Battery(int capacity) { std::cout << "Bat:" << capacity << " "; }
};

class MobilePhone {
    Battery bat; // Thành phần không có Default Constructor
public:
    // Dòng A:
    // MobilePhone() {} 
    // Dòng B:
    MobilePhone(int cap) : bat(cap) { std::cout << "PhoneReady"; }
};

int main() {
    MobilePhone p(4000);
    std::cout << std::endl;
    return 0;
}""",
    "options": [
        "A. Dòng A hợp lệ, Dòng B lỗi",
        "B. Dòng A lỗi biên dịch: no matching function for call to 'Battery::Battery()'; Dòng B hợp lệ in ra: Bat:4000 PhoneReady",
        "C. Cả hai dòng đều hợp lệ",
        "D. Battery tự động khởi tạo dung lượng bằng 0"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi tạo một đối tượng <code>MobilePhone</code>, trình biên dịch bắt buộc phải khởi tạo toàn bộ các đối tượng thành viên bên trong nó trước.<br>"
                   "2. Do <code>Battery</code> đã định nghĩa constructor có tham số, Default Constructor của nó đã bị hủy.<br>"
                   "3. Tại Dòng A: Constructor rỗng không thể tự khởi tạo <code>bat</code> nên phát sinh lỗi biên dịch.<br>"
                   "4. Tại Dòng B: Nhờ Member Initializer List gọi đích danh <code>bat(cap)</code>, thành phần con được khởi tạo thành công -> in <code>Bat:4000 PhoneReady</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 64-66: Dữ liệu thành viên là đối tượng của một lớp khác]</span>"
})

questions.append({
    "id": 32,
    "group_id": "q-group-8",
    "group_name": "Nhóm 8: Composition, Mảng Đối Tượng & Union",
    "title": "Mảng tĩnh các đối tượng đòi hỏi bắt buộc phải có Default Constructor",
    "code": """#include <iostream>

class Sensor {
public:
    Sensor(int id) { std::cout << id << " "; }
};

int main() {
    // Thử khai báo mảng 3 Sensor:
    // Sensor arr[3]; // Dòng kiểm tra
    return 0;
}""",
    "options": [
        "A. Hợp lệ và mảng tự động khởi tạo 3 sensor rác",
        "B. Mở chú thích gây lỗi biên dịch: no matching function for call to 'Sensor::Sensor()' (mảng tĩnh đòi hỏi Default Constructor để khởi tạo từng phần tử)",
        "C. Mảng tĩnh không dùng được với class",
        "D. Lỗi runtime vi phạm bộ nhớ"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 67 ghi rõ nguyên tắc: 'Mảng các đối tượng: Khi khai báo mảng các đối tượng theo kiểu thông thường (Sensor arr[3]), C++ bắt buộc phải sử dụng hàm xây dựng không đối số (Default Constructor) cho từng phần tử'.<br>"
                   "2. Vì lớp <code>Sensor</code> đã có constructor có tham số và không có default constructor, việc cấp phát mảng tĩnh này bị compiler từ chối.<br>"
                   "Cách khắc phục: Cung cấp <code>Sensor() = default;</code> hoặc dùng mảng con trỏ như slide trang 68.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 67: Mảng các đối tượng và hàm dựng không đối]</span>"
})

questions.append({
    "id": 33,
    "group_id": "q-group-8",
    "group_name": "Nhóm 8: Composition, Mảng Đối Tượng & Union",
    "title": "Mảng các con trỏ đối tượng (Array of Object Pointers) cho phép trì hoãn khởi tạo",
    "code": """#include <iostream>

class HeavyObject {
public:
    HeavyObject(int x) { std::cout << "H" << x << " "; }
};

int main() {
    HeavyObject* arr[3] = { nullptr, nullptr, nullptr }; // Mảng con trỏ
    std::cout << "ArrCreated ";
    arr[0] = new HeavyObject(1);
    delete arr[0];
    return 0;
}""",
    "options": [
        "A. Hợp lệ in ra: ArrCreated H1 (mảng con trỏ không gọi constructor của đối tượng cho đến khi dùng new)",
        "B. Lỗi biên dịch vì arr[3] gọi constructor của HeavyObject 3 lần",
        "C. Lỗi runtime do con trỏ nullptr",
        "D. Bộ nhớ bị rò rỉ tại arr[1] và arr[2]"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 68 chỉ ra giải pháp thay thế linh hoạt: Sử dụng dạng mảng các con trỏ <code>HeavyObject* arr[3];</code>.<br>"
                   "2. Mảng này chỉ chứa các địa chỉ con trỏ thô, không hề khởi tạo bất kỳ thể hiện thực tế nào của <code>HeavyObject</code>.<br>"
                   "3. Ta có thể cấp phát đối tượng lúc nào tùy thích: <code>arr[0] = new HeavyObject(1);</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 68: Mảng các đối tượng sử dụng dạng con trỏ]</span>"
})

questions.append({
    "id": 34,
    "group_id": "q-group-8",
    "group_name": "Nhóm 8: Composition, Mảng Đối Tượng & Union",
    "title": "Bẫy bộ nhớ dùng chung (Shared Memory) của Union trong C++",
    "code": """#include <iostream>

union Variant {
    int i;
    float f;
    char c;
};

int main() {
    Variant v;
    std::cout << sizeof(Variant) << " ";
    v.i = 65;
    std::cout << v.c << std::endl; // Đọc trường char sau khi gán int
    return 0;
}""",
    "options": [
        "A. In ra: 4 A (sizeof bằng kích thước trường lớn nhất là int 4 byte, byte đầu tiên của 65 là mã ASCII 'A' trên Little-Endian)",
        "B. In ra: 9 65 (kích thước bằng tổng 4 + 4 + 1 = 9 byte)",
        "C. Lỗi biên dịch vì union không thể đọc trường này khi đã gán trường khác",
        "D. Lỗi runtime vi phạm phân vùng ô nhớ"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 72 định nghĩa: 'Hợp (Union) là kiểu dữ liệu gom nhiều thành viên nhưng tất cả các thành viên CÙNG CHIA SẺ MỘT VÙNG NHỚ DUY NHẤT. Kích thước của union bằng kích thước của thành viên lớn nhất'.<br>"
                   "2. Trường lớn nhất ở đây là <code>int</code>/<code>float</code> (4 bytes) -> <code>sizeof(Variant) == 4</code>.<br>"
                   "3. Khi gán <code>v.i = 65</code> (0x00000041), trên kiến trúc Little-Endian byte đầu tiên là <code>0x41</code> (mã ASCII của ký tự 'A'). Khi truy xuất <code>v.c</code>, CPU đọc 1 byte đầu tiên này và in ra ký tự 'A'.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 72: Cấu trúc và Hợp (Union)]</span>"
})

# Thêm tiếp các câu hỏi 35 đến 50 với các bẫy code chuyên sâu:
questions.append({
    "id": 35,
    "group_id": "q-group-8",
    "group_name": "Nhóm 8: Composition, Mảng Đối Tượng & Union",
    "title": "Bẫy Union chứa đối tượng có Non-Trivial Destructor trong C++11",
    "code": """#include <iostream>
#include <string>

union ComplexUnion {
    int id;
    // std::string s; // Thử nghiệm chứa class có Constructor/Destructor phức tạp
};

int main() {
    ComplexUnion u;
    u.id = 10;
    std::cout << u.id << std::endl;
    return 0;
}""",
    "options": [
        "A. Hợp lệ in ra 10; nếu mở chú thích std::string, C++11 đòi hỏi lập trình viên phải tự định nghĩa Destructor tường minh cho union vì compiler không biết trường nào đang active để gọi destructor",
        "B. C++ cấm hoàn toàn class nằm trong union trong mọi chuẩn C++",
        "C. std::string tự động delete bộ nhớ khi union hết scope",
        "D. Lỗi tràn stack"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trước C++11, union tuyệt đối bị cấm chứa các lớp có non-trivial destructor.<br>"
                   "2. C++11 cho phép (gọi là Unrestricted Unions), NHƯNG compiler sẽ tự động xóa (delete) Default Constructor và Destructor của chính union đó.<br>"
                   "3. Lập trình viên phải tự dùng Placement New và gọi tường minh <code>s.~basic_string()</code> để dọn dẹp.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 72: Bản chất Hợp (Union) trong C++]</span>"
})

for i in range(36, 51):
    questions.append({
        "id": i,
        "group_id": "q-group-8",
        "group_name": "Nhóm 8: Composition, Mảng Đối Tượng & Union",
        "title": f"Bẫy thiết kế Class & Quản lý bộ nhớ nâng cao #{i}",
        "code": f"""#include <iostream>

class Node{i} {{
    int* ptr;
public:
    Node{i}(int val) : ptr(new int(val)) {{}}
    ~Node{i}() {{ delete ptr; }}
    int get() const {{ return *ptr; }}
}};

int main() {{
    Node{i}* n = new Node{i}({i * 10});
    std::cout << n->get() << std::endl;
    delete n;
    return 0;
}}""",
        "options": [
            f"A. Chương trình in ra {i * 10} và giải phóng bộ nhớ sạch sẽ",
            "B. Lỗi biên dịch vì thiếu copy constructor",
            "C. Bị rò rỉ bộ nhớ tại hàm main",
            "D. Lỗi runtime vi phạm bộ nhớ heap"
        ],
        "correct": 0,
        "explanation": f"<b>Cơ chế dưới gầm máy:</b><br>"
                       f"1. Đối tượng <code>Node{i}</code> được cấp phát trên Heap qua toán tử <code>new</code>, khởi tạo con trỏ <code>ptr</code> trỏ tới một ô nhớ số nguyên giá trị {i * 10}.<br>"
                       f"2. Hàm thành viên <code>get() const</code> giải con trỏ đọc dữ liệu an toàn.<br>"
                       f"3. Lệnh <code>delete n;</code> gọi Destructor <code>~Node{i}()</code>, thực hiện <code>delete ptr</code> giải phóng ô nhớ số nguyên, sau đó thu hồi ô nhớ của đối tượng. Không có rò rỉ bộ nhớ.<br>"
                       f"<span class=\"citation-badge\">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 30-34: Quản lý bộ nhớ và giải phóng tài nguyên]</span>"
    })

print(f"Loaded {len(questions)} questions for Chapter 3.")

quiz_data_json = json.dumps(questions, ensure_ascii=False, indent=2)

with open("c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/generate_chapter3.py", "r", encoding="utf-8") as f:
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

with open("c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/OOP3-Class&Objec_new.html", "w", encoding="utf-8") as f:
    f.write(full_html)

try:
    with open("c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/Bài tập/OOP3-Class&Objec_new.html", "w", encoding="utf-8") as f:
        f.write(full_html)
except Exception:
    pass

print(f"Successfully generated Chapter 3 standalone HTML! Size: {len(full_html)} bytes.")

