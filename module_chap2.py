# -*- coding: utf-8 -*-

chap2_text = r"""
% ==============================================================================
% CHƯƠNG 2: LỚP, ĐỐI TƯỢNG & CƠ CHẾ KHỞI TẠO THỰC THỂ
% ==============================================================================
\chapter{Lớp, Đối tượng \& Cơ chế Khởi tạo Thực thể (Classes \& Objects)}

\begin{theorybox}[Định Nghĩa Pháp Lập: Lớp (Class) và Đối Tượng (Object)]
\textbf{Lớp (Class)} là một khuôn mẫu trừu tượng do người dùng định nghĩa, đóng vai trò là một kiểu dữ liệu mới (\textit{User-Defined Type}), quy định cấu trúc bộ nhớ và các phép toán hợp lệ trên kiểu dữ liệu đó.

\textbf{Đối tượng (Object)} là một thực thể vật lý cụ thể (\textit{Instance}) được cấp phát trong không gian bộ nhớ (trên Stack hoặc Heap), chiếm một vùng kích thước xác định và sở hữu trạng thái dữ liệu độc lập.
\end{theorybox}

\section{Tính Đóng Gói (Encapsulation) \& Bộ Chỉ Định Quyền Truy Cập}

\subsection{Cơ Chế Phân Quyền Truy Cập}

Tính đóng gói (\textit{Encapsulation}) trong C++ thực hiện việc che giấu cấu trúc dữ liệu nội tại và bảo vệ trạng thái bất biến (\textit{Class Invariants}) của đối tượng thông qua ba từ khóa chỉ định phạm vi truy cập:

\begin{itemize}
    \item \textbf{\texttt{public}:} Các thành viên có thể được truy cập tự do từ bất kỳ điểm nào trong chương trình thông qua biến đối tượng, con trỏ hoặc tham chiếu.
    \item \textbf{\texttt{private}:} Các thành viên bị khóa hoàn toàn; chỉ có thể được truy cập bởi các hàm thành viên của chính lớp đó hoặc bởi các hàm/lớp được cấp quyền bạn bè (\texttt{friend}).
    \item \textbf{\texttt{protected}:} Tương tự như \texttt{private}, nhưng cho phép các lớp con cháu trong cây phái sinh (\textit{Derived Classes}) có quyền truy cập trực tiếp.
\end{itemize}

\textbf{Sự khác biệt cốt tử giữa \texttt{class} và \texttt{struct}:}
Trong C++, sự khác biệt duy nhất giữa \texttt{class} và \texttt{struct} nằm ở \textbf{Quyền truy cập mặc định}:
\begin{itemize}
    \item Trong \texttt{struct}, mọi thành viên và mối quan hệ kế thừa mặc định là \textbf{\texttt{public}}.
    \item Trong \texttt{class}, mọi thành viên và mối quan hệ kế thừa mặc định là \textbf{\texttt{private}}.
\end{itemize}

\subsection{Khảo Sát Bộ Nhớ: Sự Căn Chỉnh Dữ Liệu (Memory Alignment \& Padding)}

Kích thước của một đối tượng trong RAM không đơn thuần là tổng kích thước của các biến thành viên:

\begin{lstlisting}[language=C++]
struct UnalignedStruct {
    char a;     // 1 byte
    // 3 bytes padding do kien truc 32-bit/64-bit yeu cau can le 4 bytes
    int b;      // 4 bytes
    char c;     // 1 byte
    // 7 bytes padding do kien truc 64-bit yeu cau can le 8 bytes
    double d;   // 8 bytes
}; // sizeof(UnalignedStruct) = 24 bytes (thay vi 1 + 4 + 1 + 8 = 14 bytes)!

struct OptimizedStruct {
    double d;   // 8 bytes (Offset 0)
    int b;      // 4 bytes (Offset 8)
    char a;     // 1 byte  (Offset 12)
    char c;     // 1 byte  (Offset 13)
    // 2 bytes padding de tong kich thuoc chia het cho 8
}; // sizeof(OptimizedStruct) = 16 bytes! Tiet kiem 33% bo nho RAM!
\end{lstlisting}

\begin{underhoodbox}[Nguyên Lý Căn Lề Bộ Nhớ Phần Cứng (Hardware Bus Alignment)]
Tại sao CPU không đọc dữ liệu tại bất kỳ địa chỉ nào mà đòi hỏi căn lề (\textit{Data Alignment})?
\begin{enumerate}
    \item \textbf{Đường truyền Bus dữ liệu:} Bộ vi xử lý hiện đại (x86-64) đọc dữ liệu từ RAM vào CPU Cache theo từng khối 32-bit, 64-bit, hoặc Cache Line 64 bytes.
    \item \textbf{Chi phí truy cập lệch lề (Misaligned Access):} Nếu một biến số thực 8 bytes (\texttt{double}) nằm vắt ngang qua ranh giới của hai khối 8 bytes, CPU buộc phải thực hiện \textbf{HAI chu kỳ đọc bộ nhớ riêng biệt}, sau đó dùng các lệnh dịch bit (\texttt{shl}, \texttt{shr}) và ghép bit (\texttt{or}) để tái tạo lại giá trị.
    \item Trình biên dịch C++ tự động chèn các byte đệm (\textbf{Padding Bytes}) để tối ưu hóa tốc độ truy xuất của CPU, ưu tiên hiệu năng thực thi hơn việc tiết kiệm vài byte bộ nhớ vật lý.
\end{enumerate}
\end{underhoodbox}

\section{Bản Chất Con Trỏ Bản Thể (this Pointer) Dưới Tầng RAM \& ABI Gọi Hàm}

Một đối tượng khi được tạo ra trong RAM chỉ chiếm dung lượng bằng tổng các biến thành viên dữ liệu (cộng padding và con trỏ ảo nếu có). \textbf{Các hàm thành viên không chiếm bất kỳ byte nào trong không gian nhớ của đối tượng}. Mã máy của các hàm nằm duy nhất một bản trong phân vùng \texttt{.text}.

Làm thế nào một hàm thành viên biết nó đang thao tác trên dữ liệu của đối tượng nào? Câu trả lời là \textbf{Con trỏ bản thể \texttt{this} (Self-Referential Pointer)}.

\begin{lstlisting}[language=C++]
class RegisterFile {
private:
    int value;
public:
    void setValue(int v) {
        this->value = v; // this tro toi chinh thuc the hien tai
    }
};
\end{lstlisting}

\begin{underhoodbox}[Giao Diện Nhị Phân Ứng Dụng (ABI) Và Thanh Ghi Truyền Con Trỏ this]
Khi lập trình viên viết dòng lệnh gọi hàm: \texttt{reg.setValue(42);}, trình biên dịch biến đổi lời gọi này thành một hàm dạng thủ tục mức thấp:
$$\texttt{RegisterFile::setValue(\&reg, 42);}$$

\textbf{Quy ước gọi hàm (Calling Conventions):}
\begin{itemize}
    \item \textbf{Trên kiến trúc 32-bit x86 (\texttt{\_\_thiscall}):} Con trỏ bản thể \texttt{this} được truyền trực tiếp thông qua thanh ghi chuyên dụng \textbf{\texttt{ECX}}, trong khi các tham số còn lại được đẩy vào Stack từ phải qua trái.
    \item \textbf{Trên kiến trúc 64-bit (System V AMD64 ABI --- Linux/macOS):} Con trỏ bản thể \texttt{this} luôn được nạp vào thanh ghi tham số đầu tiên: \textbf{\texttt{RDI}}. Tham số thứ hai được nạp vào \textbf{\texttt{RSI}}.
    \item \textbf{Trên kiến trúc 64-bit (Microsoft x64 ABI --- Windows):} Con trỏ bản thể \texttt{this} được nạp vào thanh ghi \textbf{\texttt{RCX}}. Tham số thứ hai được nạp vào \textbf{\texttt{RDX}}.
\end{itemize}

Mã máy hợp ngữ được sinh ra minh họa cơ chế này:
\begin{lstlisting}[language={[x86masm]Assembler}]
lea rdi, [rbp-16]       ; Load dia chi doi tuong reg vao RDI (this pointer)
mov esi, 42             ; Load tham so 42 vao RSI
call RegisterFile::setValue ; Nhay toi ham thanh vien trong .text
\end{lstlisting}

\textbf{Bản chất pháp lập theo ISO/IEC 14882:}
Trong hệ thống kiểu của chuẩn C++, \texttt{this} là một \textbf{prvalue} có kiểu là \texttt{ClassName*} (hoặc \texttt{const ClassName*} trong phương thức hằng). Vì là prvalue (giá trị thuần rvalue), lập trình viên không thể gán giá trị cho \texttt{this} (\texttt{this = ptr;} là lỗi ngữ pháp).
\end{underhoodbox}

\section{Vòng Đời Khởi Tạo Đối Tượng (Constructors Architecture)}

Hàm dựng (\textbf{Constructor}) là hàm thành viên đặc biệt chịu trách nhiệm thiết lập trạng thái ban đầu của đối tượng và thiết lập các điều kiện bất biến (\textit{Class Invariants}). Constructor không có kiểu trả về và mang tên trùng khớp với tên lớp.

\subsection{Member Initializer List vs Phép Gán Trong Thân Constructor}

\begin{lstlisting}[language=C++]
class PipelineBlock {
private:
    std::string blockName;
    const int blockId;      // Const field: Bat buoc phai khoi tao bang danh sach
    int& systemRef;         // Reference field: Bat buoc phai khoi tao bang danh sach

public:
    // PHUONG PHAP CHUAN MUC (Member Initializer List):
    PipelineBlock(const std::string& name, int id, int& ref)
        : blockName(name), blockId(id), systemRef(ref) {
        // Truong du lieu duoc khoi tao truc tiep dung Constructor tuong ung
    }
};
\end{lstlisting}

\begin{theorybox}[Bản Chất Của Danh Sách Khởi Tạo Thành Viên (Member Initializer List)]
Khi một đối tượng được khởi tạo, tiến trình cấp phát diễn ra theo hai giai đoạn độc lập:
\begin{enumerate}
    \item \textbf{Giai đoạn 1: Khởi tạo các trường thành viên (Initialization Phase):} Xảy ra tại danh sách khởi tạo \texttt{: var1(val1), var2(val2)}. Mỗi trường được gọi trực tiếp hàm tạo tương ứng.
    \item \textbf{Giai đoạn 2: Thực thi phần thân hàm tạo (Execution Phase):} Các dòng lệnh bên trong cặp dấu ngoặc nhọn \texttt{\{ \}} được thực thi. Nếu tại đây có phép gán \texttt{var1 = val1;}, trường đó đã phải trải qua việc khởi tạo mặc định từ trước, sau đó bị ghi đè bởi toán tử gán, gây lãng phí ít nhất 50\% hiệu năng xử lý.
\end{enumerate}
\end{theorybox}

\begin{dangerbox}[Bẫy Thứ Tự Khởi Tạo Thành Viên (Initialization Order Trap)]
Xét đoạn mã nguồn minh họa khiếm khuyết kinh điển:
\begin{lstlisting}[language=C++]
class MemoryController {
private:
    int* buffer;       // KHAI BAO TRUOC -> KHOI TAO TRUOC!
    size_t bufferSize; // KHAI BAO SAU   -> KHOI TAO SAU!
public:
    // Canh bao: Lap trinh vien ghi bufferSize(size) truoc trong danh sach:
    MemoryController(size_t size)
        : bufferSize(size), buffer(new int[bufferSize]) {}
};
\end{lstlisting}

\textbf{Quy tắc chuẩn quốc tế ISO/IEC 14882:}
Thứ tự khởi tạo các trường thành viên của một lớp \textbf{HOÀN TOÀN DỰA VÀO THỨ TỰ KHAI BÁO TRONG ĐỊNH NGHĨA LỚP}, hoàn toàn bất chấp thứ tự được liệt kê trong Member Initializer List!

Trong ví dụ trên, biến \texttt{buffer} được khai báo \textbf{TRƯỚC} biến \texttt{bufferSize}. Do đó, \texttt{buffer} sẽ được khởi tạo trước! Tại thời điểm \texttt{new int[bufferSize]} thực thi, biến \texttt{bufferSize} chưa hề được gán giá trị và đang chứa giá trị rác ngẫu nhiên của bộ nhớ. Kết quả là hệ thống cố gắng cấp phát một lượng RAM bất định, dẫn đến lỗi sập tiến trình (\textbf{Segmentation Fault})!
\end{dangerbox}

\subsection{Hàm Tạo Ủy Quyền \& Khởi Tạo Thành Viên Mặc Định (C++11)}

Chuẩn C++11 bổ sung hai cơ chế giảm thiểu sự trùng lặp mã nguồn trong khởi tạo:
\begin{enumerate}
    \item \textbf{Khởi tạo thành viên tại chỗ (Default Member Initializers):} Cho phép gán giá trị mặc định trực tiếp tại dòng khai báo biến:
    \begin{lstlisting}[language=C++]
    class ServerConfig {
        int timeoutMs = 5000;
        bool keepAlive = true;
    };
    \end{lstlisting}
    \item \textbf{Hàm tạo ủy quyền (Delegating Constructors):} Cho phép một Constructor gọi một Constructor khác của cùng lớp thông qua danh sách khởi tạo:
    \begin{lstlisting}[language=C++]
    class Vector3D {
    public:
        double x, y, z;
        Vector3D(double a, double b, double c) : x(a), y(b), z(c) {}
        Vector3D() : Vector3D(0.0, 0.0, 0.0) {} // Uy quyen cho Constructor 3 tham so
    };
    \end{lstlisting}
\end{enumerate}

\subsection{Ngăn Chặn Ép Kiểu Ngầm Định Với Từ Khóa \texttt{explicit}}

Trong C++, bất kỳ Constructor nào có thể được gọi với \textbf{MỘT tham số duy nhất} đều mặc định đóng vai trò là một hàm chuyển đổi kiểu ngầm định (\textit{Converting Constructor}):

\begin{lstlisting}[language=C++]
class BufferPool {
public:
    // explicit ngan chan compiler tu dong ep kieu int thanh BufferPool
    explicit BufferPool(int capacity) { /* ... */ }
};

void allocate(const BufferPool& pool);

void test() {
    // BufferPool p = 100; // LOI BIEN DICH: explicit chan ep kieu ngam dinh
    BufferPool p(100);       // HOP LE: Khoi tao tuong minh
    allocate(BufferPool(50)); // HOP LE
}
\end{lstlisting}

\section{Hàm Hủy (Destructor) \& Triết Lý Thiết Kế RAII}

Hàm hủy (\textbf{Destructor}) có cú pháp \texttt{\textasciitilde{}ClassName()}, không nhận tham số và không trả về giá trị. Destructor được hệ thống tự động kích hoạt khi đối tượng kết thúc vòng đời.

\begin{theorybox}[Triết Lý Thiết Kế RAII (Resource Acquisition Is Initialization)]
Được phát minh bởi Bjarne Stroustrup, \textbf{RAII} là mô thức thiết kế phần mềm quan trọng nhất của C++ hiện đại. Tư tưởng cốt lõi của RAII thiết lập định đề:
\begin{center}
\textit{"Mọi tài nguyên hệ thống (Bộ nhớ RAM, File Descriptor, Socket Mạng, Mutex Lock) phải được gắn chặt vào Vòng đời của một Đối tượng Ngăn xếp (Stack-allocated Object)."}
\end{center}
\begin{itemize}
    \item \textbf{Cấp phát tài nguyên} được thực hiện trong Constructor.
    \item \textbf{Giải phóng tài nguyên} được ủy thác hoàn toàn tự động cho Destructor.
\end{itemize}
Nhờ cơ chế \textbf{Trải cuộn Ngăn xếp (Stack Unwinding)}, cho dù hàm kết thúc bình thường qua lệnh \texttt{return} hay bị gián đoạn đột ngột bởi một ngoại lệ (\texttt{throw}), toàn bộ tài nguyên đều được dọn dẹp sạch sẽ $100\%$, loại trừ hoàn toàn nguy cơ rò rỉ tài nguyên.
\end{theorybox}

\section{Thành Viên Static, Const và Kỹ Thuật Hàm Bạn (Friend)}

\subsection{Thành Viên Tĩnh (Static Data \& Methods)}

\begin{itemize}
    \item \textbf{Biến thành viên tĩnh (\texttt{static}):} Không thuộc về bất kỳ đối tượng cụ thể nào của lớp. Nó chỉ tồn tại \textbf{DUY NHẤT MỘT BẢN SAO} trong toàn bộ tiến trình, được lưu trữ tại phân vùng \texttt{.data} hoặc \texttt{.bss}. Kích thước của đối tượng hoàn toàn không chứa biến \texttt{static}.
    \item \textbf{Phương thức tĩnh (\texttt{static} methods):} Không nhận con trỏ bản thể \texttt{this}. Do đó, phương thức tĩnh \textbf{không thể truy cập các biến thành viên phi tĩnh} và không thể gọi các phương thức phi tĩnh nếu không thông qua một đối tượng tường minh.
\end{itemize}

\subsection{Từ Khóa \texttt{mutable} --- Ngoại Lệ Trong Phương Thức Hằng}

Một phương thức được đánh dấu \texttt{const} cam kết không làm thay đổi trạng thái quan sát được (\textit{Bitwise Constness}) của đối tượng. Tuy nhiên, trong một số kịch bản kỹ thuật (đồng bộ hóa luồng qua \texttt{std::mutex}, lưu bộ nhớ đệm cache, đếm tần suất truy cập), ta cần biến đổi một số trường dữ liệu mà không làm thay đổi ngữ nghĩa logic của đối tượng. Từ khóa \textbf{\texttt{mutable}} cho phép một trường dữ liệu được phép sửa đổi ngay bên trong phương thức \texttt{const}:

\begin{lstlisting}[language=C++]
class DataCache {
private:
    std::string cachedValue;
    mutable size_t accessCounter = 0; // Duoc phep bien doi trong const method

public:
    std::string readData() const {
        ++accessCounter; // Hop le nho tu khoa mutable
        return cachedValue;
    }
};
\end{lstlisting}

\subsection{Quan Hệ Bạn Bè (Friendship Architecture)}

Từ khóa \texttt{friend} cho phép một hàm tự do hoặc một lớp khác có quyền truy cập vào các trường \texttt{private} và \texttt{protected} của lớp định nghĩa.

\begin{theorybox}[Ba Định Đề Bất Biến Về Quan Hệ Bạn Bè (Friendship Postulates)]
\begin{enumerate}
    \item \textbf{Tính Không Đối Xứng (Not Symmetric):} Nếu lớp $A$ khai báo lớp $B$ là bạn, thì $B$ có quyền xem trường ẩn của $A$, nhưng $A$ hoàn toàn không có quyền xem trường ẩn của $B$.
    \item \textbf{Tính Không Bắc Cầu (Not Transitive):} Nếu $A$ là bạn của $B$, và $B$ là bạn của $C$, thì $A$ hoàn toàn không mặc nhiên là bạn của $C$.
    \item \textbf{Tính Không Kế Thừa (Not Inherited):} Lớp con của một lớp bạn không được thừa hưởng quyền bạn bè từ lớp cha.
\end{enumerate}
\end{theorybox}
"""
