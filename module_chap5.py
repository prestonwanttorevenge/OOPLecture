# -*- coding: utf-8 -*-

chap5_text = r"""
% ==============================================================================
% CHƯƠNG 5: ĐA HÌNH & LIÊN KẾT ĐỘNG (POLYMORPHISM & DYNAMIC BINDING)
% ==============================================================================
\chapter{Đa hình \& Liên kết Động (Polymorphism \& Dynamic Binding)}

\begin{theorybox}[Định Nghĩa: Tính Đa Hình (Polymorphism)]
\textbf{Đa hình (Polymorphism)} --- xuất phát từ tiếng Hy Lạp cổ mang nghĩa "nhiều hình thái" --- là trụ cột thứ ba và là linh hồn của Lập trình Hướng Đối tượng. Đa hình cho phép một biến con trỏ hoặc tham chiếu thuộc lớp cơ sở (\texttt{Base}) có khả năng trỏ tới đối tượng của bất kỳ lớp phái sinh nào (\texttt{Derived}), và khi thực hiện lời gọi hàm thành viên, phiên bản hàm chính xác tương ứng với kiểu đối tượng thực tế sẽ được kích hoạt.\footnote{Nguồn: OOP6-Polymorphism\_new.pdf - Trang 3-7: Khái niệm tính đa hình trong lập trình hướng đối tượng}
\end{theorybox}

\section{Triết lý Đa hình \& Cơ chế Liên kết (Binding)}

Để hiểu sâu sắc bản chất của Đa hình, ta phải phân tích sự khác biệt cốt tử giữa hai cơ chế liên kết lời gọi hàm với mã máy:

\begin{enumerate}
    \item \textbf{Liên kết Tĩnh (Early Binding / Static Binding):}
    \begin{itemize}
        \item Xảy ra tại \textbf{thời điểm biên dịch (Compile-time)}. Trình biên dịch dựa hoàn toàn vào \textbf{kiểu dữ liệu tĩnh (Static Type)} của biến hoặc con trỏ để xác định địa chỉ hàm cần thực thi.
        \item Mã máy sinh ra là một lệnh nhảy trực tiếp: \texttt{call 0x004012A0}.
        \item \textit{Ưu điểm:} Tốc độ thực thi cực nhanh, không tốn thêm bất kỳ byte bộ nhớ nào, cho phép trình biên dịch thực hiện tối ưu hóa nội dòng (\textbf{Function Inlining}).
        \item \textit{Nhược điểm:} Thiếu sự linh hoạt, không thể thay đổi hành vi theo ngữ cảnh thời gian chạy.
    \end{itemize}

    \item \textbf{Liên kết Động (Late Binding / Dynamic Binding):}
    \begin{itemize}
        \item Xảy ra tại \textbf{thời điểm thực thi (Runtime)}. Việc quyết định gọi phiên bản hàm nào được hoãn lại cho tới khi chương trình đang chạy, dựa vào \textbf{kiểu dữ liệu thực tế (Dynamic Type)} của đối tượng mà con trỏ đang trỏ tới.
        \item Mã máy sinh ra là một lệnh nhảy gián tiếp thông qua con trỏ bộ nhớ: \texttt{call qword ptr [rax + offset]}.
        \item \textit{Ưu điểm:} Tạo ra kiến trúc phần mềm mở rộng cực kỳ mạnh mẽ (Open-Closed Principle: mở rộng bằng cách thêm lớp mới mà không cần sửa code cũ).
        \item \textit{Nhược điểm:} Tốn chi phí gián tiếp (Indirection overhead), tăng kích thước đối tượng và vô hiệu hóa inlining.\footnote{Nguồn: OOP6-Polymorphism\_new.pdf - Trang 8-15: Early Binding vs Late Binding}
    \end{itemize}
\end{enumerate}

\begin{theorybox}[Nguyên Lý Zero-Overhead Của C++]
Trong các ngôn ngữ như Java hay C\#, mọi phương thức thành viên mặc định đều là \textbf{Dynamic Binding}. Ngược lại, triết lý thiết kế của C++ kiên định với tôn chỉ \textbf{Zero-Overhead Principle}: \textit{"Bạn không phải trả giá cho những gì bạn không sử dụng"}. 

Do đó, trong C++, mọi hàm thành viên mặc định \textbf{100\% là Static Binding}. Chỉ khi lập trình viên chủ động gắn từ khóa \texttt{virtual}, trình biên dịch mới kích hoạt cơ chế Dynamic Binding!
\end{theorybox}

\section{Hàm Ảo, \texttt{override} và \texttt{final} trong C++11}

\subsection{Cơ chế Hàm Ảo (\texttt{virtual})}

Khi khai báo một phương thức với từ khóa \texttt{virtual} ở lớp cơ sở, ta đã thiết lập một "hợp đồng đa hình":
\begin{lstlisting}[language=C++]
class Shape {
public:
    virtual void draw() const {
        std::cout << "Drawing generic shape\n";
    }
    virtual ~Shape() = default;
};

class Circle : public Shape {
public:
    void draw() const override { // Override virtual method
        std::cout << "Drawing Circle\n";
    }
};
\end{lstlisting}

\textbf{Quy tắc lan truyền ảo (Virtual Propagation):} Một khi một phương thức đã được khai báo là \texttt{virtual} ở lớp cơ sở, nó sẽ \textbf{tự động mang tính ảo vĩnh viễn} trong toàn bộ cây thừa kế của các lớp con cháu, cho dù ở lớp con ta có viết lại từ khóa \texttt{virtual} hay không.\footnote{Nguồn: OOP6-Polymorphism\_new.pdf - Trang 16-22: Khai báo và ghi đè hàm ảo}

\subsection{Bộ Đôi Từ Khóa Ngữ Cảnh C++11: \texttt{override} và \texttt{final}}

Trước C++11, lỗi ngầm phổ biến nhất của lập trình viên là viết sai chữ ký hàm con dẫn đến việc vô tình tạo ra một hàm mới thay vì ghi đè hàm cha:
\begin{lstlisting}[language=C++]
class Base {
public:
    virtual void process(int x) const;
};

// C++98: Signature mismatch pitfall
class Derived : public Base {
public:
    void process(long x) const; // LOGICAL FLAW: Overloads instead of overriding!
    void process(int x);        // LOGICAL FLAW: Missing const qualifier!
};
\end{lstlisting}

Để chấm dứt thảm họa này, chuẩn C++11 bổ sung hai từ khóa ngữ cảnh (\textit{contextual keywords}):

\begin{itemize}
    \item \textbf{\texttt{override}}: Yêu cầu trình biên dịch kiểm tra nghiêm ngặt xem hàm này có thực sự ghi đè một hàm ảo nào từ lớp cha hay không. Nếu chữ ký hàm, kiểu trả về, hoặc thuộc tính \texttt{const} không khớp 100\%, trình biên dịch lập tức báo lỗi biên dịch (\textit{Compilation Error}):
    \begin{lstlisting}[language=C++]
    class DerivedC11 : public Base {
    public:
        void process(int x) const override; // VALID: Perfectly matches Base signature
        // void process(long x) const override; // COMPILATION ERROR: Detected immediately!
    };
    \end{lstlisting}

    \item \textbf{\texttt{final}}: Mang hai mục đích kiểm soát kiến trúc:
    \begin{enumerate}
        \item Khóa không cho lớp con tiếp tục ghi đè phương thức ảo:
        \begin{lstlisting}[language=C++]
        virtual void process(int x) const override final; // Blocks further overriding
        \end{lstlisting}
        \item Khóa không cho phép bất kỳ lớp nào kế thừa từ lớp này nữa:
        \begin{lstlisting}[language=C++]
        class SecureKey final : public Base { /* ... */ }; // Prohibits inheritance
        \end{lstlisting}
    \end{enumerate}
    \textit{Tối ưu hóa Devirtualization:} Khi trình biên dịch thấy một hàm hoặc lớp được đánh dấu \texttt{final}, nó có thể biến đổi các lời gọi gián tiếp thành lệnh gọi trực tiếp (\textbf{Direct Call}), loại bỏ hoàn toàn chi phí tra cứu bảng ảo!\footnote{Nguồn: OOP6-Polymorphism\_new.pdf - Trang 23-28: Từ khóa override và final trong C++11}
\end{itemize}

\section{Phân tích Dưới Gầm Máy: Bảng Ảo (VTable) \& Con trỏ vptr}

Làm thế nào mà CPU có thể tìm ra đúng hàm \texttt{Circle::draw()} khi nó chỉ đang giữ một con trỏ kiểu \texttt{Shape*}? Đây là bí ẩn cấu trúc sâu sắc nhất của C++.

\begin{figure}[htbp]
\centering
\resizebox{0.95\textwidth}{!}{%
\begin{tikzpicture}[every node/.style={font=\small\sffamily, align=center}]
    % Object RAM on left
    \draw[thick, fill=bgsoftblue, draw=primaryblue, rounded corners=2pt] (0, 0) rectangle (4.2, 4.2);
    \node[above, font=\bfseries\sffamily, primaryblue] at (2.1, 4.2) {Đối Tượng Circle (Stack/Heap)};

    \draw[thick, fill=white, draw=primaryblue] (0.2, 3.1) rectangle (4.0, 3.9);
    \node at (2.1, 3.5) {\textbf{\texttt{\_\_vptr}} (8 bytes con trỏ ẩn)};

    \draw[thick, fill=white, draw=primaryblue] (0.2, 1.8) rectangle (4.0, 2.9);
    \node at (2.1, 2.35) {\texttt{int id} (4 bytes)};

    \draw[thick, fill=white, draw=primaryblue] (0.2, 0.4) rectangle (4.0, 1.6);
    \node at (2.1, 1.0) {\texttt{double radius} (8 bytes)};

    % VTable in .rodata on right
    \draw[thick, fill=bglighterblue, draw=accentblue, rounded corners=2pt] (7.5, 0.4) rectangle (13.5, 4.2);
    \node[above, font=\bfseries\sffamily, darkblue] at (10.5, 4.2) {VTable của Circle (.rodata)};

    \draw[thick, fill=white, draw=accentblue] (7.8, 3.0) rectangle (13.2, 3.8);
    \node at (10.5, 3.4) {\texttt{Slot [0]: \&Circle::draw()}};

    \draw[thick, fill=white, draw=accentblue] (7.8, 2.0) rectangle (13.2, 2.8);
    \node at (10.5, 2.4) {\texttt{Slot [1]: \&Circle::area()}};

    \draw[thick, fill=white, draw=accentblue] (7.8, 0.8) rectangle (13.2, 1.6);
    \node at (10.5, 1.2) {\texttt{Slot [2]: \&Circle::\textasciitilde{}Circle()}};

    % Pointer arrow from __vptr to VTable
    \draw[-{Stealth[length=3mm]}, ultra thick, accentblue] (4.0, 3.5) -- (7.5, 3.5) node[midway, above=2pt, font=\footnotesize\bfseries] {Trỏ bảng ảo};
\end{tikzpicture}%
}
\caption{Cấu trúc nhị phân của Bảng Phương Thức Ảo (VTable) và con trỏ \texttt{\_\_vptr} trong bộ nhớ.}
\end{figure}

\begin{underhoodbox}[Kiến Trúc Bảng Ảo VTable và Con Trỏ vptr Dưới RAM]
Để hiện thực hóa Dynamic Binding mà không phải trả giá bằng việc kiểm tra kiểu dạng chuỗi chậm chạp (\texttt{instanceof}), trình biên dịch C++ sử dụng một cấu trúc dữ liệu nhị phân nội tại:

\begin{enumerate}
    \item \textbf{Virtual Method Table (VTable):}
    \begin{itemize}
        \item Là một mảng tĩnh các con trỏ hàm (\texttt{const void*[]}), được trình biên dịch sinh ra duy nhất một bản cho \textbf{mỗi lớp có ít nhất một hàm ảo}.
        \item VTable được lưu trữ trong phân vùng bộ nhớ chỉ đọc (\textbf{Read-Only Data Segment} --- \texttt{.rodata} trên Linux ELF hoặc \texttt{.rdata} trên Windows PE). Nó tồn tại suốt vòng đời của tiến trình.
        \item Mỗi phần tử trong VTable chứa địa chỉ bắt đầu của mã máy của một phương thức ảo tương ứng theo thứ tự khai báo.
    \end{itemize}

    \item \textbf{Virtual Table Pointer (vptr):}
    \begin{itemize}
        \item Khi một lớp có hàm ảo, trình biên dịch âm thầm chèn thêm một trường dữ liệu ẩn vào đầu đối tượng: con trỏ \texttt{\_\_vptr} (kích thước 8 bytes trên nền tảng 64-bit).
        \item Con trỏ \texttt{vptr} này trỏ thẳng tới bảng VTable tương ứng của lớp mà đối tượng thuộc về.
        \item \texttt{vptr} được tự động thiết lập bởi mã máy của \textbf{Constructor} ngay khi đối tượng được sinh ra trong RAM.
    \end{itemize}
\end{enumerate}

\textbf{Giải phẫu Lệnh Nhảy Gián Tiếp (Indirect Dispatching):}
Khi thực thi dòng lệnh \texttt{pShape->draw()}:
\begin{enumerate}
    \item CPU lấy địa chỉ của đối tượng từ thanh ghi con trỏ \texttt{pShape} (ví dụ \texttt{RCX} hoặc \texttt{RDI}).
    \item CPU giải tham chiếu offset 0 để lấy giá trị con trỏ \texttt{\_\_vptr}: \texttt{RAX = *(pShape)}.
    \item CPU tra cứu mảng VTable tại vị trí của hàm \texttt{draw()} (ví dụ slot 0): \texttt{RDX = *(RAX + 0)}.
    \item CPU thực hiện lệnh nhảy gián tiếp: \texttt{call RDX}, đồng thời truyền con trỏ đối tượng \texttt{pShape} làm con trỏ \texttt{this} ẩn.\footnote{Nguồn: OOP6-Polymorphism\_new.pdf - Trang 29-45: Kiến trúc VTable, vptr và Assembly Dispatch}
\end{enumerate}
\end{underhoodbox}

\subsection{Cơ Chế Điều Chỉnh Con Trỏ Thunk (Adjustor Thunk)}

Trong Đa kế thừa (Multiple Inheritance), khi một lớp \texttt{C} kế thừa từ cả \texttt{A} và \texttt{B}:
\begin{lstlisting}[language=C++]
class A { public: virtual void fa() {} };
class B { public: virtual void fb() {} };
class C : public A, public B {
public:
    void fa() override {}
    void fb() override {}
};
\end{lstlisting}

Trong lòng đối tượng \texttt{C}, Subobject \texttt{A} nằm ở offset 0, nhưng Subobject \texttt{B} nằm ở offset lệch đi một khoảng $\Delta$ (ví dụ $+8$ bytes). Khi ta gọi:
\begin{lstlisting}[language=C++]
B* pb = new C();
pb->fb(); // Invokes virtual method of B on object C
\end{lstlisting}

Lúc này, thanh ghi con trỏ truyền vào hàm \texttt{C::fb()} đang trỏ vào Subobject \texttt{B} (tại offset $+8$), trong khi mã máy của \texttt{C::fb()} lại kỳ vọng con trỏ \texttt{this} trỏ vào đầu đối tượng toàn vẹn \texttt{C} (tại offset 0)!

\textbf{Giải pháp Thunk:} Trình biên dịch sinh ra một đoạn mã đệm siêu nhỏ gọi là \textbf{Adjustor Thunk}. Trong VTable của Subobject \texttt{B}, địa chỉ hàm không trỏ thẳng vào \texttt{C::fb()}, mà trỏ vào Thunk:
\begin{lstlisting}[language={[x86masm]Assembler}]
__thunk_for_C_fb:
    sub rcx, 8          ; Rewind this pointer to offset 0 of full object C
    jmp C::fb           ; Direct jump to actual implementation
\end{lstlisting}
Đây là minh chứng tuyệt đỉnh cho sự tinh vi của các kỹ sư thiết kế trình biên dịch C++ để bảo đảm an toàn bộ nhớ tuyệt đối.

\section{Hàm Thuần Ảo \& Lớp Cơ Sở Trừu Tượng (Abstract Base Classes)}

\begin{theorybox}[Lớp Trừu Tượng (Abstract Base Class - ABC)]
Một hàm ảo được gán cú pháp \texttt{= 0} ở cuối khai báo được gọi là một \textbf{Hàm thuần ảo (Pure Virtual Function)}.

Một lớp chứa ít nhất một hàm thuần ảo được định nghĩa là một \textbf{Lớp Cơ sở Trừu tượng (Abstract Base Class)}. Đặc tính tối thượng của lớp trừu tượng là:
\begin{itemize}
    \item \textbf{Tuyệt đối không thể khởi tạo thực thể (Cannot instantiate)} trực tiếp trên Stack hoặc Heap. Cố tình viết \texttt{Shape s;} sẽ dẫn đến lỗi biên dịch ngay lập tức.
    \item Lớp con kế thừa từ ABC bắt buộc phải ghi đè (\texttt{override}) và hiện thực hóa toàn bộ các hàm thuần ảo; nếu bỏ sót dù chỉ một hàm, lớp con đó tiếp tục bị coi là lớp trừu tượng!\footnote{Nguồn: OOP6-Polymorphism\_new.pdf - Trang 46-55: Hàm thuần ảo và lớp cơ sở trừu tượng}
\end{itemize}
\end{theorybox}

\begin{lstlisting}[language=C++]
class IDevice {
public:
    virtual void boot() = 0;      // Pure virtual function
    virtual void shutdown() = 0;  // Pure virtual function
    virtual ~IDevice() = default;
};
\end{lstlisting}

\subsection{Bẫy Tinh Vi: Hàm Thuần Ảo Vẫn Có Thể Có Body!}

Rất nhiều lập trình viên C++ nhầm tưởng rằng hàm thuần ảo (\texttt{= 0}) thì không được phép có phần thân code (body). Đây là một sai lầm phổ biến!

Chuẩn C++ cho phép hoàn toàn việc viết định nghĩa (body) cho một hàm thuần ảo, miễn là phần định nghĩa đó nằm \textbf{bên ngoài khai báo của lớp}:
\begin{lstlisting}[language=C++]
class BaseAbstract {
public:
    virtual void logStatus() = 0; // Pure virtual, BaseAbstract is ABC!
    virtual ~BaseAbstract() = default;
};

// Define body for pure virtual function OUTSIDE class declaration:
void BaseAbstract::logStatus() {
    std::cout << "[BASE AUDIT LOG] Standard audit log record\n";
}

class ConcreteChild : public BaseAbstract {
public:
    void logStatus() override {
        // Reuse base default implementation, then add custom logic:
        BaseAbstract::logStatus(); 
        std::cout << "[CHILD LOG] Custom specialized processing\n";
    }
};
\end{lstlisting}

\textit{Ý nghĩa kiến trúc:} Kỹ thuật này cho phép kiến trúc sư hệ thống vừa \textbf{ép buộc lớp con phải chủ động override} (không thể vô tình quên), vừa \textbf{cung cấp sẵn mã nguồn mặc định tái sử dụng} cho các lớp con gọi khi cần thiết.

\subsection{Pure Virtual Destructor: Phải Luôn Có Body!}

Nếu bạn muốn tạo một Abstract Base Class nhưng lớp của bạn không có hàm nghiệp vụ nào để gán \texttt{= 0}, bạn có thể biến Destructor thành thuần ảo:
\begin{lstlisting}[language=C++]
class InterfaceOnly {
public:
    virtual ~InterfaceOnly() = 0; // Pure virtual destructor makes class ABC
};

// MANDATORY DEFINITION OUTSIDE CLASS BODY:
InterfaceOnly::~InterfaceOnly() {} 
\end{lstlisting}
\begin{warningbox}
Nếu bạn quên không viết định nghĩa rỗng \texttt{InterfaceOnly::\textasciitilde{}InterfaceOnly() \{\}}, trình biên dịch sẽ cho qua nhưng \textbf{Trình liên kết (Linker) sẽ báo lỗi sập hệ thống (Undefined Reference / LNK2019)} ngay khi bất kỳ lớp con nào bị hủy, bởi vì trong chuỗi hủy kế thừa, Destructor của lớp con luôn tự động gọi ngầm Destructor của lớp cha!
\end{warningbox}

\section{Destructor Ảo (Virtual Destructor) --- Luật Sống Còn}

Đây là câu hỏi phỏng vấn kinh điển và là bẫy rò rỉ bộ nhớ phổ biến nhất trong các dự án C++ thực tế. Hãy quan sát đoạn mã thảm họa sau:

\begin{lstlisting}[language=C++]
class BaseResource {
public:
    BaseResource() { std::cout << "Base acquired\n"; }
    ~BaseResource() { std::cout << "Base freed\n"; } // Non-virtual destructor!
};

class DerivedResource : public BaseResource {
private:
    int* largeBuffer;
public:
    DerivedResource() : largeBuffer(new int[1000000]) {
        std::cout << "Derived allocated 4MB RAM\n";
    }
    ~DerivedResource() {
        delete[] largeBuffer; // Free 4MB RAM
        std::cout << "Derived buffer freed successfully\n";
    }
};

void cleanup() {
    BaseResource* ptr = new DerivedResource();
    delete ptr; // THAM HOA RO RI BO NHO XAY RA TAI DAY!
}
\end{lstlisting}

\begin{underhoodbox}[Phân Tích Cơ Chế Thảm Họa Khi Thiếu Virtual Destructor]
Tại dòng lệnh \texttt{delete ptr;}:
\begin{enumerate}
    \item Con trỏ \texttt{ptr} có kiểu tĩnh là \texttt{BaseResource*}.
    \item Vì Destructor \texttt{\textasciitilde{}BaseResource()} \textbf{KHÔNG CÓ TỪ KHÓA \texttt{virtual}}, trình biên dịch áp dụng cơ chế \textbf{Static Binding (Early Binding)}.
    \item Trình biên dịch sinh mã máy gọi trực tiếp địa chỉ của hàm \texttt{BaseResource::\textasciitilde{}BaseResource()}.
    \item \textbf{Hậu quả:} Hàm \texttt{DerivedResource::\textasciitilde{}DerivedResource()} \textbf{HOÀN TOÀN BỊ BỎ QUA}! Lệnh \texttt{delete[] largeBuffer} không bao giờ được chạy. Toàn bộ 4 Megabytes RAM bị rò rỉ vĩnh viễn trong không gian nhớ của hệ điều hành!
    \item Tệ hơn nữa, chuẩn ISO C++11 quy định: Việc xóa một đối tượng phái sinh thông qua con trỏ lớp cơ sở không có virtual destructor dẫn đến \textbf{Hành Vi Không Xác Định (Undefined Behavior)}.\footnote{Nguồn: OOP6-Polymorphism\_new.pdf - Trang 59-65: Virtual Destructor và Hiểm họa rò rỉ bộ nhớ}
\end{enumerate}
\end{underhoodbox}

\begin{theorybox}[Quy Tắc Vàng Của Scott Meyers Về Destructor]
\begin{itemize}
    \item \textbf{Quy tắc 1:} Bất kỳ lớp nào được thiết kế để làm lớp cơ sở có tính đa hình (\textit{Polymorphic Base Class}), Destructor của nó \textbf{BẮT BUỘC PHẢI LÀ \texttt{public virtual}}.
    \item \textbf{Quy tắc 2:} Nếu một lớp không được thiết kế để làm lớp cha đa hình (hoặc không muốn cho phép người dùng xóa qua con trỏ lớp cơ sở), hãy khai báo Destructor là \textbf{\texttt{protected non-virtual}}. Cách này ngăn chặn hoàn toàn việc gọi \texttt{delete ptrBase} từ bên ngoài, triệt tiêu lỗi rò rỉ ngay tại compile-time!
\end{itemize}
\end{theorybox}

\section{Bẫy Tử Thần: Gọi Hàm Ảo Trong Constructor \& Destructor}

Trong các ngôn ngữ như Java hoặc C\#, gọi một phương thức ảo trong Constructor sẽ nhảy ngay tới phiên bản của lớp con. Tuy nhiên, trong C++, hành động này là một \textbf{Bẫy chết người} có thể làm sập toàn bộ ứng dụng!

\begin{lstlisting}[language=C++]
class Transaction {
public:
    Transaction() {
        logCreation(); // Pitfall: Virtual call in Constructor!
    }
    virtual void logCreation() const {
        std::cout << "Base Transaction logged\n";
    }
    virtual ~Transaction() = default;
};

class BuyTransaction : public Transaction {
private:
    std::string stockCode;
public:
    BuyTransaction(const std::string& code) : stockCode(code) {}
    void logCreation() const override {
        std::cout << "BuyTransaction logged for: " << stockCode << "\n";
    }
};
\end{lstlisting}

Khi ta thực thi lệnh: \texttt{BuyTransaction tx("AAPL");}, điều gì sẽ in ra màn hình?
\begin{itemize}
    \item Đa số lập trình viên mới nghĩ rằng nó sẽ in: \texttt{"BuyTransaction logged for: AAPL"}.
    \item \textbf{KẾT QUẢ THỰC TẾ:} Màn hình in ra \texttt{"Base Transaction logged"}! Đa hình đã hoàn toàn biến mất!
\end{itemize}

\begin{underhoodbox}[Nguyên Nhân Gầm Máy: Sự Tiến Hóa Của vptr Trong Vòng Đời Đối Tượng]
Hãy nhìn vào tiến trình khởi tạo bộ nhớ từng bước của CPU:
\begin{enumerate}
    \item Để khởi tạo \texttt{BuyTransaction}, trước hết Constructor của \texttt{Transaction} (lớp cha) phải được thực thi.
    \item Tại thời điểm Constructor của \texttt{Transaction} đang chạy, \textbf{phần dữ liệu của \texttt{BuyTransaction} (chuỗi \texttt{stockCode}) CHƯA ĐƯỢC CẤP PHÁT VÀ CHƯA ĐƯỢC KHỞI TẠO}.
    \item Do đó, con trỏ \texttt{\_\_vptr} của đối tượng lúc này \textbf{đang trỏ tới VTable của \texttt{Transaction}}, chứ CHƯA trỏ tới VTable của \texttt{BuyTransaction}!
    \item Trình biên dịch C++ cố tình cô lập lời gọi này về dạng \textbf{Static Binding} của lớp cha để bảo vệ bạn: Nếu nó cho phép gọi \texttt{BuyTransaction::logCreation()}, hàm này sẽ truy cập vào biến \texttt{stockCode} chưa tồn tại, dẫn đến đọc rác bộ nhớ hoặc làm sập chương trình (Segmentation Fault)!
\end{enumerate}

\textbf{Thảm Họa Crash Runtime Với Hàm Thuần Ảo (\texttt{\_\_cxa\_pure\_virtual}):}
Nếu phương thức ảo được gọi trong Constructor là \textbf{Hàm thuần ảo (\texttt{= 0})}:
\begin{lstlisting}[language=C++]
class Engine {
public:
    Engine() { start(); } // start() is pure virtual!
    virtual void start() = 0;
};
\end{lstlisting}
VTable của \texttt{Engine} tại slot của \texttt{start} chứa con trỏ trỏ tới hàm xử lý lỗi nội bộ của trình biên dịch: \texttt{\_\_cxa\_pure\_virtual}. Khi chương trình chạy qua dòng này, hệ điều hành lập tức chấm dứt tiến trình và ném lỗi kinh hoàng:\footnote{Nguồn: OOP6-Polymorphism\_new.pdf - Trang 66-72: Pitfall - Virtual Function in Constructor/Destructor}
\begin{center}
\textbf{\texttt{pure virtual method called - terminate called without an active exception (Aborted)}}
\end{center}
Điều tương tự diễn ra chính xác trong \textbf{Destructor}: Khi Destructor của lớp con chạy xong, đối tượng bị "hạ cấp" về lớp cha và \texttt{vptr} bị đổi ngược về VTable của lớp cha trước khi chạy Destructor của cha!
\end{underhoodbox}
"""
