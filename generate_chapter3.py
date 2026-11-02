# -*- coding: utf-8 -*-
"""
Script to generate the complete standalone HTML for Chapter 3:
'OOP3-Class&Objec_new.pdf' - Lớp và Đối Tượng trong C++ (Classes & Objects Deep Dive)
Style: MOSTest5_2 (Minimalist Academic Brutalism, Red-800 Tor-sur-ton, Lora / Inter / JetBrains Mono)
"""

html_template = """<!DOCTYPE html>
<html lang="vi" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chương 3: Lớp và Đối Tượng trong C++ (Classes & Objects) - MOSTest5_2</title>

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=JetBrains+Mono:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">

    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        serif: ['Lora', 'serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                    },
                    colors: {
                        crimson: {
                            50: '#fff1f2',
                            100: '#ffe4e6',
                            200: '#fecdd3',
                            300: '#fda4af',
                            400: '#fb7185',
                            500: '#f43f5e',
                            600: '#e11d48',
                            700: '#be123c',
                            800: '#991b1b',
                            900: '#881337',
                            950: '#4c0519',
                        }
                    }
                }
            }
        }
    </script>

    <!-- PrismJS Dark Tomorrow Theme -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-c.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-cpp.min.js"></script>

    <style>
        body {
            background-color: #fafafa;
            color: #18181b;
            font-family: 'Inter', sans-serif;
        }

        .theory-content {
            font-family: 'Lora', serif;
            font-size: 1.05rem;
            line-height: 1.8;
            color: #27272a;
        }

        .theory-content h3 {
            font-family: 'Inter', sans-serif;
            font-weight: 700;
            color: #991b1b;
            letter-spacing: -0.02em;
        }

        .theory-content h4 {
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            color: #18181b;
        }

        .under-the-hood {
            background-color: #ffffff;
            border-left: 4px solid #991b1b;
            padding: 1.25rem 1.5rem;
            margin: 1.5rem 0;
            border-radius: 0 0.5rem 0.5rem 0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
        }

        .under-the-hood-title {
            font-weight: 700;
            text-transform: uppercase;
            font-size: 0.8rem;
            letter-spacing: 0.05em;
            color: #991b1b;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-bottom: 0.5rem;
        }

        .citation-badge {
            display: inline-block;
            background-color: #fef2f2;
            color: #991b1b;
            border: 1px solid #fecdd3;
            padding: 0.15rem 0.5rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-family: 'JetBrains Mono', monospace;
            font-weight: 600;
            margin-top: 0.5rem;
        }

        .inline-code {
            font-family: 'JetBrains Mono', monospace;
            background-color: #f4f4f5;
            color: #991b1b;
            padding: 0.15rem 0.4rem;
            border-radius: 0.25rem;
            font-size: 0.88em;
            border: 1px solid #e4e4e7;
        }

        /* Quiz interactive styles */
        .option-btn {
            transition: all 0.15s ease-in-out;
            text-align: left;
            width: 100%;
            background-color: #ffffff;
            border: 1.5px solid #e4e4e7;
            padding: 0.85rem 1.15rem;
            border-radius: 0.5rem;
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
            color: #27272a;
            display: flex;
            align-items: flex-start;
            gap: 0.75rem;
            cursor: pointer;
        }

        .option-btn:hover:not(:disabled) {
            border-color: #dc2626;
            background-color: #fef2f2;
        }

        .option-btn.selected-correct {
            background-color: #f0fdf4 !important;
            border-color: #22c55e !important;
            color: #14532d !important;
            font-weight: 600;
        }

        .option-btn.selected-wrong {
            background-color: #fef2f2 !important;
            border-color: #ef4444 !important;
            color: #7f1d1d !important;
            font-weight: 600;
        }

        .option-btn.show-correct {
            background-color: #f0fdf4 !important;
            border-color: #22c55e !important;
            color: #14532d !important;
            font-weight: 600;
        }

        .option-btn:disabled {
            cursor: default;
        }

        .answer-block {
            display: none;
            margin-top: 1.25rem;
            padding: 1.25rem 1.5rem;
            background-color: #fafafa;
            border-left: 3px solid #991b1b;
            border-radius: 0 0.375rem 0.375rem 0;
            color: #3f3f46;
            font-size: 0.92rem;
            line-height: 1.65;
        }

        .answer-block.show {
            display: block;
            animation: fadeIn 0.25s ease-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-4px); }
            to { opacity: 1; transform: translateY(0); }
        }

        pre[class*="language-"] {
            border-radius: 0.5rem;
            margin: 1rem 0;
            border: 1px solid #3f3f46;
            font-size: 0.9rem !important;
        }

        @media print {
            .no-print { display: none !important; }
            .answer-block { display: block !important; }
            body { background: white; }
        }
    </style>
</head>
<body class="antialiased selection:bg-red-100 selection:text-red-900">

    <!-- Top Navigation Bar -->
    <header class="bg-[#991b1b] text-white sticky top-0 z-50 shadow-md no-print">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-white text-[#991b1b] flex items-center justify-center font-black font-mono text-xl rounded shadow-inner">
                    C++
                </div>
                <div>
                    <h1 class="font-bold text-lg leading-tight tracking-tight">Chương 3: Lớp & Đối Tượng (Class & Object)</h1>
                    <p class="text-xs text-red-200">Giáo trình OOP ĐHBK-ĐN | TS. Lê Thị Mỹ Hạnh | Chuẩn MOSTest5_2</p>
                </div>
            </div>
            <div class="flex items-center gap-4">
                <div class="bg-red-950/60 border border-red-700/50 px-3.5 py-1.5 rounded-lg flex items-center gap-2">
                    <i class="fa-solid fa-trophy text-amber-400 text-sm"></i>
                    <span id="score-display" class="font-mono font-bold text-white text-sm">Điểm: 0/50</span>
                </div>
                <button onclick="resetQuiz()" class="bg-red-800 hover:bg-red-700 text-white text-xs font-semibold px-3 py-1.5 rounded transition border border-red-600 flex items-center gap-1.5">
                    <i class="fa-solid fa-rotate-right"></i> Làm lại
                </button>
                <button onclick="window.print()" class="bg-white text-[#991b1b] hover:bg-red-50 text-xs font-bold px-3.5 py-1.5 rounded transition shadow-sm flex items-center gap-1.5">
                    <i class="fa-solid fa-print"></i> In PDF
                </button>
            </div>
        </div>
    </header>

    <!-- Main Container -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 flex flex-col lg:flex-row gap-8">
        
        <!-- Left Sidebar: Table of Contents -->
        <aside class="w-full lg:w-72 flex-shrink-0 no-print">
            <div class="sticky top-24 bg-white border border-zinc-200 rounded-lg p-5 shadow-sm space-y-5">
                <div>
                    <div class="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-zinc-500 mb-3">
                        <i class="fa-solid fa-book-bookmark text-[#991b1b]"></i> Lý thuyết Cốt Lõi
                    </div>
                    <nav class="space-y-1 text-sm border-l-2 border-red-100 pl-3">
                        <a href="#theory-section" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">1. Định nghĩa Lớp & File Phân Tách</a>
                        <a href="#theory-this-scope" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">2. Con trỏ this & Toán tử phạm vi</a>
                        <a href="#theory-constructor" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">3. Constructor & Initializer List</a>
                        <a href="#theory-copy-ctor" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">4. Copy Constructor & Deep Copy</a>
                        <a href="#theory-destructor" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">5. Hàm Hủy (Destructor) & RAII</a>
                        <a href="#theory-friend" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">6. Cơ chế Bạn (Friend)</a>
                        <a href="#theory-const-static" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">7. Thành viên Const & Static</a>
                        <a href="#theory-composition" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">8. Composition & Mảng Đối Tượng</a>
                    </nav>
                </div>

                <div class="pt-4 border-t border-zinc-200">
                    <div class="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-zinc-500 mb-3">
                        <i class="fa-solid fa-list-check text-[#991b1b]"></i> Quiz Bẫy Code (50 Câu)
                    </div>
                    <nav class="space-y-1 text-xs border-l-2 border-zinc-200 pl-3">
                        <a href="#q-group-1" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 1: Khai báo & Header (1-5)</a>
                        <a href="#q-group-2" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 2: this & Scope :: (6-10)</a>
                        <a href="#q-group-3" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 3: Constructor & Init List (11-18)</a>
                        <a href="#q-group-4" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 4: Copy Constructor (19-25)</a>
                        <a href="#q-group-5" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 5: Destructor & RAII (26-30)</a>
                        <a href="#q-group-6" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 6: Friend Function & Class (31-36)</a>
                        <a href="#q-group-7" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 7: Const & Static (37-44)</a>
                        <a href="#q-group-8" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 8: Composition & Mảng (45-50)</a>
                    </nav>
                </div>

                <div class="pt-3 border-t border-zinc-200 text-xs text-zinc-400">
                    <p><i class="fa-solid fa-circle-info text-red-700 mr-1"></i> Chuẩn C++11 ISO/IEC 14882.</p>
                </div>
            </div>
        </aside>

        <!-- Right Main Column -->
        <main class="flex-grow max-w-4xl space-y-12">
            
            <!-- THEORETICAL DEEP-DIVE SECTION -->
            <article id="theory-section" class="bg-white border border-zinc-200 rounded-lg p-6 sm:p-10 shadow-sm space-y-8">
                
                <div class="border-b-2 border-[#991b1b] pb-4">
                    <div class="flex items-center gap-2 text-xs font-mono font-bold text-[#991b1b] uppercase tracking-wider mb-1">
                        Chuyên khảo Lý thuyết C++11 & Bản đồ Kiến trúc
                    </div>
                    <h2 class="text-3xl font-extrabold text-zinc-900 tracking-tight font-sans">
                        Chương 3: Lớp và Đối Tượng trong C++
                    </h2>
                    <p class="text-sm text-zinc-500 mt-1">
                        Trích xuất toàn diện từ giáo trình <code class="inline-code">OOP3-Class&Objec_new.pdf</code> | Đi sâu bản chất trình biên dịch, bảng ký hiệu và quản lý vòng đời đối tượng
                    </p>
                </div>

                <!-- Theory Part 1 -->
                <section class="theory-content space-y-4">
                    <h3 class="text-xl">1. Khái Niệm Lớp & Mô Hình Tách File Header / Source</h3>
                    <p>
                        Lớp (Class) là một kiểu dữ liệu trừu tượng do người dùng định nghĩa, bao gói hai thành phần cơ bản: <strong>Dữ liệu (Thuộc tính)</strong> và <strong>Các hàm thao tác (Phương thức)</strong>.
                    </p>
                    <ul class="list-disc pl-6 space-y-1 text-zinc-700">
                        <li><strong>Quyền truy xuất (Access Specifiers):</strong>
                            <br>- <code class="inline-code">public</code>: Có thể truy cập từ bất kỳ đâu bên ngoài lớp.
                            <br>- <code class="inline-code">private</code>: Chỉ các hàm thành viên của lớp đó hoặc các hàm/lớp bạn (<code class="inline-code">friend</code>) mới có quyền truy cập.
                            <br>- <code class="inline-code">protected</code>: Như <code class="inline-code">private</code> nhưng cho phép các lớp con dẫn xuất truy cập trực tiếp.
                        </li>
                    </ul>

                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-file-code"></i> Cơ chế biên dịch: Phân tách .h và .cpp</div>
                        <p class="text-zinc-700">
                            Để tuân thủ triệt để nguyên lý đóng gói (Encapsulation) và bảo mật mã nguồn trong công nghiệp:
                            <br>1. <strong>File Header (<code class="inline-code">ClassName.h</code>):</strong> Chứa định nghĩa lớp, khai báo nguyên mẫu hàm (Prototype), hằng số và khai báo bạn bè. File này đóng vai trò giao diện (Interface Contract) cung cấp cho người sử dụng thư viện.
                            <br>2. <strong>File Source (<code class="inline-code">ClassName.cpp</code>):</strong> Chứa mã nguồn cài đặt chi tiết của các phương thức bằng toán tử phạm vi <code class="inline-code">ClassName::MethodName()</code>. Mã nguồn này được biên dịch thành file đối tượng (<code class="inline-code">.o</code> hoặc <code class="inline-code">.lib</code>), che giấu hoàn toàn giải thuật nghiệp vụ.
                            <br>3. <strong>Hàm nội tuyến ngầm định:</strong> Các phương thức được định nghĩa <em>trực tiếp ngay bên trong khai báo class</em> sẽ được trình biên dịch tự động coi là hàm <code class="inline-code">inline</code>.
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 4-15: Khái niệm lớp, đóng gói & đặt khai báo lớp ở đâu]</span>
                </section>

                <!-- Theory Part 2 -->
                <section id="theory-this-scope" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">2. Con Trỏ this & Toán Tử Định Phạm Vi (ClassName::)</h3>
                    <p>
                        Mỗi phương thức thành viên phi tĩnh khi thực thi đều cần biết nó đang thao tác trên ô nhớ của đối tượng cụ thể nào. Trình biên dịch hiện thực điều này bằng <strong>Đối số thành viên ẩn: Con trỏ <code class="inline-code">this</code></strong>.
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-crosshairs"></i> Bản chất của con trỏ this</div>
                        <ul class="list-disc pl-5 space-y-1.5 text-zinc-700">
                            <li><code class="inline-code">this</code> là một hằng con trỏ (Const Pointer): <code class="inline-code">ClassName* const this</code>. Lập trình viên không thể gán lại địa chỉ cho <code class="inline-code">this = &other;</code>.</li>
                            <li>Trong hàm thành viên hằng (<code class="inline-code">const</code> method), <code class="inline-code">this</code> có kiểu là: <code class="inline-code">const ClassName* const this</code>, ngăn chặn việc sửa đổi mọi thuộc tính thông qua con trỏ.</li>
                            <li><strong>Phân giải biến trùng tên:</strong> Khi tham số hàm trùng tên với thuộc tính của lớp, toán tử <code class="inline-code">this->x = x;</code> hoặc <code class="inline-code">ClassName::x = x;</code> giúp phân biệt rõ ràng giữa biến cục bộ và biến thành viên.</li>
                            <li><strong>Method Chaining:</strong> Trả về <code class="inline-code">*this</code> theo kiểu tham chiếu (<code class="inline-code">ClassName&</code>) cho phép gọi liên tiếp các phương thức trên cùng một đối tượng.</li>
                        </ul>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 16-19: Đối số thành viên ẩn & Con trỏ this]</span>
                </section>

                <!-- Theory Part 3 -->
                <section id="theory-constructor" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">3. Hàm Xây Dựng (Constructor) & Member Initializer List</h3>
                    <p>
                        Hàm xây dựng (Constructor) là phương thức đặc biệt được gọi tự động ngay tại thời điểm đối tượng được sinh ra trên bộ nhớ. Tên hàm trùng hoàn toàn với tên lớp và <strong>tuyệt đối không có kiểu trả về</strong> (kể cả <code class="inline-code">void</code>).
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-list-check"></i> Member Initializer List vs Gán trong thân Constructor</div>
                        <p class="text-zinc-700">
                            Có 2 cách khởi tạo thành viên dữ liệu:
                            <br>- <em>Cách 1: Gán trong thân hàm tạo</em> (<code class="inline-code">ClassName() { x = 10; }</code>): Trình biên dịch trước hết phải gọi Default Constructor để dựng nên <code>x</code>, sau đó mới gọi toán tử gán <code class="inline-code">operator=</code> để ghi đè giá trị 10. Điều này làm lãng phí hiệu năng nghiêm trọng đối với các đối tượng phức tạp.
                            <br>- <em>Cách 2: Danh sách khởi tạo thành viên (Member Initializer List)</em> (<code class="inline-code">ClassName() : x(10) {}</code>): Khởi tạo trực tiếp ô nhớ của <code>x</code> ngay lúc cấp phát.
                            <br><strong>Các trường hợp BẮT BUỘC phải dùng Initializer List:</strong>
                            <br>&nbsp;&nbsp;&bull; Thành viên dữ liệu hằng (<code class="inline-code">const Type member;</code>).
                            <br>&nbsp;&nbsp;&bull; Thành viên dữ liệu tham chiếu (<code class="inline-code">Type& ref_member;</code>).
                            <br>&nbsp;&nbsp;&bull; Thành viên là đối tượng của một lớp không có Default Constructor.
                            <br>&nbsp;&nbsp;&bull; Khởi tạo lớp cơ sở (Base Class) trong kế thừa.
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 20-25 & 47-48: Hàm xây dựng & Danh sách khởi tạo]</span>
                </section>

                <!-- Theory Part 4 -->
                <section id="theory-copy-ctor" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">4. Hàm Dựng Sao Chép (Copy Constructor) & Sao Chép Sâu</h3>
                    <p>
                        Hàm dựng sao chép (Copy Constructor) dùng để khởi tạo một đối tượng mới từ một đối tượng đã tồn tại cùng lớp. Cú pháp bắt buộc: <code class="inline-code">ClassName(const ClassName& other);</code>.
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-copy"></i> Cơ chế Sao chép Nông vs Sao chép Sâu (Deep Copy)</div>
                        <p class="text-zinc-700">
                            <strong>Tại sao tham số bắt buộc phải là Tham chiếu (&)?</strong> Nếu truyền theo giá trị (<code class="inline-code">ClassName(ClassName other)</code>), để truyền đối số vào hàm thì hệ thống lại cần gọi Copy Constructor... dẫn đến vòng lặp đệ quy vô tận làm tràn stack ngay tại compile-time!
                            <br><br>
                            <strong>3 trường hợp Copy Constructor được kích hoạt:</strong>
                            <br>1. Khởi tạo đối tượng mới từ đối tượng cũ: <code class="inline-code">ClassName a = b;</code> hoặc <code class="inline-code">ClassName a(b);</code>.
                            <br>2. Truyền đối tượng vào một hàm theo dạng tham trị (Pass-by-value).
                            <br>3. Hàm trả về một đối tượng theo giá trị (Return-by-value).
                            <br><br>
                            <strong>Lời khuyên của Dr. Guru:</strong> Khi một lớp chứa con trỏ cấp phát động trên heap, Copy Constructor mặc định chỉ sao chép nông (Shallow Copy) địa chỉ con trỏ, gây lỗi Double Free khi hai đối tượng cùng delete một ô nhớ. Bắt buộc phải tự cài đặt Deep Copy (cấp phát vùng nhớ mới và copy nội dung) và Destructor tương ứng.
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 26-29: Hàm dựng sao chép & Lời khuyên của Dr. Guru]</span>
                </section>

                <!-- Theory Part 5 -->
                <section id="theory-destructor" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">5. Hàm Hủy (Destructor) & Cơ Chế RAII</h3>
                    <p>
                        Hàm hủy (Destructor) đảm nhiệm việc giải phóng tài nguyên (bộ nhớ heap, file handle, socket) mà đối tượng đã chiếm dụng trước khi đối tượng bị xóa sổ khỏi RAM.
                    </p>
                    <ul class="list-disc pl-6 space-y-1.5 text-zinc-700">
                        <li>Cú pháp: <code class="inline-code">~ClassName();</code>. Không nhận đối số, không có kiểu trả về, mỗi lớp chỉ có duy nhất 1 hàm hủy.</li>
                        <li>Được tự động gọi khi đối tượng cục bộ thoát khỏi phạm vi (scope) hoặc khi giải phóng con trỏ bằng toán tử <code class="inline-code">delete</code>.</li>
                        <li><strong>Thứ tự hủy:</strong> Các đối tượng trên Stack bị hủy theo thứ tự ngược lại hoàn toàn với thứ tự khởi tạo (LIFO - Last In, First Out).</li>
                    </ul>
                    <span class="citation-badge">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 30-34: Hàm hủy Destructor & Rò rỉ bộ nhớ]</span>
                </section>

                <!-- Theory Part 6 -->
                <section id="theory-friend" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">6. Cơ Chế Bạn (Friend Functions & Friend Classes)</h3>
                    <p>
                        Cơ chế <code class="inline-code">friend</code> cho phép các hàm hoặc lớp bên ngoài có quyền truy cập vào các thành viên <code class="inline-code">private</code> và <code class="inline-code">protected</code> của lớp khai báo nó.
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-handshake"></i> Ba đặc tính cốt tử của Friend</div>
                        <ul class="list-disc pl-5 space-y-1.5 text-zinc-700">
                            <li><strong>1. Không có tính đối xứng:</strong> Nếu lớp A là bạn của lớp B, không có nghĩa lớp B tự động là bạn của lớp A (B không có quyền xem private của A).</li>
                            <li><strong>2. Không có tính bắc cầu:</strong> Nếu A là bạn của B, và B là bạn của C, thì A hoàn toàn KHÔNG PHẢI là bạn của C.</li>
                            <li><strong>3. Không có tính kế thừa:</strong> Lớp con dẫn xuất của A không thừa hưởng tình bạn với B. Bạn của cha không mặc nhiên là bạn của con.</li>
                        </ul>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 35-46: Cơ chế Friend - Hàm bạn và Lớp bạn]</span>
                </section>

                <!-- Theory Part 7 -->
                <section id="theory-const-static" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">7. Thành Viên Hằng (Const) & Thành Viên Tĩnh (Static)</h3>
                    <p>
                        C++ phân biệt rõ ràng giữa thành viên ở cấp độ Thể hiện (Instance-level) và cấp độ Lớp (Class-level):
                    </p>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-3 font-sans text-sm">
                        <div class="border border-zinc-200 p-4 rounded-lg bg-zinc-50">
                            <h4 class="font-bold text-[#991b1b] uppercase mb-2"><i class="fa-solid fa-lock mr-1"></i> Thành Viên Const</h4>
                            <p class="text-xs text-zinc-600 font-serif leading-relaxed">
                                - <strong>Thuộc tính const:</strong> Giá trị bất biến suốt vòng đời, bắt buộc khởi tạo trong Member Initializer List.
                                <br>- <strong>Phương thức const:</strong> Khóa con trỏ <code class="inline-code">this</code>, cam kết không làm thay đổi trạng thái của đối tượng.
                                <br>- <strong>Đối tượng const:</strong> Chỉ được phép gọi các phương thức có đánh dấu <code class="inline-code">const</code>.
                            </p>
                        </div>
                        <div class="border border-zinc-200 p-4 rounded-lg bg-zinc-50">
                            <h4 class="font-bold text-[#991b1b] uppercase mb-2"><i class="fa-solid fa-layer-group mr-1"></i> Thành Viên Static</h4>
                            <p class="text-xs text-zinc-600 font-serif leading-relaxed">
                                - <strong>Thuộc tính static:</strong> Cấp phát trong phân vùng dữ liệu tĩnh (Data/BSS), dùng chung cho toàn bộ các thể hiện của lớp. Không làm tăng kích thước đối tượng. Bắt buộc phải định nghĩa bên ngoài file .cpp.
                                <br>- <strong>Phương thức static:</strong> Không có con trỏ <code class="inline-code">this</code>, chỉ truy cập được các thành viên tĩnh khác của lớp.
                            </p>
                        </div>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 49-63: Thành viên hằng, thành viên tĩnh, hàm tĩnh]</span>
                </section>

                <!-- Theory Part 8 -->
                <section id="theory-composition" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">8. Composition (Bao Hàm), Mảng Đối Tượng & Union</h3>
                    <p>
                        Lớp có thể chứa thành viên là đối tượng của một lớp khác (Composition). Thứ tự khởi tạo các đối tượng con luôn tuân theo thứ tự chúng được khai báo trong định nghĩa lớp.
                        <br>Khi khai báo mảng tĩnh các đối tượng (<code class="inline-code">ClassName arr[10];</code>), lớp bắt buộc phải có <strong>Default Constructor</strong> để khởi tạo từng phần tử.
                    </p>
                    <span class="citation-badge">[Nguồn: OOP3-Class&Objec_new.pdf - Trang 64-73: Thành viên là đối tượng của lớp khác, mảng đối tượng, struct & union]</span>
                </section>

            </article>

            <!-- INTERACTIVE QUIZ SECTION: EXACTLY 50 CODE-CENTRIC QUESTIONS -->
            <article class="bg-white border border-zinc-200 rounded-lg p-6 sm:p-10 shadow-sm">
                <div class="border-b-2 border-[#991b1b] pb-4 mb-8 flex flex-col sm:flex-row justify-between sm:items-end gap-3">
                    <div>
                        <div class="flex items-center gap-2 text-xs font-mono font-bold text-[#991b1b] uppercase tracking-wider mb-1">
                            Bài Kiểm Tra Năng Lực Trắc Nghiệm Tương Tác
                        </div>
                        <h2 class="text-2xl font-black text-zinc-900 tracking-tight font-sans uppercase">
                            50 Câu Trắc Nghiệm Code & Bẫy Class / Object C++11
                        </h2>
                        <p class="text-xs text-zinc-500 mt-1">
                            100% dựa trên các đoạn code thực tế: bẫy Copy Constructor, Initializer List, Destructor, Friend, Static và RAM Layout
                        </p>
                    </div>
                    <div class="text-xs text-zinc-500 font-mono">
                        Tổng số câu: <span class="font-bold text-[#991b1b]">50</span> | Đã trả lời: <span id="answered-count" class="font-bold text-zinc-800">0</span>
                    </div>
                </div>

                <!-- Questions Container -->
                <div id="quiz-container" class="space-y-12">
                    <!-- Injected by JavaScript -->
                </div>
            </article>

        </main>
    </div>

    <!-- Script Quiz Engine & Data -->
    <script>
        const quizData = [
"""

print("Writing template for Chapter 3...")

