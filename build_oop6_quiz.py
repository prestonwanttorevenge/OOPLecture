# -*- coding: utf-8 -*-
"""
Builder for Chapter 6: Đa Hình (Polymorphism) - MOSTest5_2
Produces: OOP6-Polymorphism_new.html
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

questions = []

# =========================================================================
# NHÓM 1: CƠ CHẾ BẢNG ẢO (VTABLE) & CON TRỎ ẢO (VPTR) DƯỚI GẦM MÁY (CÂU 1 - 8)
# =========================================================================

questions.append({
    "id": 1,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bảng Ảo (VTable) & Con Trỏ Ảo (vptr)",
    "title": "Kích thước của Class khi xuất hiện hàm ảo (Chi phí con trỏ vptr)",
    "code": """#include <iostream>

struct NoVirtual {
    int a;
    void func() {}
};

struct WithVirtual {
    int a;
    virtual void func() {}
};

int main() {
    // Trên nền tảng hệ điều hành 64-bit:
    std::cout << sizeof(NoVirtual) << " ";
    std::cout << (sizeof(WithVirtual) > sizeof(NoVirtual)) << " ";
    std::cout << sizeof(WithVirtual);
    return 0;
}""",
    "options": [
        "A. 4 1 16 (WithVirtual chứa thêm con trỏ vptr 8 bytes + 4 bytes int + 4 bytes padding căn lề 8-byte = 16 bytes)",
        "B. 4 0 4 (Hàm ảo không làm tăng kích thước đối tượng)",
        "C. 4 1 8",
        "D. 4 1 12"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Một class thông thường không có hàm ảo chỉ chứa các biến thành viên dữ liệu (<code>sizeof(NoVirtual) == sizeof(int) == 4 bytes</code>).<br>"
                   "2. Ngay khi có ít nhất một hàm <code>virtual</code>, trình biên dịch âm thầm chèn thêm một con trỏ bí mật <strong>vptr</strong> (Virtual Table Pointer) có kích thước 8 bytes (trên kiến trúc 64-bit).<br>"
                   "3. Cùng với biến <code>int a</code> (4 bytes) và 4 bytes padding căn lề để kích thước là bội số của 8, tổng kích thước <code>sizeof(WithVirtual)</code> là <strong>16 bytes</strong>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 21-24: Hàm ảo & Con trỏ bảng ảo]</span>"
})

questions.append({
    "id": 2,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bảng Ảo (VTable) & Con Trỏ Ảo (vptr)",
    "title": "Bản chất VTable: Bao nhiêu bảng ảo được sinh ra cho mỗi Lớp vs mỗi Đối tượng?",
    "code": """#include <iostream>

struct Base {
    virtual void f() {}
    virtual void g() {}
};

int main() {
    Base b1;
    Base b2;
    Base b3;

    void** vptr1 = *(void***)&b1;
    void** vptr2 = *(void***)&b2;
    void** vptr3 = *(void***)&b3;

    std::cout << (vptr1 == vptr2 && vptr2 == vptr3 ? "SameVTable" : "Different");
    return 0;
}""",
    "options": [
        "A. SameVTable (Mỗi Class chỉ có duy nhất MỘT bảng VTable trong vùng nhớ tĩnh, mọi đối tượng cùng lớp đều trỏ chung vptr về bảng này)",
        "B. Different (Mỗi đối tượng tự sao chép một bảng VTable riêng biệt trong RAM)",
        "C. Lỗi biên dịch vì không thể truy cập con trỏ vptr",
        "D. Chương trình crash do vi phạm truy cập bộ nhớ"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <strong>Bảng ảo (VTable)</strong> là một mảng tĩnh chứa các con trỏ hàm được trình biên dịch tạo ra tại thời điểm biên dịch và đặt trong vùng nhớ chỉ đọc (Read-Only Data Section <code>.rodata</code>).<br>"
                   "2. Mỗi LỚP (Class) chỉ sở hữu duy nhất MỘT VTable. Dù bạn có tạo ra hàng triệu đối tượng <code>Base b1, b2, ...</code>, mỗi đối tượng chỉ tốn một con trỏ <code>vptr</code> và tất cả các <code>vptr</code> này đều trỏ tới cùng một địa chỉ VTable dùng chung.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 21-23: Bảng phương thức ảo]</span>"
})

questions.append({
    "id": 3,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bảng Ảo (VTable) & Con Trỏ Ảo (vptr)",
    "title": "Cơ chế phân giải hàm ảo (Dynamic Dispatch) qua VTable Index",
    "code": """#include <iostream>

struct Base {
    virtual void a() { std::cout << "Base::a "; }
    virtual void b() { std::cout << "Base::b "; }
};

struct Derived : public Base {
    void a() override { std::cout << "Derived::a "; }
    // Không override b()
};

int main() {
    Base* p = new Derived();
    p->a();
    p->b();
    delete p;
    return 0;
}""",
    "options": [
        "A. Derived::a Base::b (VTable của Derived chứa slot 0 trỏ tới Derived::a và slot 1 trỏ kế thừa tới Base::b)",
        "B. Base::a Base::b",
        "C. Derived::a Derived::a",
        "D. Lỗi biên dịch vì Derived không override toàn bộ hàm ảo"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. VTable của <code>Derived</code> sao chép cấu trúc từ <code>Base</code>:<br>"
                   "   - Slot 0 (ứng với <code>a()</code>): Do <code>Derived</code> ghi đè, slot này được cập nhật trỏ tới <code>&Derived::a</code>.<br>"
                   "   - Slot 1 (ứng với <code>b()</code>): Không ghi đè, slot này giữ nguyên địa chỉ của <code>&Base::b</code>.<br>"
                   "2. Khi gọi <code>p->a()</code>, mã máy thực hiện: <code>(*(p->vptr[0]))(p)</code> -> gọi <code>Derived::a</code>.<br>"
                   "3. Khi gọi <code>p->b()</code>, mã máy thực hiện: <code>(*(p->vptr[1]))(p)</code> -> gọi <code>Base::b</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 22-26: Phân giải hàm ảo]</span>"
})

questions.append({
    "id": 4,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bảng Ảo (VTable) & Con Trỏ Ảo (vptr)",
    "title": "Gọi hàm ảo qua Biến Giá Trị Thường (Value) vs Con Trỏ (Early Binding Devirtualization)",
    "code": """#include <iostream>

struct Animal {
    virtual void speak() { std::cout << "Sound "; }
};

struct Dog : public Animal {
    void speak() override { std::cout << "Woof "; }
};

int main() {
    Dog d;
    d.speak();         // Gọi trực tiếp qua biến giá trị

    Animal* p = &d;
    p->speak();        // Gọi qua con trỏ
    return 0;
}""",
    "options": [
        "A. Woof Woof (Cả hai đều in Woof, nhưng d.speak() được compiler liên kết tĩnh trực tiếp mà không cần tra cứu VTable)",
        "B. Sound Woof",
        "C. Sound Sound",
        "D. Woof Sound"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Cả hai lời gọi đều in ra <code>Woof</code>.<br>"
                   "2. Tuy nhiên, với <code>d.speak()</code>, vì biến <code>d</code> có kiểu cụ thể là <code>Dog</code> được khai báo rõ ràng trên stack, trình biên dịch thực hiện tối ưu hóa <strong>Devirtualization</strong>: nó gọi thẳng địa chỉ hàm <code>Dog::speak</code> lúc biên dịch (Early Binding) mà không hề tốn chỉ lệnh tra cứu bảng VTable!<br>"
                   "3. Với <code>p->speak()</code>, do <code>p</code> là con trỏ kiểu <code>Animal*</code>, compiler bắt buộc phải sinh mã tra cứu bảng ảo (Late / Dynamic Binding) tại thời điểm chạy.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 14-20 & Devirtualization Optimization]</span>"
})

questions.append({
    "id": 5,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bảng Ảo (VTable) & Con Trỏ Ảo (vptr)",
    "title": "Đa hình Runtime qua Tham Chiếu Base& bảo toàn VTable",
    "code": """#include <iostream>

struct Base {
    virtual void who() const { std::cout << "Base "; }
};

struct Sub : public Base {
    void who() const override { std::cout << "Sub "; }
};

void invoke(const Base& ref) {
    ref.who();
}

int main() {
    Base b;
    Sub s;
    invoke(b);
    invoke(s);
    return 0;
}""",
    "options": [
        "A. Base Sub (Tham chiếu Base& trỏ trực tiếp vào đối tượng gốc trong bộ nhớ, vptr của đối tượng Sub được giữ nguyên)",
        "B. Base Base",
        "C. Sub Sub",
        "D. Lỗi biên dịch vì tham chiếu không thể có tính đa hình"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, tính đa hình động (Dynamic Polymorphism) CHỈ hoạt động thông qua <strong>Con trỏ (Pointers)</strong> hoặc <strong>Tham chiếu (References)</strong>.<br>"
                   "2. Khi truyền <code>s</code> vào <code>invoke(const Base& ref)</code>, biến <code>ref</code> thực chất là một con trỏ ngầm định trỏ tới địa chỉ của <code>s</code>. Con trỏ <code>vptr</code> nằm trong 8 byte đầu của <code>s</code> vẫn trỏ tới VTable của <code>Sub</code>, do đó <code>ref.who()</code> dispatch chính xác vào <code>Sub::who</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 21-23: Cơ chế tham chiếu và liên kết động]</span>"
})

questions.append({
    "id": 6,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bảng Ảo (VTable) & Con Trỏ Ảo (vptr)",
    "title": "Hiểm họa bảo mật: Con trỏ vptr bị phá hủy do ghi đè bộ nhớ (Memory Corruption)",
    "code": """#include <iostream>
#include <cstring>

struct Polymorphic {
    int id;
    virtual void print() { std::cout << "ID:" << id; }
};

int main() {
    Polymorphic obj;
    obj.id = 7;

    // Lỗi cực nặng: memset xóa sạch cả vùng nhớ đối tượng, bao gồm vptr!
    std::memset(&obj, 0, sizeof(obj));

    // obj.print(); // Gọi qua con trỏ hoặc gián tiếp
    std::cout << "MemsetDone";
    return 0;
}""",
    "options": [
        "A. MemsetDone; Nếu gọi hàm ảo sau lệnh memset, chương trình sẽ sập ngay lập tức (Crash/SIGSEGV) do vptr bị gán thành nullptr (0x0)",
        "B. In ra ID:0 an toàn",
        "C. memset tự động bỏ qua vùng nhớ của con trỏ vptr",
        "D. Lỗi biên dịch tại lệnh memset"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Lệnh <code>std::memset(&obj, 0, sizeof(obj))</code> ghi đè số 0 lên TOÀN BỘ các byte của <code>obj</code>, bao gồm cả 8 byte đầu tiên lưu trữ con trỏ <code>vptr</code>.<br>"
                   "2. <code>vptr</code> giờ đây mang giá trị <code>0x0 (NULL)</code>. Khi có bất kỳ lời gọi hàm ảo nào cần tra cứu VTable, CPU cố gắng đọc địa chỉ bộ nhớ 0x0 và kích hoạt lỗi truy cập trái phép <strong>Segmentation Fault (Crash)</strong> ngay lập tức.<br>"
                   "3. <em>Cảnh báo sống còn: Tuyệt đối không bao giờ dùng memset/memcpy trên các lớp có tính đa hình!</em><br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 21-24 & C++ Object Memory Model]</span>"
})

questions.append({
    "id": 7,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bảng Ảo (VTable) & Con Trỏ Ảo (vptr)",
    "title": "Cơ chế Thunk (Adjustor Thunk) trong Đa Kế Thừa với Hàm Ảo",
    "code": """#include <iostream>

struct Base1 {
    virtual void f1() { std::cout << "f1 "; }
};

struct Base2 {
    virtual void f2() { std::cout << "f2 "; }
};

struct Multi : public Base1, public Base2 {
    void f2() override { std::cout << "Multi::f2 "; }
};

int main() {
    Multi m;
    Base2* p2 = &m; // Con trỏ p2 bị dịch chuyển (offset adjustment)
    p2->f2();
    return 0;
}""",
    "options": [
        "A. Multi::f2 (Trình biên dịch dùng một đoạn mã ngắn gọi là 'Thunk' để điều chỉnh con trỏ this lùi về đầu đối tượng Multi trước khi gọi hàm)",
        "B. f2 của Base2",
        "C. Lỗi biên dịch vì p2 không trỏ vào đầu đối tượng Multi",
        "D. Chương trình crash do sai lệch địa chỉ this"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong <code>Multi</code>, subobject <code>Base2</code> nằm ở offset +8 bytes sau <code>Base1</code>. Con trỏ <code>p2</code> trỏ thẳng vào subobject <code>Base2</code> này.<br>"
                   "2. Tuy nhiên, hàm <code>Multi::f2</code> mong đợi con trỏ <code>this</code> trỏ vào ĐẦU của toàn bộ đối tượng <code>Multi</code> (offset 0).<br>"
                   "3. Để giải quyết, VTable của <code>Base2</code> trong <code>Multi</code> trỏ tới một đoạn mã hợp ngữ trung gian gọi là <strong>Adjustor Thunk</strong>. Thunk sẽ lấy con trỏ <code>this</code> trừ đi 8 bytes, rồi mới nhảy tới thân hàm <code>Multi::f2</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 21-26 & ABI Virtual Dispatch Thunks]</span>"
})

questions.append({
    "id": 8,
    "group_id": "q-group-1",
    "group_name": "Nhóm 1: Bảng Ảo (VTable) & Con Trỏ Ảo (vptr)",
    "title": "Hàm ảo có quyền Private trong Base vẫn tham gia Đa Hình Động bình thường",
    "code": """#include <iostream>

class Base {
private:
    virtual void secret() { std::cout << "BaseSecret "; }
public:
    void run() { secret(); }
};

class Derived : public Base {
public:
    void secret() override { std::cout << "DerivedRevealed "; }
};

int main() {
    Derived d;
    d.run();
    return 0;
}""",
    "options": [
        "A. DerivedRevealed (Quyền truy cập private/public được kiểm tra lúc biên dịch, còn phân giải hàm ảo diễn ra lúc runtime qua VTable)",
        "B. BaseSecret",
        "C. Lỗi biên dịch vì hàm private không được phép là virtual",
        "D. Lỗi biên dịch vì Derived không thể override hàm private của Base"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, <strong>Access Control (private/protected/public)</strong> và <strong>Virtual Dispatch</strong> là hai cơ chế hoàn toàn tách biệt!<br>"
                   "2. Kiểm tra quyền truy cập diễn ra tại thời điểm biên dịch đối với hàm <code>run()</code> (nó là public nên hợp lệ).<br>"
                   "3. Tại runtime, lời gọi <code>secret()</code> tra cứu VTable của đối tượng thực tế (<code>Derived</code>). Vì <code>Derived</code> đã ghi đè slot đó, địa chỉ của <code>Derived::secret</code> được thực thi -> in ra <code>DerivedRevealed</code>. Đây chính là nền tảng của <strong>Template Method Pattern / NVI Idiom</strong>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 21-24 & NVI Pattern Architecture]</span>"
})

print(f"Loaded {len(questions)} questions for Group 1.")
# =========================================================================
# NHÓM 2: OVERRIDING, TỪ KHÓA OVERRIDE & FINAL TRONG C++11 (CÂU 9 - 16)
# =========================================================================

questions.append({
    "id": 9,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Overriding, override & final trong C++11",
    "title": "Bẫy ngộ nhận Overriding khi sai khác tính chất const (Signature Mismatch)",
    "code": """#include <iostream>

struct Base {
    virtual void action() const { std::cout << "BaseConst "; }
};

struct Derived : public Base {
    // Không có từ khóa const ở cuối!
    void action() { std::cout << "DerivedNonConst "; }
};

int main() {
    Base* p = new Derived();
    p->action();
    delete p;
    return 0;
}""",
    "options": [
        "A. DerivedNonConst",
        "B. BaseConst (Do thiếu const, hàm ở Derived không hề override hàm của Base mà tạo ra một overload mới!)",
        "C. Lỗi biên dịch vì Derived thiếu const",
        "D. Chương trình crash tại runtime"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, tính chất <code>const</code> của hàm thành viên là một phần cấu thành nên chữ ký hàm (Function Signature).<br>"
                   "2. <code>Base::action() const</code> và <code>Derived::action()</code> là HAI HÀM HOÀN TOÀN KHÁC NHAU. Hàm trong <code>Derived</code> không ghi đè slot trong VTable của Base mà chỉ nạp chồng (overload) / che khuất.<br>"
                   "3. Khi gọi <code>p->action()</code> qua con trỏ <code>Base*</code>, slot VTable của <code>Base::action() const</code> vẫn trỏ về hàm của Base -> in ra <code>BaseConst</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 6-12: Overloading vs Overriding]</span>"
})

questions.append({
    "id": 10,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Overriding, override & final trong C++11",
    "title": "Lợi ích cứu rỗi của từ khóa override trong chuẩn C++11",
    "code": """#include <iostream>

struct Base {
    virtual void render(int width, int height) {}
};

struct Derived : public Base {
    // Cố tình viết sai tên tham số hoặc thiếu từ khóa
    // void render(int w, float h) override; // Dòng X
    void render(int w, int h) override {
        std::cout << "RenderSuccess ";
    }
};

int main() {
    Derived d;
    d.render(10, 20);
    return 0;
}""",
    "options": [
        "A. In ra: RenderSuccess; Nếu mở Dòng X sẽ bị LỖI BIÊN DỊCH ngay lập tức vì từ khóa override buộc compiler kiểm tra khớp signature",
        "B. Dòng X hợp lệ vì float ép kiểu tự động thành int",
        "C. In ra: RenderSuccess và sinh warning",
        "D. Lỗi biên dịch vì override không hỗ trợ 2 tham số"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trước C++11, nếu bạn gõ nhầm một kiểu dữ liệu trong tham số (ví dụ <code>float</code> thay vì <code>int</code>), trình biên dịch sẽ âm thầm coi đó là một hàm mới, dẫn tới bug logic cực kỳ khó dò.<br>"
                   "2. Từ khóa <code>override</code> trong C++11 thông báo cho compiler: 'Hàm này BẮT BUỘC phải ghi đè một hàm ảo sẵn có ở lớp cha'. Nếu không tìm thấy hàm ảo nào khớp 100% signature, compiler lập tức báo lỗi tại thời điểm dịch mã.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 11: Lưu ý khi override & C++11 override specifier]</span>"
})

questions.append({
    "id": 11,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Overriding, override & final trong C++11",
    "title": "Từ khóa final trên phương thức ảo ngăn chặn ghi đè ở thế hệ sau",
    "code": """#include <iostream>

struct A {
    virtual void step() { std::cout << "A "; }
};

struct B : public A {
    void step() override final { std::cout << "B "; } // Đóng chốt tại đây
};

struct C : public B {
    // void step() override { std::cout << "C "; } // Dòng Z
};

int main() {
    A* p = new B();
    p->step();
    delete p;
    return 0;
}""",
    "options": [
        "A. In ra: B; Dòng Z nếu mở ra sẽ bị LỖI BIÊN DỊCH: cannot override 'final' function 'B::step'",
        "B. Dòng Z hợp lệ nhưng chỉ gọi khi ép kiểu về C*",
        "C. Lỗi biên dịch vì từ khóa final chỉ dùng cho class chứ không dùng cho function",
        "D. In ra: A B"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi một phương thức ảo được khai báo là <code>final</code> trong C++11, nó tuyên bố rằng phiên bản này là phiên bản cuối cùng không được phép tùy biến thêm.<br>"
                   "2. Bất kỳ lớp dẫn xuất kế tiếp nào (như <code>C</code>) cố tình ghi đè lại <code>step()</code> sẽ bị compiler phát hiện và ném lỗi biên dịch ngay lập tức.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 12 & C++11 final specifier]</span>"
})

questions.append({
    "id": 12,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Overriding, override & final trong C++11",
    "title": "Kiểu trả về đồng biến (Covariant Return Types) trong Overriding",
    "code": """#include <iostream>

struct Shape {};
struct Circle : public Shape {};

struct Factory {
    virtual Shape* create() {
        std::cout << "BaseFactory ";
        return new Shape();
    }
};

struct CircleFactory : public Factory {
    // Ghi đè nhưng kiểu trả về là Circle* (lớp con của Shape*)!
    Circle* create() override {
        std::cout << "CircleFactory ";
        return new Circle();
    }
};

int main() {
    Factory* f = new CircleFactory();
    Shape* s = f->create();
    delete s;
    delete f;
    return 0;
}""",
    "options": [
        "A. CircleFactory (C++ cho phép Covariant Return Type: kiểu trả về của hàm ghi đè có thể là con trỏ/tham chiếu tới lớp dẫn xuất của kiểu trả về hàm cha)",
        "B. Lỗi biên dịch vì kiểu trả về của hàm override phải giống hệt lớp cha",
        "C. BaseFactory",
        "D. Lỗi runtime bad_cast"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Theo chuẩn C++, ngoại lệ duy nhất cho quy tắc 'kiểu trả về phải giống nhau khi overriding' là <strong>Covariant Return Types (Kiểu trả về đồng biến)</strong>.<br>"
                   "2. Nếu hàm ở Base trả về <code>BaseClass*</code> (hoặc <code>BaseClass&</code>), thì hàm override ở Derived được phép trả về <code>DerivedClass*</code> (hoặc <code>DerivedClass&</code>).<br>"
                   "3. Mã máy VTable vẫn hoàn toàn tương thích và an toàn tuyệt đối.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 11-12 & Covariant Return Types rules]</span>"
})

questions.append({
    "id": 13,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Overriding, override & final trong C++11",
    "title": "Bẫy thay đổi kiểu trả về nguyên thủy trong Overriding",
    "code": """#include <iostream>

struct Base {
    virtual int calculate() { return 10; }
};

struct Derived : public Base {
    // Thay int bằng double:
    // double calculate() override { return 10.5; } // Dòng Err
};

int main() {
    Base b;
    std::cout << b.calculate();
    return 0;
}""",
    "options": [
        "A. In ra 10; Dòng Err nếu mở ra sẽ bị LỖI BIÊN DỊCH vì kiểu nguyên thủy không có tính đồng biến (conflicting return type)",
        "B. Dòng Err hợp lệ vì int tự động ép kiểu lên double",
        "C. In ra 10.5",
        "D. Lỗi biên dịch tại main()"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Tính đồng biến (Covariance) CHỈ ÁP DỤNG cho con trỏ hoặc tham chiếu tới các lớp có quan hệ kế thừa.<br>"
                   "2. Đối với các kiểu dữ liệu nguyên thủy (như <code>int</code>, <code>double</code>, <code>float</code>), kiểu trả về của hàm ghi đè <strong>BẮT BUỘC PHẢI GIỐNG HỆT NHAU</strong>.<br>"
                   "3. Nếu khác nhau, trình biên dịch báo lỗi <em>'conflicting return type specified for virtual function'</em>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 11: Ràng buộc kiểu trả về]</span>"
})

questions.append({
    "id": 14,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Overriding, override & final trong C++11",
    "title": "Đa hình xuyên qua các mức bảo vệ: Base là Public nhưng Derived là Private",
    "code": """#include <iostream>

class Base {
public:
    virtual void execute() { std::cout << "BaseExec "; }
};

class Derived : public Base {
private:
    // Hàm override được đặt trong mục private!
    void execute() override { std::cout << "DerivedPrivateExec "; }
};

int main() {
    Base* p = new Derived();
    p->execute(); // Gọi qua con trỏ Base*
    // Derived d;
    // d.execute(); // Dòng M
    delete p;
    return 0;
}""",
    "options": [
        "A. In ra DerivedPrivateExec; Dòng M nếu mở ra sẽ bị lỗi biên dịch vì execute là private trong Derived",
        "B. Lỗi biên dịch tại p->execute() vì hàm trong Derived là private",
        "C. In ra BaseExec",
        "D. Chương trình ném ngoại lệ std::bad_access"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trình biên dịch kiểm tra quyền truy cập dựa trên <strong>Kiểu tĩnh (Static Type)</strong> của biến lúc gọi.<br>"
                   "2. Con trỏ <code>p</code> có kiểu <code>Base*</code>, và trong <code>Base</code> hàm <code>execute()</code> là <code>public</code> -> Trình biên dịch đồng ý cho phép gọi!<br>"
                   "3. Tại runtime, con trỏ vptr trong <code>Derived</code> trỏ tới hàm <code>Derived::execute</code> và thực thi nó bình thường, hoàn toàn bỏ qua việc nó được khai báo là private trong lớp con!<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 21-24 & C++ Access Control vs Dynamic Dispatch]</span>"
})

questions.append({
    "id": 15,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Overriding, override & final trong C++11",
    "title": "Lệnh cấm: Phương thức mẫu (Member Function Template) không được phép là Virtual",
    "code": """#include <iostream>

struct Processor {
    // Cố tình khai báo template kết hợp virtual:
    // template <typename T>
    // virtual void process(T val) {} // Dòng Lỗi
};

int main() {
    std::cout << "Valid";
    return 0;
}""",
    "options": [
        "A. In ra Valid; Dòng Lỗi nếu mở ra sẽ bị LỖI BIÊN DỊCH vì member function template không thể là virtual",
        "B. Dòng Lỗi hoàn toàn hợp lệ trong C++11",
        "C. Chỉ được phép nếu T là kiểu nguyên thủy",
        "D. Chương trình crash tại runtime"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Bảng ảo VTable đòi hỏi phải có <strong>KÍCH THƯỚC CỐ ĐỊNH</strong> tại thời điểm biên dịch một đơn vị dịch (Translation Unit).<br>"
                   "2. Nếu một hàm template là virtual, số lượng thể hiện (instantiations) của nó có thể là vô hạn tùy thuộc vào các file mã nguồn khác nhau trong dự án, khiến trình biên dịch không thể biết trước VTable cần bao nhiêu slot con trỏ hàm!<br>"
                   "3. Do đó, chuẩn C++ cấm tuyệt đối <code>virtual member function template</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 21 & OOP7-Template.pdf: Template vs Virtual functions]</span>"
})

questions.append({
    "id": 16,
    "group_id": "q-group-2",
    "group_name": "Nhóm 2: Overriding, override & final trong C++11",
    "title": "Tối ưu hóa Devirtualization và Inline Expansion của trình biên dịch nhờ final",
    "code": """#include <iostream>

struct Base {
    virtual int compute(int x) { return x * 2; }
};

struct FinalDerived final : public Base {
    int compute(int x) override final { return x + 10; }
};

int test(FinalDerived& obj, int val) {
    return obj.compute(val); // Compiler có thể devirtualize không?
}

int main() {
    FinalDerived fd;
    std::cout << test(fd, 5);
    return 0;
}""",
    "options": [
        "A. In ra 15; Nhờ từ khóa final, compiler biết chắc không thể có lớp con nào override hàm compute nữa, nên nó loại bỏ hoàn toàn việc tra cứu VTable và có thể inline trực tiếp hàm compute",
        "B. In ra 10",
        "C. Lỗi biên dịch vì không thể dùng cả override và final cùng lúc",
        "D. In ra 15 nhưng vẫn bắt buộc tra cứu VTable lúc runtime"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Một trong những cải tiến hiệu năng lớn nhất của C++11 là từ khóa <code>final</code>.<br>"
                   "2. Khi trình biên dịch thấy <code>FinalDerived</code> là <code>final</code>, nó biết rằng không có bất kỳ lớp nào khác trong tương lai có thể kế thừa và thay đổi hành vi của <code>compute()</code>.<br>"
                   "3. Do đó, lời gọi <code>obj.compute(val)</code> trong hàm <code>test</code> được chuyển đổi từ Dynamic Call (gián tiếp qua VTable) thành Static Call (trực tiếp) hoặc thậm chí nhúng mã thẳng (Inline Expansion <code>val + 10</code>), triệt tiêu 100% chi phí runtime của hàm ảo.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 25-26: Tối ưu hóa đa hình tĩnh & Devirtualization]</span>"
})

print(f"Loaded {len(questions)} questions for Groups 1-2.")
# =========================================================================
# NHÓM 3: VIRTUAL DESTRUCTOR & QUẢN LÝ VÙNG NHỚ HEAP (CÂU 17 - 24)
# =========================================================================

questions.append({
    "id": 17,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Virtual Destructor & Vùng Nhớ Heap",
    "title": "Hiểm họa Memory Leak & Undefined Behavior khi Base thiếu Virtual Destructor",
    "code": """#include <iostream>

struct Base {
    ~Base() { std::cout << "BaseDtor "; } // Không có virtual!
};

struct Derived : public Base {
    int* data;
    Derived() : data(new int[500]) {}
    ~Derived() {
        delete[] data;
        std::cout << "DerivedDtor ";
    }
};

int main() {
    Base* ptr = new Derived();
    delete ptr; // Xóa đối tượng qua con trỏ lớp cơ sở
    return 0;
}""",
    "options": [
        "A. DerivedDtor BaseDtor",
        "B. Chỉ in ra BaseDtor (Destructor của Derived bị bỏ qua hoàn toàn, 500 phần tử int bị rò rỉ trên heap)",
        "C. Lỗi biên dịch vì không thể delete con trỏ Base*",
        "D. Chương trình tự động giải phóng toàn bộ vùng nhớ"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 28-30 nhấn mạnh: 'Nếu ta dùng một con trỏ tới lớp cơ sở thay cho con trỏ tới lớp dẫn xuất, chỉ có destructor của lớp cơ sở được gọi. Việc gọi nhầm destructor làm rò rỉ bộ nhớ!'.<br>"
                   "2. Khi <code>~Base()</code> không phải là <code>virtual</code>, trình biên dịch thực hiện liên kết tĩnh dựa trên kiểu <code>Base*</code>, chỉ gọi <code>Base::~Base()</code>. Phần dữ liệu <code>new int[500]</code> của <code>Derived</code> không bao giờ được giải phóng.<br>"
                   "3. Theo chuẩn C++ (§5.3.5/3), hành vi này là <strong>Undefined Behavior (UB)</strong>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 27-30: Destructor ảo & Quy tắc giải phóng]</span>"
})

questions.append({
    "id": 18,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Virtual Destructor & Vùng Nhớ Heap",
    "title": "Thứ tự hủy LIFO hoàn chỉnh khi Base sở hữu Virtual Destructor",
    "code": """#include <iostream>

struct Base {
    virtual ~Base() { std::cout << "~Base "; }
};

struct Middle : public Base {
    ~Middle() override { std::cout << "~Middle "; }
};

struct Derived : public Middle {
    ~Derived() override { std::cout << "~Derived "; }
};

int main() {
    Base* p = new Derived();
    delete p;
    return 0;
}""",
    "options": [
        "A. ~Derived ~Middle ~Base (Hủy từ ngoài vào trong, từ lớp con sâu nhất ngược về lớp gốc)",
        "B. ~Base ~Middle ~Derived",
        "C. ~Base ~Derived ~Middle",
        "D. Chỉ in ra ~Derived"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Nhờ từ khóa <code>virtual ~Base()</code>, destructor được đưa vào slot của bảng ảo VTable.<br>"
                   "2. Lệnh <code>delete p;</code> tra cứu VTable của đối tượng thực tế (<code>Derived</code>) và gọi <code>Derived::~Derived()</code>.<br>"
                   "3. Thân destructor của <code>Derived</code> chạy trước -> in <code>~Derived </code>, sau đó tự động gọi chuỗi ngược lên <code>Middle::~Middle()</code> -> in <code>~Middle </code>, và cuối cùng kết thúc tại <code>Base::~Base()</code> -> in <code>~Base </code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 30: Quy tắc chung về virtual destructor]</span>"
})

questions.append({
    "id": 19,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Virtual Destructor & Vùng Nhớ Heap",
    "title": "Destructor Thuần Ảo (Pure Virtual Destructor) và Bắt Buộc Cung Cấp Định Nghĩa",
    "code": """#include <iostream>

class AbstractBase {
public:
    virtual ~AbstractBase() = 0; // Pure virtual destructor
};

// Cung cấp định nghĩa ngoài class:
AbstractBase::~AbstractBase() {
    std::cout << "~AbstractBase ";
}

class Concrete : public AbstractBase {
public:
    ~Concrete() override {
        std::cout << "~Concrete ";
    }
};

int main() {
    AbstractBase* p = new Concrete();
    delete p;
    return 0;
}""",
    "options": [
        "A. ~Concrete ~AbstractBase (C++ cho phép pure virtual destructor, nhưng BẮT BUỘC phải cung cấp thân hàm định nghĩa cho nó vì mọi lớp con khi hủy đều phải gọi lên)",
        "B. Lỗi biên dịch vì hàm thuần ảo không được phép có định nghĩa",
        "C. Chỉ in ra ~Concrete",
        "D. Lỗi Linker: undefined reference to AbstractBase::~AbstractBase()"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Một lớp có thể được biến thành Abstract Class bằng cách duy nhất là khai báo <code>virtual ~Base() = 0;</code>.<br>"
                   "2. Tuy nhiên, <strong>Destructor của lớp cơ sở luôn luôn được gọi ngầm định</strong> khi lớp con bị hủy. Nếu lập trình viên không cung cấp phần thân <code>AbstractBase::~AbstractBase() {}</code>, Linker sẽ báo lỗi thiếu biểu tượng (Undefined symbol) ngay lập tức!<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 40-41: Hàm thuần ảo có định nghĩa]</span>"
})

questions.append({
    "id": 20,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Virtual Destructor & Vùng Nhớ Heap",
    "title": "Cú pháp Virtual Default Destructor chuẩn C++11",
    "code": """#include <iostream>

class Interface {
public:
    virtual ~Interface() = default; // Chuẩn C++11!
    virtual void action() = 0;
};

class Impl : public Interface {
public:
    void action() override { std::cout << "ActionDone "; }
};

int main() {
    Interface* p = new Impl();
    p->action();
    delete p;
    std::cout << "Cleaned";
    return 0;
}""",
    "options": [
        "A. ActionDone Cleaned (virtual ~Interface() = default là best practice chuẩn C++11 để vừa có virtual destructor vừa giữ cho class có tính chất trivial/mặc định tối ưu)",
        "B. Lỗi biên dịch vì = default không thể đi cùng với virtual",
        "C. Rò rỉ bộ nhớ tại delete p",
        "D. Lỗi runtime bad_alloc"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Chuẩn C++11 cho phép kết hợp từ khóa <code>virtual</code> và <code>= default;</code> để chỉ đạo trình biên dịch sinh destructor mặc định nhưng vẫn đăng ký nó vào bảng ảo VTable.<br>"
                   "2. Đây là thành ngữ chuẩn mực (Idiomatic C++11) cho mọi lớp cơ sở và giao diện trừu tượng.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 30 & C++11 =default specifier]</span>"
})

questions.append({
    "id": 21,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Virtual Destructor & Vùng Nhớ Heap",
    "title": "Hiểm họa khi dùng std::unique_ptr<Base> với lớp thiếu Virtual Destructor",
    "code": """#include <iostream>
#include <memory>

struct Base {
    ~Base() { std::cout << "~B "; } // Không virtual!
};

struct Derived : public Base {
    ~Derived() { std::cout << "~D "; }
};

int main() {
    {
        std::unique_ptr<Base> ptr(new Derived());
    } // Hết scope, unique_ptr gọi deleter mặc định
    return 0;
}""",
    "options": [
        "A. Chỉ in ra ~B (std::unique_ptr<Base> sử dụng default deleter gọi delete trên con trỏ Base*, gặp chính xác bẫy thiếu virtual destructor)",
        "B. In ra ~D ~B",
        "C. Lỗi biên dịch vì unique_ptr bắt buộc Base phải có virtual destructor",
        "D. In ra ~D"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <code>std::unique_ptr<Base></code> là con trỏ thông minh không có overhead (zero-overhead smart pointer), Deleter mặc định của nó là <code>std::default_delete<Base></code> gọi thẳng <code>delete ptr;</code>.<br>"
                   "2. Vì kiểu lưu trữ tĩnh là <code>Base*</code>, nó hoàn toàn phụ thuộc vào việc <code>Base</code> có virtual destructor hay không. Do Base không có, destructor của <code>Derived</code> bị bỏ qua, dẫn tới rò rỉ tài nguyên và UB.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 28-30 & std::unique_ptr memory model]</span>"
})

questions.append({
    "id": 22,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Virtual Destructor & Vùng Nhớ Heap",
    "title": "Bất ngờ lớn: Tại sao std::shared_ptr<Base> giải phóng đúng Derived dù Base thiếu Virtual Dtor?",
    "code": """#include <iostream>
#include <memory>

struct Base {
    ~Base() { std::cout << "~B "; } // Không có virtual!
};

struct Derived : public Base {
    ~Derived() { std::cout << "~D "; }
};

int main() {
    {
        std::shared_ptr<Base> p(new Derived());
    } // Hết scope
    return 0;
}""",
    "options": [
        "A. ~D ~B (shared_ptr lưu trữ kiểu thực sự Derived* trong Control Block tại thời điểm khởi tạo, nên deleter luôn xóa đúng Derived* ngay cả khi Base thiếu virtual dtor)",
        "B. Chỉ in ra ~B",
        "C. Lỗi biên dịch",
        "D. Lỗi runtime bad_weak_ptr"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Đây là một sự khác biệt kiến trúc kinh điển giữa <code>std::unique_ptr</code> và <code>std::shared_ptr</code>!<br>"
                   "2. Khi <code>std::shared_ptr<Base> p(new Derived());</code> được khởi tạo, nó tạo một <strong>Control Block</strong> lưu trữ con trỏ hàm xóa (Deleter) được tham số hóa dựa trên kiểu thực tế lúc khởi tạo (tức <code>delete (Derived*)ptr;</code>).<br>"
                   "3. Khi ref-count về 0, Deleter trong Control Block được thực thi với kiểu gốc <code>Derived*</code>, đảm bảo gọi đủ <code>~Derived</code> rồi mới tới <code>~Base</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 30 & std::shared_ptr Type Erasure Deleter]</span>"
})

questions.append({
    "id": 23,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Virtual Destructor & Vùng Nhớ Heap",
    "title": "Ngoại lệ văng ra từ Virtual Destructor và sập chương trình với noexcept(true)",
    "code": """#include <iostream>

struct Base {
    virtual ~Base() {
        // Trong C++11, mọi destructor mặc định là noexcept(true)!
        // throw 1; // Dòng X
    }
};

struct Derived : public Base {
    ~Derived() override {
        std::cout << "~Derived ";
    }
};

int main() {
    Base* p = new Derived();
    delete p;
    std::cout << "Done";
    return 0;
}""",
    "options": [
        "A. In ra: ~Derived Done; Nếu mở Dòng X, std::terminate() sẽ được gọi làm sập chương trình ngay lập tức vì destructor mặc định là noexcept(true)",
        "B. Ngoại lệ ở Dòng X được ném ra và có thể bắt bằng try-catch trong main",
        "C. Lỗi biên dịch tại Dòng X",
        "D. In ra: ~Derived Done mà không có lỗi gì"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong chuẩn C++11, tất cả các Destructor (dù là ảo hay thường) đều mặc định mang thuộc tính ngầm định <code>noexcept(true)</code>.<br>"
                   "2. Nếu một ngoại lệ bị ném ra khỏi destructor mà không được bắt bên trong chính nó, runtime sẽ coi đây là hành vi vi phạm cam kết <code>noexcept</code> và lập tức gọi <code>std::terminate()</code> để kết liễu tiến trình.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP8-Exception.pdf - Trang 43 & OOP6-Polymorphism_new.pdf: Destructor noexcept]</span>"
})

questions.append({
    "id": 24,
    "group_id": "q-group-3",
    "group_name": "Nhóm 3: Virtual Destructor & Vùng Nhớ Heap",
    "title": "Kỹ thuật Protected Non-Virtual Destructor ngăn chặn delete con trỏ Base",
    "code": """#include <iostream>

class Base {
protected:
    ~Base() { std::cout << "~Base "; } // Không virtual, nhưng đặt trong protected!
public:
    virtual void run() { std::cout << "Run "; }
};

class Derived : public Base {
public:
    ~Derived() { std::cout << "~Derived "; }
};

int main() {
    Base* p = new Derived();
    p->run();
    // delete p; // Dòng Err: Compiler báo lỗi gì?
    delete static_cast<Derived*>(p); // Cách xóa an toàn
    return 0;
}""",
    "options": [
        "A. In ra: Run ~Derived ~Base ; Dòng Err bị LỖI BIÊN DỊCH vì ~Base() là protected, ngăn chặn hoàn toàn nguy cơ delete nhầm con trỏ Base thiếu virtual destructor",
        "B. Dòng Err hợp lệ",
        "C. Lỗi biên dịch tại p->run()",
        "D. Chương trình crash do ép kiểu static_cast"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Đây là một thiết kế mẫu mực thay thế cho virtual destructor (thường dùng trong các thư viện hiệu năng cao để tiết kiệm 8 byte vptr cho destructor): Đặt <code>~Base()</code> ở mục <code>protected</code>.<br>"
                   "2. Khi đó, người dùng bên ngoài không thể vô tình gọi <code>delete p;</code> (bị compiler chặn vì destructor là protected).<br>"
                   "3. Đối tượng chỉ có thể được xóa an toàn thông qua con trỏ kiểu <code>Derived*</code>, đảm bảo gọi đủ cả destructor của Derived và Base.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 30 & Protected Non-virtual Destructor Idiom]</span>"
})

print(f"Loaded {len(questions)} questions for Groups 1-3.")
# =========================================================================
# NHÓM 4: LỚP TRỪU TƯỢNG (ABSTRACT CLASS) & PURE VIRTUAL FUNCTIONS (CÂU 25 - 34)
# =========================================================================

questions.append({
    "id": 25,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Lớp Trừu Tượng & Hàm Thuần Ảo",
    "title": "Lỗi biên dịch khi khởi tạo thể hiện của Lớp Trừu Tượng",
    "code": """#include <iostream>

class AbstractShape {
public:
    virtual void draw() = 0; // Pure virtual function
};

int main() {
    // AbstractShape shape; // Dòng X
    std::cout << "CannotInstantiate";
    return 0;
}""",
    "options": [
        "A. In ra: CannotInstantiate; Dòng X nếu mở ra sẽ bị LỖI BIÊN DỊCH: cannot declare variable 'shape' to be of abstract type 'AbstractShape'",
        "B. Dòng X hợp lệ nhưng khi gọi draw() sẽ crash",
        "C. Dòng X tự động sinh thân hàm draw rỗng",
        "D. Lỗi biên dịch ngay từ khai báo class AbstractShape"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 37-38 nêu rõ: 'Nếu một lớp có một phương thức không có định nghĩa (thuần ảo), C++ sẽ không cho phép tạo thể hiện từ lớp đó'.<br>"
                   "2. Trình biên dịch đánh dấu kiểu <code>AbstractShape</code> là Abstract Type trong bảng ký hiệu (Symbol Table). Mọi nỗ lực cấp phát đối tượng biến (trên stack hoặc qua <code>new AbstractShape</code>) đều bị chặn ngay tại thời điểm biên dịch.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 37-38: Lớp trừu tượng & Hàm thuần ảo]</span>"
})

questions.append({
    "id": 26,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Lớp Trừu Tượng & Hàm Thuần Ảo",
    "title": "Con trỏ và Tham chiếu tới Lớp Trừu Tượng hoàn toàn hợp lệ",
    "code": """#include <iostream>

class Renderer {
public:
    virtual void render() = 0;
    virtual ~Renderer() = default;
};

class OpenGLRenderer : public Renderer {
public:
    void render() override { std::cout << "OpenGL "; }
};

void execute(Renderer& r, Renderer* p) {
    r.render();
    p->render();
}

int main() {
    OpenGLRenderer gl;
    execute(gl, &gl);
    return 0;
}""",
    "options": [
        "A. OpenGL OpenGL (Dù không thể tạo đối tượng, con trỏ và tham chiếu tới Abstract Class là công cụ nền tảng để đạt được Dependency Inversion)",
        "B. Lỗi biên dịch vì tham chiếu không thể trỏ tới Abstract Class",
        "C. Lỗi biên dịch vì con trỏ không thể trỏ tới Abstract Class",
        "D. OpenGL và crash tại p->render()"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Một lớp trừu tượng đại diện cho một <strong>Giao diện (Interface / Contract)</strong>.<br>"
                   "2. Mặc dù không thể khởi tạo đối tượng trực tiếp, nhưng việc khai báo <code>Renderer*</code> hoặc <code>Renderer&</code> là hoàn toàn hợp lệ. Chúng đóng vai trò là con trỏ đa hình trỏ tới đối tượng cụ thể (<code>OpenGLRenderer</code>) có VTable đầy đủ.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 36-38: Sử dụng lớp trừu tượng]</span>"
})

questions.append({
    "id": 27,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Lớp Trừu Tượng & Hàm Thuần Ảo",
    "title": "Lớp con không override toàn bộ hàm thuần ảo vẫn tiếp tục là Abstract Class",
    "code": """#include <iostream>

class Base {
public:
    virtual void f() = 0;
    virtual void g() = 0;
};

class Mid : public Base {
public:
    void f() override { std::cout << "Mid::f "; }
    // Không override g()
};

int main() {
    // Mid m; // Dòng M
    std::cout << "MidIsStillAbstract";
    return 0;
}""",
    "options": [
        "A. In ra: MidIsStillAbstract; Dòng M bị LỖI BIÊN DỊCH vì Mid chưa override g(), nên Mid vẫn là lớp trừu tượng",
        "B. Dòng M hợp lệ và g() mặc định không làm gì",
        "C. Lỗi biên dịch ngay tại class Mid vì bắt buộc phải override hết",
        "D. Mid tự động kế thừa định nghĩa rỗng của Base"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, nếu một lớp kế thừa từ một Abstract Class mà không cung cấp định nghĩa cho TẤT CẢ các hàm thuần ảo của cha, thì những hàm thuần ảo còn lại sẽ được truyền tiếp xuống lớp con.<br>"
                   "2. Lớp con <code>Mid</code> vẫn chứa hàm thuần ảo <code>g() = 0</code> trong VTable của nó, do đó <code>Mid</code> tiếp tục là một Abstract Class và không thể khởi tạo đối tượng.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 38-39: Kế thừa hàm thuần ảo]</span>"
})

questions.append({
    "id": 28,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Lớp Trừu Tượng & Hàm Thuần Ảo",
    "title": "Bất ngờ: Cung cấp phần thân định nghĩa cho Hàm Thuần Ảo bên ngoài Class",
    "code": """#include <iostream>

class Base {
public:
    virtual void log() = 0; // Pure virtual
};

// Định nghĩa phần thân cho hàm thuần ảo bên ngoài class:
void Base::log() {
    std::cout << "BaseDefaultLog ";
}

class Derived : public Base {
public:
    void log() override {
        Base::log(); // Tái sử dụng cài đặt mặc định của cha
        std::cout << "DerivedLog ";
    }
};

int main() {
    Derived d;
    d.log();
    return 0;
}""",
    "options": [
        "A. BaseDefaultLog DerivedLog (C++ cho phép định nghĩa thân hàm cho pure virtual function ở ngoài class, lớp con có thể gọi qua Base::log())",
        "B. Lỗi biên dịch vì pure virtual function cấm có thân hàm",
        "C. Chỉ in ra DerivedLog",
        "D. Lỗi Linker do duplicate definition"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Slide trang 40-41 chỉ rõ: <em>'Cũng có thể cung cấp định nghĩa cho hàm thuần ảo... trong file chứa định nghĩa (.cpp)'</em>.<br>"
                   "2. Khai báo <code>= 0</code> chỉ có tác dụng biến lớp thành trừu tượng và bắt buộc các lớp con phải override.<br>"
                   "3. C++ hoàn toàn cho phép cung cấp mã cài đặt mặc định cho hàm thuần ảo bên ngoài class. Lớp con có thể tường minh tái sử dụng mã nguồn này bằng cú pháp <code>Base::log()</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 40-41: Hàm thuần ảo có định nghĩa]</span>"
})

questions.append({
    "id": 29,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Lớp Trừu Tượng & Hàm Thuần Ảo",
    "title": "Interface trong C++ và quy chuẩn thiết kế",
    "code": """#include <iostream>

// Giao diện thuần túy (Pure Interface)
struct ISerializable {
    virtual void serialize() = 0;
    virtual void deserialize() = 0;
    virtual ~ISerializable() = default;
};

struct UserData : public ISerializable {
    void serialize() override { std::cout << "Saved "; }
    void deserialize() override { std::cout << "Loaded "; }
};

int main() {
    ISerializable* s = new UserData();
    s->serialize();
    s->deserialize();
    delete s;
    return 0;
}""",
    "options": [
        "A. Saved Loaded (Trong C++, Interface được mô hình hóa bằng struct/class chỉ chứa các hàm thuần ảo = 0 và virtual destructor = default)",
        "B. Lỗi biên dịch vì C++ không có từ khóa interface",
        "C. Saved Loaded nhưng bị rò rỉ bộ nhớ",
        "D. Chỉ in ra Saved"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Không giống Java hay C# có từ khóa <code>interface</code> riêng biệt, C++ sử dụng cơ chế Abstract Class thuần túy (chỉ gồm pure virtual methods và virtual destructor) để tạo ra Interface.<br>"
                   "2. Đây là kỹ thuật thiết kế chuẩn mực bậc nhất trong lập trình hướng đối tượng C++.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 42: Xây dựng chặt chẽ các cây thừa kế]</span>"
})

questions.append({
    "id": 30,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Lớp Trừu Tượng & Hàm Thuần Ảo",
    "title": "Abstract Class vẫn có thể chứa Biến Thành Viên và Constructor",
    "code": """#include <iostream>

class AbstractAccount {
protected:
    double balance;
public:
    AbstractAccount(double b) : balance(b) {
        std::cout << "Acc(" << balance << ") ";
    }
    virtual void applyInterest() = 0;
    virtual ~AbstractAccount() = default;
};

class SavingsAccount : public AbstractAccount {
public:
    SavingsAccount(double b) : AbstractAccount(b) {}
    void applyInterest() override {
        balance += balance * 0.05;
        std::cout << "Bal=" << balance << " ";
    }
};

int main() {
    SavingsAccount sa(1000);
    sa.applyInterest();
    return 0;
}""",
    "options": [
        "A. Acc(1000) Bal=1050 (Abstract Class hoàn toàn có thể sở hữu trường dữ liệu và constructor để lớp con tái sử dụng)",
        "B. Lỗi biên dịch vì Abstract Class không được phép có Constructor",
        "C. Lỗi biên dịch vì Abstract Class không được phép có biến balance",
        "D. Acc(1000) Bal=1000"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Rất nhiều lập trình viên lầm tưởng Abstract Class không thể có constructor.<br>"
                   "2. Thực tế, khi một đối tượng cụ thể (<code>SavingsAccount</code>) được tạo ra, Base subobject (<code>AbstractAccount</code>) bắt buộc phải được khởi tạo đầu tiên. Do đó Constructor của Abstract Class chạy bình thường để khởi tạo biến <code>balance</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 36 & OOP5-Inheritance_new.pdf: Constructor của lớp trừu tượng]</span>"
})

questions.append({
    "id": 31,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Lớp Trừu Tượng & Hàm Thuần Ảo",
    "title": "Gọi hàm thuần ảo gián tiếp từ phương thức Non-Virtual của Base Class",
    "code": """#include <iostream>

class Document {
public:
    void print() { // Non-virtual template method
        std::cout << "[Header] ";
        renderBody(); // Gọi hàm thuần ảo!
        std::cout << "[Footer]";
    }
    virtual void renderBody() = 0;
    virtual ~Document() = default;
};

class Report : public Document {
public:
    void renderBody() override {
        std::cout << "ReportContent ";
    }
};

int main() {
    Report r;
    r.print();
    return 0;
}""",
    "options": [
        "A. [Header] ReportContent [Footer] (Phương thức non-virtual của Base hoàn toàn có thể gọi hàm thuần ảo; khi chạy, vptr của Report sẽ dispatch tới đúng phiên bản override)",
        "B. Lỗi biên dịch vì Base::print() gọi hàm chưa có định nghĩa",
        "C. Runtime crash: pure virtual method called",
        "D. [Header] [Footer]"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong thân hàm <code>Document::print()</code>, lời gọi <code>renderBody()</code> thực chất là <code>this->renderBody()</code>.<br>"
                   "2. Tại thời điểm chạy trong hàm <code>main()</code>, đối tượng hoàn chỉnh là <code>Report</code>, bảng VTable của nó đã chứa con trỏ tới <code>Report::renderBody</code>.<br>"
                   "3. Quá trình dynamic dispatch diễn ra mượt mà -> in ra đầy đủ Header, Nội dung Report, và Footer. Đây là thiết kế kinh điển của <strong>Template Method Pattern</strong>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 38-42: Template Method & Hàm thuần ảo]</span>"
})

questions.append({
    "id": 32,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Lớp Trừu Tượng & Hàm Thuần Ảo",
    "title": "Quyền truy cập của hàm thuần ảo có thể thay đổi khi ghi đè ở Derived",
    "code": """#include <iostream>

class Base {
protected:
    virtual void step() = 0; // Protected ở Base
public:
    virtual ~Base() = default;
};

class Derived : public Base {
public:
    void step() override { // Công khai thành Public ở Derived!
        std::cout << "StepPublic ";
    }
};

int main() {
    Derived d;
    d.step(); // Gọi trực tiếp trên Derived
    // Base* p = &d;
    // p->step(); // Dòng P
    return 0;
}""",
    "options": [
        "A. In ra: StepPublic ; Dòng P nếu mở ra sẽ bị LỖI BIÊN DỊCH vì qua con trỏ Base* thì step() là protected",
        "B. Cả hai đều hợp lệ",
        "C. Lỗi biên dịch vì hàm override bắt buộc phải giữ nguyên mức truy cập protected",
        "D. StepPublic StepPublic"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong C++, lớp con được phép tự do thay đổi mức truy cập của hàm ảo khi override (từ protected thành public hoặc ngược lại).<br>"
                   "2. Khi gọi qua <code>d.step()</code>, kiểu tĩnh là <code>Derived</code> (nơi <code>step()</code> là public), nên lệnh gọi hợp lệ.<br>"
                   "3. Khi gọi qua <code>p->step()</code>, kiểu tĩnh là <code>Base*</code> (nơi <code>step()</code> là protected), compiler sẽ chặn ngay vì vi phạm access specifier của Base.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 21 & OOP5-Inheritance_new.pdf - Trang 38]</span>"
})

questions.append({
    "id": 33,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Lớp Trừu Tượng & Hàm Thuần Ảo",
    "title": "Bẫy dynamic_cast với Lớp Trừu Tượng không cùng nhánh (Sideways Cast)",
    "code": """#include <iostream>

struct IReader {
    virtual void read() = 0;
    virtual ~IReader() = default;
};

struct IWriter {
    virtual void write() = 0;
    virtual ~IWriter() = default;
};

struct FileStream : public IReader, public IWriter {
    void read() override { std::cout << "Reading "; }
    void write() override { std::cout << "Writing "; }
};

int main() {
    IReader* reader = new FileStream();
    // Ép kiểu ngang từ giao diện IReader sang giao diện IWriter:
    IWriter* writer = dynamic_cast<IWriter*>(reader);
    if (writer) {
        writer->write();
    }
    delete reader;
    return 0;
}""",
    "options": [
        "A. In ra: Writing (dynamic_cast hỗ trợ Sideways Cast giữa hai Abstract Class hoàn toàn không có quan hệ kế thừa với nhau nhờ RTTI)",
        "B. Lỗi biên dịch vì IReader và IWriter không cùng cây kế thừa",
        "C. writer luôn nhận giá trị nullptr",
        "D. Chương trình crash tại dynamic_cast"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Cả <code>IReader</code> và <code>IWriter</code> đều là các lớp đa hình (Polymorphic Class) chứa con trỏ VTable.<br>"
                   "2. Khi thực hiện <code>dynamic_cast<IWriter*>(reader)</code>, hệ thống RTTI kiểm tra Type Descriptor của đối tượng thực sự trong heap (đó là <code>FileStream</code>).<br>"
                   "3. Nhận thấy <code>FileStream</code> cũng đồng thời kế thừa <code>IWriter</code>, runtime tự động tính toán pointer offset để trỏ con trỏ vào subobject <code>IWriter</code>, cho phép gọi <code>write()</code> mượt mà.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 22 & C++11 RTTI Cross-cast Spec]</span>"
})

questions.append({
    "id": 34,
    "group_id": "q-group-4",
    "group_name": "Nhóm 4: Lớp Trừu Tượng & Hàm Thuần Ảo",
    "title": "Hàm thuần ảo kết hợp Tham số mặc định (Default Parameters)",
    "code": """#include <iostream>

struct Base {
    virtual void render(int mode = 1) = 0;
    virtual ~Base() = default;
};

struct Derived : public Base {
    void render(int mode = 2) override {
        std::cout << "Mode=" << mode << " ";
    }
};

int main() {
    Base* p = new Derived();
    p->render(); // Lời gọi không truyền đối số
    delete p;
    return 0;
}""",
    "options": [
        "A. Mode=1 (Tham số mặc định được nạp tĩnh lúc biên dịch theo kiểu Base*, còn hàm được dispatch động theo Derived)",
        "B. Mode=2",
        "C. Lỗi biên dịch vì hàm thuần ảo không được phép có tham số mặc định",
        "D. Lỗi runtime bad_argument"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Chuẩn C++ cho phép hàm thuần ảo có tham số mặc định.<br>"
                   "2. Vì <code>p</code> có kiểu tĩnh là <code>Base*</code>, trình biên dịch điền tham số mặc định của <code>Base::render</code> (tức <code>mode = 1</code>) vào lệnh gọi trước khi biên dịch ra mã máy.<br>"
                   "3. Khi chạy, mã máy nhảy tới <code>Derived::render</code> với tham số <code>mode = 1</code> đã được đẩy vào stack/thanh ghi -> in ra <code>Mode=1</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 21 & Default arguments in Pure Virtual]</span>"
})

print(f"Loaded {len(questions)} questions for Groups 1-4.")
# =========================================================================
# NHÓM 5: BẪY TỬ THẦN: GỌI HÀM ẢO TRONG CONSTRUCTOR & DESTRUCTOR (CÂU 35 - 42)
# =========================================================================

questions.append({
    "id": 35,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Gọi Hàm Ảo trong Constructor & Destructor",
    "title": "Bẫy Gọi Hàm Ảo trong Constructor: Vô hiệu hóa tính Đa Hình Động!",
    "code": """#include <iostream>

struct Base {
    Base() {
        whoAmI(); // Gọi hàm ảo ngay trong Constructor!
    }
    virtual void whoAmI() {
        std::cout << "Base ";
    }
};

struct Derived : public Base {
    Derived() {
        whoAmI();
    }
    void whoAmI() override {
        std::cout << "Derived ";
    }
};

int main() {
    Derived d;
    return 0;
}""",
    "options": [
        "A. Derived Derived",
        "B. Base Derived (Trong lúc Base constructor chạy, phần Derived chưa hề được hình thành nên vptr trỏ vào Base VTable, gọi Base::whoAmI)",
        "C. Base Base",
        "D. Lỗi biên dịch vì không được phép gọi hàm ảo trong constructor"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khác với Java hay C# (nơi hàm ảo trong constructor vẫn gọi tới lớp con và có thể truy cập biến chưa khởi tạo), <strong>C++ bảo vệ an toàn bộ nhớ tuyệt đối</strong>.<br>"
                   "2. Khi Constructor của <code>Base</code> đang chạy, phần đối tượng <code>Derived</code> thậm chí còn chưa được cấp phát các trường dữ liệu riêng. Nếu cho phép gọi <code>Derived::whoAmI</code>, nó sẽ thao tác trên vùng nhớ rác!<br>"
                   "3. Vì vậy, trong suốt thời gian Base Constructor chạy, con trỏ <code>vptr</code> được trỏ vào <strong>VTable của Base</strong>. Khi sang Derived Constructor, <code>vptr</code> mới được cập nhật lại trỏ vào <strong>VTable của Derived</strong>. Do đó in ra <code>Base Derived </code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 23-26 & C++ Virtual Dispatch in Ctors]</span>"
})

questions.append({
    "id": 36,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Gọi Hàm Ảo trong Constructor & Destructor",
    "title": "Sự biến đổi trạng thái của con trỏ vptr theo từng bước kế thừa",
    "code": """#include <iostream>

struct A {
    virtual void tag() { std::cout << "A "; }
    A() { tag(); }
};

struct B : public A {
    void tag() override { std::cout << "B "; }
    B() { tag(); }
};

struct C : public B {
    void tag() override { std::cout << "C "; }
    C() { tag(); }
};

int main() {
    C obj;
    return 0;
}""",
    "options": [
        "A. C C C",
        "B. A B C (vptr được cập nhật qua từng bước: VTable(A) -> VTable(B) -> VTable(C))",
        "C. A A A",
        "D. Lỗi runtime do đa tầng constructor"
    ],
    "correct": 1,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi tạo đối tượng <code>C</code>, trình biên dịch thực thi chuỗi constructor từ gốc lên ngọn:<br>"
                   "   - Bước 1: <code>A::A()</code> chạy: <code>vptr</code> trỏ vào VTable của <code>A</code> -> <code>tag()</code> in ra <code>A </code>.<br>"
                   "   - Bước 2: <code>B::B()</code> chạy: <code>vptr</code> được ghi đè trỏ vào VTable của <code>B</code> -> <code>tag()</code> in ra <code>B </code>.<br>"
                   "   - Bước 3: <code>C::C()</code> chạy: <code>vptr</code> được cập nhật trỏ vào VTable của <code>C</code> -> <code>tag()</code> in ra <code>C </code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 24-26: Trình tự khởi tạo VTable]</span>"
})

questions.append({
    "id": 37,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Gọi Hàm Ảo trong Constructor & Destructor",
    "title": "Bẫy gọi trực tiếp hàm thuần ảo trong Constructor",
    "code": """#include <iostream>

class Base {
public:
    virtual void pureFunc() = 0;
    Base() {
        // pureFunc(); // Dòng Gọi Trực Tiếp
    }
};

class Derived : public Base {
public:
    void pureFunc() override { std::cout << "DerivedPure"; }
};

int main() {
    // Derived d;
    std::cout << "CannotCallPureDirectly";
    return 0;
}""",
    "options": [
        "A. In ra: CannotCallPureDirectly; Dòng Gọi Trực Tiếp nếu mở ra sẽ bị LỖI BIÊN DỊCH ngay lập tức vì compiler phát hiện gọi trực tiếp pure virtual function trong constructor",
        "B. Gọi trực tiếp hợp lệ và in ra DerivedPure",
        "C. Chương trình biên dịch được nhưng thoát ngầm",
        "D. Tự động sinh hàm pureFunc rỗng"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Nếu lập trình viên gọi trực tiếp một hàm thuần ảo <code>pureFunc()</code> trong constructor của <code>Base</code>, hầu hết các trình biên dịch hiện đại (GCC, Clang, MSVC) sẽ phát hiện ngay tại compile-time và báo lỗi: <em>call to pure virtual function 'pureFunc'</em>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 38 & Pure virtual calls in Ctor]</span>"
})

questions.append({
    "id": 38,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Gọi Hàm Ảo trong Constructor & Destructor",
    "title": "Hiểm họa sập chương trình: Gọi hàm thuần ảo gián tiếp trong Constructor (Pure Virtual Crash)",
    "code": """#include <iostream>

class Base {
public:
    virtual void pureFunc() = 0;
    void helper() {
        pureFunc(); // Gọi gián tiếp qua hàm trợ giúp!
    }
    Base() {
        helper(); // Đánh lừa compiler!
    }
};

class Derived : public Base {
public:
    void pureFunc() override { std::cout << "DerivedPure "; }
};

int main() {
    // Derived d; // Dòng Tử Thần
    std::cout << "PureVirtualTrap";
    return 0;
}""",
    "options": [
        "A. In ra PureVirtualTrap; Nếu chạy Dòng Tử Thần, chương trình sẽ SẬP NGAY LẬP TỨC (Crash) tại runtime với thông báo lỗi: 'pure virtual method called'",
        "B. Dòng Tử Thần chạy bình thường và in ra DerivedPure",
        "C. Lỗi biên dịch tại helper()",
        "D. Chương trình ném ngoại lệ std::runtime_error có thể bắt được"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Vì lời gọi nằm bên trong hàm <code>helper()</code>, trình biên dịch không thể phát hiện lỗi lúc biên dịch (vượt qua compile-time check).<br>"
                   "2. Khi <code>Base()</code> thực thi, <code>vptr</code> trỏ vào VTable của <code>Base</code>. Trong VTable của Base, slot của <code>pureFunc</code> chứa con trỏ tới hàm xử lý lỗi của hệ thống thời gian chạy C++ (gọi là <code>__cxa_pure_virtual()</code> trên Linux hoặc <code>_purecall()</code> trên Windows).<br>"
                   "3. Hàm này in ra màn hình dòng chữ chết chóc <em>'pure virtual method called'</em> và gọi ngay <code>abort()</code> để tiêu diệt tiến trình tức thì!<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 38-40: Cơ chế __cxa_pure_virtual]</span>"
})

questions.append({
    "id": 39,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Gọi Hàm Ảo trong Constructor & Destructor",
    "title": "Hạ cấp vptr trong Destructor: Gọi hàm ảo trong lúc hủy đối tượng",
    "code": """#include <iostream>

struct Base {
    virtual void clean() { std::cout << "BaseClean "; }
    virtual ~Base() {
        clean(); // Gọi hàm ảo trong Destructor của Base!
    }
};

struct Derived : public Base {
    void clean() override { std::cout << "DerivedClean "; }
    ~Derived() override {
        clean(); // Gọi hàm ảo trong Destructor của Derived!
    }
};

int main() {
    Base* p = new Derived();
    delete p;
    return 0;
}""",
    "options": [
        "A. DerivedClean BaseClean (Trong Destructor, vptr bị 'hạ cấp' tương ứng theo từng tầng hủy: khi ở Derived dtor gọi Derived::clean, khi tụt xuống Base dtor gọi Base::clean)",
        "B. DerivedClean DerivedClean",
        "C. BaseClean BaseClean",
        "D. Lỗi runtime crash"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Khi đối tượng <code>Derived</code> bắt đầu hủy, <code>Derived::~Derived()</code> chạy với <code>vptr</code> trỏ tới Derived -> gọi <code>DerivedClean</code>.<br>"
                   "2. Khi phần <code>Derived</code> đã bị hủy xong, runtime chuyển sang gọi <code>Base::~Base()</code>. Ngay trước khi vào thân <code>Base::~Base()</code>, con trỏ <code>vptr</code> được <strong>HẠ CẤP (demoted)</strong> trỏ ngược về VTable của <code>Base</code>!<br>"
                   "3. Do đó, lời gọi <code>clean()</code> trong <code>Base::~Base()</code> sẽ gọi <code>Base::clean</code> -> in ra <code>DerivedClean BaseClean </code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 27-30: VTable trong destructor]</span>"
})

questions.append({
    "id": 40,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Gọi Hàm Ảo trong Constructor & Destructor",
    "title": "Kỹ thuật Khởi tạo Hai Pha (Two-Phase Initialization) an toàn cho Hàm Ảo",
    "code": """#include <iostream>
#include <memory>

class Worker {
protected:
    virtual void init() { std::cout << "BaseInit "; }
public:
    virtual ~Worker() = default;
    // Static Factory Method đảm bảo đối tượng xây dựng xong 100% rồi mới gọi hàm ảo!
    template <typename T>
    static std::unique_ptr<T> create() {
        auto obj = std::unique_ptr<T>(new T());
        obj->init(); // Gọi hàm ảo an toàn khi đối tượng đã hoàn chỉnh!
        return obj;
    }
};

class SpecialWorker : public Worker {
protected:
    void init() override { std::cout << "SpecialInit "; }
public:
    SpecialWorker() = default;
};

int main() {
    auto worker = Worker::create<SpecialWorker>();
    return 0;
}""",
    "options": [
        "A. SpecialInit (Two-Phase Initialization tách biệt việc cấp phát bộ nhớ và kích hoạt hàm ảo, đảm bảo đa hình chạy đúng)",
        "B. BaseInit",
        "C. BaseInit SpecialInit",
        "D. Lỗi biên dịch vì create() là hàm static"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Để tránh bẫy hàm ảo trong Constructor, các kỹ sư phần mềm C++ chuyên nghiệp sử dụng mẫu <strong>Two-Phase Initialization</strong> kết hợp <strong>Factory Method</strong>.<br>"
                   "2. Pha 1: <code>new SpecialWorker()</code> hoàn thành trọn vẹn toàn bộ chuỗi constructor, thiết lập <code>vptr</code> trỏ tới VTable của <code>SpecialWorker</code>.<br>"
                   "3. Pha 2: Lời gọi <code>obj->init()</code> diễn ra khi đối tượng đã hoàn chỉnh, kích hoạt dynamic dispatch chính xác vào <code>SpecialWorker::init</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 23-26 & Two-Phase Initialization Pattern]</span>"
})

questions.append({
    "id": 41,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Gọi Hàm Ảo trong Constructor & Destructor",
    "title": "Hiểm họa lọt con trỏ this (Leaked this pointer) ra ngoài Constructor",
    "code": """#include <iostream>

struct Base;
void inspect(Base* b);

struct Base {
    Base() {
        // inspect(this); // Lọt con trỏ this khi chưa hoàn thiện
    }
    virtual void status() { std::cout << "BaseStatus "; }
};

struct Derived : public Base {
    int secret = 777;
    void status() override { std::cout << "Secret=" << secret << " "; }
};

void inspect(Base* b) {
    b->status();
}

int main() {
    std::cout << "DangerAvoided";
    return 0;
}""",
    "options": [
        "A. In ra DangerAvoided; Nếu truyền this vào inspect(this) từ Base ctor, hàm status() sẽ gọi Base::status vì vptr lúc đó vẫn là của Base, chưa thấy được Derived",
        "B. Luôn in ra Secret=777",
        "C. Lỗi biên dịch vì this là hằng con trỏ",
        "D. Chương trình crash với lỗi nullptr"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Việc để con trỏ <code>this</code> rò rỉ (escape) ra bên ngoài constructor của lớp cha là một antipattern nguy hiểm.<br>"
                   "2. Dù hàm <code>inspect</code> nhận con trỏ <code>b</code>, nhưng do đối tượng đang nằm ở pha xây dựng của <code>Base</code>, <code>b->vptr</code> vẫn trỏ vào <code>Base VTable</code>, nên nó chỉ gọi <code>Base::status</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 23-25 & Leaked this pointer antipattern]</span>"
})

questions.append({
    "id": 42,
    "group_id": "q-group-5",
    "group_name": "Nhóm 5: Gọi Hàm Ảo trong Constructor & Destructor",
    "title": "Toán tử typeid() phản ánh đúng kiểu hiện tại của đối tượng trong Constructor",
    "code": """#include <iostream>
#include <typeinfo>

struct Base {
    virtual ~Base() = default;
    Base() {
        std::cout << (typeid(*this) == typeid(Base) ? "IsBase " : "NotBase ");
    }
};

struct Derived : public Base {
    Derived() {
        std::cout << (typeid(*this) == typeid(Derived) ? "IsDerived" : "NotDerived");
    }
};

int main() {
    Derived d;
    return 0;
}""",
    "options": [
        "A. IsBase IsDerived (Thông tin RTTI gắn liền với VTable, trong Base ctor nó nhận diện chính xác là Base, sang Derived ctor mới là Derived)",
        "B. IsDerived IsDerived",
        "C. NotBase IsDerived",
        "D. Lỗi biên dịch vì typeid không dùng được trong constructor"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Trong chuẩn C++, con trỏ tới cấu trúc RTTI (<code>std::type_info</code>) được lưu trữ ngay trước hoặc tại header của bảng ảo VTable.<br>"
                   "2. Khi Constructor của <code>Base</code> đang chạy, <code>vptr</code> trỏ vào VTable của Base, do đó <code>typeid(*this)</code> trả về <code>typeid(Base)</code>.<br>"
                   "3. Khi chuyển sang Constructor của <code>Derived</code>, <code>vptr</code> trỏ sang VTable của Derived, <code>typeid(*this)</code> lập tức cập nhật thành <code>typeid(Derived)</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 21-24 & C++11 RTTI in Constructors]</span>"
})

print(f"Loaded {len(questions)} questions for Groups 1-5.")
# =========================================================================
# NHÓM 6: ĐA HÌNH NÂNG CAO, RTTI & PATTERN THIẾT KẾ C++11 (CÂU 43 - 50)
# =========================================================================

questions.append({
    "id": 43,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Đa Hình Nâng Cao, RTTI & Design Patterns",
    "title": "Toán tử typeid xác định kiểu thực tế tại Runtime cho kiểu đa hình",
    "code": """#include <iostream>
#include <typeinfo>

struct Base {
    virtual ~Base() = default;
};

struct Derived : public Base {};

int main() {
    Base* p = new Derived();
    std::cout << (typeid(*p) == typeid(Derived) ? "MatchDerived " : "Mismatch ");
    std::cout << (typeid(*p) == typeid(Base) ? "MatchBase" : "NotBase");
    delete p;
    return 0;
}""",
    "options": [
        "A. MatchDerived NotBase (Với kiểu đa hình có virtual, typeid(*p) tra cứu RTTI tại runtime và trả về kiểu thực tế của đối tượng là Derived)",
        "B. Mismatch MatchBase (typeid chỉ xét kiểu tĩnh của con trỏ)",
        "C. MatchDerived MatchBase",
        "D. Lỗi biên dịch vì không thể so sánh hai typeid"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Chuẩn C++ quy định: Nếu biểu thức truyền vào <code>typeid</code> là một lvalue thuộc một kiểu đa hình (Polymorphic Class - có ít nhất 1 hàm virtual), nó sẽ <strong>được đánh giá tại Runtime</strong>.<br>"
                   "2. Biểu thức <code>*p</code> đọc con trỏ <code>vptr</code> trong đối tượng, truy cập vào cấu trúc <code>type_info</code> được liên kết và trả về kiểu thực sự là <code>Derived</code>.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 21 & C++11 RTTI Typeid evaluation]</span>"
})

questions.append({
    "id": 44,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Đa Hình Nâng Cao, RTTI & Design Patterns",
    "title": "Hiểm họa ném ngoại lệ std::bad_typeid khi giải tham chiếu nullptr",
    "code": """#include <iostream>
#include <typeinfo>

struct Base {
    virtual ~Base() = default;
};

int main() {
    Base* p = nullptr;
    try {
        std::cout << typeid(*p).name(); // Giải tham chiếu nullptr bên trong typeid!
    } catch (const std::bad_typeid& e) {
        std::cout << "CaughtBadTypeid";
    }
    return 0;
}""",
    "options": [
        "A. CaughtBadTypeid (Chuẩn C++ quy định nếu biểu thức đa hình trong typeid là *p với p == nullptr, runtime bắt buộc phải ném ngoại lệ std::bad_typeid thay vì crash)",
        "B. Chương trình crash với lỗi Segmentation Fault",
        "C. In ra chuỗi Base",
        "D. In ra chuỗi nullptr"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Đây là cơ chế an toàn đặc biệt của C++: Khi thực hiện <code>typeid(*p)</code> trên một kiểu đa hình, trình biên dịch tự động chèn một đoạn kiểm tra: <code>if (p == nullptr) throw std::bad_typeid();</code> trước khi truy cập bộ nhớ.<br>"
                   "2. Điều này ngăn chặn việc CPU truy cập vào địa chỉ 0x0 để đọc <code>vptr</code>, biến một lỗi sập chương trình nghiêm trọng thành một ngoại lệ có thể bắt và xử lý được.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 21 & std::bad_typeid specification]</span>"
})

questions.append({
    "id": 45,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Đa Hình Nâng Cao, RTTI & Design Patterns",
    "title": "So sánh dynamic_cast vs typeid: Đẳng cấu kiểu chính xác vs Quan hệ thừa kế",
    "code": """#include <iostream>
#include <typeinfo>

struct Base { virtual ~Base() = default; };
struct Derived : public Base {};

void test(Base* p) {
    // Cách 1: dùng dynamic_cast
    bool isSubtype = (dynamic_cast<Derived*>(p) != nullptr);
    // Cách 2: dùng typeid
    bool isExactType = (typeid(*p) == typeid(Base));

    std::cout << isSubtype << " " << isExactType;
}

int main() {
    Derived d;
    test(&d);
    return 0;
}""",
    "options": [
        "A. 1 0 (dynamic_cast kiểm tra quan hệ IS-A kế thừa, còn typeid kiểm tra chính xác 100% kiểu lớp cụ thể)",
        "B. 1 1",
        "C. 0 0",
        "D. 0 1"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <code>dynamic_cast<Derived*>(p)</code> trả về true (con trỏ khác null) vì <code>d</code> là một thể hiện của <code>Derived</code> (thỏa mãn quan hệ IS-A).<br>"
                   "2. <code>typeid(*p) == typeid(Base)</code> trả về false (0) vì kiểu thực tế của đối tượng là <code>Derived</code>, không phải <code>Base</code>. <code>typeid</code> chỉ trả về true khi hai kiểu hoàn toàn trùng khớp chính xác (Exact type identity).<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 21-23 & RTTI type comparison]</span>"
})

questions.append({
    "id": 46,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Đa Hình Nâng Cao, RTTI & Design Patterns",
    "title": "Mẫu thiết kế Non-Virtual Interface (NVI Idiom) trong C++11",
    "code": """#include <iostream>

class GameCharacter {
public:
    // Giao diện public là NON-VIRTUAL
    void attack() {
        std::cout << "PrepWeapon ";
        doAttack(); // Gọi cài đặt cụ thể
        std::cout << "Cooldown ";
    }
    virtual ~GameCharacter() = default;
private:
    // Cài đặt ảo là PRIVATE
    virtual void doAttack() {
        std::cout << "FistPunch ";
    }
};

class Warrior : public GameCharacter {
private:
    void doAttack() override {
        std::cout << "SwordSlash ";
    }
};

int main() {
    GameCharacter* hero = new Warrior();
    hero->attack();
    delete hero;
    return 0;
}""",
    "options": [
        "A. PrepWeapon SwordSlash Cooldown (NVI Idiom: lớp cơ sở kiểm soát luồng thực thi chung qua hàm public non-virtual, lớp con tùy biến hành vi qua private virtual)",
        "B. PrepWeapon FistPunch Cooldown",
        "C. Lỗi biên dịch vì hàm doAttack() là private trong Warrior",
        "D. Chỉ in ra SwordSlash"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Đây là <strong>NVI Idiom (Non-Virtual Interface)</strong> - một trong những triết lý thiết kế hướng đối tượng được khuyến nghị bởi các chuyên gia C++ hàng đầu thế giới (Herb Sutter).<br>"
                   "2. Lớp cha kiểm soát chặt chẽ điều kiện tiên quyết (Pre-conditions: <code>PrepWeapon</code>) và hậu điều kiện (Post-conditions: <code>Cooldown</code>).<br>"
                   "3. Lớp con <code>Warrior</code> được phép ghi đè phương thức <code>private virtual doAttack()</code> thông qua bảng VTable mà không làm phá vỡ kiến trúc lớp cha.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 21-24 & Herb Sutter's NVI Idiom]</span>"
})

questions.append({
    "id": 47,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Đa Hình Nâng Cao, RTTI & Design Patterns",
    "title": "Khả năng Inline của Hàm Ảo (Virtual Function Inlining)",
    "code": """#include <iostream>

struct Base {
    virtual int getVal() { return 10; }
};

int main() {
    Base b;
    int v1 = b.getVal(); // Trường hợp 1: Gọi qua biến giá trị

    Base* p = &b;
    int v2 = p->getVal(); // Trường hợp 2: Gọi qua con trỏ
    
    std::cout << v1 << " " << v2;
    return 0;
}""",
    "options": [
        "A. 10 10 (Trường hợp 1 trình biên dịch hoàn toàn có thể INLINE hàm ảo vì biết chắc 100% kiểu đối tượng; Trường hợp 2 thường không thể inline vì phải qua con trỏ VTable)",
        "B. Hàm ảo tuyệt đối không bao giờ được phép inline trong bất kỳ trường hợp nào",
        "C. Cả hai trường hợp đều bắt buộc tra cứu VTable lúc runtime",
        "D. Lỗi biên dịch"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Một ngộ nhận phổ biến là 'hàm ảo không thể inline'.<br>"
                   "2. Thực tế, khi gọi hàm ảo trên một đối tượng cụ thể bằng giá trị (<code>b.getVal()</code>), trình biên dịch xác định được chính xác kiểu tại compile-time, nên nó có toàn quyền <strong>Devirtualize và Inline Expansion</strong> mã nguồn để đạt hiệu năng tối đa.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 25-26 & Virtual Inlining Optimization]</span>"
})

questions.append({
    "id": 48,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Đa Hình Nâng Cao, RTTI & Design Patterns",
    "title": "Bẫy Hàm Ảo Tái Khai Báo Tham Số Mặc Định Khác Nhau",
    "code": """#include <iostream>

struct Base {
    virtual void show(int x = 100) {
        std::cout << "Base:" << x << " ";
    }
};

struct Derived : public Base {
    void show(int x = 200) override {
        std::cout << "Derived:" << x << " ";
    }
};

int main() {
    Derived d;
    Base* pB = &d;
    Derived* pD = &d;

    pB->show(); // Gọi qua con trỏ Base*
    pD->show(); // Gọi qua con trỏ Derived*
    return 0;
}""",
    "options": [
        "A. Derived:100 Derived:200 (Cùng một đối tượng thực tế d và cùng hàm ảo Derived::show, nhưng tham số mặc định được nạp tĩnh lúc biên dịch theo kiểu tĩnh của từng con trỏ!)",
        "B. Derived:200 Derived:200",
        "C. Base:100 Derived:200",
        "D. Lỗi biên dịch do khai báo tham số mặc định xung đột"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <strong>Cảnh báo thiết kế kinh điển:</strong> Tuyệt đối không bao giờ định nghĩa lại giá trị tham số mặc định cho một hàm ảo bị ghi đè!<br>"
                   "2. Vì tham số mặc định được gắn tĩnh tại call-site lúc biên dịch:<br>"
                   "   - <code>pB->show()</code> có kiểu tĩnh là <code>Base*</code> -> compiler chèn giá trị <code>100</code>.<br>"
                   "   - <code>pD->show()</code> có kiểu tĩnh là <code>Derived*</code> -> compiler chèn giá trị <code>200</code>.<br>"
                   "3. Cả hai đều nhảy vào hàm ảo <code>Derived::show</code> tại runtime, tạo ra hai kết quả khác biệt gây bối rối tột độ.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 21 & Scott Meyers Effective C++ Item 37]</span>"
})

questions.append({
    "id": 49,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Đa Hình Nâng Cao, RTTI & Design Patterns",
    "title": "Đa Hình Tĩnh CRTP (Curiously Recurring Template Pattern) loại bỏ chi phí VTable",
    "code": """#include <iostream>

template <typename Derived>
struct BaseStatic {
    void interface() {
        static_cast<Derived*>(this)->actualImplementation();
    }
};

struct MyService : public BaseStatic<MyService> {
    void actualImplementation() {
        std::cout << "CRTP_Success ";
    }
};

int main() {
    MyService service;
    service.interface();
    std::cout << "Size=" << sizeof(service);
    return 0;
}""",
    "options": [
        "A. CRTP_Success Size=1 (CRTP cài đặt đa hình hoàn toàn tại thời điểm biên dịch, không hề tốn con trỏ vptr hay bảng VTable, kích thước đối tượng rỗng chỉ là 1 byte)",
        "B. CRTP_Success Size=8 (vẫn tốn vptr)",
        "C. Lỗi biên dịch vì MyService chưa hoàn chỉnh khi truyền vào BaseStatic",
        "D. Chương trình crash do static_cast không an toàn"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. <strong>CRTP (Curiously Recurring Template Pattern)</strong> là kỹ thuật cài đặt <em>Đa hình tĩnh (Static Polymorphism)</em> thượng thừa trong C++.<br>"
                   "2. Bằng cách kế thừa từ template chính nó (<code>BaseStatic<MyService></code>), lớp cha có thể ép kiểu con trỏ <code>this</code> về lớp con và gọi phương thức thực thi lúc biên dịch.<br>"
                   "3. Không có con trỏ <code>vptr</code>, không có bảng <code>VTable</code>, không có chi phí gọi gián tiếp runtime, và trình biên dịch có thể inline 100% mã nguồn.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 18-20: Đa hình tĩnh & Hiệu năng tối đa]</span>"
})

questions.append({
    "id": 50,
    "group_id": "q-group-6",
    "group_name": "Nhóm 6: Đa Hình Nâng Cao, RTTI & Design Patterns",
    "title": "Tương tác giữa Đa Hình và Vòng Đời Đối Tượng: Đơn vị thu hồi bộ nhớ của Toán Tử delete",
    "code": """#include <iostream>

struct Base {
    virtual ~Base() { std::cout << "~Base "; }
};

struct BigDerived : public Base {
    char memoryChunk[1024];
    ~BigDerived() override { std::cout << "~BigDerived "; }
};

int main() {
    Base* p = new BigDerived();
    delete p;
    return 0;
}""",
    "options": [
        "A. ~BigDerived ~Base (Toán tử delete thực hiện 2 việc: gọi virtual destructor qua VTable, và sau đó chuyển địa chỉ gốc cho operator delete(void*) để thu hồi trọn vẹn 1024 bytes)",
        "B. Chỉ in ra ~Base và chỉ thu hồi sizeof(Base)",
        "C. Lỗi biên dịch",
        "D. Thu hồi bộ nhớ bị lỗi phân mảnh"
    ],
    "correct": 0,
    "explanation": "<b>Cơ chế dưới gầm máy:</b><br>"
                   "1. Lệnh <code>delete p;</code> thực hiện chính xác 2 bước độc lập dưới gầm máy:<br>"
                   "   - Bước 1: Tra cứu VTable để thực thi đúng chuỗi Destructor ảo từ <code>BigDerived::~BigDerived()</code> ngược về <code>Base::~Base()</code>.<br>"
                   "   - Bước 2: Gọi hàm giải phóng bộ nhớ <code>operator delete(void* ptr)</code>. Do heap manager lưu trữ kích thước cấp phát trong Heap Control Block (Cookie) phía trước con trỏ cấp phát ban đầu, toàn bộ khối 1024 bytes + Base subobject được trả về cho hệ điều hành một cách hoàn hảo.<br>"
                   "<span class=\"citation-badge\">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 27-30 & C++ Memory Deallocation Model]</span>"
})

print(f"Loaded ALL {len(questions)} questions for Chapter 6 successfully!")
