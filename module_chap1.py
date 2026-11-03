# -*- coding: utf-8 -*-

chap1_text = r"""
% ==============================================================================
% CHƯƠNG 1: TRIẾT LÝ HỆ HÌNH & KHÔNG GIAN BỘ NHỚ MÁY TÍNH
% ==============================================================================
\chapter{Triết lý Hệ hình \& Không gian Bộ nhớ Máy tính (Philosophy \& Memory Model)}

\begin{theorybox}[Định Nghĩa: Sự Dịch Chuyển Hệ Hình (Paradigm Shift)]
Lập trình Hướng Đối tượng (\textit{Object-Oriented Programming --- OOP}) trong C++ không đơn thuần là sự bổ sung cú pháp từ khóa \texttt{class} vào ngôn ngữ C. Đây là một cuộc cách mạng về \textbf{Hệ hình Tư duy Trừu tượng hóa (Abstraction Paradigm)}:
\begin{itemize}
    \item \textbf{Ngôn ngữ C (Hệ hình Hướng Thủ tục --- Procedural Paradigm):} Tiếp cận thế giới thực dưới góc nhìn của \textit{Thuật toán và Luồng dữ liệu} ($Algorithms + Data\ Structures = Programs$). Dữ liệu là các cấu trúc thụ động (\texttt{struct}), trong khi các hàm nghiệp vụ thao tác tự do trên dữ liệu đó. Trạng thái toàn vẹn của dữ liệu không có bất kỳ cơ chế tự bảo vệ nào ở cấp độ biên dịch.
    \item \textbf{Ngôn ngữ C++ (Hệ hình Đa thức --- Multi-Paradigm):} Tiếp cận bài toán thông qua việc mô hình hóa các \textit{Thực thể Tự trị (Autonomous Entities)}. Một đối tượng là sự kết hợp hữu cơ không thể tách rời giữa \textbf{Trạng thái (Dữ liệu thành viên)} và \textbf{Hành vi (Phương thức thành viên)}. Tính toàn vẹn của đối tượng được bảo đảm tuyệt đối thông qua cơ chế đóng gói và kiểm soát quyền truy cập.
\end{itemize}
\end{theorybox}

\section{Ma Trận So Sánh Kiến Trúc: C vs C++}

Bảng đối chiếu dưới đây tổng hợp các khác biệt bản thể luận giữa ngôn ngữ C và C++:

\begin{table}[htbp]
\centering
\caption{Ma trận so sánh các đặc tính kiến trúc giữa C và C++}
\vspace{0.2cm}
\resizebox{0.95\textwidth}{!}{%
\begin{tabular}{lll}
\toprule
\textbf{Đặc Tính Kiến Trúc} & \textbf{Ngôn Ngữ C (C99/C11)} & \textbf{Ngôn Ngữ C++ (C++11/14/17)} \\
\midrule
Hệ hình chủ đạo & Lập trình Thủ tục / Hướng chức năng & Đa hệ hình: Hướng đối tượng, Tổng quát, Hàm \\
Cơ chế kiểm soát truy cập & Hoàn toàn không có (Toàn bộ là public) & Ba tầng: \texttt{public}, \texttt{protected}, \texttt{private} \\
Cấp phát bộ nhớ động & Hàm thư viện \texttt{malloc()}, \texttt{free()} & Toán tử ngôn ngữ \texttt{new}, \texttt{delete}, Smart Pointers \\
Quản trị vòng đời đối tượng & Thủ công, dễ rò rỉ bộ nhớ & Tự động hóa qua Constructor/Destructor (RAII) \\
Tính đa hình & Con trỏ hàm thủ công trong struct & Bảng phương thức ảo tĩnh \texttt{vtable} và con trỏ \texttt{vptr} \\
Xử lý lỗi hệ thống & Mã lỗi trả về (\textit{Error Codes}), biến \texttt{errno} & Cơ chế ném và bắt ngoại lệ (\textit{Exceptions}), \texttt{noexcept} \\
Không gian tên & Toàn cục phẳng (\textit{Flat namespace}), dễ xung đột & Phân cấp mô-đun qua \texttt{namespace} \\
Khả năng mở rộng toán tử & Không hỗ trợ & Nạp chồng toán tử toàn diện (\textit{Operator Overloading}) \\
\bottomrule
\end{tabular}%
}
\end{table}

\section{Kiến Trúc Bộ Nhớ Tiến Trình (Process Memory Layout)}

Để nắm vững bản chất của mô hình đối tượng C++, kỹ sư phần mềm phải thấu suốt cách thức hệ điều hành và bộ vi xử lý tổ chức không gian bộ nhớ ảo (\textit{Virtual Address Space}). Trên kiến trúc x86-64 với cơ chế phân trang 48-bit tiêu chuẩn, không gian địa chỉ $256\text{ TB}$ được chia tách thành hai dải địa chỉ chuẩn tắc (\textit{Canonical Ranges}) $128\text{ TB}$, phân cách bởi một khoảng trống không định tuyến (\textit{Non-canonical Addressing Gap}) rộng $16\text{ Exabytes}$:

\begin{figure}[htbp]
\centering
\resizebox{0.95\textwidth}{!}{%
\begin{tikzpicture}[every node/.style={font=\small\sffamily, align=center}]
    % Column 1: Address labels on the left (ending cleanly at x = 4.2, leaving 0.3cm margin)
    \node[left, font=\footnotesize\ttfamily, primaryblue] at (4.2, 0.0) {0x0000000000000000};
    \node[left, font=\footnotesize\ttfamily, primaryblue] at (4.2, 5.0) {0x00007FFFFFFFFFFF};
    \node[left, font=\footnotesize\ttfamily, primaryblue] at (4.2, 6.7) {0xFFFF800000000000};
    \node[left, font=\footnotesize\ttfamily, primaryblue] at (4.2, 9.4) {0xFFFFFFFFFFFFFFFF};
    
    % Address axis
    \draw[-{Stealth[length=3mm]}, thick, primaryblue] (0.3, 0) -- (0.3, 9.4);
    \node[font=\footnotesize\bfseries, primaryblue, rotate=90] at (-0.1, 4.7) {Chiều tăng địa chỉ ảo x86-64};

    % Column 2: Memory blocks in the center (x from 4.5 to 12.5, width = 8.0cm)
    \draw[thick, fill=gray!20, draw=primaryblue] (4.5, 0) rectangle (12.5, 1.2) 
        node[pos=0.5] {\textbf{Text Segment (.text)}\\Mã máy thực thi nhị phân --- Read-Only \& Executable};
    \draw[thick, fill=blue!10, draw=primaryblue] (4.5, 1.2) rectangle (12.5, 2.4) 
        node[pos=0.5] {\textbf{Initialized Data Segment (.data)}\\Biến toàn cục \& tĩnh đã khởi tạo khác 0};
    \draw[thick, fill=blue!18, draw=primaryblue] (4.5, 2.4) rectangle (12.5, 3.6) 
        node[pos=0.5] {\textbf{BSS Segment (.bss)}\\Biến toàn cục \& tĩnh chưa khởi tạo (HĐH xóa về 0)};
    \draw[thick, fill=bgsoftblue, draw=primaryblue] (4.5, 3.6) rectangle (12.5, 5.0) 
        node[pos=0.5] {\textbf{Heap (Vùng nhớ động)}\\Cấp phát thông qua \texttt{malloc} / \texttt{new}};
    \draw[thick, dashed, fill=white, draw=commentgray] (4.5, 5.0) rectangle (12.5, 6.7) 
        node[pos=0.5] {\textit{Khoảng trống địa chỉ chuẩn tắc (Non-canonical Gap)}\\\scriptsize Cấm truy xuất --- Phần cứng kích hoạt \#GP Fault};
    \draw[thick, fill=bglighterblue, draw=primaryblue] (4.5, 6.7) rectangle (12.5, 8.2) 
        node[pos=0.5] {\textbf{User Stack (Ngăn xếp khung hàm)}\\Biến cục bộ, Khung hàm, Địa chỉ hoàn trả};
    \draw[thick, fill=darkblue!25, draw=primaryblue] (4.5, 8.2) rectangle (12.5, 9.4) 
        node[pos=0.5] {\textbf{Kernel Space (Nhân hệ điều hành)}\\Không gian bảo vệ nghiêm ngặt (Ring 0)};

    % Column 3: Stack and Heap Growth indicators (placed at x = 13.0, completely separate)
    \draw[-{Stealth[length=2.5mm]}, very thick, accentblue] (13.0, 3.8) -- (13.0, 4.8);
    \node[right=2pt, font=\scriptsize\bfseries, accentblue] at (13.0, 4.3) {Tăng lên};
    
    \draw[-{Stealth[length=2.5mm]}, very thick, primaryblue] (13.0, 8.0) -- (13.0, 7.0);
    \node[right=2pt, font=\scriptsize\bfseries, primaryblue] at (13.0, 7.5) {Tăng xuống};
\end{tikzpicture}%
}
\caption{Kiến trúc phân tầng không gian địa chỉ ảo của tiến trình người dùng trong kiến trúc x86-64.}
\end{figure}

\begin{underhoodbox}[Giải Phẫu Chi Tiết Các Phân Vùng Bộ Nhớ]
\begin{enumerate}
    \item \textbf{Text/Code Segment:} Chứa mã máy nhị phân của tất cả các hàm thành viên và thuật toán. Phân vùng này được nạp cờ bảo vệ \textbf{Read-Only và Executable} (\texttt{RX}) từ bảng trang MMU để ngăn ngừa mã độc ghi đè lên lệnh thực thi.
    \item \textbf{Data Segment (\texttt{.data}) \& BSS Segment (\texttt{.bss}):}
    \begin{itemize}
        \item \texttt{.data}: Chứa các biến toàn cục (\textit{global variables}) và biến tĩnh (\textit{static variables}) đã được khởi tạo giá trị khác 0 tại thời điểm biên dịch.
        \item \texttt{.bss} (\textit{Block Started by Symbol}): Chứa các biến tĩnh/toàn cục chưa khởi tạo hoặc khởi tạo bằng 0. Khi nạp tiến trình, kernel chỉ cần cấp phát kích thước mà không tốn dung lượng lưu trữ trên đĩa cứng, sau đó ánh xạ về các trang bộ nhớ vật lý được xóa trắng về 0.
    \end{itemize}
    \item \textbf{Heap Segment:} Bộ nhớ động được điều phối bởi Trình quản lý bộ nhớ (\textit{Memory Allocator}) của C/C++ runtime. Vùng nhớ này tăng trưởng theo chiều địa chỉ tăng dần thông qua các lời gọi hệ thống \texttt{brk()} hoặc \texttt{mmap()}.
    \item \textbf{Stack Segment:} Vùng nhớ quản lý các khung hàm (\textit{Stack Frames}). Khi một hàm được gọi, một khung ngăn xếp mới được cấp phát; khi hàm trả về, đỉnh ngăn xếp tự động co rút thông qua con trỏ thanh ghi \texttt{RSP}. Ngăn xếp tăng trưởng từ địa chỉ cao xuống địa chỉ thấp. Vị trí cơ sở của Stack được ngẫu nhiên hóa tại runtime bởi cơ chế ASLR (\textit{Address Space Layout Randomization}) nhằm vô hiệu hóa các cuộc tấn công tràn bộ đệm.
\end{enumerate}
\end{underhoodbox}

\section{Quản Lý Bộ Nhớ Động: So Sánh Đối Kháng malloc/free và new/delete}

Sự khác biệt cốt tử giữa việc quản lý bộ nhớ trong C và C++ nằm ở sự hiểu biết về \textbf{Vòng đời của một Thực thể (Object Lifecycle)}.

\begin{lstlisting}[language=C++]
#include <iostream>
#include <cstdlib>

class SocketConnection {
private:
    int socketFd;
    char* networkBuffer;
public:
    SocketConnection(int port) : socketFd(port), networkBuffer(new char[1024]) {
        std::cout << "[Hardware] Socket initialized on port " << socketFd << "\n";
    }
    
    ~SocketConnection() {
        delete[] networkBuffer;
        std::cout << "[Hardware] Socket closed and buffer destroyed\n";
    }
};

void architecturalComparison() {
    // 1. C-STYLE ALLOCATION:
    // malloc() ONLY allocates raw bytes on Heap. It NEVER calls the Constructor!
    SocketConnection* pC = (SocketConnection*)malloc(sizeof(SocketConnection));
    
    // free() ONLY releases raw bytes. It NEVER calls the Destructor!
    // Result: networkBuffer is leaked forever in RAM!
    free(pC);
    
    // 2. C++ PROPER ALLOCATION:
    // Operator new allocates memory AND executes SocketConnection::SocketConnection(8080)
    SocketConnection* pCpp = new SocketConnection(8080);
    
    // Operator delete executes ~SocketConnection() AND releases memory
    delete pCpp;
}
\end{lstlisting}

\begin{underhoodbox}[Điều Kiện Tồn Tại Của Tiền Tố Phân Bổ Mảng (Array Cookie) Theo Chuẩn Itanium ABI]
Khi toán tử \texttt{new[]} cấp phát một mảng đối tượng:
\begin{lstlisting}[language=C++]
SocketConnection* array = new SocketConnection[10];
\end{lstlisting}

Trình biên dịch thực hiện các thao tác mức máy sau:
\begin{enumerate}
    \item \textbf{Quy tắc điều kiện Itanium C++ ABI (§2.7):} Trình biên dịch \textbf{CHỈ chèn thêm Array Cookie} (kích thước thường là 8 bytes trên kiến trúc 64-bit) khi và chỉ khi kiểu dữ liệu có \textbf{Hàm hủy phi tầm thường (Non-trivial Destructor)} hoặc lớp khai báo toán tử giải phóng chấp nhận tham số kích thước. Đối với các kiểu nguyên thủy (\texttt{int}, \texttt{double}) hoặc POD struct, trình biên dịch \textbf{hoàn toàn KHÔNG cấp phát cookie}.
    \item \textbf{Ghi nhận số lượng phần tử:} Với lớp \texttt{SocketConnection} (có hàm hủy người dùng tự định nghĩa), trình biên dịch ghi số nguyên \texttt{10} vào 8 bytes đầu tiên của khối bộ nhớ được cấp phát trên Heap:
    $$\text{Total Bytes} = \text{sizeof}(\text{size\_t}) + 10 \times \text{sizeof}(\text{SocketConnection})$$
    \item \textbf{Dịch chuyển con trỏ:} Con trỏ trả về cho chương trình \texttt{array} được dịch chuyển qua khỏi Array Cookie (trỏ thẳng vào phần tử đầu tiên).
    \item \textbf{Hậu quả khi gọi sai toán tử (\texttt{delete array} thay vì \texttt{delete[] array}):}
    Trình biên dịch sẽ đối xử với \texttt{array} như một đối tượng đơn lẻ. Nó chỉ gọi Destructor đúng 1 lần cho phần tử đầu tiên, bỏ qua 9 phần tử còn lại (thất thoát toàn bộ tài nguyên nội tại). Sau đó, nó truyền địa chỉ lệch 8 bytes cho hàm thu hồi bộ nhớ của hệ điều hành, làm hỏng cấu trúc siêu dữ liệu của Heap (\textbf{Heap Corruption}) và vi phạm điều khoản [expr.delete] p2 của Tiêu chuẩn Quốc tế ISO/IEC 14882.
\end{enumerate}
\end{underhoodbox}

\section{Con Trỏ, Tham Chiếu và Các Toán Tử Ép Kiểu Chuẩn Mực}

\subsection{Bản Chất Dưới Tầng Hợp Ngữ: Tham Chiếu Lvalue (Lvalue Reference)}

Trong ngôn ngữ C, mọi tham số truyền vào hàm mặc định là truyền theo giá trị (\textit{Pass-by-value}). Để hàm có thể biến đổi giá trị bên ngoài, lập trình viên buộc phải sử dụng con trỏ (\textit{Pointers}). Chuẩn C++ giới thiệu khái niệm \textbf{Tham chiếu (References)}, đóng vai trò là một định danh bí danh (\textit{Alias}) cho một vùng nhớ đã tồn tại.

\begin{lstlisting}[language=C++]
void incrementPointer(int* ptr) {
    if (ptr != nullptr) {
        *ptr += 1;
    }
}

void incrementReference(int& ref) {
    ref += 1; // Direct syntax without explicit dereferencing
}
\end{lstlisting}

\begin{underhoodbox}[Bản Chất Của Tham Chiếu Dưới Mã Máy Hợp Ngữ (Assembly)]
Nhiều tài liệu dẫn giải rằng tham chiếu "không chiếm bộ nhớ". Dưới lăng kính kiến trúc máy tính, nhận định này chỉ đúng khi trình biên dịch thực hiện tối ưu hóa nội dòng (\textit{Inlining}). 

Khi một tham chiếu được truyền qua ranh giới của một hàm không được inline, \textbf{MÃ MÁY HỢP NGỮ SINH RA HOÀN TOÀN TRÙNG KHỚP VỚI CON TRỎ HẰNG}:
\begin{lstlisting}[language={[x86masm]Assembler}]
; Call incrementReference(val):
lea rax, [rbp-4]        ; Load dia chi bien val vao thanh ghi RAX
mov rdi, rax            ; Chuyen dia chi vao RDI (tham so 1 theo System V AMD64 ABI)
call incrementReference ; Goi ham

; Ben trong ham incrementReference(int& ref):
mov rax, rdi            ; Nhan dia chi truyen vao
mov edx, [rax]          ; Giai tham chieu: doc gia tri tu dia chi
add edx, 1              ; Tang gia tri
mov [rax], edx          ; Ghi nguoc lai bo nho
\end{lstlisting}
\textbf{Sự khác biệt cốt tử giữa Con trỏ và Tham chiếu:}
\begin{enumerate}
    \item Tham chiếu bắt buộc phải được khởi tạo ngay khi khai báo. Không tồn tại khái niệm "tham chiếu rỗng" (\textit{Null Reference}) trong ngữ nghĩa hợp lệ của C++.
    \item Tham chiếu không thể tái gán để trỏ sang một đối tượng khác sau khi đã khởi tạo (\textit{Immutable Binding}). Mọi phép gán \texttt{ref = val2} thực chất là ghi đè giá trị lên đối tượng mà \texttt{ref} đang đại diện.
\end{enumerate}
\end{underhoodbox}

\subsection{Hệ Thống Bốn Toán Tử Ép Kiểu An Toàn (C++ Named Casts)}

C++ kiên quyết loại bỏ kiểu ép thô lỗ kiểu C (\texttt{(TargetType)expression}) vì nó che giấu các lỗi suy thoái con trỏ nguy hiểm. Thay vào đó, C++ cung cấp 4 toán tử chuyển đổi kiểu tường minh:

\begin{enumerate}
    \item \textbf{\texttt{static\_cast<T>(expr)}:} Chuyển đổi giữa các kiểu dữ liệu liên quan tại compile-time (ép kiểu số nguyên, số thực, chuyển đổi con trỏ trong cùng cây kế thừa khi đã chắc chắn về kiểu).
    \item \textbf{\texttt{const\_cast<T>(expr)}:} Thêm hoặc gỡ bỏ thuộc tính \texttt{const} hoặc \texttt{volatile} của biến. Đây là toán tử duy nhất trong C++ có năng lực gỡ bỏ tính chất hằng.
    \item \textbf{\texttt{dynamic\_cast<T>(expr)}:} Thực hiện ép kiểu an toàn trong cây phái sinh đa hình tại runtime thông qua bảng RTTI (\textit{Run-Time Type Information}). Nếu thất bại trên con trỏ, nó trả về \texttt{nullptr}; nếu thất bại trên tham chiếu, nó ném ra ngoại lệ \texttt{std::bad\_cast}.
    \item \textbf{\texttt{reinterpret\_cast<T>(expr)}:} Ép kiểu thô mức bit giữa các kiểu con trỏ không liên quan (ví dụ: chuyển đổi con trỏ thành số nguyên địa chỉ \texttt{uintptr\_t}). Hoàn toàn không sinh mã máy biến đổi dữ liệu, chỉ thay đổi góc nhìn của trình biên dịch đối với chuỗi bit bộ nhớ.
\end{enumerate}
"""
