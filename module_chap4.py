# -*- coding: utf-8 -*-

chap4_text = r"""
% ==============================================================================
% CHƯƠNG 4: KẾ THỪA (INHERITANCE)
% ==============================================================================
\chapter{Kế thừa (Inheritance)}

\begin{theorybox}[Định Nghĩa: Tính Kế Thừa (Inheritance)]
\textbf{Kế thừa (Inheritance)} là cơ chế cho phép một lớp mới (\textbf{Lớp dẫn xuất / Lớp con --- Derived Class}) tiếp nhận lại toàn bộ cấu trúc dữ liệu và hành vi của một lớp đã tồn tại (\textbf{Lớp cơ sở / Lớp cha --- Base Class}), đồng thời mở rộng hoặc tái định nghĩa các hành vi chuyên biệt mà không cần viết lại mã nguồn ban đầu.\footnote{Nguồn: OOP5-Inheritance\_new.pdf - Trang 3-12: Khái niệm thừa kế và quan hệ kế thừa}
\end{theorybox}

\section{Bản Chất Quan Hệ IS-A và HAS-A}

Trong thiết kế phần mềm, việc lựa chọn sai lầm giữa Kế thừa và Hợp thành là nguyên nhân hàng đầu dẫn đến các hệ thống giòn vỡ (\textit{Brittle Architecture}):

\begin{itemize}
    \item \textbf{Mối quan hệ IS-A (Là một):} Thể hiện tính phân loại bản thể luận. Ví dụ: \textit{"Hình tròn LÀ MỘT Hình học"} (\texttt{Circle IS-A Shape}). Mối quan hệ này phải được biểu diễn bằng \textbf{Kế thừa Công khai (Public Inheritance)}. Đối tượng lớp con phải thay thế được hoàn toàn cho đối tượng lớp cha trong mọi hoàn cảnh mà không phá vỡ tính đúng đắn của chương trình (Nguyên lý Thay thế Liskov - Liskov Substitution Principle).
    \item \textbf{Mối quan hệ HAS-A (Có một / Sở hữu):} Thể hiện sự hợp thành của các thành phần. Ví dụ: \textit{"Ô tô CÓ MỘT Động cơ"} (\texttt{Car HAS-A Engine}). Mối quan hệ này bắt buộc phải được mô hình hóa bằng \textbf{Hợp Thành (Composition)} hoặc \textbf{Tụ Hợp (Aggregation)}: Đưa đối tượng thành viên vào trong lớp, tuyệt đối không dùng kế thừa!
\end{itemize}

\subsection{Bố Cục Bộ Nhớ Đối Tượng Kế Thừa Đơn (Single Inheritance Memory Layout)}

Trong C++, lớp con kế thừa từ lớp cha được tổ chức theo nguyên lý lồng ghép cấu trúc nhị phân liên tục trong RAM:

\begin{figure}[htbp]
\centering
\resizebox{0.92\textwidth}{!}{%
\begin{tikzpicture}[every node/.style={font=\small\sffamily, align=center}]
    % Outer container
    \draw[thick, fill=bgsoftblue, draw=primaryblue, rounded corners=3pt] (0, 0) rectangle (11, 4.2);
    \node[above, font=\bfseries\sffamily, primaryblue] at (5.5, 4.2) {Không Gian Bộ Nhớ Của Đối Tượng Phái Sinh (Derived Object)};

    % Base subobject
    \draw[thick, fill=white, draw=primaryblue, rounded corners=2pt] (2.2, 2.2) rectangle (10.5, 3.8);
    \node at (6.35, 3.0) {\textbf{Base Class Subobject} (Bắt đầu tại Offset 0)\\Chứa các trường dữ liệu của Base Class (\texttt{int base\_id; double base\_val;})};

    % Derived unique fields
    \draw[thick, fill=bglighterblue, draw=accentblue, rounded corners=2pt] (2.2, 0.4) rectangle (10.5, 2.0);
    \node at (6.35, 1.2) {\textbf{Derived Class Unique Fields} (Offset $+\text{sizeof(Base)}$)\\Chứa các trường thành viên bổ sung riêng của Derived Class};

    % Left offset annotations
    \node[font=\footnotesize\ttfamily, left, primaryblue] at (2.0, 3.0) {Offset 0x00};
    \node[font=\footnotesize\ttfamily, left, accentblue] at (2.0, 1.2) {Offset +$\Delta$};
\end{tikzpicture}%
}
\caption{Bố cục bộ nhớ nhị phân của đối tượng phái sinh trong Kế thừa Đơn.}
\end{figure}

\begin{underhoodbox}[Đặc Điểm Con Trỏ Trong Kế Thừa Đơn]
Vì Subobject của Base nằm tại vị trí bắt đầu (Offset 0) của đối tượng Derived, nên:
$$\texttt{\&derived == static\_cast<Base*>(\&derived)}$$
Địa chỉ con trỏ của đối tượng con và địa chỉ con trỏ khi ép kiểu lên đối tượng cha là \textbf{hoàn toàn trùng khớp về mặt giá trị số nguyên}! Trình biên dịch không cần sinh thêm bất kỳ lệnh cộng trừ offset nào khi thực hiện phép Upcast trong kế thừa đơn.\footnote{Nguồn: OOP5-Inheritance\_new.pdf - Trang 13-22: Bố cục bộ nhớ đối tượng kế thừa}
\end{underhoodbox}

\section{Ma Trận Biến Đổi Quyền Truy Cập Trong Kế Thừa}

Quyền truy cập của các thành viên kế thừa từ lớp cha vào lớp con phụ thuộc vào kiểu kế thừa:

\begin{table}[htbp]
\centering
\caption{Ma trận biến đổi quyền truy cập các trường dữ liệu trong kế thừa}
\vspace{0.2cm}
\resizebox{0.95\textwidth}{!}{%
\begin{tabular}{lccc}
\toprule
\textbf{Quyền Tại Lớp Base} & \textbf{Kế Thừa Public} & \textbf{Kế Thừa Protected} & \textbf{Kế Thừa Private} \\
\midrule
\texttt{public} & \texttt{public} & \texttt{protected} & \texttt{private} \\
\texttt{protected} & \texttt{protected} & \texttt{protected} & \texttt{private} \\
\texttt{private} & \textit{Bị ẩn hoàn toàn} & \textit{Bị ẩn hoàn toàn} & \textit{Bị ẩn hoàn toàn} \\
\bottomrule
\end{tabular}%
}
\end{table}

\begin{itemize}
    \item \textbf{Kế thừa Public:} Thiết lập mối quan hệ IS-A thực sự. Cho phép chuyển đổi con trỏ tự do từ con lên cha ở bất kỳ đâu.
    \item \textbf{Kế thừa Private:} Thiết lập mối quan hệ \textit{"Được cài đặt bằng cách sử dụng"} (\textit{Implemented-in-terms-of}). Toàn bộ giao diện của cha bị đóng kín bên trong con.
    \item \textbf{Tối ưu hóa Lớp Cơ sở Rỗng (Empty Base Optimization - EBO):}
    Theo chuẩn C++, một lớp hoàn toàn rỗng không chứa biến thành viên vẫn phải có kích thước tối thiểu $\text{sizeof} = 1$ byte để đảm bảo mỗi đối tượng có một địa chỉ phân biệt. Tuy nhiên, khi kế thừa theo dạng \texttt{private}, trình biên dịch C++ áp dụng EBO để tiêu trừ byte này: Kích thước của lớp con \textbf{không bị tăng thêm 1 byte nào}! Kỹ thuật này được STL sử dụng triệt để trong các bộ nén con trỏ và bộ cấp phát tĩnh (\texttt{std::allocator}).
\end{itemize}

\section{Vòng Đời Khởi Tạo và Hủy Kế Thừa}

\subsection{Trình Tự Thực Thi Khởi Tạo và Giải Phóng Bộ Nhớ}

\begin{theorybox}[Định Đề Bất Biến Về Trình Tự Vòng Đời Kế Thừa]
Khi khởi tạo một đối tượng lớp con:
\begin{enumerate}
    \item \textbf{Khởi tạo Lớp Cơ sở (Base First):} Constructor của lớp cha được thực thi đầu tiên để bảo đảm phần nền tảng được định hình vững chắc.
    \item \textbf{Khởi tạo Các Thành Viên Lớp Con (Member Fields):} Các biến dữ liệu riêng của lớp con được khởi tạo theo thứ tự khai báo.
    \item \textbf{Thực thi Thân Constructor Lớp Con (Derived Body):} Phần thân hàm tạo của lớp con hoàn thiện các nghiệp vụ cuối cùng.
\end{enumerate}

Khi đối tượng bị tiêu hủy:
\begin{center}
\textbf{Trình tự hủy diễn ra theo đúng quy tắc LIFO (Last-In, First-Out) ngược lại hoàn toàn:}\\
Destructor Lớp Con chạy trước $\longrightarrow$ Dọn dẹp thành viên $\longrightarrow$ Destructor Lớp Cha chạy sau cùng!\footnote{Nguồn: OOP5-Inheritance\_new.pdf - Trang 23-38: Thứ tự thực thi Constructor và Destructor}
\end{center}
\end{theorybox}

\begin{dangerbox}[Bẫy Tử Thần: Quên Gọi Base Copy Constructor]
Khi lập trình viên tự tay viết Copy Constructor cho lớp con:
\begin{lstlisting}[language=C++]
class Base {
public:
    int baseVal;
    Base(int v) : baseVal(v) {}
    Base(const Base& other) : baseVal(other.baseVal) {
        std::cout << "Base copied\n";
    }
};

class Derived : public Base {
public:
    int derivedVal;
    Derived(int b, int d) : Base(b), derivedVal(d) {}

    // DANGEROUS ERROR: Forgot to invoke Base(other) in initializer list!
    Derived(const Derived& other) : derivedVal(other.derivedVal) {
        // Compiler will silently invoke Base::Base() default constructor!
        // If Base has no default ctor -> Compilation error.
        // If Base has default ctor -> baseVal is reset, losing copied data!
    }

    // CORRECT CANONICAL IMPLEMENTATION:
    // Derived(const Derived& other) : Base(other), derivedVal(other.derivedVal) {}
};
\end{lstlisting}
\end{dangerbox}

\section{Hiện Tượng Che Khuất Tên (Name Hiding) vs Nạp Chồng}

Trong C++, cơ chế phân giải tên (\textit{Name Lookup}) tuân theo nguyên tắc: \textbf{Dừng lại ở phạm vi gần nhất tìm thấy định danh trùng khớp}!

\begin{lstlisting}[language=C++]
class Base {
public:
    void process(int x) { std::cout << "Base::process(int)\n"; }
    void process(double x) { std::cout << "Base::process(double)\n"; }
};

class Derived : public Base {
public:
    // Hides all Base::process overloads:
    void process(std::string s) { std::cout << "Derived::process(string)\n"; }
};

void test() {
    Derived d;
    d.process("Hello"); // VALID: Calls Derived::process(string)
    // d.process(10);   // COMPILATION ERROR: Compiler cannot find process(int)!
}
\end{lstlisting}

\begin{underhoodbox}[Bản Chất Của Hiện Tượng Name Hiding]
Tại sao \texttt{d.process(10)} không gọi \texttt{Base::process(int)}?
\begin{enumerate}
    \item Khi phân tích cú pháp biểu thức \texttt{d.process(10)}, trình biên dịch bắt đầu tìm kiếm tên định danh \texttt{process} từ phạm vi của lớp \texttt{Derived}.
    \item Nó tìm thấy \texttt{void Derived::process(std::string)}.
    \item \textbf{Cơ chế dừng tìm kiếm:} Khi đã tìm thấy ít nhất một tên khớp trong một phạm vi, trình biên dịch \textbf{DỪNG TÌM KIẾM NGAY LẬP TỨC} và không bao giờ quét tiếp lên phạm vi của lớp cha \texttt{Base}!
    \item Sau đó, nó tiến hành phân giải nạp chồng (\textit{Overload Resolution}) trên tập hợp các hàm tìm được tại lớp con. Vì tập hợp này chỉ có phiên bản nhận \texttt{std::string}, việc truyền số nguyên \texttt{10} bị báo lỗi biên dịch!
    \item \textbf{Giải pháp chuẩn mực:} Sử dụng từ khóa \textbf{\texttt{using}} để kéo toàn bộ họ hàm của cha vào lớp con:
    \begin{lstlisting}[language=C++]
    class Derived : public Base {
    public:
        using Base::process; // Pull all Base::process overloads into Derived scope
        void process(std::string s);
    };
    \end{lstlisting}
    Dòng lệnh \texttt{using Base::process} tái lập khả năng nạp chồng hoàn hảo giữa cha và con!\footnote{Nguồn: OOP5-Inheritance\_new.pdf - Trang 39-48: Hiện tượng Name Hiding và từ khóa using}
\end{enumerate}
\end{underhoodbox}

\section{Upcasting, Downcasting và Hiểm Họa Cắt Xén Đối Tượng}

\subsection{Cắt Xén Đối Tượng (Object Slicing)}

\begin{dangerbox}[Thảm Họa Cắt Xén Đối Tượng Khi Truyền Tham Trị]
Xét đoạn mã sau:
\begin{lstlisting}[language=C++]
void renderEntity(Base b) { // DANGEROUS: Passed by VALUE
    // ...
}

void execution() {
    Derived d(10, 20);
    renderEntity(d); // OBJECT SLICING OCCURS HERE!
}
\end{lstlisting}

\textbf{Giải phẫu cơ chế cắt xén dưới RAM:}
\begin{enumerate}
    \item Hàm \texttt{renderEntity} yêu cầu một biến có kích thước đúng bằng $\text{sizeof}(\text{Base})$ trên ngăn xếp Stack của nó.
    \item Khi truyền đối tượng \texttt{d} vào, trình biên dịch gọi Copy Constructor của lớp cơ sở: \texttt{Base::Base(const Base\&)}.
    \item Trình biên dịch sao chép chính xác phần Subobject của Base từ \texttt{d}, và \textbf{GỌT BỎ HOÀN TOÀN (SLICE OFF)} toàn bộ các trường dữ liệu riêng và bản chất đa hình của \texttt{Derived}!
    \item Mọi hành vi đa hình và dữ liệu của lớp con bị tiêu biến hoàn toàn mà không có bất kỳ cảnh báo biên dịch nào!
    \item \textbf{Quy tắc Vàng:} Trong hướng đối tượng, luôn luôn truyền đối tượng đa hình qua \textbf{Tham Chiếu Hằng (\texttt{const Base\&})} hoặc \textbf{Con Trỏ (\texttt{Base*})}, tuyệt đối cấm truyền theo giá trị!\footnote{Nguồn: OOP5-Inheritance\_new.pdf - Trang 49-62: Upcasting, Object Slicing và Downcasting}
\end{enumerate}
\end{dangerbox}

\section{Đa Kế Thừa \& Bài Toán Kim Cương (Diamond Problem)}

\subsection{Mô Hình Bài Toán Kim Cương}

Đa kế thừa (\textit{Multiple Inheritance}) cho phép một lớp kế thừa từ nhiều lớp cha độc lập. Tuy nhiên, nó dẫn tới cấu trúc đồ thị hình thoi kinh điển:

\begin{figure}[htbp]
\centering
\resizebox{0.65\textwidth}{!}{%
\begin{tikzpicture}[
    box/.style={draw=primaryblue, thick, rounded corners=3pt, fill=white, inner sep=6pt, font=\small\bfseries\sffamily, align=center, text width=3.2cm}
]
    \node[box, fill=bglighterblue] (A) at (0, 3.6) {Lớp Cơ Sở A\\\footnotesize\ttfamily int id;};
    \node[box, fill=white] (B) at (-3.2, 1.8) {Lớp Con B};
    \node[box, fill=white] (C) at (3.2, 1.8) {Lớp Con C};
    \node[box, fill=bgsoftblue, draw=accentblue, line width=1.4pt] (D) at (0, 0) {Lớp Đa Kế Thừa D};

    \draw[-{Stealth[length=2.5mm]}, thick, primaryblue] (B.north) -- (A.south west);
    \draw[-{Stealth[length=2.5mm]}, thick, primaryblue] (C.north) -- (A.south east);
    \draw[-{Stealth[length=2.5mm]}, thick, accentblue] (D.north west) -- (B.south);
    \draw[-{Stealth[length=2.5mm]}, thick, accentblue] (D.north east) -- (C.south);
\end{tikzpicture}%
}
\caption{Mô hình phân cấp kế thừa hình thoi (The Diamond Problem).}
\end{figure}

\begin{itemize}
    \item \textbf{Nếu không có kế thừa ảo:} Đối tượng \texttt{D} trong RAM sẽ chứa \textbf{HAI BẢN SAO ĐỘC LẬP CỦA $A$} (một bản đi qua nhánh $B$, một bản đi qua nhánh $C$). Kích thước đối tượng bị nhân đôi, và lời gọi \texttt{d.id} bị trình biên dịch từ chối ngay lập tức vì không thể xác định đang truy cập \texttt{id} của nhánh $B$ hay nhánh $C$ (\textit{Ambiguity Error}).
    \item \textbf{Giải pháp: Kế Thừa Ảo (\texttt{virtual public A}):}
    \begin{lstlisting}[language=C++]
    class A { public: int id; A(int x) : id(x) {} };
    class B : virtual public A { public: B() : A(1) {} };
    class C : virtual public A { public: C() : A(2) {} };
    class D : public B, public C {
    public:
        // MOST-DERIVED CLASS EXCLUSIVE DUTY:
        // D is directly responsible for initializing A, ignoring calls from B and C!
        D() : A(100), B(), C() {}
    };
    \end{lstlisting}
\end{itemize}

\begin{underhoodbox}[Kiến Trúc Bộ Nhớ Kế Thừa Ảo (vbptr \& vbtbl)]
Để đảm bảo trong lòng đối tượng $D$ chỉ tồn tại duy nhất \textbf{MỘT Subobject $A$ dùng chung}, trình biên dịch C++ thay đổi hoàn toàn kiến trúc bộ nhớ:
\begin{enumerate}
    \item Subobject $A$ ảo được đẩy xuống tận cùng của cấu trúc đối tượng $D$.
    \item Các lớp trung gian $B$ và $C$ được chèn thêm một con trỏ cơ sở ảo: \textbf{\texttt{vbptr} (Virtual Base Pointer)}.
    \item \texttt{vbptr} trỏ tới một bảng độ lệch \textbf{Virtual Base Table (vbtbl)}. Tại runtime, khi $B$ hoặc $C$ muốn truy cập thành viên của $A$, CPU đọc bảng \texttt{vbtbl} để tính toán khoảng dịch chuyển bộ nhớ động tới vị trí thực tế của $A$ trong $D$.
    \item Do đó, kế thừa ảo làm tăng kích thước đối tượng thêm từ 8 đến 16 bytes (cho các con trỏ \texttt{vbptr}) và làm chậm tốc độ truy cập dữ liệu do phải qua thêm một bước gián tiếp.\footnote{Nguồn: OOP5-Inheritance\_new.pdf - Trang 71-76: Đa thừa kế, Sự mơ hồ \& Lớp cơ sở ảo}
\end{enumerate}
\end{underhoodbox}
"""
