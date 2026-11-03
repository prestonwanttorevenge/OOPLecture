# -*- coding: utf-8 -*-

chap7_text = r"""
% ==============================================================================
% CHƯƠNG 7: XỬ LÝ NGOẠI LỆ & KIẾN TRÚC THƯ VIỆN CHUẨN STL
% ==============================================================================
\chapter{Xử lý Ngoại lệ \& Kiến trúc Thư viện Chuẩn STL (Exceptions \& STL)}

\begin{theorybox}[Triết Lý Xử Lý Lỗi Hiện Đại]
Trong kỹ thuật lập trình hướng thủ tục cổ điển, việc quản lý lỗi dựa hoàn toàn vào \textbf{Mã lỗi trả về (Return Error Codes)} và biến toàn cục \texttt{errno}. Cách tiếp cận này bộc lộ ba khiếm khuyết mang tính bản chất:
\begin{enumerate}
    \item \textbf{Nguy cơ bỏ quên lỗi:} Lập trình viên dễ dàng bỏ qua việc kiểm tra giá trị trả về của hàm, khiến trạng thái lỗi lan truyền âm thầm và phá hủy dữ liệu hệ thống ở những bước tiếp theo.
    \item \textbf{Ô nhiễm chữ ký hàm:} Mã lỗi làm trộn lẫn giá trị trả về hợp lệ với trạng thái thất thường, làm phức tạp hóa cấu trúc logic của chương trình (\textit{Happy Path} bị chìm ngập trong các khối \texttt{if (err != 0)}).
    \item \textbf{Sự bất lực trong Constructor:} \textbf{Constructor hoàn toàn không có kiểu trả về}! Do đó, mã lỗi hoàn toàn bất lực trong việc thông báo thất bại khi khởi tạo một đối tượng.
\end{enumerate}
\textbf{Cơ chế Ngoại lệ (Exception Handling)} tách bạch triệt để luồng thực thi nghiệp vụ bình thường ra khỏi luồng cứu vãn sự cố (\textit{Error Recovery Path}), tạo tiền đề cho các hệ thống phần mềm có độ tin cậy cấp công nghiệp.
\end{theorybox}

\section{Cơ Chế Bắt Ngoại Lệ \& Tránh Cắt Xén Đối Tượng}

Khi một đoạn mã phát hiện một tình huống bất thường vượt quá thẩm quyền xử lý nội bộ, nó kích hoạt ngoại lệ bằng lệnh \texttt{throw}:

\begin{lstlisting}[language=C++]
#include <iostream>
#include <stdexcept>
#include <string>

void executeTransaction(int balance, int withdrawalAmount) {
    if (withdrawalAmount > balance) {
        throw std::runtime_error("Insufficient funds: Overdraft limit exceeded");
    }
    std::cout << "[Banking] Withdrawal successful. Remaining: " << (balance - withdrawalAmount) << "\n";
}

void processAccount() {
    try {
        executeTransaction(500, 1000);
    }
    catch (const std::exception& e) { // STANDARD: Catch by const reference!
        std::cerr << "[Exception Handler] Audit log: " << e.what() << "\n";
    }
}
\end{lstlisting}

\begin{dangerbox}[Quy Tắc Bắt Ngoại Lệ Bằng Tham Chiếu Hằng]
Nếu bắt ngoại lệ theo giá trị (\texttt{catch (std::exception e)}), hiện tượng \textbf{Cắt xén đối tượng đa hình (Polymorphic Object Slicing)} sẽ xảy ra: toàn bộ thông điệp và kiểu lỗi của lớp con (\texttt{std::runtime\_error}) bị gọt bỏ, chỉ còn lại vỏ bọc rỗng của \texttt{std::exception}.

\textbf{Quy tắc Vàng:} Luôn luôn bắt ngoại lệ bằng \textbf{Tham Chiếu Hằng (\texttt{const ExceptionType\& e})}.
\end{dangerbox}

\section{Trải Cuộn Ngăn Xếp (Stack Unwinding) \& Liên Minh RAII}

\begin{underhoodbox}[Cơ Chế Stack Unwinding \& Bảng Ngoại Lệ Zero-Cost]
Trong các hệ thống C++ hiện đại (tuân thủ Itanium C++ ABI trên Linux hoặc Structured Exception Handling trên Windows), trình biên dịch áp dụng mô hình \textbf{Xử lý ngoại lệ Zero-Cost (Table-Driven Zero-Cost Exception Handling)}:
\begin{enumerate}
    \item \textbf{Tại thời điểm bình thường (Zero Runtime Overhead):} Không có bất kỳ chi phí thực thi nào cho các khối \texttt{try}. Mã máy chạy với tốc độ tối đa $100\%$.
    \item \textbf{Khi lệnh \texttt{throw} kích hoạt ngoại lệ:}
    \begin{itemize}
        \item Hệ thống thực hiện \textbf{Pha 1 (Search Phase):} Quét ngược Call Stack dựa trên bảng thông tin khung hàm \textbf{Call Frame Information (DWARF CFI trong phân vùng \texttt{.eh\_frame})} để tìm khối \texttt{catch} hợp lệ mà \textit{chưa thu hồi tài nguyên}.
        \item Nếu tìm thấy khối catch hợp lệ, hệ thống thực hiện \textbf{Pha 2 (Cleanup / Unwind Phase):} Quét ngược lại Call Stack lần thứ hai. Tại mỗi khung hàm bị thoát ra, \textbf{MỌI ĐỐI TƯỢNG ĐỊA PHƯƠNG TRÊN STACK ĐỀU ĐƯỢC TỰ ĐỘNG GỌI DESTRUCTOR} theo thứ tự LIFO!
    \end{itemize}
    \item \textbf{Liên minh hoàn hảo với RAII:} Nếu toàn bộ tài nguyên được bọc trong các đối tượng RAII (\texttt{std::unique\_ptr}, \texttt{std::ofstream}, \texttt{std::lock\_guard}), thì cho dù ngoại lệ có bay qua 10 tầng hàm, toàn bộ bộ nhớ và file đều được đóng sạch sẽ $100\%$.
\end{enumerate}
\end{underhoodbox}

\section{Đặc Tả \texttt{noexcept} \& Tối Ưu Hóa Tái Cấp Phát \texttt{std::vector}}

\begin{lstlisting}[language=C++]
void hardwareReset() noexcept {
    // Cam ket khong bao gio de ngoai le thoat ra ngoai
}
\end{lstlisting}

\begin{underhoodbox}[Toán Tử \texttt{noexcept(expr)} Và Chiến Lược Tái Cấp Phát Của \texttt{std::vector}]
Xét kịch bản \texttt{std::vector<Widget>} bị đầy dung lượng và phải cấp phát một vùng nhớ mới có dung lượng gấp đôi trên Heap:
\begin{enumerate}
    \item Để đáp ứng \textbf{Cam Kết An Toàn Ngoại Lệ Mạnh Mẽ (Strong Exception Guarantee)}: Nếu có lỗi xảy ra trong quá trình di dời dữ liệu, trạng thái của vector cũ phải được bảo toàn nguyên vẹn $100\%$ như trước khi gọi hàm.
    \item Trình biên dịch sử dụng toán tử compile-time: \texttt{noexcept(Widget(std::declval<Widget\&\&>()))}.
    \item \textbf{Move Constructor CÓ \texttt{noexcept}:} Vector sử dụng Move Constructor để di dời từng phần tử sang vùng nhớ mới với chi phí hoán đổi con trỏ $O(1)$.
    \item \textbf{Move Constructor THIẾU \texttt{noexcept}:} Vector lo ngại ngoại lệ xảy ra giữa chừng sẽ làm hỏng dữ liệu gốc không thể khôi phục được. Do đó, \textbf{Vector BẮT BUỘC PHẢI DÙNG COPY CONSTRUCTOR}! Toàn bộ dữ liệu bị sao chép sâu chậm chạp, triệt tiêu lợi thế tốc độ của C++11.
\end{enumerate}
\end{underhoodbox}

\section{Ba Cấp Độ Cam Kết An Toàn Ngoại Lệ (Exception Safety Guarantees)}

Một hệ thống phần mềm C++ chuẩn mực phải phân định rõ ba cấp độ an toàn ngoại lệ theo phân loại của David Abrahams:

\begin{enumerate}
    \item \textbf{Cam Kết Cơ Bản (Basic Guarantee):} Nếu một ngoại lệ xảy ra, hệ thống bảo đảm \textbf{không có tài nguyên nào bị rò rỉ} và tất cả các đối tượng đều ở trạng thái hợp lệ nội tại (\textit{Valid Invariants}).
    \item \textbf{Cam Kết Mạnh Mẽ (Strong Guarantee / Commit-or-Rollback):} Thao tác mang tính nguyên tử (\textit{Atomic}): Hoặc là thành công trọn vẹn, hoặc nếu có ngoại lệ thì trạng thái của toàn bộ hệ thống được phục hồi nguyên vẹn $100\%$ như trước khi gọi hàm (Copy-and-Swap).
    \item \textbf{Cam Kết Không Bao Giờ Thất Bại (Nothrow / No-fail Guarantee):} Hàm cam đoan $100\%$ thành công và không bao giờ ném ra bất kỳ ngoại lệ nào (Mọi Destructor, hàm giải phóng tài nguyên, và Move Constructors).
\end{enumerate}

\begin{underhoodbox}[Lý Do Thiết Kế Đằng Sau \texttt{std::stack::pop()}]
Tại sao trong STL, hàm \texttt{std::stack::pop()} chỉ xóa phần tử đỉnh mà trả về kiểu \texttt{void}?
\begin{itemize}
    \item Nếu hàm \texttt{T pop()} trả về theo giá trị, sau khi phần tử đã bị xóa khỏi Stack, lệnh \texttt{return result;} kích hoạt Copy Constructor của kiểu \texttt{T}.
    \item Nếu phép sao chép ném ra ngoại lệ \texttt{std::bad\_alloc}: Phần tử đã bị xóa mất khỏi Stack nhưng hàm gọi chưa hề nhận được dữ liệu! Dữ liệu bị \textbf{mất trắng vĩnh viễn}, phá vỡ Cam Kết An Toàn Mạnh Mẽ!
    \item Bằng cách tách biệt \texttt{top()} (chỉ đọc tham chiếu) và \texttt{pop()} (xóa an toàn \texttt{noexcept}), STL bảo đảm trọn vẹn tính toàn vẹn dữ liệu.
\end{itemize}
\end{underhoodbox}

\section{Kiến Trúc Tách Rời Trong Thư Viện Chuẩn C++ (STL)}

Thư viện Chuẩn C++ (\textbf{Standard Template Library --- STL}) do Alexander Stepanov sáng tạo là kiệt tác của sự kết hợp giữa Lập trình Tổng quát và Tư duy Hướng Đối tượng.

\subsection{Kiến Trúc Ba Tầng Tách Rời (Decoupled Architecture)}

\begin{figure}[htbp]
\centering
\resizebox{0.95\textwidth}{!}{%
\begin{tikzpicture}[
    box/.style={draw=primaryblue, thick, rounded corners=4pt, fill=white, inner sep=8pt, font=\small\sffamily, align=center},
    arrowstyle/.style={<->, line width=1.5pt, primaryblue}
]
    % Containers (x = 0, width = 4.2cm)
    \node[box, fill=bgsoftblue, text width=4.2cm] (C) at (0, 0) {
        \textbf{Containers (Thùng Chứa)}\\[2pt]
        \footnotesize \texttt{vector, list, deque, map}\\
        \scriptsize Quản lý lưu trữ bộ nhớ vật lý
    };

    % Iterators (x = 6.5, width = 4.4cm)
    \node[box, fill=bglighterblue, draw=accentblue, text width=4.4cm] (I) at (6.5, 0) {
        \textbf{Iterators (Bộ Lặp Chuẩn)}\\[2pt]
        \footnotesize Cầu nối trừu tượng tổng quát\\
        \scriptsize Che giấu cấu trúc dữ liệu nội tại
    };

    % Algorithms (x = 13.0, width = 4.2cm)
    \node[box, fill=bgsoftblue, text width=4.2cm] (A) at (13.0, 0) {
        \textbf{Algorithms (Thuật Toán)}\\[2pt]
        \footnotesize \texttt{sort, find, transform, count}\\
        \scriptsize Thao tác thuần túy trên dải bộ lặp
    };

    % Clean bidirectional arrows with labels in 2.2cm open gap
    \draw[arrowstyle] (C.east) -- (I.west) node[midway, above=5pt, font=\footnotesize\bfseries, accentblue] {Cung cấp};
    \draw[arrowstyle] (I.east) -- (A.west) node[midway, above=5pt, font=\footnotesize\bfseries, accentblue] {Vận hành};
\end{tikzpicture}%
}
\caption{Kiến trúc ba tầng tách rời (Decoupled Architecture) của Alexander Stepanov trong STL.}
\end{figure}

Bằng cách phân tách hoàn toàn Thuật toán và Cấu trúc dữ liệu thông qua giao diện trung gian là \textbf{Bộ lặp (Iterators)}, $N$ cấu trúc dữ liệu và $M$ thuật toán chỉ đòi hỏi đúng $N + M$ thành phần độc lập thay vì $N \times M$ phương thức!

\subsection{Kỹ Thuật Tag Dispatching Tại Compile-Time}

\begin{lstlisting}[language=C++]
// Optimal implementation for Random Access Iterator in O(1)
template <typename RandomAccessIterator, typename Distance>
void advance_impl(RandomAccessIterator& it, Distance n, std::random_access_iterator_tag) {
    it += n; 
}

// Fallback implementation for Bidirectional Iterator in O(N)
template <typename BidirectionalIterator, typename Distance>
void advance_impl(BidirectionalIterator& it, Distance n, std::bidirectional_iterator_tag) {
    while (n > 0) { ++it; --n; }
    while (n < 0) { --it; ++n; }
}

template <typename Iterator, typename Distance>
void advance(Iterator& it, Distance n) {
    advance_impl(it, n, typename std::iterator_traits<Iterator>::iterator_category());
}
\end{lstlisting}

\subsection{Bộ Cấp Phát Bộ Nhớ Tùy Biến (Allocators \& Rebind Mechanism)}

Khi \texttt{std::list<T>} cần cấp phát bộ nhớ cho nút \texttt{ListNode<T>} thay vì kiểu \texttt{T} đơn thuần, nó sử dụng \textbf{Cơ Chế Tái Liên Kết (The Rebind Mechanism)}:
\begin{lstlisting}[language=C++]
template <typename T, typename Allocator = std::allocator<T>>
class CustomList {
    // Rebind Allocator from type T to ListNode<T>:
    using NodeAlloc = typename std::allocator_traits<Allocator>::template rebind_alloc<ListNode<T>>;
    NodeAlloc nodeAllocator;
};
\end{lstlisting}
"""
