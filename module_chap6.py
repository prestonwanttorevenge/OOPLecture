# -*- coding: utf-8 -*-

chap6_text = r"""
% ==============================================================================
% CHƯƠNG 6: KHUÔN MẪU & LẬP TRÌNH TỔNG QUÁT (TEMPLATES & GENERIC PROGRAMMING)
% ==============================================================================
\chapter{Khuôn mẫu \& Lập trình Tổng quát (Templates \& Generic Programming)}

\begin{theorybox}[Định Nghĩa: Lập Trình Tổng Quát (Generic Programming)]
\textbf{Lập trình Tổng quát (Generic Programming)} là hệ hình lập trình trong đó mã nguồn được viết một cách trừu tượng hóa, độc lập hoàn toàn với các kiểu dữ liệu cụ thể. Thay vì phải sao chép thuật toán tìm kiếm hay cấu trúc danh sách liên kết cho từng kiểu \texttt{int}, \texttt{double}, \texttt{Student}, lập trình viên sử dụng \textbf{Khuôn mẫu (Templates)} để biến \textbf{Kiểu dữ liệu thành Tham số (Type-as-a-Parameter)}.
\end{theorybox}

\section{Khuôn Mẫu Hàm \& Khuôn Mẫu Lớp (Function \& Class Templates)}

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

\section{Cơ Chế Phân Giải Tên Hai Giai Đoạn (Two-Phase Name Lookup)}

Một trong những cơ chế phức tạp nhất của trình biên dịch C++ khi xử lý template là quy trình phân giải tên hai giai đoạn:

\begin{enumerate}
    \item \textbf{Giai đoạn 1 (Phân tích cú pháp định nghĩa --- Parsing Phase):} Xảy ra khi trình biên dịch lần đầu tiên quét qua khai báo khuôn mẫu. Trình biên dịch kiểm tra tính hợp lệ cú pháp của các thành phần không phụ thuộc vào tham số kiểu $T$.
    \item \textbf{Giai đoạn 2 (Tạo thực thể --- Instantiation Phase):} Xảy ra khi lập trình viên thực sự sử dụng template với kiểu cụ thể (ví dụ \texttt{SafeStack<int> s;}). Trình biên dịch thay thế tham số kiểu và sinh mã máy thực tế.
\end{enumerate}

\subsection{Từ Khóa \texttt{typename} và \texttt{.template} Cho Tên Phụ Thuộc (Dependent Names)}

\begin{lstlisting}[language=C++]
template <typename Container>
void printFirstElement(const Container& c) {
    // BAT BUOC CO 'typename' vi const_iterator la kieu phu thuoc:
    typename Container::const_iterator it = c.begin();
    if (it != c.end()) {
        std::cout << *it << "\n";
    }
}

template <typename T>
void parseData(T& parser) {
    // BAT BUOC CO '.template' de compiler khong nham '<' thanh toan tu so sanh:
    parser.template parse<int>();
}
\end{lstlisting}

\section{Chuyên Biệt Hóa Khuôn Mẫu \& Giải Pháp Hiện Đại C++17}

\subsection{Chuyên Biệt Hóa Toàn Phần (Full Specialization)}

\begin{lstlisting}[language=C++]
// 1. Primary Template
template <typename T>
struct Serializer {
    static void serialize(const T& val) { /* Generic serialization */ }
};

// 2. Full Specialization for bool:
template <>
struct Serializer<bool> {
    static void serialize(const bool& val) { /* Bit-packing optimization */ }
};
\end{lstlisting}

\subsection{C++17 \texttt{if constexpr}: Chấm Dứt Bẫy Nạp Chồng Herb Sutter}

Trước C++17, việc nạp chồng hoặc chuyên biệt hóa hàm template thường dẫn đến các bẫy phân giải phức tạp theo phân tích của Herb Sutter. Chuẩn C++17 giới thiệu \textbf{\texttt{if constexpr}}, cho phép rẽ nhánh điều kiện ngay tại thời điểm biên dịch một cách thanh lịch:

\begin{lstlisting}[language=C++]
#include <type_traits>

template <typename T>
void processEntity(T val) {
    if constexpr (std::is_pointer_v<T>) {
        if (val) std::cout << "Pointer value: " << *val << "\n";
    } else {
        std::cout << "Direct value: " << val << "\n";
    }
}
\end{lstlisting}
Nhánh không thỏa mãn điều kiện sẽ bị loại bỏ hoàn toàn khỏi mã máy mà không cần viết các lớp chuyên biệt hóa phụ trợ!

\section{Các Tính Năng Khuôn Mẫu Hiện Đại: Variadics \& Fold Expressions}

\subsection{Biểu Thức Gập C++17 (Fold Expressions)}

Từ chuẩn C++17, kỹ thuật đệ quy gói tham số phức tạp của C++11 được thay thế bằng \textbf{Biểu Thức Gập (Fold Expressions)}:

\begin{lstlisting}[language=C++]
// C++17 Binary Right Fold: Zero recursion, zero base cases!
template <typename... Args>
void printAll(const Args&... args) {
    ((std::cout << args << " "), ...) << "\n";
}

template <typename... Args>
auto sumAll(Args... args) {
    return (... + args); // Unary left fold over + operator
}
\end{lstlisting}

\section{CRTP: Đa Hình Tĩnh (Static Polymorphism)}

Làm thế nào để đạt được sức mạnh của Đa hình nhưng \textbf{không phải trả giá cho VTable, con trỏ vptr, và indirect jump}? Câu trả lời là kỹ thuật \textbf{Curiously Recurring Template Pattern (CRTP)}:

\begin{figure}[htbp]
\centering
\resizebox{0.95\textwidth}{!}{%
\begin{tikzpicture}[
    box/.style={draw=primaryblue, thick, rounded corners=3pt, fill=white, inner sep=6pt, font=\small\sffamily, align=center},
    stepbox/.style={draw=accentblue, thick, rounded corners=2pt, fill=bglighterblue, inner sep=5pt, font=\footnotesize\sffamily, align=center}
]
    % Dynamic Polymorphism branch (Left side centered at x = -3.8)
    \node[box, fill=bgsoftblue, text width=6.2cm] (dyn_title) at (-3.8, 4.4) {\textbf{Đa Hình Động (Virtual Functions)}\\\footnotesize Chi Phí Thời Gian Thực Thi (Runtime)};
    \node[stepbox, text width=5.6cm, minimum height=0.75cm] (dyn_step1) at (-3.8, 3.0) {1. Lấy con trỏ ẩn \texttt{\_\_vptr} từ RAM đối tượng};
    \node[stepbox, text width=5.6cm, minimum height=0.75cm] (dyn_step2) at (-3.8, 1.5) {2. Tra cứu mảng VTable trong \texttt{.rodata}};
    \node[stepbox, text width=5.6cm, minimum height=0.75cm] (dyn_step3) at (-3.8, 0.0) {3. Nhảy gián tiếp \texttt{call [rax+offset]} (Mất Inline)};

    % Static Polymorphism branch (Right side centered at x = 3.8)
    \node[box, fill=bgsoftblue, text width=6.2cm] (stat_title) at (3.8, 4.4) {\textbf{Đa Hình Tĩnh CRTP (\texttt{template})}\\\footnotesize Tối Ưu Compile-Time (Zero-Overhead)};
    \node[stepbox, text width=5.6cm, minimum height=0.75cm] (stat_step1) at (3.8, 3.0) {1. Phân giải kiểu \texttt{Derived} tại Compile-time};
    \node[stepbox, text width=5.6cm, minimum height=0.75cm] (stat_step2) at (3.8, 1.5) {2. Ép kiểu tĩnh \texttt{static\_cast<Derived*>(this)}};
    \node[stepbox, text width=5.6cm, minimum height=0.75cm] (stat_step3) at (3.8, 0.0) {3. Tối ưu hóa Inlining 100\% thành mã máy trực tiếp};

    % Clean downward arrows pointing south to north
    \draw[-{Stealth[length=2.5mm]}, thick, primaryblue] (dyn_step1.south) -- (dyn_step2.north);
    \draw[-{Stealth[length=2.5mm]}, thick, primaryblue] (dyn_step2.south) -- (dyn_step3.north);

    \draw[-{Stealth[length=2.5mm]}, thick, accentblue] (stat_step1.south) -- (stat_step2.north);
    \draw[-{Stealth[length=2.5mm]}, thick, accentblue] (stat_step2.south) -- (stat_step3.north);
\end{tikzpicture}%
}
\caption{So sánh cơ chế phân giải giữa Đa hình động (VTable) và Đa hình tĩnh CRTP.}
\end{figure}

\begin{lstlisting}[language=C++]
template <typename Derived>
class BaseProcessor {
public:
    void execute() {
        // Ep kieu tinh con tro ban the tai compile-time:
        static_cast<Derived*>(this)->processImpl();
    }
};

class FastNetworkProcessor : public BaseProcessor<FastNetworkProcessor> {
public:
    void processImpl() { // Khong can tu khoa virtual!
        std::cout << "High-speed zero-overhead processing\n";
    }
};

template <typename T>
void run(BaseProcessor<T>& proc) {
    proc.execute(); // Inlined 100%, toc do toi da!
}
\end{lstlisting}
"""
