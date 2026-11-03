# -*- coding: utf-8 -*-

chap8_text = r"""
% ==============================================================================
% CHƯƠNG 8: NGUYÊN LÝ THIẾT KẾ SOLID & MẪU KIẾN TRÚC HIỆN ĐẠI
% ==============================================================================
\chapter{Nguyên lý Thiết kế SOLID \& Mẫu Kiến trúc Hiện đại (SOLID \& Design Patterns)}

\begin{theorybox}[Bản Chất Của Thiết Kế Kiến Trúc Hướng Đối Tượng]
Một chương trình C++ có thể biên dịch thành công và quản lý bộ nhớ không bị rò rỉ, nhưng vẫn có thể là một phần mềm thất bại nếu kiến trúc của nó giòn vỡ (\textit{Brittle}), cứng nhắc (\textit{Rigid}), và khó kiểm thử (\textit{Untestable}).

Thiết kế Hướng Đối tượng chuẩn mực nhằm tối ưu hóa hai thước đo nền tảng của khoa học kỹ nghệ phần mềm:
\begin{enumerate}
    \item \textbf{Độ Kết Dính Cao (High Cohesion):} Mỗi mô-đun, lớp, hoặc hàm chỉ tập trung hiện thực hóa một chức năng chuyên biệt duy nhất. Mọi biến thành viên và phương thức đều phục vụ một mục đích cốt lõi nhất quán.
    \item \textbf{Độ Liên Kết Thấp (Low Coupling):} Các lớp trong hệ thống hạn chế tối đa sự phụ thuộc trực tiếp vào cấu trúc cài đặt cụ thể của nhau, giao tiếp thuần túy qua các giao diện trừu tượng (\textit{Abstract Interfaces}).
\end{enumerate}
\end{theorybox}

\section{Hệ Thống Năm Nguyên Lý Thiết Kế SOLID}

Bộ năm nguyên lý SOLID do Robert C. Martin tổng hợp là bộ quy tắc vàng cho mọi kỹ sư phần mềm chuyên nghiệp:

\subsection{1. Single Responsibility Principle (Nguyên Lý Đơn Trách Nhiệm - SRP)}
\textit{"Một lớp chỉ nên có duy nhất một lý do để thay đổi."}

\begin{lstlisting}[language=C++]
// VI PHAM SRP: Lop vua quan ly du lieu vua phu trach ghi file va gui mang
class UserProfileBad {
    std::string username;
public:
    void changePassword(const std::string& newPass);
    void saveToDatabase(); // Trach nhiem luu tru
    void sendWelcomeEmail(); // Trach nhiem giao tiep mang
};

// TUAN THU SRP: Tach biet ro rang ba pham vi trach nhiem
class UserProfile {
    std::string username;
public:
    void changePassword(const std::string& newPass);
};

class UserRepository {
public:
    void save(const UserProfile& user); // Chuyen trach luu tru
};

class NotificationService {
public:
    void sendEmail(const UserProfile& user, const std::string& message); // Chuyen trach truyen thong
};
\end{lstlisting}

\subsection{2. Open/Closed Principle (Nguyên Lý Đóng/Mở - OCP)}
\textit{"Thực thể phần mềm phải mở cho việc mở rộng (Open for extension), nhưng đóng đối với việc sửa đổi (Closed for modification)."}

Thay vì dùng chuỗi lệnh \texttt{switch-case} hay \texttt{if-else} kiểm tra kiểu để thực hiện hành vi, ta sử dụng tính Đa hình (\textit{Polymorphism}) để thêm hành vi mới bằng cách tạo thêm lớp phái sinh mà không sửa một dòng code cũ nào!

\subsection{3. Liskov Substitution Principle (Nguyên Lý Thay Thế Liskov - LSP)}
\textit{"Các đối tượng của lớp con phải có khả năng thay thế hoàn toàn cho các đối tượng của lớp cha mà không làm phá vỡ tính đúng đắn của chương trình."}

\begin{dangerbox}[Nghịch Lý Hình Vuông --- Hình Chữ Nhật (The Rectangle-Square Dilemma)]
Trong toán học hình học, \textit{"Hình vuông là một Hình chữ nhật đặc biệt"}. Tuy nhiên, mô hình hóa mối quan hệ này bằng kế thừa trong C++ là một sai lầm chết người:
\begin{lstlisting}[language=C++]
class Rectangle {
protected:
    double width, height;
public:
    virtual void setWidth(double w) { width = w; }
    virtual void setHeight(double h) { height = h; }
    double getArea() const { return width * height; }
};

class Square : public Rectangle {
public:
    void setWidth(double w) override { width = height = w; }
    void setHeight(double h) override { width = height = h; }
};

void clientFunction(Rectangle& r) {
    r.setWidth(5);
    r.setHeight(4);
    // Voi Rectangle: Dien tich phai la 20!
    // Voi Square: r.setHeight(4) lam width bien thanh 4 -> Dien tich = 16!
    assert(r.getArea() == 20); // THAT BAI VOI SQUARE! VI PHAM LSP!
}
\end{lstlisting}
\textbf{Hệ luận kiến trúc:} Quan hệ kế thừa trong lập trình không chỉ yêu cầu tính tương thích về mặt từ vựng (\textit{IS-A}), mà đòi hỏi sự tương thích tuyệt đối về \textbf{Hành vi và Điều kiện bất biến (\textit{Behavioral Subtyping})}.
\end{dangerbox}

\subsection{4. Interface Segregation Principle (Nguyên Lý Phân Tách Giao Diện - ISP)}
\textit{"Khách hàng không nên bị ép buộc phải phụ thuộc vào các giao diện mà họ không sử dụng."}

Thay vì tạo ra một giao diện "toàn năng" khổng lồ với 50 phương thức ảo, hãy chia nhỏ thành nhiều giao diện chuyên biệt, gọn gàng.

\subsection{5. Dependency Inversion Principle (Nguyên Lý Đảo Ngược Phụ Thuộc - DIP)}
\textit{"Các mô-đun cấp cao không nên phụ thuộc vào các mô-đun cấp thấp. Cả hai phải cùng phụ thuộc vào sự trừu tượng hóa (Abstractions)."}

\section{Các Mẫu Thiết Kế GoF Hiện Đại Hóa Trong C++11/14/17}

\subsection{Meyers Singleton (Thread-Safe Static Local Initialization)}

Trong C++98, mẫu Singleton đòi hỏi kỹ thuật khóa hai lần phức tạp (\textit{Double-Checked Locking Pattern}) và dễ vỡ do tái sắp xếp lệnh của CPU. Từ C++11, điều khoản [stmt.dcl] p4 quy định: Việc khởi tạo biến tĩnh cục bộ được bảo đảm **An toàn Đa luồng 100\% bởi Hệ điều hành**:

\begin{lstlisting}[language=C++]
class SystemLogger {
private:
    SystemLogger() = default; // Private constructor
    ~SystemLogger() = default;
    SystemLogger(const SystemLogger&) = delete;
    SystemLogger& operator=(const SystemLogger&) = delete;

public:
    static SystemLogger& getInstance() {
        // Thread-safe dynamic initialization guaranteed by C++11 magic statics:
        static SystemLogger instance;
        return instance;
    }

    void log(const std::string& msg) {
        std::cout << "[SYSTEM AUDIT] " << msg << "\n";
    }
};
\end{lstlisting}

\subsection{Mẫu Nhà Máy (Factory Method Pattern) Kết Hợp Smart Pointers}

\begin{lstlisting}[language=C++]
#include <memory>

class IProtocolHandler {
public:
    virtual void send(const std::string& payload) = 0;
    virtual ~IProtocolHandler() = default;
};

class TcpHandler : public IProtocolHandler {
public:
    void send(const std::string& payload) override { /* TCP logic */ }
};

class UdpHandler : public IProtocolHandler {
public:
    void send(const std::string& payload) override { /* UDP logic */ }
};

// Modern Factory Method returning exclusive ownership:
std::unique_ptr<IProtocolHandler> createHandler(const std::string& type) {
    if (type == "TCP") return std::make_unique<TcpHandler>();
    if (type == "UDP") return std::make_unique<UdpHandler>();
    return nullptr;
}
\end{lstlisting}

\subsection{Mẫu Chiến Lược (Strategy Pattern): Đa Hình Động vs Đa Hình Tĩnh}

Mẫu Chiến lược cho phép hoán đổi thuật toán linh hoạt tại runtime hoặc compile-time:

\begin{figure}[htbp]
\centering
\resizebox{0.88\textwidth}{!}{%
\begin{tikzpicture}[
    box/.style={draw=primaryblue, thick, rounded corners=3pt, fill=white, inner sep=6pt, font=\small\sffamily, align=center},
    umlarrow/.style={-{Triangle[open, length=3mm, width=3mm]}, thick, primaryblue}
]
    % Context class
    \node[box, fill=bglighterblue, text width=4.5cm] (ctx) at (0, 2.5) {
        \textbf{CompressionContext}\\[2pt]
        \footnotesize \texttt{-strategy: ICompressionStrategy*}\\[2pt]
        \footnotesize \texttt{+setStrategy(s: Strategy*)}\\
        \footnotesize \texttt{+compress(file: string)}
    };

    % Strategy interface
    \node[box, fill=bgsoftblue, draw=accentblue, text width=4.5cm] (strat) at (7.0, 2.5) {
        \textbf{<<interface>>}\\[1pt]
        \textbf{ICompressionStrategy}\\[2pt]
        \footnotesize \texttt{+compress(data: string)* = 0}
    };

    % Concrete strategies
    \node[box, fill=white, text width=3.4cm] (zip) at (5.0, 0) {
        \textbf{ZipStrategy}\\[2pt]
        \footnotesize \texttt{+compress(data)}
    };

    % Concrete strategy 2
    \node[box, fill=white, text width=3.4cm] (rar) at (9.0, 0) {
        \textbf{RarStrategy}\\[2pt]
        \footnotesize \texttt{+compress(data)}
    };

    % Associations and generalizations
    \draw[-{Diamond[open, length=3.5mm, width=3.5mm]}, thick, accentblue] (ctx.east) -- (strat.west)
        node[midway, above=5pt, font=\footnotesize\bfseries, accentblue] {uses};

    % Clean textbook UML shared inheritance fork
    \draw[thick, primaryblue] (zip.north) -- (5.0, 1.2) -- (9.0, 1.2) -- (rar.north);
    \draw[umlarrow] (7.0, 1.2) -- (strat.south);
\end{tikzpicture}%
}
\caption{Biểu đồ lớp UML chuẩn của Mẫu Thiết Kế Chiến Lược (Strategy Pattern).}
\end{figure}

% ==============================================================================
% LỜI KẾT & TỔNG KẾT
% ==============================================================================
\chapter*{Lời Kết: Con Đường Làm Chủ C++ Hiện Đại}
\addcontentsline{toc}{chapter}{Lời Kết: Con Đường Làm Chủ C++ Hiện Đại}

Trải qua 8 chương sách kinh điển của \textbf{"The OOP C++ Bible"}, chúng ta đã cùng nhau du hành từ tầng kiến trúc bộ nhớ vật lý thấp nhất (Stack, Heap, Cache, Calling Conventions, ABI Assembly Dispatching, VTable) lên đến những tầng trừu tượng thanh lịch nhất của khoa học máy tính hiện đại (RAII, Move Semantics, Variadic Templates, CRTP, Exception Safety Guarantees, và Bộ nguyên lý SOLID).

C++ không phải là một ngôn ngữ dễ dãi. Nó không che giấu sự phức tạp của phần cứng sau một máy ảo chậm chạp. Nó trao toàn bộ quyền kiểm soát tối thượng vào tay lập trình viên, và như Bjarne Stroustrup từng đúc kết:
\begin{center}
\textit{"C makes it easy to shoot yourself in the foot; C++ makes it harder, but when you do, it blows your whole leg off."}
\end{center}

Nhưng khi bạn đã nắm vững các nguyên lý "dưới gầm máy" được trình bày trong cuốn sách này, bạn không còn sợ hãi những cạm bẫy ngầm của bộ nhớ nữa. Bạn đã nắm trong tay sức mạnh để kiến tạo nên những hệ thống phần mềm có hiệu năng vô song, an toàn tuyệt đối và trường tồn cùng thời gian.

Chúc các bạn luôn giữ vững niềm đam mê và tự hào trên con đường trở thành một \textbf{C++ Master}!

% ==============================================================================
% TÀI LIỆU THAM KHẢO CHUẨN MỰC QUỐC TẾ (SCHOLARLY BIBLIOGRAPHY)
% ==============================================================================
\begin{thebibliography}{99}
\addcontentsline{toc}{chapter}{Tài Liệu Tham Khảo (Bibliography)}

\bibitem{iso11}
ISO/IEC 14882:2011, \textit{Information technology --- Programming languages --- C++}, International Organization for Standardization, Geneva, Switzerland.

\bibitem{iso14}
ISO/IEC 14882:2014, \textit{Information technology --- Programming languages --- C++}, International Organization for Standardization, Geneva, Switzerland.

\bibitem{iso17}
ISO/IEC 14882:2017, \textit{Information technology --- Programming languages --- C++}, International Organization for Standardization, Geneva, Switzerland.

\bibitem{stroustrup-cpp}
Bjarne Stroustrup (2013), \textit{The C++ Programming Language} (4th Edition), Addison-Wesley Professional.

\bibitem{stroustrup-design}
Bjarne Stroustrup (1994), \textit{The Design and Evolution of C++}, Addison-Wesley Professional.

\bibitem{meyers-effective}
Scott Meyers (2005), \textit{Effective C++: 55 Specific Ways to Improve Your Programs and Designs} (3rd Edition), Addison-Wesley Professional.

\bibitem{meyers-modern}
Scott Meyers (2014), \textit{Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14}, O'Reilly Media.

\bibitem{alexandrescu}
Andrei Alexandrescu (2001), \textit{Modern C++ Design: Generic Programming and Design Patterns Applied}, Addison-Wesley Professional.

\bibitem{gamma-gof}
Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides (1994), \textit{Design Patterns: Elements of Reusable Object-Oriented Software}, Addison-Wesley Professional.

\bibitem{lippman}
Stanley B. Lippman (1996), \textit{Inside the C++ Object Model}, Addison-Wesley Professional.

\bibitem{vandevoorde}
David Vandevoorde, Nicolai M. Josuttis, Douglas Gregor (2017), \textit{C++ Templates: The Complete Guide} (2nd Edition), Addison-Wesley Professional.

\bibitem{itanium-abi}
Codesourcery, Compaq, EDG, HP, IBM, Intel, SGI (2001--2024), \textit{Itanium C++ ABI (Revision 1.86)}, Mentored by the LLVM and GCC Compiler Working Groups.

\bibitem{stepanov}
Alexander Stepanov, Meng Lee (1995), \textit{The Standard Template Library}, HP Laboratories Technical Report 95-11(R.1).

\end{thebibliography}

\end{document}
"""
