# -*- coding: utf-8 -*-

chap5_text = r"""
% ==============================================================================
% CHƯƠNG 5: TÍNH ĐA HÌNH, LIÊN KẾT ĐỘNG & KIỂU TRẢ VỀ ĐỒNG BIẾN
% ==============================================================================
\chapter{Tính Đa hình, Liên kết Động \& Kiểu Trả về Đồng biến (Polymorphism)}

\begin{theorybox}[Định Nghĩa: Tính Đa Hình (Polymorphism)]
\textbf{Đa hình (Polymorphism)} --- xuất phát từ tiếng Hy Lạp cổ mang nghĩa "nhiều hình thái" --- là trụ cột thứ ba và là linh hồn của Lập trình Hướng Đối tượng. Đa hình cho phép một biến con trỏ hoặc tham chiếu thuộc lớp cơ sở (\texttt{Base}) có khả năng trỏ tới đối tượng của bất kỳ lớp phái sinh nào (\texttt{Derived}), và khi thực hiện lời gọi phương thức thành viên, phiên bản hàm chính xác tương ứng với kiểu đối tượng thực tế sẽ được kích hoạt tại thời điểm thực thi.
\end{theorybox}

\section{Triết lý Đa hình \& Cơ chế Liên kết (Binding)}

Để hiểu sâu sắc bản chất của Đa hình, ta phân tích sự khác biệt cốt tử giữa hai cơ chế liên kết lời gọi hàm với mã máy:

\begin{enumerate}
    \item \textbf{Liên kết Tĩnh (Early Binding / Static Binding):}
    \begin{itemize}
        \item Xảy ra tại \textbf{thời điểm biên dịch (Compile-time)}. Trình biên dịch dựa hoàn toàn vào \textbf{kiểu dữ liệu tĩnh (Static Type)} của biến hoặc con trỏ để xác định địa chỉ hàm cần thực thi.
        \item Mã máy sinh ra là một lệnh nhảy trực tiếp: \texttt{call 0x004012A0}.
        \item \textit{Ưu điểm:} Tốc độ thực thi tối đa, không tốn thêm bất kỳ byte bộ nhớ nào, cho phép trình biên dịch thực hiện tối ưu hóa nội dòng (\textbf{Function Inlining}).
        \item \textit{Nhược điểm:} Thiếu sự linh hoạt, không thể thay đổi hành vi theo ngữ cảnh thời gian chạy.
    \end{itemize}

    \item \textbf{Liên kết Động (Late Binding / Dynamic Binding):}
    \begin{itemize}
        \item Xảy ra tại \textbf{thời điểm thực thi (Runtime)}. Việc quyết định gọi phiên bản hàm nào được hoãn lại cho tới khi chương trình đang chạy, dựa vào \textbf{kiểu dữ liệu thực tế (Dynamic Type)} của đối tượng mà con trỏ đang trỏ tới.
        \item Mã máy sinh ra là một lệnh nhảy gián tiếp thông qua con trỏ bộ nhớ: \texttt{call qword ptr [rax + offset]}.
        \item \textit{Ưu điểm:} Cho phép mở rộng hệ thống phần mềm mà không cần sửa đổi mã nguồn đã tồn tại (Nguyên lý Đóng/Mở --- Open-Closed Principle).
        \item \textit{Nhược điểm:} Tốn chi phí gián tiếp (Indirection overhead), tăng kích thước đối tượng và vô hiệu hóa inlining.
    \end{itemize}
\end{enumerate}

\begin{theorybox}[Nguyên Lý Không Phụ Trội Của C++ (Zero-Overhead Principle)]
Trong các ngôn ngữ như Java hay C\#, mọi phương thức thành viên mặc định đều là \textbf{Dynamic Binding}. Ngược lại, triết lý thiết kế của C++ kiên định với tôn chỉ \textbf{Zero-Overhead Principle}: \textit{"Bạn không phải trả giá cho những gì bạn không sử dụng"}. 

Do đó, trong C++, mọi hàm thành viên mặc định \textbf{100\% là Static Binding}. Chỉ khi lập trình viên chủ động gắn từ khóa \texttt{virtual}, trình biên dịch mới kích hoạt cơ chế Dynamic Binding.
\end{theorybox}

\section{Hàm Ảo, \texttt{override} và \texttt{final} trong C++11}

\subsection{Cơ chế Hàm Ảo (\texttt{virtual})}

Khi khai báo một phương thức với từ khóa \texttt{virtual} ở lớp cơ sở, ta đã thiết lập một giao ước đa hình:
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

\textbf{Quy tắc lan truyền ảo (Virtual Propagation):} Một khi một phương thức đã được khai báo là \texttt{virtual} ở lớp cơ sở, nó sẽ \textbf{tự động mang tính ảo vĩnh viễn} trong toàn bộ cây thừa kế của các lớp con cháu, cho dù ở lớp con ta có viết lại từ khóa \texttt{virtual} hay không.

\subsection{Bộ Đôi Từ Khóa Ngữ Cảnh C++11: \texttt{override} và \texttt{final}}

Trước C++11, lỗi ngầm phổ biến nhất của lập trình viên là viết sai chữ ký hàm con dẫn đến việc vô tình tạo ra một hàm nạp chồng mới thay vì ghi đè hàm cha. Chuẩn C++11 bổ sung hai từ khóa ngữ cảnh (\textit{contextual keywords}):

\begin{itemize}
    \item \textbf{\texttt{override}}: Yêu cầu trình biên dịch kiểm tra nghiêm ngặt xem hàm này có thực sự ghi đè một hàm ảo nào từ lớp cha hay không. Nếu chữ ký hàm, kiểu trả về, hoặc thuộc tính \texttt{const} không khớp 100\%, trình biên dịch lập tức báo lỗi biên dịch (\textit{Compilation Error}):
    \begin{lstlisting}[language=C++]
    class DerivedC11 : public Base {
    public:
        void process(int x) const override; // Hop le: Khop chinh xac chu ky cua Base
    };
    \end{lstlisting}

    \item \textbf{\texttt{final}}: Khóa không cho lớp con tiếp tục ghi đè phương thức ảo hoặc khóa hoàn toàn không cho phép kế thừa lớp:
    \begin{lstlisting}[language=C++]
    virtual void process(int x) const override final; // Chan ghi de o lop chau
    class SecureKey final : public Base { /* ... */ }; // Chan ke thua
    \end{lstlisting}
    \textit{Tối ưu hóa Bỏ ảo hóa (Devirtualization):} Khi trình biên dịch phát hiện một phương thức hoặc lớp được đánh dấu \texttt{final}, nó có thể biến đổi các lời gọi gián tiếp thành lệnh gọi trực tiếp (\textbf{Direct Call}), loại bỏ hoàn toàn chi phí tra cứu bảng ảo.
\end{itemize}

\section{Phân tích Dưới Gầm Máy: Bảng Ảo (VTable) \& Con trỏ vptr}

Làm thế nào mà CPU có thể tìm ra đúng hàm \texttt{Circle::draw()} khi nó chỉ đang giữ một con trỏ kiểu \texttt{Shape*}? Câu trả lời nằm ở cấu trúc nhị phân của Bảng Phương Thức Ảo:

\begin{figure}[htbp]
\centering
\resizebox{0.95\textwidth}{!}{%
\begin{tikzpicture}[every node/.style={font=\small\sffamily, align=center}]
    % Object RAM on left (x from 0 to 5.0, y from -0.3 to 3.4)
    \draw[thick, fill=bgsoftblue, draw=primaryblue, rounded corners=4pt] (0, -0.3) rectangle (5.0, 3.4);
    \node[above=2pt, font=\bfseries\sffamily, primaryblue] at (2.5, 3.4) {Đối Tượng Circle (Stack/Heap)};

    \node[draw=accentblue, thick, fill=bglighterblue, rounded corners=3pt, text width=4.4cm, minimum height=0.75cm] (vptr_slot) at (2.5, 2.5) {
        \textbf{\texttt{\_\_vptr}} (8 bytes con trỏ ẩn)
    };
    \node[draw=primaryblue, fill=white, rounded corners=3pt, text width=4.4cm, minimum height=0.75cm] at (2.5, 1.4) {
        \texttt{int id} (4B + 4B padding)
    };
    \node[draw=primaryblue, fill=white, rounded corners=3pt, text width=4.4cm, minimum height=0.75cm] at (2.5, 0.3) {
        \texttt{double radius} (8 bytes)
    };

    % VTable in .rodata on right (x from 9.0 to 15.0, y from 0.0 to 5.0)
    \draw[thick, fill=bgsoftblue, draw=accentblue, rounded corners=4pt] (9.0, 0.0) rectangle (15.0, 5.0);
    \node[above=2pt, font=\bfseries\sffamily, darkblue] at (12.0, 5.0) {VTable của Circle (.rodata)};

    % Negative offset prefix slots
    \node[draw=commentgray, fill=gray!15, rounded corners=3pt, text width=5.2cm, minimum height=0.65cm, font=\scriptsize\ttfamily] at (12.0, 4.3) {
        Slot [-2]: Offset-to-top (0x00)
    };
    \node[draw=commentgray, fill=gray!15, rounded corners=3pt, text width=5.2cm, minimum height=0.65cm, font=\scriptsize\ttfamily] at (12.0, 3.4) {
        Slot [-1]: RTTI Descriptor (\&typeinfo)
    };

    % Virtual function slots (Starting at index 0, exactly aligned with __vptr at y = 2.5)
    \node[draw=accentblue, thick, fill=white, rounded corners=3pt, text width=5.2cm, minimum height=0.65cm, font=\footnotesize\ttfamily] (vtable_slot0) at (12.0, 2.5) {
        Slot [0]: \&Circle::draw()
    };
    \node[draw=accentblue, fill=white, rounded corners=3pt, text width=5.2cm, minimum height=0.65cm, font=\footnotesize\ttfamily] at (12.0, 1.6) {
        Slot [1]: \&Circle::area()
    };
    \node[draw=accentblue, fill=white, rounded corners=3pt, text width=5.2cm, minimum height=0.65cm, font=\footnotesize\ttfamily] at (12.0, 0.7) {
        Slot [2]: \&Circle::\textasciitilde{}Circle()
    };

    % Pure horizontal arrow from __vptr to VTable Slot [0] in 4.6cm wide clear gap
    \draw[-{Stealth[length=3mm]}, ultra thick, accentblue] (vptr_slot.east) -- (vtable_slot0.west)
        node[midway, above=6pt, font=\footnotesize\bfseries, accentblue] {Trỏ bảng ảo (Slot 0)};
\end{tikzpicture}%
}
\caption{Cấu trúc nhị phân của Bảng Phương Thức Ảo (VTable) bao gồm các slot tiền tố âm RTTI.}
\end{figure}

\begin{underhoodbox}[Kiến Trúc Bảng Ảo VTable và Con Trỏ vptr Dưới RAM]
\begin{enumerate}
    \item \textbf{Virtual Method Table (VTable):} Là mảng tĩnh các con trỏ hàm được sinh ra duy nhất một bản cho mỗi lớp có phương thức ảo, lưu tại phân vùng chỉ đọc (\texttt{.rodata} trên Linux ELF hoặc \texttt{.rdata} trên Windows PE).
    \item \textbf{Tiền tố offset âm (Negative Prefix Slots):} Phía trước vị trí con trỏ trỏ tới (offset 0), VTable chứa hai trường thông tin cực kỳ quan trọng:
    \begin{itemize}
        \item \textbf{Offset-to-top (Offset -16 bytes):} Khoảng cách byte từ subobject hiện tại tới đỉnh của đối tượng toàn vẹn, phục vụ cho việc ép kiểu ngược trong đa kế thừa.
        \item \textbf{RTTI Descriptor Pointer (Offset -8 bytes):} Con trỏ trỏ tới cấu trúc \texttt{std::type\_info}, phục vụ cho toán tử \texttt{typeid} và \texttt{dynamic\_cast}.
    \end{itemize}
    \item \textbf{Virtual Table Pointer (vptr):} Con trỏ ẩn 8 bytes được chèn vào đầu đối tượng, trỏ thẳng tới Slot [0] của VTable, được thiết lập tự động bởi mã máy của Constructor.
\end{enumerate}

\textbf{Giải phẫu Lệnh Nhảy Gián Tiếp (Indirect Dispatching):}
Khi thực thi \texttt{pShape->draw()}:
\begin{enumerate}
    \item CPU lấy địa chỉ đối tượng từ thanh ghi con trỏ (ví dụ \texttt{RDI} hoặc \texttt{RCX}).
    \item CPU giải tham chiếu offset 0 để lấy giá trị con trỏ \texttt{\_\_vptr}: \texttt{RAX = *(pShape)}.
    \item CPU tra cứu mảng VTable tại slot của hàm \texttt{draw()} (slot 0): \texttt{RDX = *(RAX + 0)}.
    \item CPU thực hiện lệnh nhảy gián tiếp: \texttt{call RDX}, đồng thời truyền con trỏ đối tượng \texttt{pShape} làm con trỏ bản thể \texttt{this}.
\end{enumerate}
\end{underhoodbox}

\subsection{Hàm Thunk Bù Độ Lệch Con Trỏ Bản Thể (Adjustor Thunk)}

Trong Đa kế thừa, khi lớp \texttt{C} kế thừa từ cả \texttt{A} và \texttt{B}, Subobject \texttt{B} nằm lệch đi một khoảng $\Delta$ (ví dụ $+8$ bytes). Khi gọi một phương thức ảo của $B$ thông qua con trỏ \texttt{B* pb = new C(); pb->fb();}, con trỏ truyền vào đang trỏ tại offset $+8$, trong khi thân hàm \texttt{C::fb()} kỳ vọng con trỏ \texttt{this} trỏ tại offset 0!

\textbf{Giải pháp Thunk:} Trình biên dịch sinh ra một đoạn mã đệm siêu nhỏ:
\begin{lstlisting}[language={[x86masm]Assembler}]
__thunk_for_C_fb:
    sub rcx, 8          ; Rewind this pointer (MSVC x64 ABI)
    ; sub rdi, 8        ; Tuong duong tren System V AMD64 ABI (Linux)
    jmp C::fb           ; Direct jump to actual implementation
\end{lstlisting}

\section{Kiểu Trả Về Đồng Biến (Covariant Return Types)}

Một trong những tính năng cao cấp và thanh lịch nhất của đa hình C++ là \textbf{Kiểu trả về đồng biến (Covariant Return Types)}: Một phương thức ghi đè ở lớp con được phép có kiểu trả về là \textbf{con trỏ hoặc tham chiếu tới lớp con}, thay vì phải giữ nguyên kiểu của lớp cha.

\begin{lstlisting}[language=C++]
class Entity {
public:
    virtual Entity* clone() const = 0; // Pure virtual clone
    virtual ~Entity() = default;
};

class Monster : public Entity {
public:
    // Covariant Return Type: Returns Monster* instead of Entity*!
    Monster* clone() const override {
        return new Monster(*this);
    }
};

void testCloning() {
    Monster original;
    // Khong can ep kieu static_cast<Monster*>!
    Monster* copyMonster = original.clone(); 
    delete copyMonster;
}
\end{lstlisting}
Đây là nền tảng của thành ngữ thiết kế \textbf{Virtual Copy Constructor (Clone Idiom)}, cho phép nhân bản đối tượng đa hình một cách hoàn toàn an toàn về kiểu mà không cần ép kiểu thủ công.

\section{Destructor Ảo (Virtual Destructor) \& Bẫy Gọi Hàm Ảo Trong Constructor}

\subsection{Destructor Ảo --- Nguyên Lý Sống Còn Trong Kế Thừa}

\begin{lstlisting}[language=C++]
class BaseResource {
public:
    virtual ~BaseResource() = default; // Mandatory virtual destructor!
};

class DerivedResource : public BaseResource {
private:
    int* largeBuffer;
public:
    DerivedResource() : largeBuffer(new int[1000000]) {}
    ~DerivedResource() override {
        delete[] largeBuffer; // Safely executed via virtual dispatch!
    }
};
\end{lstlisting}

\begin{theorybox}[Quy Tắc Vàng Của Scott Meyers Về Destructor]
\begin{itemize}
    \item \textbf{Quy tắc 1:} Bất kỳ lớp nào được thiết kế để làm lớp cơ sở có tính đa hình (\textit{Polymorphic Base Class}), Destructor của nó \textbf{BẮT BUỘC PHẢI LÀ \texttt{public virtual}}.
    \item \textbf{Quy tắc 2:} Nếu một lớp không được thiết kế để làm lớp cha đa hình, hãy khai báo Destructor là \textbf{\texttt{protected non-virtual}}. Cách này ngăn chặn việc gọi \texttt{delete ptrBase} từ bên ngoài, triệt tiêu lỗi rò rỉ ngay tại compile-time.
\end{itemize}
\end{theorybox}

\subsection{Bẫy Gọi Hàm Ảo Trong Constructor \& Destructor}

Trong C++, gọi một hàm ảo bên trong Constructor hoặc Destructor sẽ \textbf{chỉ kích hoạt phiên bản của chính lớp đang thực thi Constructor đó}, hoàn toàn không kích hoạt phiên bản ghi đè của lớp con!

\begin{underhoodbox}[Nguyên Nhân Gầm Máy: Sự Tiến Hóa Của vptr Trong Vòng Đời Đối Tượng]
\begin{enumerate}
    \item Khi Constructor của lớp cha đang thực thi, phần dữ liệu của lớp con \textbf{chưa hề được cấp phát và khởi tạo}.
    \item Do đó, con trỏ \texttt{\_\_vptr} lúc này \textbf{đang trỏ tới VTable của lớp cha}, chưa trỏ tới VTable của lớp con.
    \item Với các lời gọi trực tiếp (\textit{Direct calls}), trình biên dịch tối ưu hóa tĩnh (\textit{Static Devirtualization}) gọi thẳng hàm cha.
    \item Với các lời gọi gián tiếp qua hàm bổ trợ mà hàm ảo là thuần ảo (\texttt{= 0}), hệ thống sẽ gọi con trỏ lỗi \texttt{\_\_cxa\_pure\_virtual} và đình chỉ tiến trình ngay lập tức.
\end{enumerate}
\end{underhoodbox}
"""
