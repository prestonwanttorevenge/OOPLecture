# -*- coding: utf-8 -*-

chap3_text = r"""
% ==============================================================================
% CHƯƠNG 3: QUẢN TRỊ BỘ NHỚ, MOVE SEMANTICS & NẠP CHỒNG TOÁN TỬ
% ==============================================================================
\chapter{Quản trị Bộ nhớ, Move Semantics \& Nạp chồng Toán tử (Memory \& Overloading)}

\begin{theorybox}[Nguyên Lý Quản Trị Tài Nguyên Bộ Nhớ]
Khả năng kiểm soát bộ nhớ RAM ở cấp độ byte là phẩm chất định nghĩa nên uy lực của C++. Tuy nhiên, tự do đi liền với trách nhiệm: Một kiến trúc phần mềm chuẩn mực phải đảm bảo hai điều kiện biên bất biến:
\begin{enumerate}
    \item \textbf{Tính Toàn Vẹn Sở Hữu (Ownership Integrity):} Mỗi khối tài nguyên động trên Heap phải có một chủ sở hữu duy nhất hoặc một nhóm chủ sở hữu được kiểm soát nghiêm ngặt.
    \item \textbf{Tính Bất Biến Về Vòng Đời (Lifecycle Invariant):} Tài nguyên phải được giải phóng đúng một lần duy nhất (\textit{Exactly-once Destruction}) ngay khi chủ sở hữu cuối cùng kết thúc vòng đời.
\end{enumerate}
\end{theorybox}

\section{Sao Chép Nông (Shallow Copy) vs Sao Chép Sâu (Deep Copy)}

Khi lập trình viên không khai báo Copy Constructor hoặc Copy Assignment Operator, trình biên dịch sẽ tự động sinh ra một phiên bản mặc định thực hiện \textbf{Sao chép nông (Shallow Copy / Memberwise Copy)}. 

\subsection{Cơ Chế Phá Hủy Bộ Nhớ Của Shallow Copy (Double-Free Hazard)}

Xét một lớp quản lý một mảng động trên Heap:
\begin{lstlisting}[language=C++]
class RawArray {
public:
    int* data;
    size_t size;

    RawArray(size_t s) : size(s), data(new int[s]) {}
    ~RawArray() { delete[] data; }
    // No custom Copy Constructor -> Compiler generates shallow copy!
};

void defectiveExecution() {
    RawArray a(100);
    RawArray b = a; // SHALLOW COPY: b.data gets the exact pointer value of a.data!
} // Scope exits: Double-free error occurs here!
\end{lstlisting}

\begin{underhoodbox}[Giải Phẫu Hiện Tượng Double-Free Dưới Tầng Bộ Nhớ]
Hãy khảo sát trạng thái của bộ nhớ trong hàm \texttt{defectiveExecution()}:
\begin{enumerate}
    \item Khi \texttt{b = a} được thực thi, trình biên dịch chỉ đơn thuần sao chép giá trị số nguyên của con trỏ: \texttt{b.data = a.data}.
    \item \textbf{Hiện tượng Con trỏ trùng lặp (Pointer Aliasing):} Cả \texttt{a.data} và \texttt{b.data} đều cùng trỏ vào \textbf{DUY NHẤT MỘT ĐỊA CHỈ HEAP} (ví dụ \texttt{0x00A01234}).
    \item \textbf{Giai đoạn Hủy (Destruction):}
    \begin{itemize}
        \item Theo quy tắc LIFO của Stack, đối tượng \texttt{b} bị hủy trước. Destructor \texttt{\textasciitilde{}RawArray()} của \texttt{b} thực thi lệnh \texttt{delete[] b.data}, giải phóng khối bộ nhớ tại \texttt{0x00A01234} về cho hệ điều hành. Vùng nhớ này bị đánh dấu là \textit{Free Chunk}.
        \item Ngay sau đó, đối tượng \texttt{a} bị hủy. Destructor của \texttt{a} tiếp tục gọi \texttt{delete[] a.data} trên cùng địa chỉ \texttt{0x00A01234}!
    \end{itemize}
    \item \textbf{Hậu quả hệ thống:} Việc giải phóng một vùng nhớ đã được giải phóng từ trước gọi là \textbf{Lỗi Double-Free}. C/C++ Memory Allocator phát hiện sự sai lệch trong danh sách liên kết của Heap và ném tín hiệu \textbf{\texttt{SIGABRT}}, đình chỉ tiến trình ngay tức khắc.
\end{enumerate}
\end{underhoodbox}

\subsection{Giải Pháp Chuẩn Mực: Sao Chép Sâu (Deep Copy)}

Sao chép sâu đòi hỏi việc cấp phát một khối bộ nhớ mới hoàn toàn độc lập trên Heap, sau đó sao chép toàn bộ nội dung dữ liệu từ nguồn sang đích:
\begin{lstlisting}[language=C++]
// Deep Copy Constructor
RawArray::RawArray(const RawArray& other)
    : size(other.size), data(new int[other.size]) {
    for (size_t i = 0; i < size; ++i) {
        data[i] = other.data[i];
    }
}
\end{lstlisting}

\section{Hệ Thống Phân Loại Giá Trị \& Ngữ Nghĩa Di Dời (Move Semantics)}

\subsection{Phân Loại Giá Trị Chuẩn Quốc Tế ISO/IEC 14882 (Value Categories)}

Trong chuẩn C++11, để hỗ trợ việc chuyển giao quyền sở hữu tài nguyên mà không cần sao chép, ủy ban ISO đã thiết lập cây phân loại giá trị (\textit{Value Categories}) dựa trên hai tiêu chí độc lập:
\begin{enumerate}
    \item \textbf{Có Định Danh Bộ Nhớ (Has Identity):} Chương trình có thể xác định được địa chỉ bộ nhớ cụ thể (\texttt{\&expr}) của đối tượng.
    \item \textbf{Có Thể Di Dời Tài Nguyên (Can be Moved):} Trạng thái nội tại của đối tượng có thể được chuyển nhượng cho đối tượng khác một cách an toàn mà không phá vỡ tính bất biến của chương trình.
\end{enumerate}

\begin{figure}[htbp]
\centering
\resizebox{0.92\textwidth}{!}{%
\begin{tikzpicture}[
    box/.style={draw=primaryblue, thick, rounded corners=4pt, fill=white, inner sep=6pt, font=\small\bfseries\sffamily, align=center},
    catbox/.style={draw=accentblue, thick, rounded corners=4pt, fill=bgsoftblue, inner sep=6pt, font=\small\bfseries\sffamily, align=center},
    leafbox/.style={draw=primaryblue, thick, rounded corners=4pt, fill=white, inner sep=6pt, font=\small\bfseries\sffamily, align=center}
]
    % Top expression banner
    \node[box, fill=bglighterblue, text width=11.4cm] (expr) at (0, 4.2) {Tất Cả Các Biểu Thức Trong C++11/14/17 (Expressions)};

    % Intermediate glvalue and rvalue categories (width = 5.2cm, zero hyphenation)
    \node[catbox, text width=5.2cm] (glval) at (-3.7, 2.4) {\textbf{glvalue (Generalized lvalue)}\\[2pt]\footnotesize Có Identity (Định danh bộ nhớ)};
    \node[catbox, text width=5.2cm] (rval) at (3.7, 2.4) {\textbf{rvalue}\\[2pt]\footnotesize Có thể di dời tài nguyên (Movable)};

    % Leaf categories: lvalue, xvalue, prvalue
    \node[leafbox, text width=3.3cm] (lval) at (-4.7, 0.0) {\textbf{lvalue}\\[2pt]\footnotesize Có Identity\\[1pt]\scriptsize Không di dời};
    \node[leafbox, fill=bglighterblue, draw=accentblue, line width=1.5pt, text width=3.8cm] (xval) at (0.0, 0.0) {\textbf{xvalue (eXpiring)}\\[2pt]\footnotesize Có Identity\\\footnotesize Di dời được (Giao điểm)};
    \node[leafbox, text width=3.3cm] (prval) at (4.7, 0.0) {\textbf{prvalue (Pure rvalue)}\\[2pt]\footnotesize Không Identity\\[1pt]\scriptsize Di dời được};

    % Top orthogonal tree branching (downward arrows only)
    \draw[thick, primaryblue] (0, 3.8) -- (0, 3.4) -- (-3.7, 3.4);
    \draw[-{Stealth[length=2.5mm]}, thick, primaryblue] (-3.7, 3.4) -- (glval.north);
    
    \draw[thick, primaryblue] (0, 3.4) -- (3.7, 3.4);
    \draw[-{Stealth[length=2.5mm]}, thick, primaryblue] (3.7, 3.4) -- (rval.north);

    % glvalue branches down to lvalue and xvalue
    \draw[thick, accentblue] (glval.south) -- (-3.7, 1.3) -- (-4.7, 1.3);
    \draw[-{Stealth[length=2.5mm]}, thick, accentblue] (-4.7, 1.3) -- (lval.north);

    \draw[thick, accentblue] (-3.7, 1.3) -- (-1.1, 1.3);
    \draw[-{Stealth[length=2.5mm]}, thick, accentblue] (-1.1, 1.3) -- (-1.1, 0.85);

    % rvalue branches down to xvalue and prvalue
    \draw[thick, accentblue] (rval.south) -- (3.7, 1.3) -- (4.7, 1.3);
    \draw[-{Stealth[length=2.5mm]}, thick, accentblue] (4.7, 1.3) -- (prval.north);

    \draw[thick, accentblue] (3.7, 1.3) -- (1.1, 1.3);
    \draw[-{Stealth[length=2.5mm]}, thick, accentblue] (1.1, 1.3) -- (1.1, 0.85);
\end{tikzpicture}%
}
\caption{Cây phân loại giá trị chuẩn mực quốc tế ISO/IEC 14882 (Value Categories).}
\end{figure}

\begin{itemize}
    \item \textbf{lvalue (Locator Value):} Đại diện cho một đối tượng có vị trí bộ nhớ xác định và có tên (ví dụ: tên biến, hàm trả về tham chiếu lvalue \texttt{T\&}).
    \item \textbf{prvalue (Pure Rvalue):} Đại diện cho các giá trị tạm thời tính toán tức thời hoặc hằng số nguyên thủy (ví dụ: số \texttt{42}, kết quả biểu thức \texttt{a + b}, hàm trả về theo giá trị \texttt{T}). Từ C++17, prvalue được định nghĩa lại là \textit{công thức khởi tạo đối tượng}, kích hoạt cơ chế \textbf{Triệt tiêu Sao chép Bảo đảm (Guaranteed Copy Elision)}.
    \item \textbf{xvalue (eXpiring Value):} Đại diện cho một đối tượng có danh tính bộ nhớ nhưng vòng đời sắp kết thúc, cho phép chuyển giao tài nguyên (ví dụ: kết quả của \texttt{std::move(var)}).
\end{itemize}

\subsection{Tham Chiếu Rvalue (\texttt{T\&\&}) \& Ngữ Nghĩa Di Dời (Move Semantics)}

Trong C++98, việc truyền các đối tượng lớn (chuỗi ký tự, mảng động, ma trận) ra khỏi hàm luôn đòi hỏi một phép sao chép sâu vô cùng đắt đỏ. Chuẩn C++11 giải quyết triệt để vấn đề này thông qua \textbf{Tham chiếu Rvalue (\texttt{T\&\&})}:

\begin{lstlisting}[language=C++]
#include <iostream>
#include <utility>

class HeavyBuffer {
public:
    size_t size;
    int* data;

    // 1. Constructor
    HeavyBuffer(size_t s) : size(s), data(new int[s]) {}

    // 2. Destructor
    ~HeavyBuffer() { delete[] data; }

    // 3. Copy Constructor (Deep Copy - O(N))
    HeavyBuffer(const HeavyBuffer& other) : size(other.size), data(new int[other.size]) {
        for (size_t i = 0; i < size; ++i) data[i] = other.data[i];
    }

    // 4. Move Constructor (Resource Transfer - O(1))
    HeavyBuffer(HeavyBuffer&& other) noexcept : size(other.size), data(other.data) {
        // Chuyen giao con tro va vo hieu hoa doi tuong nguon
        other.data = nullptr;
        other.size = 0;
    }
};
\end{lstlisting}

\begin{underhoodbox}[Bản Chất Của \texttt{std::move} Dưới Tầng Trình Biên Dịch]
Rất nhiều kỹ sư ngộ nhận rằng hàm \texttt{std::move} thực hiện thao tác di dời dữ liệu trong bộ nhớ. \textbf{Đây là một hiểu lầm tai hại}!

Dưới góc nhìn mã máy, \texttt{std::move} hoàn toàn \textbf{KHÔNG SINH RA BẤT KỲ DÒNG MÃ THỰC THI NÀO}! Về bản chất, \texttt{std::move} chỉ là một phép \textbf{Ép Kiểu Tĩnh Không Điều Kiện (Unconditional Static Cast)}:
$$\texttt{static\_cast<typename std::remove\_reference<T>::type\&\&>(t)}$$

Mục đích duy nhất của \texttt{std::move} là biến đổi một \textbf{lvalue} thành một \textbf{xvalue}, thông báo cho cơ chế giải quyết nạp chồng (\textit{Overload Resolution}) của trình biên dịch ưu tiên lựa chọn Move Constructor hoặc Move Assignment Operator thay vì Copy Constructor.
\end{underhoodbox}

\section{Tiến Hóa Bộ Quy Tắc Quản Trị Tài Nguyên: Rule of 3, 5, 0}

\subsection{Quy Tắc Bộ Ba Cổ Điển (The Rule of Three --- C++98)}

\begin{theorybox}[Quy Tắc Bộ Ba (The Rule of Three)]
Nếu một lớp đòi hỏi phải hiện thực hóa tường minh một trong ba phương thức sau:
\begin{enumerate}
    \item \textbf{Hàm Hủy (Destructor)}
    \item \textbf{Hàm Tạo Sao Chép (Copy Constructor)}
    \item \textbf{Toán Tử Gán Sao Chép (Copy Assignment Operator)}
\end{enumerate}
thì lớp đó \textbf{HẦU NHƯ CHẮC CHẮN PHẢI HIỆN THỰC HÓA CẢ BA PHƯƠNG THỨC}. Sự hiện diện của một hàm hủy tường minh chứng minh rằng lớp đang nắm giữ một tài nguyên thô; do đó các phương thức sao chép mặc định sẽ gây ra lỗi Shallow Copy.
\end{theorybox}

\subsection{Quy Tắc Bộ Năm Hiện Đại (The Rule of Five --- C++11)}

Sự xuất hiện của Ngữ nghĩa Di dời trong chuẩn C++11 mở rộng Rule of Three thành \textbf{Rule of Five}. Một lớp quản lý tài nguyên phải thiết lập 5 phương thức đặc biệt:
\begin{enumerate}
    \item \textbf{Destructor:} \texttt{\textasciitilde{}Resource()}
    \item \textbf{Copy Constructor:} \texttt{Resource(const Resource\&)}
    \item \textbf{Copy Assignment Operator:} \texttt{Resource\& operator=(const Resource\&)}
    \item \textbf{Move Constructor:} \texttt{Resource(Resource\&\&) noexcept}
    \item \textbf{Move Assignment Operator:} \texttt{Resource\& operator=(Resource\&\&) noexcept}
\end{enumerate}

\begin{warningbox}[Quy Tắc Vô Hiệu Hóa Hàm Di Dời Ngầm Định (Move Generation Inhibition)]
Theo chuẩn ISO C++: Nếu lập trình viên khai báo bất kỳ hàm nào trong số \textbf{Destructor, Copy Constructor, hoặc Copy Assignment Operator}, trình biên dịch sẽ \textbf{TỰ ĐỘNG KHÓA VÀ KHÔNG SINH RA Move Constructor và Move Assignment Operator ngầm định}!

Hậu quả là các lời gọi \texttt{std::move(obj)} sẽ \textbf{âm thầm thoái hóa thành phép sao chép sâu} (\textit{Silent Fallback to Deep Copy}) mà không hề có bất kỳ cảnh báo biên dịch nào! Để khôi phục, lập trình viên bắt buộc phải yêu cầu trình biên dịch sinh tường minh:
\begin{lstlisting}[language=C++]
Resource(Resource&&) noexcept = default;
Resource& operator=(Resource&&) noexcept = default;
\end{lstlisting}
\end{warningbox}

\subsection{Thành Ngữ Sao Chép và Hoán Vị (The Copy-and-Swap Idiom)}

Để hiện thực hóa cả Copy Assignment và Move Assignment một cách thanh lịch, an toàn ngoại lệ tuyệt đối mà không lặp lại mã nguồn, kỹ sư C++ sử dụng kỹ thuật \textbf{Copy-and-Swap}:

\begin{lstlisting}[language=C++]
#include <utility>
#include <algorithm>

class ManagedBuffer {
private:
    size_t length;
    char* buffer;

public:
    // 1. Constructor
    ManagedBuffer(size_t len = 0)
        : length(len), buffer(len ? new char[len] : nullptr) {}

    // 2. Destructor
    ~ManagedBuffer() { delete[] buffer; }

    // 3. Copy Constructor (Deep Copy - Protected against nullptr UB)
    ManagedBuffer(const ManagedBuffer& other)
        : length(other.length), buffer(other.length ? new char[other.length] : nullptr) {
        if (length > 0) {
            std::copy(other.buffer, other.buffer + length, buffer);
        }
    }

    // 4. Move Constructor (Zero Overhead Transfer)
    ManagedBuffer(ManagedBuffer&& other) noexcept
        : ManagedBuffer() { // Delegate to Default Ctor
        swap(*this, other);
    }

    // Friend swap function: No-fail guarantee
    friend void swap(ManagedBuffer& first, ManagedBuffer& second) noexcept {
        using std::swap;
        swap(first.length, second.length);
        swap(first.buffer, second.buffer);
    }

    // 5. UNIFIED ASSIGNMENT OPERATOR (Covers both Copy and Move!)
    // Parameter passed BY VALUE triggers Copy Ctor for lvalue or Move Ctor for rvalue!
    ManagedBuffer& operator=(ManagedBuffer other) noexcept {
        swap(*this, other); // Swap internal state with temporary copy
        return *this;
    } // temporary other is destroyed here, cleanly freeing old resource
};
\end{lstlisting}

\subsection{Quy Tắc Số Không (The Rule of Zero --- Modern C++)}

\begin{theorybox}[Đỉnh Cao Thiết Kế: Quy Tắc Số Không (The Rule of Zero)]
Trong kiến trúc hướng đối tượng C++ hiện đại, lập trình viên \textbf{KHÔNG NÊN TỰ VIẾT BẤT KỲ PHƯƠNG THỨC NÀO TRONG BỘ NĂM}. 

Thay vì quản lý con trỏ thô, hãy ủy thác toàn bộ việc quản lý tài nguyên cho các lớp thư viện chuẩn đã đạt chuẩn RAII như \texttt{std::unique\_ptr}, \texttt{std::vector}, hoặc \texttt{std::string}. Khi đó, trình biên dịch sẽ tự động sinh ra toàn bộ các hàm tạo sao chép, di chuyển và hàm hủy với độ an toàn và hiệu năng tối ưu tuyệt đối.
\end{theorybox}

\section{Nạp Chồng Toán Tử Toàn Diện (Operator Overloading Deep Dive)}

\subsection{Toán Tử Tiền Tố (++x) vs Hậu Tố (x++)}

\begin{lstlisting}[language=C++]
class Counter {
private:
    int value = 0;
public:
    // 1. PREFIX (++c): Returns reference to current instance
    Counter& operator++() {
        ++value;
        return *this; // Optimal: No temporary object created
    }

    // 2. POSTFIX (c++): Takes dummy int parameter to differentiate
    Counter operator++(int) {
        Counter temp = *this; // Mandatory: Must create a temporary copy
        ++value;              // Increment actual state
        return temp;          // Return old value before increment
    } // Overhead: Triggers Copy Constructor
};
\end{lstlisting}
\textit{Hệ luận kỹ thuật:} Trong các vòng lặp thuật toán, luôn ưu tiên sử dụng toán tử tiền tố (\texttt{++it}) thay vì hậu tố (\texttt{it++}) để triệt tiêu chi phí khởi tạo đối tượng tạm thời.

\subsection{Nạp Chồng new/delete Cấp Lớp (Class-specific Allocators) \& Placement New}

Placement New cho phép lập trình viên khởi tạo một đối tượng trực tiếp trên một địa chỉ bộ nhớ đã được phân bổ sẵn mà \textbf{hoàn toàn không thực hiện bất kỳ lệnh xin cấp phát RAM nào}:

\begin{lstlisting}[language=C++]
#include <new> // Required for placement new

alignas(SocketConnection) char arenaBuffer[sizeof(SocketConnection)];

void testPlacementNew() {
    // 1. Construct object directly on arenaBuffer:
    SocketConnection* pConn = new (arenaBuffer) SocketConnection(9090);

    // 2. DESTRUCTION RULE: STRICTLY FORBIDDEN TO CALL delete pConn!
    // Since arenaBuffer is on Stack/Static, calling delete triggers a crash!
    
    // 3. MUST MANUALLY INVOKE DESTRUCTOR EXPLICITLY:
    pConn->~SocketConnection();
}
\end{lstlisting}

\section{Kiến Trúc Con Trỏ Thông Minh Chuẩn C++11 (Smart Pointers Architecture)}

Để chấm dứt kỷ nguyên rò rỉ bộ nhớ của con trỏ thô (\textit{Raw Pointers}), chuẩn C++11 giới thiệu bộ ba con trỏ thông minh trong thư viện \texttt{<memory>}.

\subsection{\texttt{std::unique\_ptr<T>} --- Quyền Sở Hữu Độc Quyền (Exclusive Ownership)}

\begin{itemize}
    \item \textbf{Đặc tính kiến trúc:} Quản lý một đối tượng duy nhất. Không thể sao chép (\texttt{Copy Constructor = delete}), chỉ có thể di dời quyền sở hữu thông qua Move Semantics (\texttt{std::move}).
    \item \textbf{Hiệu năng và Tối ưu hóa Lớp Cơ sở Rỗng (EBO):} Khi sử dụng bộ giải phóng mặc định (\texttt{std::default\_delete<T>}), trình biên dịch áp dụng EBO để kích thước của \texttt{std::unique\_ptr<T>} đúng bằng \textbf{MỘT con trỏ thô} (8 bytes trên 64-bit). Tuy nhiên, nếu truyền vào một con trỏ hàm giải phóng tùy biến (\texttt{void(*)(T*)}), kích thước của nó sẽ tăng gấp đôi lên \textbf{16 bytes}.
\end{itemize}

\subsection{\texttt{std::shared\_ptr<T>} --- Quyền Sở Hữu Chia Sẻ (Shared Ownership)}

Nhiều con trỏ \texttt{shared\_ptr} có thể cùng trỏ tới một đối tượng. Đối tượng sẽ được tự động giải phóng khi con trỏ \texttt{shared\_ptr} cuối cùng bị hủy.

\begin{figure}[htbp]
\centering
\resizebox{0.95\textwidth}{!}{%
\begin{tikzpicture}[every node/.style={font=\small\sffamily, align=center}]
    % Outer container for shared_ptr in Stack (x from 0 to 5.8, y from 0 to 4.0)
    \draw[thick, fill=bgsoftblue, draw=primaryblue, rounded corners=4pt] (0, 0) rectangle (5.8, 4.0);
    \node[above=2pt, font=\bfseries\sffamily, primaryblue] at (2.9, 4.0) {\texttt{std::shared\_ptr<T>} (Stack)};
    \node[font=\scriptsize\sffamily, commentgray] at (2.9, 3.55) {Kích thước: 16 bytes (Double Pointer)};

    % Two slots inside shared_ptr
    \draw[thick, fill=white, draw=primaryblue, rounded corners=3pt] (0.4, 1.9) rectangle (5.4, 3.2);
    \node at (2.9, 2.55) {\textbf{\texttt{T* ptr}}\\[1pt]\scriptsize Con trỏ dữ liệu đối tượng (8 bytes)};

    \draw[thick, fill=bglighterblue, draw=accentblue, rounded corners=3pt] (0.4, 0.4) rectangle (5.4, 1.7);
    \node at (2.9, 1.05) {\textbf{\texttt{ControlBlock* cb}}\\[1pt]\scriptsize Con trỏ khối điều khiển (8 bytes)};

    % Managed Object on Heap (Top Right: x from 10.2 to 15.8, y from 1.9 to 3.2)
    \draw[thick, fill=white, draw=primaryblue, rounded corners=3pt] (10.2, 1.9) rectangle (15.8, 3.2);
    \node at (13.0, 2.55) {\textbf{Đối Tượng Dữ Liệu T (Heap)}\\[1pt]\scriptsize Cấp phát \texttt{sizeof(T)} bytes};

    % Control block on Heap (Bottom Right: x from 10.2 to 15.8, y from 0.4 to 1.7)
    \draw[thick, fill=bglighterblue, draw=accentblue, rounded corners=3pt] (10.2, 0.4) rectangle (15.8, 1.7);
    \node at (13.0, 1.05) {\textbf{Control Block (Heap)}\\[1pt]\scriptsize Strong: N $\mid$ Weak: M $\mid$ Deleter};

    % Horizontal straight parallel arrows in 4.8cm wide clear gap
    \draw[-{Stealth[length=3mm]}, thick, primaryblue] (5.4, 2.55) -- (10.2, 2.55)
        node[midway, above=4pt, font=\footnotesize\bfseries, primaryblue] {Trỏ tới instance};

    \draw[-{Stealth[length=3mm]}, thick, accentblue] (5.4, 1.05) -- (10.2, 1.05)
        node[midway, above=4pt, font=\footnotesize\bfseries, accentblue] {Quản lý vòng đời};
\end{tikzpicture}%
}
\caption{Kiến trúc bộ nhớ hai con trỏ và Khối Điều Khiển (Control Block) của \texttt{std::shared\_ptr}.}
\end{figure}

\begin{underhoodbox}[Kiến Trúc Khối Điều Khiển (Control Block) \& Cạm Bẫy Ghim Bộ Nhớ Của \texttt{std::make\_shared}]
Kích thước của một \texttt{std::shared\_ptr} gấp đôi con trỏ thô (16 bytes trên nền tảng 64-bit), bao gồm một con trỏ trỏ tới dữ liệu và một con trỏ trỏ tới Khối Điều Khiển (\textit{Control Block}).

\textbf{So sánh giữa \texttt{std::make\_shared} và cấp phát hai lần:}
\begin{enumerate}
    \item \textbf{Lợi thế của \texttt{std::make\_shared<T>()}:} Cấp phát duy nhất một khối RAM liên tục chứa cả Control Block và Đối tượng dữ liệu. Tối ưu hóa tính cục bộ bộ nhớ đệm (\textit{Cache Locality}) và loại trừ chi phí gọi allocator hai lần.
    \item \textbf{Cạm bẫy ghim bộ nhớ (Memory Retention Trap):} Vì đối tượng \texttt{T} và Control Block nằm chung trên một khối nhớ Heap duy nhất:
    \begin{itemize}
        \item Khi Strong Reference Count giảm về 0, Destructor của \texttt{T} được thực thi ngay lập tức.
        \item Tuy nhiên, \textbf{TOÀN BỘ KHỐI BỘ NHỚ HEAP KHÔNG THỂ ĐƯỢC GIẢI PHÓNG} chừng nào Weak Reference Count vẫn còn lớn hơn 0!
        \item Nếu đối tượng \texttt{T} có kích thước lớn (ví dụ ma trận 50 MB) và có một đối tượng quan sát nắm giữ \texttt{std::weak\_ptr} trong thời gian dài, toàn bộ 50 MB RAM sẽ bị ghim chặt trong bộ nhớ! Trong kịch bản này, sử dụng \texttt{std::shared\_ptr<T>(new T())} là lựa chọn an toàn hơn vì vùng nhớ 50 MB của \texttt{T} được giải phóng ngay khi strong ref về 0.
    \end{itemize}
\end{enumerate}
\end{underhoodbox}

\subsection{\texttt{std::weak\_ptr<T>} --- Phá Vỡ Vòng Lặp Tham Chiếu (Circular Reference)}

Nếu hai đối tượng \texttt{A} và \texttt{B} cùng sở hữu \texttt{std::shared\_ptr} trỏ chéo lẫn nhau, bộ đếm Strong Reference Count của cả hai không bao giờ giảm về 0, dẫn tới rò rỉ bộ nhớ vĩnh viễn.

\textbf{Giải pháp:} Thay thế một trong hai liên kết bằng \textbf{\texttt{std::weak\_ptr<T>}}. \texttt{weak\_ptr} không làm tăng Strong Reference Count. Khi muốn sử dụng dữ liệu, nó thăng hạng an toàn thành \texttt{shared\_ptr} thông qua phương thức \texttt{wp.lock()}; nếu đối tượng đã bị giải phóng, \texttt{lock()} trả về con trỏ rỗng an toàn.
"""
