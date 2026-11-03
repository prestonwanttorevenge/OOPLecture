# -*- coding: utf-8 -*-

chap6_text = r"""
% ==============================================================================
% CHƯƠNG 6: KHUÔN MẪU & LẬP TRÌNH TỔNG QUÁT (TEMPLATES & GENERIC PROGRAMMING)
% ==============================================================================
\chapter{Khuôn mẫu \& Lập trình Tổng quát (Templates \& Generic Programming)}

\begin{theorybox}[Định Nghĩa: Lập Trình Tổng Quát (Generic Programming)]
\textbf{Lập trình Tổng quát (Generic Programming)} là hệ hình lập trình trong đó mã nguồn được viết một cách trừu tượng hóa, độc lập hoàn toàn với các kiểu dữ liệu cụ thể. Thay vì phải sao chép thuật toán tìm kiếm hay cấu trúc danh sách liên kết cho từng kiểu \texttt{int}, \texttt{double}, \texttt{Student}, lập trình viên sử dụng \textbf{Khuôn mẫu (Templates)} để biến \textbf{Kiểu dữ liệu thành Tham số (Type-as-a-Parameter)}.\footnote{Nguồn: OOP7-Template.pdf - Trang 2-9: Khái niệm khuôn mẫu hàm và khuôn mẫu lớp}
\end{theorybox}

\section{Khuôn Mẫu Hàm \& Khuôn Mẫu Lớp (Function \& Class Templates)}

\subsection{Cú pháp và Sự tương đương giữa \texttt{typename} và \texttt{class}}

\begin{lstlisting}[language=C++]
// Generic swap function template
template <typename T>
void genericSwap(T& a, T& b) {
    T temp = std::move(a);
    a = std::move(b);
    b = std::move(temp);
}

// Generic safe stack class template
template <typename T>
class SafeStack {
private:
    std::vector<T> elements;
public:
    void push(const T& val) { elements.push_back(val); }
    void push(T&& val) { elements.push_back(std::move(val)); }
    T pop() {
        if (elements.empty()) throw std::out_of_range("Stack empty");
        T val = std::move(elements.back());
        elements.pop_back();
        return val;
    }
};
\end{lstlisting}

\textit{Phân biệt \texttt{typename} và \texttt{class} trong khai báo template:}
Trong danh sách tham số kiểu khuôn mẫu \texttt{template <typename T>} và \texttt{template <class T>}, hai từ khóa này \textbf{hoàn toàn đồng nghĩa 100\%} về mặt ngữ nghĩa ngữ pháp. Từ khóa \texttt{typename} được chuẩn hóa sau này để tránh gây hiểu lầm rằng kiểu truyền vào bắt buộc phải là một \texttt{class} (vì các kiểu nguyên thủy như \texttt{int}, \texttt{double}, con trỏ thô đều truyền vào được).

\section{Quá Trình Biên Dịch Hai Pha (Two-Phase Lookup) \& Dependent Types}

Một trong những cơ chế phức tạp nhất của trình biên dịch C++ khi xử lý template là quy trình phân giải tên hai pha:

\begin{enumerate}
    \item \textbf{Pha 1 (Pha định nghĩa khuôn mẫu - Parsing Phase):}
    \begin{itemize}
        \item Xảy ra khi trình biên dịch lần đầu tiên quét qua đoạn mã \texttt{template <typename T> ...}.
        \item Trình biên dịch chỉ kiểm tra cú pháp cơ bản độc lập với kiểu (dấu chấm phẩy, đóng mở ngoặc, các biến không phụ thuộc vào \texttt{T}).
    \end{itemize}
    \item \textbf{Pha 2 (Pha tạo thực thể - Instantiation Phase):}
    \begin{itemize}
        \item Xảy ra khi lập trình viên thực sự sử dụng template với một kiểu cụ thể (ví dụ \texttt{SafeStack<int> s;}).
        \item Trình biên dịch thay thế toàn bộ tham số \texttt{T} bằng \texttt{int} và tiến hành biên dịch mã máy thực tế, kiểm tra tính hợp lệ của các phép toán trên kiểu đó.\footnote{Nguồn: OOP7-Template.pdf - Trang 15-24: Quá trình biên dịch Template và Two-Phase Lookup}
    \end{itemize}
\end{enumerate}

\subsection{Bắt Buộc Sử Dụng Từ Khóa \texttt{typename} Cho Kiểu Phụ Thuộc (Dependent Types)}

Xét đoạn mã template kinh điển sau:
\begin{lstlisting}[language=C++]
template <typename Container>
void printFirstElement(const Container& c) {
    // COMPILATION ERROR IF MISSING 'typename':
    typename Container::const_iterator it = c.begin();
    if (it != c.end()) {
        std::cout << *it << "\n";
    }
}
\end{lstlisting}

\begin{underhoodbox}[Tại Sao Bắt Buộc Viết \texttt{typename Container::const\_iterator}?]
Trong Pha 1 của quá trình biên dịch, trình biên dịch chưa hề biết kiểu cụ thể của \texttt{Container} là gì.

Xét biểu thức có dạng: \texttt{Container::foo * bar;}
\begin{itemize}
    \item \textbf{Trường hợp A:} Nếu \texttt{foo} là một \textbf{Kiểu dữ liệu} (Type), đây là dòng lệnh khai báo một con trỏ \texttt{bar} có kiểu là \texttt{Container::foo}.
    \item \textbf{Trường hợp B:} Nếu \texttt{foo} là một \textbf{Biến tĩnh} (Static Data Member), đây là một \textbf{Phép nhân số học}: Lấy giá trị biến tĩnh \texttt{foo} nhân với biến \texttt{bar}!
\end{itemize}
Theo quy tắc chuẩn của ISO C++, khi đứng trước một tên phụ thuộc (\textit{Dependent Name}), trình biên dịch \textbf{mặc định coi đó là một biến tĩnh}. 

Do đó, nếu \texttt{Container::const\_iterator} thực sự là một kiểu dữ liệu nội bộ (Nested Type), bạn \textbf{bắt buộc phải gắn từ khóa \texttt{typename} ở phía trước} để thông báo cho trình biên dịch: \textit{"Đây là một kiểu dữ liệu, hãy phân tích cú pháp theo ngữ cảnh khai báo kiểu!"}\footnote{Nguồn: OOP7-Template.pdf - Trang 25-28: Từ khóa typename cho dependent types}
\end{underhoodbox}

\section{Cơ Chế Tạo Thực Thể \& Hiện Tượng Phình To Mã (Code Bloat)}

\subsection{Tại Sao Phải Viết Toàn Bộ Code Template Trong File Header (\texttt{.hpp})?}

Đây là lỗi phổ biến nhất của sinh viên chuyển từ lập trình hướng thủ tục sang lập trình hướng đối tượng với template: Tách khai báo vào file \texttt{.h} và viết định nghĩa thân hàm vào file \texttt{.cpp}.

\begin{lstlisting}[language=C++]
// File: MyStack.h
template <typename T>
class MyStack {
public:
    void push(T val);
};

// File: MyStack.cpp
#include "MyStack.h"
template <typename T>
void MyStack<T>::push(T val) { /* logic */ } // ERROR ARCHITECTURE!

// File: main.cpp
#include "MyStack.h"
int main() {
    MyStack<int> s;
    s.push(10); // LINKER ERROR: undefined reference to MyStack<int>::push(int)
}
\end{lstlisting}

\begin{underhoodbox}[Nguyên Nhân Gầm Máy: Mô Hình Biên Dịch Độc Lập (Separate Compilation)]
\begin{enumerate}
    \item C++ biên dịch từng file mã nguồn (\texttt{.cpp}) thành các đơn vị dịch độc lập (\textbf{Translation Units - TU}) để tạo ra các file đối tượng (\texttt{.obj} / \texttt{.o}).
    \item Khi biên dịch file \texttt{MyStack.cpp}, trình biên dịch thấy template \texttt{MyStack<T>}, nhưng vì \textbf{không có mã nào gọi \texttt{MyStack<int>}} trong file này, trình biên dịch \textbf{không thể sinh ra một dòng mã máy nào}! File \texttt{MyStack.o} hoàn toàn trống rỗng!
    \item Khi biên dịch file \texttt{main.cpp}, trình biên dịch thấy lệnh gọi \texttt{s.push(10)}, nhưng vì file \texttt{MyStack.h} chỉ chứa khai báo mà không có phần thân hàm, nó không thể sinh mã máy được. Nó tạm thời xuất ra một lời gọi hàm ngoại vi chưa phân giải.
    \item Đến giai đoạn liên kết (\textbf{Linking}), Linker đi tìm mã máy của \texttt{MyStack<int>::push(int)} trong toàn bộ các file \texttt{.o} nhưng không tìm thấy ở đâu $\rightarrow$ Báo lỗi chết người: \textbf{LNK2019 / Undefined Reference}!
    \item \textbf{Kết luận:} Template không phải là mã máy, template chỉ là \textbf{Bản Thiết Kế (Blueprint)}. Do đó, toàn bộ khai báo và định nghĩa của template \textbf{bắt buộc phải nằm trọn vẹn trong file Header (\texttt{.hpp})} để bất kỳ file \texttt{.cpp} nào gọi nó cũng có đầy đủ mã nguồn để tự sinh mã máy.\footnote{Nguồn: OOP7-Template.pdf - Trang 29-38: Template Compilation Model \& Header-only requirement}
\end{enumerate}
\end{underhoodbox}

\subsection{Hiện Tượng Phình To Mã Nguồn (Code Bloat)}

Khi chương trình gọi \texttt{SafeStack<int>}, \texttt{SafeStack<double>}, \texttt{SafeStack<std::string>}, và \texttt{SafeStack<void*>}, trình biên dịch sẽ sinh ra \textbf{4 bản sao mã máy nhị phân hoàn toàn riêng biệt}. Nếu template của bạn lớn, dung lượng file thực thi (\texttt{.exe}) sẽ tăng vọt theo cấp số nhân.

\textbf{Giải pháp Thin Template Idiom của STL:}
Đối với các kiểu con trỏ (\texttt{T*}), STL sử dụng một lớp cơ sở không phải template thao tác hoàn toàn trên \texttt{void*}. Sau đó, các template con trỏ chỉ đơn thuần kế thừa và ép kiểu an toàn:
\begin{lstlisting}[language=C++]
class RawPointerStack { // Compiled ONCE into machine code
protected:
    std::vector<void*> rawPtrs;
    void pushRaw(void* ptr);
    void* popRaw();
};

template <typename T>
class PointerStack : private RawPointerStack { // Inlined, zero overhead
public:
    void push(T* ptr) { pushRaw(static_cast<void*>(ptr)); }
    T* pop() { return static_cast<T*>(popRaw()); }
};
\end{lstlisting}

\section{Tham Số Không Phải Kiểu (NTTP) \& Template Template Parameters}

\subsection{Tham Số Không Phải Kiểu (Non-type Template Parameters - NTTP)}

Template không chỉ nhận kiểu dữ liệu mà còn có thể nhận các giá trị hằng số nguyên, con trỏ, hoặc tham chiếu tại thời điểm biên dịch:
\begin{lstlisting}[language=C++]
// Memory optimization: Zero heap allocation
template <typename T, std::size_t Capacity>
class FixedCapacityArray {
private:
    T data[Capacity]; // Array allocated directly on STACK!
    std::size_t size = 0;
public:
    constexpr std::size_t max_size() const { return Capacity; }
    void push(const T& val) {
        if (size >= Capacity) throw std::overflow_error("Buffer full");
        data[size++] = val;
    }
};

// Usage:
FixedCapacityArray<int, 256> fastBuffer; // 1024 bytes on Stack, 0 ns alloc overhead!
\end{lstlisting}
Đây chính là nền tảng hoạt động của \texttt{std::array<T, N>} trong thư viện chuẩn C++11.\footnote{Nguồn: OOP7-Template.pdf - Trang 39-48: Non-type Template Parameters và ứng dụng}

\section{Chuyên Biệt Hóa Khuôn Mẫu (Template Specialization) \& Bẫy Herb Sutter}

Đôi khi, một thuật toán tổng quát không tối ưu cho một kiểu dữ liệu đặc thù. C++ cho phép ta cung cấp các phiên bản chuyên biệt hóa:

\subsection{Chuyên Biệt Hóa Toàn Phần \& Một Phần (Full vs Partial Specialization)}

\begin{lstlisting}[language=C++]
// 1. Primary Template
template <typename T, typename Allocator>
class DynamicList { /* Generic implementation */ };

// 2. Partial Specialization for pointer types:
template <typename T, typename Allocator>
class DynamicList<T*, Allocator> {
    /* Specialized implementation for pointers */
};

// 3. Full / Explicit Specialization for bool:
template <>
class DynamicList<bool, std::allocator<bool>> {
    /* Bit-packing optimization: 1 BIT per boolean instead of 1 BYTE! */
};
\end{lstlisting}

\subsection{Bẫy Tử Thần Herb Sutter: Function Template Không Hỗ Trợ Partial Specialization!}

Chuẩn C++ \textbf{TUYỆT ĐỐI CẤM} việc Chuyên biệt hóa một phần đối với Khuôn mẫu hàm (\textit{Function Template Partial Specialization is illegal}).

Nhiều lập trình viên cố gắng kết hợp Nạp chồng hàm template (Function Template Overloading) với Chuyên biệt hóa toàn phần (Full Specialization), tạo ra các lỗi logic thảm họa:
\begin{lstlisting}[language=C++]
template <typename T> void process(T);       // (1) Primary template 1
template <typename T> void process(T*);      // (2) Primary template 2 (Overload)

template <> void process<int*>(int*);        // (3) Specialization of which?
\end{lstlisting}

\begin{underhoodbox}[Bẫy Sutter's Trap Dưới Lăng Kính Phân Giải Overload]
Theo chuẩn ISO C++: \textbf{Quá trình phân giải nạp chồng (Overload Resolution) chỉ xem xét các Primary Templates!}
\begin{enumerate}
    \item Trình biên dịch xem xét (1) và (2) để chọn ra template phù hợp nhất.
    \item Nếu hàm (3) được khai báo sau (2), nó là specialization của (2). Nhưng nếu nó khai báo trước (2), nó lại trở thành specialization của (1)!
    \item Khi có sự xuất hiện của các chuyển đổi kiểu ngầm định, hàm specialization có thể bị bỏ qua hoàn toàn, dẫn đến trình biên dịch gọi một template mà lập trình viên không hề mong muốn.
    \item \textbf{Quy Tắc Herb Sutter (C++ Guru):} \textit{"Không bao giờ chuyên biệt hóa khuôn mẫu hàm. Khi cần đa dạng hóa hành vi của hàm template, hãy nạp chồng hàm bình thường, hoặc ủy quyền (delegate) việc thực thi cho một Class Template nội bộ!"}\footnote{Nguồn: OOP7-Template.pdf - Trang 49-62: Chuyên biệt hóa khuôn mẫu và Bẫy nạp chồng Herb Sutter}
\end{enumerate}
\end{underhoodbox}

\section{Các Tính Năng Khuôn Mẫu C++11 Hiện Đại}

\subsection{Variadic Templates (Khuôn Mẫu Tham Số Biến Thiên)}

Trước C++11, để viết một hàm in ra số lượng tham số tùy ý, lập trình viên phải viết hàng chục bản nạp chồng quá tải. C++11 giới thiệu \textbf{Variadic Templates} thông qua \textbf{Parameter Pack}:

\begin{lstlisting}[language=C++]
// 1. Base case to terminate compile-time recursion
void printAll() {
    std::cout << "\n";
}

// 2. Recursive pack expansion at COMPILE-TIME
template <typename Head, typename... Tail>
void printAll(const Head& head, const Tail&... tail) {
    std::cout << head << " ";
    printAll(tail...); // Unpack parameter pack recursively
}

// Usage:
printAll(1, 3.14, "C++ Bible", 'A', true);
\end{lstlisting}
Cơ chế này hoàn toàn không dùng con trỏ ngăn xếp biến thiên kiểu C (\texttt{va\_list}), đảm bảo \textbf{Type-safety 100\%} và được tối ưu hóa inline hoàn toàn tại compile-time! Đây là nền tảng xây dựng nên \texttt{std::tuple} và phương thức \texttt{emplace\_back}.\footnote{Nguồn: OOP7-Template.pdf - Trang 63-70: C++11 Variadic Templates và Parameter Packs}

\subsection{CRTP: Đa Hình Tĩnh (Static Polymorphism)}

Làm thế nào để đạt được sức mạnh của Đa hình nhưng \textbf{không phải trả giá cho VTable, con trỏ vptr, và indirect jump}? Câu trả lời là kỹ thuật \textbf{Curiously Recurring Template Pattern (CRTP)}:

\begin{figure}[htbp]
\centering
\resizebox{0.95\textwidth}{!}{%
\begin{tikzpicture}[
    box/.style={draw=primaryblue, thick, rounded corners=3pt, fill=white, inner sep=6pt, font=\small\sffamily, align=center},
    stepbox/.style={draw=accentblue, thick, rounded corners=2pt, fill=bglighterblue, inner sep=5pt, font=\footnotesize\sffamily, align=center}
]
    % Dynamic Polymorphism branch
    \node[box, fill=bgsoftblue, text width=6.2cm] (dyn_title) at (-3.6, 3.5) {\textbf{Đa Hình Động (Virtual Functions)}\\\footnotesize Chi Phí Thời Gian Thực Thi (Runtime)};
    \node[stepbox, text width=5.6cm] (dyn_step1) at (-3.6, 2.2) {1. Lấy con trỏ ẩn \texttt{\_\_vptr} từ RAM đối tượng};
    \node[stepbox, text width=5.6cm] (dyn_step2) at (-3.6, 1.1) {2. Tra cứu mảng VTable trong phân vùng \texttt{.rodata}};
    \node[stepbox, text width=5.6cm] (dyn_step3) at (-3.6, 0.0) {3. Nhảy gián tiếp \texttt{call [rax+offset]} (Mất Inline)};

    % Static Polymorphism branch
    \node[box, fill=bgsoftblue, text width=6.2cm] (stat_title) at (3.6, 3.5) {\textbf{Đa Hình Tĩnh CRTP (\texttt{template})}\\\footnotesize Tối Ưu Compile-Time (Zero-Overhead)};
    \node[stepbox, text width=5.6cm] (stat_step1) at (3.6, 2.2) {1. Phân giải kiểu \texttt{Derived} tại Compile-time};
    \node[stepbox, text width=5.6cm] (stat_step2) at (3.6, 1.1) {2. Ép kiểu tĩnh \texttt{static\_cast<Derived*>(this)}};
    \node[stepbox, text width=5.6cm] (stat_step3) at (3.6, 0.0) {3. Tối ưu hóa Inlining 100\% thành mã máy trực tiếp};

    % Connections
    \draw[-{Stealth[length=2mm]}, thick, primaryblue] (dyn_step1) -- (dyn_step2);
    \draw[-{Stealth[length=2mm]}, thick, primaryblue] (dyn_step2) -- (dyn_step3);

    \draw[-{Stealth[length=2mm]}, thick, accentblue] (stat_step1) -- (stat_step2);
    \draw[-{Stealth[length=2mm]}, thick, accentblue] (stat_step2) -- (stat_step3);
\end{tikzpicture}%
}
\caption{So sánh cơ chế phân giải giữa Đa hình động (VTable) và Đa hình tĩnh CRTP.}
\end{figure}

\begin{lstlisting}[language=C++]
template <typename Derived>
class BaseProcessor {
public:
    void execute() {
        // Static downcast of this pointer to derived class at compile-time:
        static_cast<Derived*>(this)->processImpl();
    }
};

class FastNetworkProcessor : public BaseProcessor<FastNetworkProcessor> {
public:
    void processImpl() { // No virtual keyword needed!
        std::cout << "High-speed zero-overhead processing\n";
    }
};

template <typename T>
void run(BaseProcessor<T>& proc) {
    proc.execute(); // Fully inlined, maximum CPU clock execution speed!
}
\end{lstlisting}
CRTP là vũ khí tối thượng được sử dụng trong các hệ thống giao dịch tài chính tần suất cao (High-Frequency Trading - HFT) và game engine, nơi từng phần tỉ giây (nanosecond) đều quý giá!
"""
