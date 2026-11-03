# -*- coding: utf-8 -*-

chap3_text = r"""
% ==============================================================================
% CHƯƠNG 3: QUẢN TRỊ BỘ NHỚ & NẠP CHỒNG TOÁN TỬ (MEMORY & OVERLOADING)
% ==============================================================================
\chapter{Quản trị Bộ nhớ \& Nạp chồng Toán tử (Memory \& Overloading)}

\begin{theorybox}[Nguyên Lý Quản Trị Tài Nguyên Bộ Nhớ]
Khả năng kiểm soát bộ nhớ RAM ở cấp độ byte là phẩm chất định nghĩa nên uy lực của C++. Tuy nhiên, tự do đi liền với trách nhiệm: Một kiến trúc phần mềm chuẩn mực phải đảm bảo hai điều kiện biên bất biến:
\begin{enumerate}
    \item \textbf{Tính Toàn Vẹn Sở Hữu (Ownership Integrity):} Mỗi khối tài nguyên động trên Heap phải có một chủ sở hữu duy nhất hoặc một nhóm chủ sở hữu được kiểm soát nghiêm ngặt.
    \item \textbf{Tính Bất Biến Về Vòng Đời (Lifecycle Invariant):} Tài nguyên phải được giải phóng đúng một lần duy nhất (\textit{Exactly-once Destruction}) ngay khi chủ sở hữu cuối cùng kết thúc vòng đời.\footnote{Nguồn: OOP4-OperatorOverloading\_new.pdf - Trang 2-10: Quản trị tài nguyên và nạp chồng toán tử}
\end{enumerate}
\end{theorybox}

\section{Sao Chép Nông (Shallow Copy) vs Sao Chép Sâu (Deep Copy)}

Khi lập trình viên không khai báo Copy Constructor hoặc Copy Assignment Operator, trình biên dịch sẽ tự động sinh ra một phiên bản mặc định thực hiện \textbf{Sao chép nông (Shallow Copy / Memberwise Copy)}. 

\subsection{Cơ Chế Phá Hủy Bộ Nhớ Của Shallow Copy (Double-Free Disaster)}

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

void catastrophicExecution() {
    RawArray a(100);
    RawArray b = a; // SHALLOW COPY: b.data gets the exact pointer value of a.data!
} // Scope exits: SYSTEM CRASH HAPPENS HERE!
\end{lstlisting}

\begin{underhoodbox}[Giải Phẫu Thảm Họa Double-Free Dưới Tầng Bộ Nhớ]
Hãy khảo sát chính xác trạng thái của thanh ghi và bộ nhớ trong hàm \texttt{catastrophicExecution()}:
\begin{enumerate}
    \item Khi \texttt{b = a} được thực thi, trình biên dịch chỉ đơn thuần sao chép giá trị số nguyên của con trỏ: \texttt{b.data = a.data}.
    \item \textbf{Hiện tượng Con trỏ trùng lặp (Pointer Aliasing):} Cả \texttt{a.data} và \texttt{b.data} đều cùng trỏ vào \textbf{DUY NHẤT MỘT ĐỊA CHỈ HEAP} (ví dụ \texttt{0x00A01234}).
    \item \textbf{Giai đoạn Hủy (Destruction):}
    \begin{itemize}
        \item Theo quy tắc LIFO của Stack, đối tượng \texttt{b} bị hủy trước. Destructor \texttt{\textasciitilde{}RawArray()} của \texttt{b} thực thi lệnh \texttt{delete[] b.data}, giải phóng khối bộ nhớ tại \texttt{0x00A01234} về cho hệ điều hành. Vùng nhớ này bị đánh dấu là \textit{Free Chunk}.
        \item Ngay sau đó, đối tượng \texttt{a} bị hủy. Destructor của \texttt{a} tiếp tục gọi \texttt{delete[] a.data} trên cùng địa chỉ \texttt{0x00A01234}!
    \end{itemize}
    \item \textbf{Hậu quả hệ thống:} Việc giải phóng một vùng nhớ đã được giải phóng từ trước gọi là \textbf{Lỗi Double-Free}. C/C++ Memory Allocator lập tức phát hiện sự sai lệch trong danh sách liên kết của Heap và ném tín hiệu \textbf{\texttt{SIGABRT}} (hoặc \texttt{Heap Corruption Exception}), làm sập tiến trình ngay lập tức!\footnote{Nguồn: OOP4-OperatorOverloading\_new.pdf - Trang 11-18: Shallow copy vs Deep copy và lỗi Double-Free}
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

\section{Tiến Hóa Bộ Quy Tắc Quản Trị Tài Nguyên: Rule of 3, 5, 0}

\subsection{Quy Tắc Bộ Ba Cổ Điển (The Rule of Three --- C++98)}

\begin{theorybox}[Quy Tắc Bộ Ba (The Rule of Three)]
Nếu một lớp đòi hỏi phải hiện thực hóa tường minh một trong ba phương thức sau:
\begin{enumerate}
    \item \textbf{Hàm Hủy (Destructor)}
    \item \textbf{Hàm Tạo Sao Chép (Copy Constructor)}
    \item \textbf{Toán Tử Gán Sao Chép (Copy Assignment Operator)}
\end{enumerate}
thì lớp đó \textbf{HẦU NHƯ CHẮC CHẮN PHẢI HIỆN THỰC HÓA CẢ BA PHƯƠNG THỨC}! Sự hiện diện của một hàm hủy tường minh chứng minh rằng lớp đang nắm giữ một tài nguyên thô (Raw Resource); do đó các phương thức sao chép mặc định sẽ gây ra lỗi Shallow Copy.\footnote{Nguồn: OOP4-OperatorOverloading\_new.pdf - Trang 19-25: Quy tắc Rule of Three trong C++98}
\end{theorybox}

\subsection{Quy Tắc Bộ Năm Hiện Đại (The Rule of Five --- C++11)}

Sự xuất hiện của Ngữ nghĩa Di chuyển (Move Semantics) trong chuẩn C++11 mở rộng Rule of Three thành \textbf{Rule of Five}. Một lớp quản lý tài nguyên phải thiết lập 5 phương thức đặc biệt:
\begin{enumerate}
    \item \textbf{Destructor:} \texttt{\textasciitilde{}Resource()}
    \item \textbf{Copy Constructor:} \texttt{Resource(const Resource\&)}
    \item \textbf{Copy Assignment Operator:} \texttt{Resource\& operator=(const Resource\&)}
    \item \textbf{Move Constructor:} \texttt{Resource(Resource\&\&) noexcept}
    \item \textbf{Move Assignment Operator:} \texttt{Resource\& operator=(Resource\&\&) noexcept}
\end{enumerate}

\subsection{Thành Ngữ Copy-and-Swap (The Copy-and-Swap Idiom)}

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

    // 3. Copy Constructor (Deep Copy)
    ManagedBuffer(const ManagedBuffer& other)
        : length(other.length), buffer(other.length ? new char[other.length] : nullptr) {
        std::copy(other.buffer, other.buffer + length, buffer);
    }

    // 4. Move Constructor (Zero Overhead Theft)
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
    } // temporary 'other' is destroyed here, cleanly freeing old resource!
};
\end{lstlisting}

\subsection{Quy Tắc Số Không (The Rule of Zero --- Modern C++)}

\begin{theorybox}[Đỉnh Cao Thiết Kế: Quy Tắc Số Không (The Rule of Zero)]
Trong kiến trúc hướng đối tượng C++ hiện đại, lập trình viên \textbf{KHÔNG NÊN TỰ VIẾT BẤT KỲ PHƯƠNG THỨC NÀO TRONG BỘ NĂM}. 

Thay vì quản lý con trỏ thô, hãy ủy thác toàn bộ việc quản lý tài nguyên cho các lớp thư viện chuẩn đã đạt chuẩn RAII như \texttt{std::unique\_ptr}, \texttt{std::vector}, hoặc \texttt{std::string}. Khi đó, trình biên dịch sẽ tự động sinh ra toàn bộ các hàm tạo sao chép, di chuyển và hàm hủy với độ an toàn và hiệu năng tối ưu tuyệt đối!\footnote{Nguồn: OOP4-OperatorOverloading\_new.pdf - Trang 26-32: Rule of Five và Rule of Zero trong C++11}
\end{theorybox}

\section{Nạp Chồng Toán Tử Toàn Diện (Operator Overloading Deep Dive)}

C++ cho phép lập trình viên định nghĩa lại ngữ nghĩa của các toán tử ngôn ngữ đối với các kiểu dữ liệu tự định nghĩa, biến mã nguồn trở nên tự nhiên và biểu cảm như các biểu thức toán học.

\subsection{Các Định Đề Bất Biến Về Toán Tử}

\begin{theorybox}[Ba Giới Hạn Cốt Tử Của Ngôn Ngữ Về Nạp Chồng Toán Tử]
\begin{enumerate}
    \item \textbf{Bất Biến Về Độ Ưu Tiên \& Kết Hợp:} Việc nạp chồng toán tử \textbf{tuyệt đối không thể làm thay đổi độ ưu tiên} (\textit{Precedence}) hoặc \textbf{tính kết hợp} (\textit{Associativity}) của toán tử (ví dụ: toán tử \texttt{*} luôn được thực thi trước toán tử \texttt{+}).
    \item \textbf{Bất Biến Về Số Lượng Toán Hạng:} Không thể biến đổi toán tử hai ngôi thành một ngôi hoặc ngược lại.
    \item \textbf{Cấm Khởi Tạo Toán Tử Mới:} Lập trình viên không thể tự chế tạo ra các ký tự toán tử mới không tồn tại trong ngữ pháp chuẩn C++ (như \texttt{**} hoặc \texttt{\%\%}).
\end{enumerate}
\end{theorybox}

\textbf{Năm toán tử CẤM TUYỆT ĐỐI không được nạp chồng trong C++:}
\begin{enumerate}
    \item Toán tử truy cập thành viên trực tiếp: \textbf{\texttt{.}}
    \item Toán tử con trỏ tới thành viên trực tiếp: \textbf{\texttt{.*}}
    \item Toán tử phân giải phạm vi: \textbf{\texttt{::}}
    \item Toán tử điều kiện tam phân: \textbf{\texttt{?:}}
    \item Toán tử kích thước: \textbf{\texttt{sizeof}} (và toán tử nhận dạng kiểu \textbf{\texttt{typeid}}).
\end{enumerate}

\subsection{Lựa Chọn Thiết Kế: Member Method vs Non-member Friend}

\begin{itemize}
    \item \textbf{Toán tử bắt buộc phải là Phương thức Thành viên (Member Functions):}
    Chuẩn C++ quy định 4 toán tử sau \textbf{bắt buộc 100\% phải là member}:
    \begin{enumerate}
        \item Toán tử gán: \texttt{operator=}
        \item Toán tử chỉ mục mảng: \texttt{operator[]}
        \item Toán tử gọi hàm: \texttt{operator()}
        \item Toán tử truy cập gián tiếp con trỏ: \texttt{operator->}
    \end{enumerate}
    
    \item \textbf{Tại sao toán tử xuất/nhập luồng (\texttt{<<} và \texttt{>>}) BẮT BUỘC phải là Non-member Function?}
    Xét biểu thức: \texttt{std::cout << myObject;}.
    Toán hạng bên trái là \texttt{std::cout} (có kiểu \texttt{std::ostream\&}). Nếu ta cài đặt dạng hàm thành viên, hàm đó bắt buộc phải nằm bên trong mã nguồn của lớp \texttt{std::ostream} thuộc thư viện chuẩn của trình biên dịch! Vì lập trình viên không thể can thiệp vào mã nguồn của \texttt{std::ostream}, ta bắt buộc phải nạp chồng \texttt{operator<<} dưới dạng \textbf{Hàm Tự Do Ngoài Lớp (Non-member Function)} và cấp quyền \texttt{friend} để truy cập trường ẩn:
    \begin{lstlisting}[language=C++]
    friend std::ostream& operator<<(std::ostream& os, const Complex& c) {
        os << "(" << c.real << " + " << c.imag << "i)";
        return os; // Tra ve ostream& de cho phep chain goi lien tiep
    }
    \end{lstlisting}
\end{itemize}

\subsection{Toán Tử Chỉ Mục \texttt{operator[]} \& Toán Tử Gọi Hàm \texttt{operator()}}

Để bảo đảm tính toàn vẹn \textit{const-correctness}, toán tử chỉ mục luôn phải được viết thành \textbf{MỘT CẶP ĐỒNG BỘ}:
\begin{lstlisting}[language=C++]
class SafeVector {
private:
    int* elements;
    size_t length;
public:
    // 1. Non-const version: Allows reading and writing
    int& operator[](size_t index) {
        return elements[index];
    }

    // 2. Const version: Allows reading from const instances
    const int& operator[](size_t index) const {
        return elements[index];
    }
};
\end{lstlisting}

\subsection{Toán Tử Tăng Giảm: Tiền Tố (Prefix) vs Hậu Tố (Postfix)}

\begin{lstlisting}[language=C++]
class Counter {
private:
    int value = 0;
public:
    // 1. PREFIX (++c): Increments and returns reference to self
    Counter& operator++() {
        ++value;
        return *this; // Optimal performance: O(1), no temporary object
    }

    // 2. POSTFIX (c++): Takes dummy int parameter to differentiate
    Counter operator++(int) {
        Counter temp = *this; // MANDATORY: Must create a temporary copy!
        ++value;              // Increment actual state
        return temp;          // Return old value before increment
    } // Overhead: Triggers Copy Constructor
};
\end{lstlisting}
\textit{Hệ luận kỹ thuật:} Trong các vòng lặp thuật toán, luôn ưu tiên sử dụng toán tử tiền tố (\texttt{++it}) thay vì hậu tố (\texttt{it++}) để triệt tiêu chi phí khởi tạo đối tượng tạm thời.\footnote{Nguồn: OOP4-OperatorOverloading\_new.pdf - Trang 33-50: Kỹ thuật nạp chồng toán tử nâng cao}

\section{Nạp Chồng Toán Tử new và delete \& Kỹ Thuật Placement New}

\subsection{Nạp Chồng new/delete Cấp Lớp (Class-specific Allocators)}

Các hệ thống giao dịch tần suất cao hoặc engine trò chơi thường không sử dụng bộ cấp phát tổng quát của hệ điều hành vì chi phí tìm kiếm vùng nhớ tự do quá lớn. C++ cho phép nạp chồng toán tử \texttt{new} và \texttt{delete} riêng cho từng lớp để lấy bộ nhớ từ một vùng nhớ được cấp phát tĩnh từ trước (\textit{Memory Pool}):

\begin{lstlisting}[language=C++]
class HighSpeedNode {
public:
    void* operator new(size_t bytes) {
        // Fast allocate from custom memory pool in O(1)
        return MemoryPool::allocateFast(bytes);
    }

    void operator delete(void* ptr) noexcept {
        // Return block back to pool in O(1)
        MemoryPool::deallocateFast(ptr);
    }
};
\end{lstlisting}

\subsection{Kỹ Thuật Khởi Tạo Tại Chỗ (Placement New)}

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
    \item \textbf{Hiệu năng:} Kích thước bộ nhớ của \texttt{std::unique\_ptr<T>} bằng chính xác \textbf{MỘT con trỏ thô} (\texttt{sizeof = 8 bytes} trên 64-bit). Mọi thao tác truy xuất đều được inline hóa 100\%, đạt hiệu năng ngang bằng con trỏ thô (\textbf{Zero Runtime Overhead})!
\end{itemize}

\subsection{\texttt{std::shared\_ptr<T>} --- Quyền Sở Hữu Chia Sẻ (Shared Ownership)}

Nhiều con trỏ \texttt{shared\_ptr} có thể cùng trỏ tới một đối tượng. Đối tượng sẽ được tự động giải phóng khi con trỏ \texttt{shared\_ptr} cuối cùng bị hủy.

\begin{figure}[htbp]
\centering
\resizebox{0.95\textwidth}{!}{%
\begin{tikzpicture}[
    box/.style={draw=primaryblue, thick, rounded corners=3pt, fill=white, inner sep=7pt, font=\small\sffamily, align=center},
    ctrlbox/.style={draw=accentblue, thick, rounded corners=3pt, fill=bglighterblue, inner sep=7pt, font=\small\sffamily, align=center}
]
    % shared_ptr in Stack
    \node[box, fill=bgsoftblue, text width=3.8cm] (sp1) at (0, 3) {\textbf{\texttt{std::shared\_ptr<T>}}\\(Trên Stack: 16 bytes)\\\footnotesize Con trỏ đối tượng: \texttt{T*}\\\footnotesize Con trỏ Control Block};

    % Managed Object on Heap
    \node[box, fill=white, draw=primaryblue, text width=4.0cm] (obj) at (6.5, 4.2) {\textbf{Đối Tượng Dữ Liệu T}\\(Cấp phát trên Heap)\\\footnotesize \texttt{sizeof(T)} bytes};

    % Control block on Heap
    \node[ctrlbox, text width=4.8cm] (cb) at (6.5, 1.8) {\textbf{Control Block (Heap)}\\\footnotesize Strong Ref Count: \texttt{1}\\\footnotesize Weak Ref Count: \texttt{0}\\\footnotesize Custom Deleter / Allocator};

    % Pointer arrows
    \draw[-{Stealth[length=2.5mm]}, thick, primaryblue] (sp1.east) -- ++(1.2, 0) |- (obj.west) node[near start, above=2pt, font=\footnotesize] {Trỏ dữ liệu};
    \draw[-{Stealth[length=2.5mm]}, thick, accentblue] (sp1.east) -- ++(1.2, 0) |- (cb.west) node[near start, below=2pt, font=\footnotesize] {Quản lý vòng đời};
\end{tikzpicture}%
}
\caption{Kiến trúc bộ nhớ hai con trỏ và Khối Điều Khiển (Control Block) của \texttt{std::shared\_ptr}.}
\end{figure}

\begin{underhoodbox}[Kiến Trúc Khối Điều Khiển (Control Block) Của \texttt{std::shared\_ptr}]
Kích thước của một \texttt{std::shared\_ptr} gấp đôi con trỏ thô (16 bytes trên nền tảng 64-bit), bao gồm:
\begin{enumerate}
    \item \textbf{Con trỏ thứ nhất (8 bytes):} Trỏ thẳng tới đối tượng dữ liệu thực tế (\texttt{T*}).
    \item \textbf{Con trỏ thứ hai (8 bytes):} Trỏ tới một cấu trúc cấp phát động độc lập gọi là \textbf{Khối Điều Khiển (Control Block)}.
\end{enumerate}

\textbf{Cấu trúc nội tại của Control Block:}
\begin{itemize}
    \item \textbf{Strong Reference Count (Bộ đếm tham chiếu mạnh):} Đếm số lượng \texttt{shared\_ptr} đang cùng sở hữu đối tượng. Mọi thao tác tăng/giảm biến đếm này đều sử dụng các chỉ lệnh khóa luồng mức máy (\textbf{Atomic Instructions} như \texttt{lock xadd} trên x86) để đảm bảo an toàn luồng (\textit{Thread-safety}).
    \item \textbf{Weak Reference Count (Bộ đếm tham chiếu yếu):} Đếm số lượng \texttt{weak\_ptr} đang quan sát đối tượng.
    \item \textbf{Custom Deleter \& Allocator:} Con trỏ hàm giải phóng tùy biến.
\end{itemize}

\textbf{Ưu thế vượt trội của \texttt{std::make\_shared<T>()}:}
\begin{itemize}
    \item Nếu dùng \texttt{std::shared\_ptr<T>(new T())}: Hệ điều hành phải thực hiện \textbf{HAI lần cấp phát bộ nhớ động riêng rẽ} (một lần cho \texttt{T}, một lần cho Control Block), làm phân mảnh bộ nhớ và suy giảm hiệu năng CPU Cache.
    \item Nếu dùng \texttt{std::make\_shared<T>()}: Hệ điều hành cấp phát \textbf{DUY NHẤT MỘT KHỐI RAM LIÊN TỤC} chứa cả Control Block và Đối tượng dữ liệu. Tối ưu hóa tuyệt đối tính cục bộ bộ nhớ đệm (\textbf{Cache Locality})!\footnote{Nguồn: OOP4-OperatorOverloading\_new.pdf - Trang 51-68: Kiến trúc Smart Pointers và Control Block}
\end{itemize}
\end{underhoodbox}

\subsection{\texttt{std::weak\_ptr<T>} --- Bẻ Gãy Vòng Lặp Tham Chiếu (Circular Reference)}

Nếu hai đối tượng \texttt{A} và \texttt{B} cùng sở hữu \texttt{std::shared\_ptr} trỏ chéo lẫn nhau:
$$\text{A} \xrightarrow{\text{shared\_ptr}} \text{B} \quad \text{và} \quad \text{B} \xrightarrow{\text{shared\_ptr}} \text{A}$$
Bộ đếm Strong Reference Count của cả hai không bao giờ giảm về 0, dẫn tới toàn bộ mạng lưới đối tượng bị \textbf{rò rỉ vĩnh viễn trong RAM}!

\textbf{Giải pháp:} Thay thế một trong hai liên kết bằng \textbf{\texttt{std::weak\_ptr<T>}}. \texttt{weak\_ptr} chỉ đóng vai trò là người quan sát: Nó không làm tăng Strong Reference Count. Khi muốn sử dụng dữ liệu, nó thăng hạng an toàn thành \texttt{shared\_ptr} thông qua phương thức \texttt{wp.lock()}; nếu đối tượng đã bị giải phóng, \texttt{lock()} trả về con trỏ rỗng an toàn.
"""
