# -*- coding: utf-8 -*-

chap4_text = r"""
% ==============================================================================
% CHƯƠNG 4: KẾ THỪA & BỐ CỤC BỘ NHỚ NHỊ PHÂN
% ==============================================================================
\chapter{Kế thừa, Bố cục Bộ nhớ Nhị phân \& Mô hình hóa UML (Inheritance)}

\begin{theorybox}[Định Nghĩa: Tính Kế Thừa (Inheritance)]
\textbf{Kế thừa (Inheritance)} là cơ chế cho phép một lớp mới (\textbf{Lớp dẫn xuất / Lớp con --- Derived Class}) tiếp nhận lại toàn bộ cấu trúc dữ liệu và hành vi của một lớp đã tồn tại (\textbf{Lớp cơ sở / Lớp cha --- Base Class}), đồng thời mở rộng hoặc tái định nghĩa các hành vi chuyên biệt mà không cần viết lại mã nguồn ban đầu.
\end{theorybox}

\section{Bản Chất Quan Hệ Hướng Đối Tượng \& Ký Hiệu UML}

Trong thiết kế phần mềm, việc phân định rạch ròi các mối quan hệ giữa các lớp là nền tảng sống còn của kiến trúc:

\begin{enumerate}
    \item \textbf{Mối quan hệ IS-A (Kế thừa / Khái quát hóa --- Generalization):}
    \begin{itemize}
        \item Thể hiện tính phân loại bản thể luận: \textit{"Hình tròn LÀ MỘT Hình học"} (\texttt{Circle IS-A Shape}).
        \item Được biểu diễn bằng \textbf{Kế thừa Công khai (Public Inheritance)}. Đối tượng lớp con phải thay thế được hoàn toàn cho đối tượng lớp cha trong mọi hoàn cảnh mà không phá vỡ tính đúng đắn của chương trình (Nguyên lý Thay thế Liskov --- Liskov Substitution Principle).
        \item \textit{Ký hiệu UML chuẩn:} Mũi tên tam giác rỗng hướng từ lớp con lên lớp cha ($\triangle-$).
    \end{itemize}

    \item \textbf{Mối quan hệ HAS-A (Sở hữu / Hợp thành --- Composition vs Aggregation):}
    \begin{itemize}
        \item \textbf{Hợp thành (Composition):} Quan hệ sở hữu vòng đời khăng khít. Thành phần con không thể tồn tại độc lập nếu đối tượng chứa nó bị hủy (ví dụ: \textit{"Ô tô CÓ Động cơ"}).
        \textit{Ký hiệu UML:} Hình thoi đặc ($\blacklozenge-$).
        \item \textbf{Tụ hợp (Aggregation):} Quan hệ sở hữu lỏng lẻo. Thành phần con có vòng đời độc lập với đối tượng chứa nó (ví dụ: \textit{"Trường học CÓ Giáo viên"}).
        \textit{Ký hiệu UML:} Hình thoi rỗng ($\lozenge-$).
    \end{itemize}

    \item \textbf{Mối quan hệ USES-A (Phụ thuộc --- Dependency):}
    Một lớp sử dụng dịch vụ của một lớp khác thông qua tham số hàm mà không nắm giữ biến thành viên lâu dài.
    \textit{Ký hiệu UML:} Mũi tên nét đứt ($\dashrightarrow$).
\end{enumerate}

\subsection{Bố Cục Bộ Nhớ Đối Tượng Kế Thừa Đơn (Single Inheritance Memory Layout)}

Trong C++, lớp con kế thừa từ lớp cha được tổ chức theo nguyên lý lồng ghép cấu trúc nhị phân liên tục trong RAM:

\begin{figure}[htbp]
\centering
\resizebox{0.95\textwidth}{!}{%
\begin{tikzpicture}[every node/.style={font=\small\sffamily, align=center}]
    % Outer container
    \draw[thick, fill=bgsoftblue, draw=primaryblue, rounded corners=4pt] (0, 0) rectangle (12.0, 4.2);
    \node[above=2pt, font=\bfseries\sffamily, primaryblue] at (6.0, 4.2) {Không Gian Bộ Nhớ Nhị Phân Của Đối Tượng Phái Sinh (Derived Object)};

    % Offset Column (Left: x from 0.4 to 2.2)
    \node[draw=primaryblue, fill=white, rounded corners=2pt, minimum width=2.0cm, minimum height=1.3cm, font=\footnotesize\ttfamily] at (1.5, 2.9) {Offset 0x00};
    \node[draw=accentblue, fill=white, rounded corners=2pt, minimum width=2.0cm, minimum height=1.3cm, font=\footnotesize\ttfamily] at (1.5, 1.1) {+sizeof(Base)};

    % Field Column (Right: x from 3.0 to 11.5)
    \node[draw=primaryblue, thick, fill=white, rounded corners=3pt, text width=8.5cm, minimum height=1.3cm] at (7.2, 2.9) {
        \textbf{Base Class Subobject} (Bắt đầu tại Offset 0)\\
        \footnotesize Chứa các trường dữ liệu của Base Class (\texttt{int base\_id; double base\_val;})
    };

    \node[draw=accentblue, thick, fill=bglighterblue, rounded corners=3pt, text width=8.5cm, minimum height=1.3cm] at (7.2, 1.1) {
        \textbf{Derived Class Unique Fields} (Offset $+\text{sizeof(Base)}$)\\
        \footnotesize Chứa các trường thành viên bổ sung riêng của Derived Class
    };
\end{tikzpicture}%
}
\caption{Bố cục bộ nhớ nhị phân của đối tượng phái sinh trong Kế thừa Đơn.}
\end{figure}

\begin{underhoodbox}[Đặc Điểm Con Trỏ Trong Kế Thừa Đơn]
Vì Subobject của Base nằm tại vị trí bắt đầu (Offset 0) của đối tượng Derived, nên:
$$\texttt{\&derived == static\_cast<Base*>(\&derived)}$$
Địa chỉ con trỏ của đối tượng con và địa chỉ con trỏ khi ép kiểu lên đối tượng cha là \textbf{hoàn toàn trùng khớp về mặt giá trị số nguyên}! Trình biên dịch không cần sinh thêm bất kỳ lệnh cộng trừ offset nào khi thực hiện phép Upcast trong kế thừa đơn.
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
    \item \textbf{Tối ưu hóa Lớp Cơ sở Rỗng (Empty Base Optimization --- EBO):}
    Theo chuẩn C++, một lớp hoàn toàn rỗng không chứa biến thành viên vẫn phải có kích thước tối thiểu $\text{sizeof} = 1$ byte để bảo đảm mỗi đối tượng có một địa chỉ phân biệt. Tuy nhiên, khi kế thừa theo dạng \texttt{private}, trình biên dịch C++ áp dụng EBO để triệt tiêu byte này: Kích thước của lớp con \textbf{không bị tăng thêm 1 byte nào}. Kỹ thuật này được STL sử dụng triệt để trong các bộ nén con trỏ và bộ cấp phát tĩnh (\texttt{std::allocator}).
\end{itemize}

\section{Vòng Đời Khởi Tạo và Hủy Kế Thừa}

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
Destructor Lớp Con chạy trước $\longrightarrow$ Dọn dẹp thành viên $\longrightarrow$ Destructor Lớp Cha chạy sau cùng.
\end{center}
\end{theorybox}

\begin{warningbox}[Yêu Cầu Gọi Base Copy Constructor Khi Tự Viết Copy Ctor Ở Lớp Con]
Khi lập trình viên tự tay viết Copy Constructor cho lớp con:
\begin{lstlisting}[language=C++]
class Base {
public:
    int baseVal;
    Base(int v) : baseVal(v) {}
    Base(const Base& other) : baseVal(other.baseVal) {}
};

class Derived : public Base {
public:
    int derivedVal;
    Derived(int b, int d) : Base(b), derivedVal(d) {}

    // DANGEROUS OMISSION: Quen goi Base(other) trong member initializer list!
    Derived(const Derived& other) : derivedVal(other.derivedVal) {
        // Compiler se am tham goi Default Constructor Base::Base()!
        // Neu Base khong co Default Ctor -> Loi bien dich.
        // Neu Base co Default Ctor -> baseVal bi dat lai mac dinh, mat du lieu sao chep!
    }

    // HIEN THUC HOA CHUAN MUC:
    // Derived(const Derived& other) : Base(other), derivedVal(other.derivedVal) {}
};
\end{lstlisting}
\end{warningbox}

\section{Hiện Tượng Che Khuất Tên (Name Hiding) vs Nạp Chồng}

Trong C++, cơ chế phân giải tên (\textit{Name Lookup}) tuân theo nguyên tắc: \textbf{Dừng lại ở phạm vi gần nhất tìm thấy định danh trùng khớp}.

\begin{lstlisting}[language=C++]
class Base {
public:
    void process(int x) { std::cout << "Base::process(int)\n"; }
    void process(double x) { std::cout << "Base::process(double)\n"; }
};

class Derived : public Base {
public:
    // Che khuat toan bo cac ham Base::process:
    void process(std::string s) { std::cout << "Derived::process(string)\n"; }
};

void test() {
    Derived d;
    d.process("Hello"); // Hop le: Goi Derived::process(string)
    // d.process(10);   // LOI BIEN DICH: Compiler khong the tim thay process(int)!
}
\end{lstlisting}

\begin{underhoodbox}[Bản Chất Của Hiện Tượng Name Hiding]
Tại sao \texttt{d.process(10)} không gọi \texttt{Base::process(int)}?
\begin{enumerate}
    \item Khi phân tích cú pháp biểu thức \texttt{d.process(10)}, trình biên dịch bắt đầu tìm kiếm tên định danh \texttt{process} từ phạm vi của lớp \texttt{Derived}.
    \item Nó tìm thấy \texttt{void Derived::process(std::string)}.
    \item \textbf{Cơ chế dừng tìm kiếm:} Khi đã tìm thấy ít nhất một tên khớp trong một phạm vi, trình biên dịch \textbf{DỪNG TÌM KIẾM NGAY LẬP TỨC} và không bao giờ quét tiếp lên phạm vi của lớp cha \texttt{Base}!
    \item Sau đó, nó tiến hành phân giải nạp chồng trên tập hợp các hàm tìm được tại lớp con. Vì tập hợp này chỉ có phiên bản nhận \texttt{std::string}, việc truyền số nguyên \texttt{10} bị báo lỗi biên dịch.
    \item \textbf{Giải pháp chuẩn mực:} Sử dụng từ khóa \textbf{\texttt{using}} để kéo toàn bộ họ hàm của cha vào lớp con:
    \begin{lstlisting}[language=C++]
    class Derived : public Base {
    public:
        using Base::process; // Keo toan bo cac ban nap chong cua Base vao Derived
        void process(std::string s);
    };
    \end{lstlisting}
\end{enumerate}
\end{underhoodbox}

\section{Cắt Xén Đối Tượng Đa Hình (Polymorphic Object Slicing)}

\begin{dangerbox}[Hiện Tượng Cắt Xén Đối Tượng Khi Truyền Tham Trị]
Xét đoạn mã sau:
\begin{lstlisting}[language=C++]
void renderEntity(Base b) { // Truyen theo GIA TRI (Pass-by-value)
    // ...
}

void execution() {
    Derived d(10, 20);
    renderEntity(d); // HIEN TUONG CAT XEN XAY RA TAI DAY
}
\end{lstlisting}

\textbf{Giải phẫu cơ chế cắt xén dưới RAM:}
\begin{enumerate}
    \item Hàm \texttt{renderEntity} yêu cầu một biến có kích thước đúng bằng $\text{sizeof}(\text{Base})$ trên ngăn xếp Stack của nó.
    \item Khi truyền đối tượng \texttt{d} vào, trình biên dịch gọi Copy Constructor của lớp cơ sở: \texttt{Base::Base(const Base\&)}.
    \item Trình biên dịch sao chép chính xác phần Subobject của Base từ \texttt{d}, và \textbf{GỌT BỎ HOÀN TOÀN (SLICE OFF)} toàn bộ các trường dữ liệu riêng và bản chất đa hình của \texttt{Derived}!
    \item Mọi hành vi đa hình và dữ liệu của lớp con bị tiêu biến hoàn toàn mà không có bất kỳ cảnh báo biên dịch nào.
    \item \textbf{Quy tắc Vàng:} Trong hướng đối tượng, luôn luôn truyền đối tượng đa hình qua \textbf{Tham Chiếu Hằng (\texttt{const Base\&})} hoặc \textbf{Con Trỏ (\texttt{Base*})}, tuyệt đối cấm truyền theo giá trị.
\end{enumerate}
\end{dangerbox}

\section{Đa Kế Thừa, Bài Toán Kim Cương \& Kế Thừa Ảo}

\subsection{Mô Hình Bài Toán Kim Cương (The Diamond Problem)}

Đa kế thừa (\textit{Multiple Inheritance}) cho phép một lớp kế thừa từ nhiều lớp cha độc lập. Tuy nhiên, nó dẫn tới cấu trúc đồ thị hình thoi kinh điển:

\begin{figure}[htbp]
\centering
\resizebox{0.70\textwidth}{!}{%
\begin{tikzpicture}[
    box/.style={draw=primaryblue, thick, rounded corners=3pt, fill=white, inner sep=6pt, font=\small\bfseries\sffamily, align=center, text width=3.4cm},
    umlarrow/.style={-{Triangle[open, length=3mm, width=3mm]}, thick, primaryblue}
]
    \node[box, fill=bglighterblue] (A) at (0, 3.8) {Lớp Cơ Sở A\\\footnotesize\ttfamily int id;};
    \node[box, fill=white] (B) at (-3.5, 1.9) {Lớp Con B};
    \node[box, fill=white] (C) at (3.5, 1.9) {Lớp Con C};
    \node[box, fill=bgsoftblue, draw=accentblue, line width=1.4pt] (D) at (0, 0.0) {Lớp Đa Kế Thừa D};

    % Standard UML generalization arrows pointing UP to base classes
    \draw[umlarrow] (B.north) -- ([xshift=-1.0cm]A.south);
    \draw[umlarrow] (C.north) -- ([xshift=1.0cm]A.south);
    \draw[umlarrow] ([xshift=-1.0cm]D.north) -- (B.south);
    \draw[umlarrow] ([xshift=1.0cm]D.north) -- (C.south);
\end{tikzpicture}%
}
\caption{Mô hình phân cấp kế thừa hình thoi chuẩn UML (The Diamond Problem).}
\end{figure}

\begin{itemize}
    \item \textbf{Nếu không có kế thừa ảo:} Đối tượng \texttt{D} trong RAM sẽ chứa \textbf{HAI BẢN SAO ĐỘC LẬP CỦA $A$} (một bản qua nhánh $B$, một bản qua nhánh $C$). Kích thước đối tượng bị nhân đôi, và lời gọi \texttt{d.id} bị trình biên dịch từ chối vì xung đột mơ hồ (\textit{Ambiguity Error}).
    \item \textbf{Giải pháp: Kế Thừa Ảo (\texttt{virtual public A}):}
    \begin{lstlisting}[language=C++]
    class A { public: int id; A(int x) : id(x) {} };
    class B : virtual public A { public: B() : A(1) {} };
    class C : virtual public A { public: C() : A(2) {} };
    class D : public B, public C {
    public:
        // MOST-DERIVED CLASS EXCLUSIVE DUTY:
        // D truc tiep chiu trach nhiem khoi tao A!
        D() : A(100), B(), C() {}
    };
    \end{lstlisting}
\end{itemize}

\begin{underhoodbox}[Kiến Trúc Bộ Nhớ Kế Thừa Ảo: MSVC vs Itanium ABI]
Để bảo đảm trong lòng đối tượng $D$ chỉ tồn tại duy nhất \textbf{MỘT Subobject $A$ dùng chung}, hai họ trình biên dịch sử dụng hai giải pháp nhị phân độc lập:
\begin{enumerate}
    \item \textbf{Microsoft Visual C++ (MSVC Model):} Chèn thêm con trỏ cơ sở ảo \textbf{\texttt{vbptr}} (Virtual Base Pointer) vào các lớp trung gian $B$ và $C$. Con trỏ này trỏ tới bảng \textbf{Virtual Base Table (vbtbl)} chứa độ lệch động tới Subobject $A$ dùng chung nằm ở cuối đối tượng.
    \item \textbf{Itanium C++ ABI (GCC / Clang Model):} Không sử dụng con trỏ \texttt{vbptr} riêng rẽ. Thay vào đó, \textbf{Virtual Base Offsets} được lưu trữ tại các \textbf{offset âm ngay bên trong VTable} của đối tượng. Đồng thời, trình biên dịch sinh ra một bảng cấu trúc phụ gọi là \textbf{VTT (Virtual Table Table)} để truyền vào Constructor khi khởi tạo các subobject.
    \item \textbf{Quy tắc Thống trị (The Dominance Rule):} Trong cây kế thừa ảo, nếu một phương thức ảo được ghi đè tại một lớp dẫn xuất $B$, thì định nghĩa tại $B$ sẽ "thống trị" định nghĩa gốc tại $A$, cho phép trình biên dịch tự động giải quyết xung đột tên mà không báo lỗi mơ hồ.
\end{enumerate}
\end{underhoodbox}
"""
