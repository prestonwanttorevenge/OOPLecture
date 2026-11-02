# -*- coding: utf-8 -*-
"""
Script to generate the complete standalone HTML for Chapter 8:
'OOP8-Exception.pdf' - Ngoại Lệ trong C++11 (Exception Handling Deep Dive)
Style: MOSTest5_2 (Minimalist Academic Brutalism, Red-800 Tor-sur-ton, Lora / Inter / JetBrains Mono)
"""

html_template = """<!DOCTYPE html>
<html lang="vi" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chương 8: Xử Lý Ngoại Lệ (Exception Handling) - MOSTest5_2</title>

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
                    <h1 class="font-bold text-lg leading-tight tracking-tight">Chương 8: Xử Lý Ngoại Lệ (Exception Handling)</h1>
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
                        <a href="#theory-section" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">1. Xử lý lỗi truyền thống vs OOP</a>
                        <a href="#theory-try-catch" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">2. Cú pháp throw, try - catch</a>
                        <a href="#theory-stack-unwinding" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">3. Cơ chế Stack Unwinding & RAII</a>
                        <a href="#theory-matching" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">4. Exception Matching & Slicing</a>
                        <a href="#theory-rethrow" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">5. Ném tiếp ngoại lệ (throw;)</a>
                        <a href="#theory-std-hierarchy" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">6. Cây phân cấp std::exception</a>
                        <a href="#theory-noexcept" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">7. noexcept & noexcept(expr)</a>
                        <a href="#theory-ctor-dtor" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">8. Ngoại lệ trong Ctor & Dtor</a>
                    </nav>
                </div>

                <div class="pt-4 border-t border-zinc-200">
                    <div class="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-zinc-500 mb-3">
                        <i class="fa-solid fa-list-check text-[#991b1b]"></i> Quiz Bẫy Code (50 Câu)
                    </div>
                    <nav class="space-y-1 text-xs border-l-2 border-zinc-200 pl-3">
                        <a href="#q-group-1" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 1: Cơ chế throw & try-catch (1-6)</a>
                        <a href="#q-group-2" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 2: Stack Unwinding & RAII (7-12)</a>
                        <a href="#q-group-3" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 3: So khớp Matching (13-18)</a>
                        <a href="#q-group-4" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 4: Re-throw & Slicing (19-24)</a>
                        <a href="#q-group-5" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 5: Cây std::exception (25-30)</a>
                        <a href="#q-group-6" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 6: noexcept C++11 (31-36)</a>
                        <a href="#q-group-7" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 7: Ngoại lệ trong Constructor (37-42)</a>
                        <a href="#q-group-8" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 8: Destructor & terminate (43-50)</a>
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
                        Chương 8: Xử Lý Ngoại Lệ (Exception Handling)
                    </h2>
                    <p class="text-sm text-zinc-500 mt-1">
                        Trích xuất toàn diện từ giáo trình <code class="inline-code">OOP8-Exception.pdf</code> | Phân tích sâu sắc cơ chế Stack Unwinding, bảng EHTable và từ khóa noexcept
                    </p>
                </div>

                <!-- Theory Part 1 -->
                <section class="theory-content space-y-4">
                    <h3 class="text-xl">1. Xử Lý Lỗi Truyền Thống vs Cơ Chế Ngoại Lệ C++</h3>
                    <p>
                        Trong ngôn ngữ C cổ điển, việc xử lý lỗi dựa vào mã trả về (Return Code: ví dụ trả về <code class="inline-code">-1</code> hoặc <code class="inline-code">NULL</code>) hoặc cờ toàn cục <code class="inline-code">errno</code>.
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-triangle-exclamation"></i> Nhược điểm chí tử của Mã trả về truyền thống</div>
                        <ul class="list-disc pl-5 space-y-1 text-zinc-700">
                            <li>Lập trình viên rất dễ "quên" kiểm tra giá trị trả về, dẫn đến lỗi âm thầm lan truyền và gây sập hệ thống ở các module xa xôi.</li>
                            <li>Làm bẩn mã nguồn: Mỗi lời gọi hàm đều phải kèm theo cấu trúc <code class="inline-code">if (res == -1) ...</code> lặp đi lặp lại.</li>
                            <li>Không thể trả về lỗi từ Constructor (hàm tạo không có kiểu trả về!).</li>
                        </ul>
                        <p class="text-zinc-700 mt-2">
                            <strong>C++ Exception:</strong> Tách biệt hoàn toàn luồng mã bình thường (Normal Flow) và luồng xử lý sự cố (Error Handling Flow). Khi xảy ra lỗi, hàm ném ra một đối tượng ngoại lệ (<code class="inline-code">throw</code>), buộc runtime phải chuyển quyền điều khiển tới khối <code class="inline-code">catch</code> phù hợp nhất.
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP8-Exception.pdf - Trang 2-8: Xử lý lỗi truyền thống vs C++ exception]</span>
                </section>

                <!-- Theory Part 2 -->
                <section id="theory-stack-unwinding" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">2. Cơ Chế Cuộn Ngược Ngăn Xếp (Stack Unwinding) & RAII</h3>
                    <p>
                        Khi lệnh <code class="inline-code">throw</code> được kích hoạt, một tiến trình phức tạp diễn ra dưới quyền điều khiển của Runtime Exception Handler: <strong>Stack Unwinding</strong>.
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-layer-group"></i> Cơ chế Stack Unwinding mức Assembly & Bảng EHTable</div>
                        <p class="text-zinc-700">
                            1. CPU ngay lập tức dừng luồng thực thi thông thường. Runtime tra cứu bảng hỗ trợ ngoại lệ (Exception Handling Table) được nhúng trong phân vùng mã máy.
                            <br>2. Runtime thu hồi lần lượt các Stack Frame từ hàm hiện tại ngược dần về các hàm cha gọi nó trên Call Stack cho đến khi tìm thấy một khối <code class="inline-code">try - catch</code> có kiểu tương thích.
                            <br>3. <strong>Trong quá trình dọn dẹp mỗi Stack Frame:</strong> Mọi đối tượng có thời gian lưu trữ tự động trên Stack đều <strong>BẮT BUỘC ĐƯỢC GỌI DESTRUCTOR</strong> theo đúng thứ tự LIFO.
                            <br>4. <strong>Bẫy Rò Rỉ Con Trỏ Thô (Raw Pointer Leak):</strong> Nếu trong hàm có cấp phát bộ nhớ heap (<code class="inline-code">int* p = new int[100];</code>) nhưng gặp ngoại lệ trước lệnh <code>delete</code>, thì con trỏ <code>p</code> bị hủy nhưng vùng nhớ heap KHÔNG ĐƯỢC GIẢI PHÓNG! Bắt buộc phải dùng mẫu thiết kế <strong>RAII</strong> (Smart Pointers <code class="inline-code">std::unique_ptr</code>).
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP8-Exception.pdf - Trang 9-13 & 27-29: Cơ chế ngoại lệ & Quản lý bộ nhớ]</span>
                </section>

                <!-- Theory Part 3 -->
                <section id="theory-matching" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">3. So Khớp Ngoại Lệ (Exception Matching) & Thứ Tự Khối catch</h3>
                    <p>
                        Các khối <code class="inline-code">catch</code> được kiểm tra tuần tự từ trên xuống dưới theo thứ tự khai báo.
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-filter"></i> Quy tắc vàng về Thứ tự Khối catch & Bắt theo Tham Chiếu</div>
                        <p class="text-zinc-700">
                            - <strong>Thứ tự từ Lớp Con đến Lớp Cha:</strong> Trong cây kế thừa ngoại lệ, khối bắt lớp dẫn xuất (Derived) bắt buộc phải đặt TRƯỚC khối bắt lớp cơ sở (Base). Nếu đặt Base lên trước, tính đa hình khiến Base bắt luôn mọi ngoại lệ con, khiến khối catch của lớp con trở thành Dead Code!
                            <br>- <strong>Khối bắt tất cả (<code class="inline-code">catch (...)</code>):</strong> Bắt mọi ngoại lệ (kể cả ngoại lệ không kế thừa từ <code>std::exception</code>), bắt buộc phải đặt ở vị trí CUỐI CÙNG trong chuỗi try-catch.
                            <br>- <strong>Bắt theo Tham Chiếu (<code class="inline-code">catch (const std::exception&amp; e)</code>):</strong> Tuyệt đối không bắt theo giá trị (by value) để tránh hiện tượng <strong>Object Slicing</strong> làm mất kiểu ngoại lệ con và mất thông điệp ảo đa hình của phương thức <code class="inline-code">e.what()</code>.
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP8-Exception.pdf - Trang 22-24: Exception Matching & Catch-all]</span>
                </section>

                <!-- Theory Part 4 -->
                <section id="theory-rethrow" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">4. Ném Tiếp Ngoại Lệ (Re-throwing Exception): throw; vs throw e;</h3>
                    <p>
                        Khi một hàm bắt được ngoại lệ để ghi log hoặc dọn dẹp một phần, sau đó muốn chuyển tiếp ngoại lệ đó lên tầng trên:
                    </p>
                    <ul class="list-disc pl-6 space-y-2 text-zinc-700">
                        <li><strong>Dùng <code class="inline-code">throw;</code> trần (Không có đối số):</strong> Ném tiếp chính đối tượng ngoại lệ ban đầu, bảo toàn nguyên vẹn tính đa hình động và kiểu dữ liệu gốc của lớp con.</li>
                        <li><strong>Dùng <code class="inline-code">throw e;</code>:</strong> Tạo ra một bản sao mới của biến <code>e</code>. Nếu <code>e</code> được bắt dưới dạng tham chiếu lớp cha, lệnh này sẽ tạo ra một đối tượng lớp cha mới và gây <strong>Object Slicing</strong>!</li>
                    </ul>
                    <span class="citation-badge">[Nguồn: OOP8-Exception.pdf - Trang 25-26: Re-Throwing Exception & Chuyển tiếp ngoại lệ]</span>
                </section>

                <!-- Theory Part 5 -->
                <section id="theory-noexcept" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">5. Từ Khóa C++11 noexcept & noexcept(expr)</h3>
                    <p>
                        C++11 chính thức phế truất (deprecated) đặc tả ngoại lệ kiểu cũ <code class="inline-code">throw(Type)</code> và thay thế bằng từ khóa <strong><code class="inline-code">noexcept</code></strong>.
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-shield-halved"></i> Bản chất của noexcept & Tối ưu hóa Compiler</div>
                        <p class="text-zinc-700">
                            - <strong>Cam kết không ném:</strong> Khai báo <code class="inline-code">void safeFunc() noexcept;</code> báo hiệu hàm này cam đoan 100% không để ngoại lệ thoát ra ngoài. Trình biên dịch có thể tối ưu hóa cắt bỏ toàn bộ mã máy dựng EHTable cho hàm này, giúp tăng tốc độ thực thi đáng kể.
                            <br>- <strong>Hình phạt nếu vi phạm:</strong> Nếu một hàm <code>noexcept</code> vẫn cố tình để ngoại lệ văng ra, hệ thống KHÔNG TÌM KIẾM khối catch mà lập tức gọi thẳng <code class="inline-code">std::terminate()</code> để tiêu diệt tiến trình ngay lập tức.
                            <br>- <strong>Toán tử <code class="inline-code">noexcept(expr)</code>:</strong> Kiểm tra tại thời điểm biên dịch xem một biểu thức có cam kết không ném ngoại lệ hay không (thường dùng trong Move Constructor của STL containers như <code>std::vector</code>).
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP8-Exception.pdf - Trang 36-42: Khai báo ngoại lệ & chuẩn C++11]</span>
                </section>

                <!-- Theory Part 6 -->
                <section id="theory-ctor-dtor" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">6. Ngoại Lệ Trong Constructor & Destructor</h3>
                    <p>
                        Hai thời điểm cực kỳ nhạy cảm trong vòng đời đối tượng đòi hỏi các quy tắc đặc biệt nghiêm ngặt:
                    </p>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-3 font-sans text-sm">
                        <div class="border border-zinc-200 p-4 rounded-lg bg-zinc-50">
                            <h4 class="font-bold text-[#991b1b] uppercase mb-2"><i class="fa-solid fa-hammer mr-1"></i> Ngoại Lệ Trong Constructor</h4>
                            <p class="text-xs text-zinc-600 font-serif leading-relaxed">
                                - Là cách chuẩn duy nhất để báo lỗi khi khởi tạo đối tượng thất bại.
                                <br>- <strong>Quy tắc vàng:</strong> Destructor của chính đối tượng đó sẽ <strong>KHÔNG BAO GIỜ ĐƯỢC GỌI</strong> vì đối tượng chưa được coi là đã hoàn thành xây dựng. Mọi con trỏ thô cấp phát trước lệnh <code>throw</code> sẽ bị rò rỉ nếu không dùng Smart Pointer.
                            </p>
                        </div>
                        <div class="border border-zinc-200 p-4 rounded-lg bg-zinc-50">
                            <h4 class="font-bold text-[#991b1b] uppercase mb-2"><i class="fa-solid fa-skull mr-1"></i> Ngoại Lệ Trong Destructor</h4>
                            <p class="text-xs text-zinc-600 font-serif leading-relaxed">
                                - <strong>CẤM TUYỆT ĐỐI</strong> để ngoại lệ văng ra khỏi Destructor!
                                <br>- Trong C++11, mọi Destructor mặc định là <code class="inline-code">noexcept(true)</code>. Nếu Destructor ném ngoại lệ trong khi hệ thống đang thực hiện Stack Unwinding cho một ngoại lệ khác, runtime gặp 2 ngoại lệ đồng thời và lập tức sập chương trình (<code class="inline-code">std::terminate</code>).
                            </p>
                        </div>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP8-Exception.pdf - Trang 43-44: Constructor, Destructor và ngoại lệ]</span>
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
                            50 Câu Trắc Nghiệm Code & Bẫy Ngoại Lệ C++11 Chuyên Sâu
                        </h2>
                        <p class="text-xs text-zinc-500 mt-1">
                            100% dựa trên các đoạn code thực tế: bẫy Stack Unwinding, noexcept, rò rỉ Ctor, Double Exception và chuẩn C++11
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

print("Writing template for Chapter 8...")

