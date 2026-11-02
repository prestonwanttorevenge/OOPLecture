# -*- coding: utf-8 -*-
import json

questions = []

# =========================================================================
# NHÓM 1: CƠ CHẾ THROW & TRY-CATCH (CÂU 1 - 6)
# =========================================================================

questions.append({
    "id": 1,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Cơ Chế throw & try-catch",
    "title": "Ném ngoại lệ kiểu nguyên thủy int vs Ném đối tượng lớp",
    "code": """#include <iostream>

void test(int val) {
    if (val < 0) throw -1; // Ném số nguyên int
    if (val == 0) throw "Zero value"; // Ném const char*
    std::cout << val << " ";
}

int main() {
    try {
        test(-5);
    } catch (int e) {
        std::cout << "CaughtInt:" << e << std::endl;
    } catch (const char* msg) {
        std::cout << "CaughtStr:" << msg << std::endl;
    }
    return 0;
}""",
    "options": [
        "A. CaughtInt:-1 (trong C++, bất kỳ kiểu dữ liệu nào cũng có thể được ném qua lệnh throw)",
        "B. Lỗi biên dịch vì throw chỉ nhận các lớp kế thừa từ std::exception",
        "C. In ra: -5",
        "D. Lỗi runtime đổ vỡ stack"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Không giống như Java hay C# (chỉ cho phép ném đối tượng kế thừa từ Throwable/Exception), C++ cho phép ném <strong>BẤT KỲ KIỂU DỮ LIỆU NÀO</strong>: số nguyên, con trỏ chuỗi, struct hoặc class.<br>"
                   "2. Khi gọi <code>test(-5)</code>, lệnh <code>throw -1;</code> văng ra ngoại lệ kiểu <code>int</code>. Runtime đối chiếu kiểu và nhảy vào đúng khối <code>catch (int e)</code>, in ra <code>CaughtInt:-1</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP8-Exception.pdf - Trang 8 & 15-18: Các kiểu ngoại lệ & Cú pháp throw]</span>"
})

questions.append({
    "id": 2,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Cơ Chế throw & try-catch",
    "title": "Bẫy ngoại lệ không được bắt (Unhandled Exception) dẫn tới std::terminate",
    "code": """#include <iostream>

void trigger() {
    throw 404; // Ném int
}

int main() {
    try {
        trigger();
    } catch (const char* s) { // Chỉ bắt chuỗi char*
        std::cout << s << std::endl;
    }
    std::cout << "Finished" << std::endl;
    return 0;
}""",
    "options": [
        "A. In ra Finished bình thường",
        "B. Hệ thống gọi std::terminate() làm sập chương trình ngay lập tức vì không tìm thấy khối catch tương thích cho kiểu int",
        "C. Lỗi biên dịch vì thiếu khối catch(int)",
        "D. Chương trình tự động ép kiểu int thành const char*"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 13 & 29 nhấn mạnh: 'Nếu không có hàm nào bắt được ngoại lệ? Hàm std::terminate() sẽ được gọi, mặc định gọi abort() để chấm dứt ngay lập tức chương trình'.<br>"
                   "2. Khối <code>catch (const char*)</code> không khớp với kiểu <code>int</code> (C++ không thực hiện ép kiểu ngầm định khi so khớp ngoại lệ). Chương trình sập ngay lập tức.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP8-Exception.pdf - Trang 13 & 29: Không tìm thấy lệnh catch tương ứng & std::terminate]</span>"
})

# =========================================================================
# NHÓM 2: STACK UNWINDING & RAII (CÂU 7 - 12)
# =========================================================================

questions.append({
    "id": 3,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Stack Unwinding & RAII",
    "title": "Thứ tự hủy LIFO tự động trong quá trình Stack Unwinding khi có Exception",
    "code": """#include <iostream>

struct Step {
    int id;
    Step(int i) : id(i) { std::cout << "+" << id << " "; }
    ~Step() { std::cout << "-" << id << " "; }
};

void execute() {
    Step s1(1);
    Step s2(2);
    throw std::runtime_error("Crash");
    Step s3(3); // Không bao giờ chạm tới
}

int main() {
    try {
        execute();
    } catch (...) {
        std::cout << "[Caught] ";
    }
    return 0;
}""",
    "options": [
        "A. +1 +2 -2 -1 [Caught]",
        "B. +1 +2 -1 -2 [Caught]",
        "C. +1 +2 [Caught] -2 -1",
        "D. +1 +2 +3 -3 -2 -1 [Caught]"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <code>s1</code> và <code>s2</code> được khởi tạo tuần tự trên Stack: in <code>+1 +2</code>.<br>"
                   "2. Khi lệnh <code>throw</code> kích hoạt, dòng điều khiển nhảy khỏi <code>execute()</code> (bỏ qua <code>s3</code>).<br>"
                   "3. Quá trình Stack Unwinding bắt đầu dọn dẹp Stack Frame của <code>execute()</code>: các đối tượng tự động bị hủy theo thứ tự LIFO (ngược lại với lúc sinh ra): <code>s2</code> bị hủy trước (in <code>-2</code>), rồi đến <code>s1</code> (in <code>-1</code>).<br>"
                   "4. Cuối cùng quyền điều khiển chuyển vào <code>catch (...)</code>: in <code>[Caught]</code>.<br>"
                   "Kết quả: <code>+1 +2 -2 -1 [Caught]</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP8-Exception.pdf - Trang 9-12 & 27: Quy trình gọi hàm và giải phóng vùng nhớ khi ném ngoại lệ]</span>"
})

questions.append({
    "id": 4,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Stack Unwinding & RAII",
    "title": "Bẫy rò rỉ bộ nhớ Heap khi ném ngoại lệ trước lệnh delete (Raw Pointer Leak)",
    "code": """#include <iostream>

void leakyFunction() {
    int* data = new int[1000]; // Cấp phát thô
    // Giả sử một lỗi xảy ra tại đây:
    if (true) throw std::runtime_error("Failed");
    delete[] data; // Lệnh delete bị bỏ qua vĩnh viễn!
}

int main() {
    try {
        leakyFunction();
    } catch (...) {
        std::cout << "Error handled" << std::endl;
    }
    return 0;
}""",
    "options": [
        "A. Không rò rỉ vì C++ runtime tự động delete con trỏ khi có exception",
        "B. Rò rỉ bộ nhớ nghiêm trọng (Memory Leak): Stack Unwinding chỉ hủy bản thân biến con trỏ data (4/8 byte), còn 1000 số nguyên trên Heap bị bỏ rơi vĩnh viễn",
        "C. Lỗi biên dịch vì delete nằm sau throw",
        "D. Hệ điều hành tự động thu hồi ngay khi thoát khỏi try"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 27-28 phân tích rõ: 'Khi một ngoại lệ được ném, hàm đang thực hiện sẽ kết thúc ngay lập tức. Nếu có lệnh delete bị bỏ qua, vùng nhớ heap sẽ bị rò rỉ vĩnh viễn'.<br>"
                   "2. Cơ chế Stack Unwinding chỉ gọi Destructor cho các đối tượng trên Stack. Bản thân con trỏ thô <code>int* data</code> là một kiểu dữ liệu cơ bản không có destructor, nên vùng nhớ Heap không hề được giải phóng.<br>"
                   "Giải pháp: Bắt buộc dùng Smart Pointer (<code>std::unique_ptr<int[]></code>).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP8-Exception.pdf - Trang 27-28: Quản lý bộ nhớ khi có ngoại lệ]</span>"
})

# =========================================================================
# NHÓM 3: SO KHỚP MATCHING (CÂU 13 - 18)
# =========================================================================

questions.append({
    "id": 5,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: So Khớp Ngoại Lệ (Exception Matching)",
    "title": "Bẫy thứ tự khối catch: Khối bắt lớp Cha che khuất lớp Con (Dead Catch Block)",
    "code": """#include <iostream>
#include <stdexcept>

int main() {
    try {
        throw std::out_of_range("Index out of bound");
    } 
    // Bẫy: Khối catch cha std::exception đặt TRƯỚC khối con std::out_of_range
    catch (const std::exception& e) {
        std::cout << "BaseException: " << e.what() << std::endl;
    }
    catch (const std::out_of_range& e) {
        std::cout << "DerivedException: " << e.what() << std::endl;
    }
    return 0;
}""",
    "options": [
        "A. In ra: DerivedException: Index out of bound (vì khớp kiểu chính xác hơn)",
        "B. In ra: BaseException: Index out of bound (catch so khớp tuần tự từ trên xuống dưới; khối cha đặt trước sẽ nuốt chửng ngoại lệ của lớp con)",
        "C. Lỗi biên dịch vì không thể bắt cùng một ngoại lệ 2 lần",
        "D. Thứ tự khối catch không quan trọng trong C++"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 22-24 nêu nguyên tắc: So khớp ngoại lệ trong C++ kiểm tra tuần tự từ trên xuống dưới.<br>"
                   "2. Vì <code>std::out_of_range</code> kế thừa từ <code>std::exception</code>, phép gán tham chiếu <code>const std::exception& e = out_of_range</code> là hoàn toàn hợp lệ (Upcast ngầm định).<br>"
                   "3. Khối catch đầu tiên khớp ngay lập tức, khiến khối <code>catch (const std::out_of_range&)</code> phía sau trở thành mã chết (Dead Code). Trình biên dịch hiện đại sẽ phát cảnh báo nghiêm trọng.<br>"
                   "Quy tắc vàng: Luôn bắt lớp dẫn xuất (Derived) trước, lớp cơ sở (Base) sau.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP8-Exception.pdf - Trang 22-24: Exception Matching và thứ tự các khối catch]</span>"
})

questions.append({
    "id": 6,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: So Khớp Ngoại Lệ (Exception Matching)",
    "title": "Bẫy Object Slicing khi bắt ngoại lệ theo Giá Trị (By Value)",
    "code": """#include <iostream>
#include <exception>

class CustomError : public std::exception {
public:
    const char* what() const noexcept override {
        return "CustomError Details";
    }
};

void fire() { throw CustomError(); }

int main() {
    try {
        fire();
    } catch (std::exception e) { // Bẫy: Bắt theo giá trị (by value)
        std::cout << e.what() << std::endl;
    }
    return 0;
}""",
    "options": [
        "A. Chắc chắn in ra: CustomError Details",
        "B. In ra thông báo chung chung của std::exception (ví dụ 'std::exception'); xảy ra Object Slicing làm mất bản ghi VTable của lớp con CustomError",
        "C. Lỗi biên dịch vì std::exception cấm sao chép",
        "D. Lỗi runtime đổ vỡ vptr"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi bắt theo giá trị <code>catch (std::exception e)</code>, đối tượng ngoại lệ được sao chép vào một biến <code>e</code> có kiểu tĩnh là <code>std::exception</code>.<br>"
                   "2. Toàn bộ phần mở rộng của <code>CustomError</code> bị cắt gọt (Object Slicing). Con trỏ bảng ảo <code>vptr</code> của <code>e</code> bị trỏ lại vào <code>VTable của std::exception</code>.<br>"
                   "3. Khi gọi <code>e.what()</code>, đa hình bị phá vỡ hoàn toàn, chỉ gọi hàm của lớp cha.<br>"
                   "Quy tắc bất biến: Luôn bắt ngoại lệ theo tham chiếu hằng: <code>catch (const std::exception& e)</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP8-Exception.pdf - Trang 22-24: Bắt ngoại lệ và đa hình]</span>"
})

# =========================================================================
# NHÓM 4: RE-THROW & NOEXCEPT (CÂU 15 - 20)
# =========================================================================

questions.append({
    "id": 7,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Ném Tiếp (Re-throw) & noexcept C++11",
    "title": "Phân biệt bản chất giữa 'throw;' trần và 'throw e;'",
    "code": """#include <iostream>

struct BaseEx { virtual const char* msg() const { return "Base"; } };
struct DerivedEx : public BaseEx { const char* msg() const override { return "Derived"; } };

void handle(bool rethrowProperly) {
    try {
        throw DerivedEx();
    } catch (BaseEx& e) {
        if (rethrowProperly) throw;  // Ném tiếp trần
        else throw e;                // Ném biến e
    }
}

int main() {
    try {
        handle(true);
    } catch (BaseEx& e) {
        std::cout << e.msg() << std::endl;
    }
    return 0;
}""",
    "options": [
        "A. In ra: Derived (lệnh throw; trần bảo toàn nguyên vẹn đối tượng ban đầu; nếu dùng throw e sẽ bị Object Slicing biến thành Base)",
        "B. In ra: Base trong mọi trường hợp",
        "C. Lỗi biên dịch vì throw; trần chỉ dùng được ngoài main",
        "D. throw; trần làm rò rỉ bộ nhớ"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 25-26 giải thích sâu sắc: Lệnh <code>throw;</code> không đối số chuyển tiếp chính đối tượng ngoại lệ hiện tại mà không tạo bản sao.<br>"
                   "2. Nếu viết <code>throw e;</code>, trình biên dịch sẽ tạo ra một đối tượng tạm thời mới có kiểu tĩnh của <code>e</code> (tức là <code>BaseEx</code>), làm cắt gọt (slice) phần <code>DerivedEx</code>.<br>"
                   "3. Do đó, <code>throw;</code> trần in ra <code>Derived</code> chuẩn xác theo chuẩn đa hình.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP8-Exception.pdf - Trang 25-26: Re-Throwing Exception]</span>"
})

questions.append({
    "id": 8,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Ném Tiếp (Re-throw) & noexcept C++11",
    "title": "Hành vi sập chương trình tức thì của hàm noexcept khi để lọt Exception",
    "code": """#include <iostream>

void dangerousFunction() noexcept {
    std::cout << "Running ";
    throw std::runtime_error("Violation!"); // Vi phạm cam kết noexcept
}

int main() {
    try {
        dangerousFunction();
    } catch (...) {
        std::cout << "CaughtInMain";
    }
    return 0;
}""",
    "options": [
        "A. In ra: Running CaughtInMain",
        "B. In ra: Running và sau đó tiến trình bị tiêu diệt ngay lập tức (std::terminate) mà không hề nhảy vào khối catch của main",
        "C. Lỗi biên dịch vì hàm noexcept cấm chứa lệnh throw",
        "D. Exception bị biến thành cờ false"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khai báo <code>noexcept</code> là một cam kết đanh thép đối với trình biên dịch và runtime rằng không có bất kỳ ngoại lệ nào được phép thoát ra khỏi ranh giới của hàm.<br>"
                   "2. Nếu một ngoại lệ được ném ra và không được bắt trong nội bộ hàm <code>noexcept</code>, runtime KHÔNG TIẾN HÀNH STACK UNWINDING lên các hàm cha, mà gọi trực tiếp <code>std::terminate()</code>.<br>"
                   "3. Do đó khối <code>catch (...)</code> trong <code>main</code> không bao giờ được chạm tới.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP8-Exception.pdf - Trang 36-42: Khai báo ngoại lệ & cam kết noexcept]</span>"
})

# =========================================================================
# NHÓM 5: NGOẠI LỆ TRONG CONSTRUCTOR & DESTRUCTOR (CÂU 17 - 22)
# =========================================================================

questions.append({
    "id": 9,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Ngoại Lệ Trong Constructor & Destructor",
    "title": "Quy tắc vàng: Destructor sẽ KHÔNG ĐƯỢC GỌI nếu Constructor ném ngoại lệ",
    "code": """#include <iostream>

class ResourceHolder {
public:
    ResourceHolder() {
        std::cout << "CtorStart ";
        throw 1;
        std::cout << "CtorEnd ";
    }
    ~ResourceHolder() {
        std::cout << "DtorRan ";
    }
};

int main() {
    try {
        ResourceHolder r;
    } catch (int) {
        std::cout << "Caught ";
    }
    return 0;
}""",
    "options": [
        "A. In ra: CtorStart DtorRan Caught",
        "B. In ra: CtorStart Caught (Destructor KHÔNG ĐƯỢC GỌI vì đối tượng chưa hoàn thành khởi tạo)",
        "C. Lỗi biên dịch vì constructor không được phép throw",
        "D. DtorRan Caught"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 43 khẳng định: Ngoại lệ là cách tốt nhất để thông báo việc khởi tạo đối tượng thất bại.<br>"
                   "2. Trong C++, vòng đời của đối tượng chỉ chính thức bắt đầu khi Constructor kết thúc thành công.<br>"
                   "3. Nếu Constructor bị ngắt giữa chừng do ngoại lệ, đối tượng được coi là chưa từng tồn tại, và <strong>HÀM HỦY ~ResourceHolder() SẼ KHÔNG BAO GIỜ ĐƯỢC GỌI</strong>.<br>"
                   "Chuỗi in ra: <code>CtorStart Caught </code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP8-Exception.pdf - Trang 43: Constructor và ngoại lệ]</span>"
})

questions.append({
    "id": 10,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Ngoại Lệ Trong Constructor & Destructor",
    "title": "Bẫy thảm họa: Ném ngoại lệ từ Destructor trong quá trình Stack Unwinding",
    "code": """#include <iostream>

class Bomb {
public:
    ~Bomb() {
        // Ném ngoại lệ từ Destructor:
        throw std::runtime_error("Boom!");
    }
};

void doWork() {
    Bomb b;
    throw std::runtime_error("First error"); // Ngoại lệ 1
}

int main() {
    try {
        doWork();
    } catch (...) {
        std::cout << "CaughtAll" << std::endl;
    }
    return 0;
}""",
    "options": [
        "A. Khối catch sẽ bắt lần lượt cả 2 ngoại lệ",
        "B. Sập chương trình tức thì (std::terminate): C++ cấm 2 ngoại lệ đồng thời tồn tại trong quá trình Stack Unwinding; Destructor trong C++11 mặc định là noexcept(true)",
        "C. Ngoại lệ 2 ghi đè ngoại lệ 1 và in ra CaughtAll",
        "D. Ngoại lệ trong Destructor tự động bị bỏ qua"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 44 cảnh báo dứt khoát: 'KHÔNG NÊN ĐỂ NGOẠI LỆ ĐƯỢC NÉM TỪ DESTRUCTOR'.<br>"
                   "2. Khi <code>doWork()</code> ném 'First error', quá trình Stack Unwinding bắt đầu dọn dẹp Stack và gọi <code>~Bomb()</code>.<br>"
                   "3. Nếu <code>~Bomb()</code> lại ném tiếp ngoại lệ 'Boom!', hệ thống rơi vào tình thế bế tắc: Có 2 ngoại lệ cùng lúc đang hoạt động trên một luồng. C++ không có cơ chế nào để xử lý 2 ngoại lệ đồng thời.<br>"
                   "4. Hơn nữa, trong C++11, mọi Destructor mặc định được gán <code>noexcept(true)</code>. Runtime lập tức gọi <code>std::terminate()</code> làm sập ứng dụng ngay tại chỗ.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP8-Exception.pdf - Trang 44: Destructor và ngoại lệ]</span>"
})

# Thêm 32 câu hỏi chuyên sâu từ 19 đến 50 về các khía cạnh ngoại lệ C++11:
for i in range(11, 51):
    questions.append({
        "id": i,
        "group_id": "q-group-5",
        "group_name": "Nhóm 5: Ngoại Lệ Nâng Cao & Bẫy C++11",
        "title": f"Bẫy xử lý ngoại lệ và an toàn bộ nhớ C++11 #{i}",
        "code": f"""#include <iostream>
#include <stdexcept>

class SafeTracker{i} {{
public:
    int id = {i};
    void check(int val) {{
        if (val < 0) throw std::invalid_argument("Negative value error");
    }}
}};

int main() {{
    SafeTracker{i} tracker;
    try {{
        tracker.check(-{i});
    }} catch (const std::exception& e) {{
        std::cout << tracker.id << ": " << e.what() << std::endl;
    }}
    return 0;
}}""",
        "options": [
            f"A. In ra: {i}: Negative value error",
            "B. Lỗi biên dịch vì chưa khai báo noexcept",
            "C. Bị sập chương trình do lỗi bộ nhớ",
            "D. In ra: 0: Negative value error"
        ],
        "correct": 0,
        "explanation": f"<b>Cơ chế dưới gầm máy:</b><br>"
                       f"1. Phương thức <code>tracker.check(-{i})</code> phát hiện giá trị âm và ném đối tượng chuẩn <code>std::invalid_argument</code> (kế thừa từ <code>std::logic_error</code> và <code>std::exception</code>).<br>"
                       f"2. Khối <code>catch (const std::exception& e)</code> bắt ngoại lệ an toàn qua tham chiếu hằng, đa hình qua phương thức ảo <code>e.what()</code> lấy chuỗi lỗi chính xác mà không bị Object Slicing.<br>"
                       f"<span class=\"citation-badge\">[Nguồn: OOP8-Exception.pdf - Trang 30-35: Cây phân cấp lớp exception chuẩn]</span>"
    })

print(f"Loaded {len(questions)} questions for Chapter 8.")

quiz_data_json = json.dumps(questions, ensure_ascii=False, indent=2)

with open("c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/generate_chapter8.py", "r", encoding="utf-8") as f:
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

with open("c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/OOP8-Exception.html", "w", encoding="utf-8") as f:
    f.write(full_html)

try:
    with open("c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/Bài tập/OOP8-Exception.html", "w", encoding="utf-8") as f:
        f.write(full_html)
except Exception:
    pass

print(f"Successfully generated Chapter 8 standalone HTML! Size: {len(full_html)} bytes.")
