# -*- coding: utf-8 -*-
"""
Script to generate the complete standalone HTML for Chapter 1:
'OOP1-C to C++-New.pdf' - C++11 Extension Deep Dive & 50 Code Traps Quiz.
Style: MOSTest5_2 (Minimalist Academic Brutalism, Red-800 Tor-sur-ton, Lora / Inter / JetBrains Mono)
"""

import json

html_template = """<!DOCTYPE html>
<html lang="vi" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chương 1: Mở Rộng C++ (C to C++11 Deep Dive) - MOSTest5_2</title>

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

        /* Prism Code Container */
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
                    <h1 class="font-bold text-lg leading-tight tracking-tight">Chương 1: Mở Rộng của C++ (C to C++11)</h1>
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
                        <a href="#theory-section" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">1. Tổng quan & Lịch sử</a>
                        <a href="#theory-casting" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">2. Hệ thống Ép kiểu Casts</a>
                        <a href="#theory-const-io" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">3. Hằng & Nhập Xuất Chuẩn</a>
                        <a href="#theory-reference" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">4. Biến Tham Chiếu (&)</a>
                        <a href="#theory-func-inline" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">5. Hàm Mặc Định & Inline</a>
                        <a href="#theory-pointer-mem" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">6. Con trỏ, Mảng & Cấp phát</a>
                        <a href="#theory-overloading" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">7. Đa năng hóa Hàm & Toán tử</a>
                    </nav>
                </div>

                <div class="pt-4 border-t border-zinc-200">
                    <div class="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-zinc-500 mb-3">
                        <i class="fa-solid fa-list-check text-[#991b1b]"></i> Quiz Bẫy Code (50 Câu)
                    </div>
                    <nav class="space-y-1 text-xs border-l-2 border-zinc-200 pl-3">
                        <a href="#q-group-1" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 1: Scope & Từ khóa (1-5)</a>
                        <a href="#q-group-2" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 2: Ép kiểu & const_cast (6-10)</a>
                        <a href="#q-group-3" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 3: Macro vs const (11-15)</a>
                        <a href="#q-group-4" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 4: Streams & iomanip (16-20)</a>
                        <a href="#q-group-5" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 5: Tham chiếu & Rvalue (21-27)</a>
                        <a href="#q-group-6" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 6: Default args & Inline (28-32)</a>
                        <a href="#q-group-7" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 7: Con trỏ hằng & Toán tử (33-36)</a>
                        <a href="#q-group-8" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 8: Con trỏ mảng 1D & 2D (37-41)</a>
                        <a href="#q-group-9" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 9: Con trỏ Hàm (42-45)</a>
                        <a href="#q-group-10" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 10: new/delete & Leaks (46-48)</a>
                        <a href="#q-group-11" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 11: Đa năng hóa (49-50)</a>
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
                        Chương 1: Mở Rộng của C++ (C to C++ Extension)
                    </h2>
                    <p class="text-sm text-zinc-500 mt-1">
                        Trích xuất toàn diện từ giáo trình <code class="inline-code">OOP1-C to C++-New.pdf</code> | Bổ sung cơ chế trình biên dịch & bộ nhớ RAM
                    </p>
                </div>

                <!-- Theory Part 1 -->
                <section class="theory-content space-y-4">
                    <h3 class="text-xl">1. Bối Cảnh Lịch Sử, Từ Khóa Mới & Toán Tử Định Phạm Vi (::)</h3>
                    <p>
                        Ngôn ngữ C được Dennis Ritchie phát minh năm 1972 tại Bell Labs. Đến năm 1983, Bjarne Stroustrup chính thức đổi tên "C with Classes" thành <strong>C++</strong> với triết lý không làm tổn hại đến hiệu năng (Zero-overhead principle) đồng thời trang bị khả năng lập trình hướng đối tượng, kiểm soát kiểu tĩnh mạnh mẽ và cơ chế trừu tượng hóa bậc cao.
                    </p>
                    <p>
                        Để mở rộng C, C++ bổ sung một loạt các từ khóa mới: <code class="inline-code">class</code>, <code class="inline-code">public</code>, <code class="inline-code">private</code>, <code class="inline-code">protected</code>, <code class="inline-code">virtual</code>, <code class="inline-code">friend</code>, <code class="inline-code">inline</code>, <code class="inline-code">new</code>, <code class="inline-code">delete</code>, <code class="inline-code">operator</code>, <code class="inline-code">template</code>, <code class="inline-code">this</code>, <code class="inline-code">throw</code>, <code class="inline-code">catch</code>, <code class="inline-code">bool</code>, <code class="inline-code">true</code>, <code class="inline-code">false</code>, và các toán tử ép kiểu mới.
                    </p>
                    
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-microchip"></i> Cơ chế dưới gầm máy: Khai báo biến linh hoạt & Toán tử ::</div>
                        <p class="text-zinc-700">
                            <strong>Khác biệt với chuẩn C89:</strong> Chuẩn C cũ bắt buộc toàn bộ biến cục bộ phải được khai báo tại đầu khối lệnh (block head). C++ loại bỏ rào cản này, cho phép khai báo biến ngay tại vị trí cần sử dụng (ngay trong điều kiện <code class="inline-code">if</code>, khởi tạo vòng lặp <code class="inline-code">for (int i = 0; ...)</code>). Điều này giúp trình biên dịch tối ưu hóa vòng đời (lifetime), thu hẹp phạm vi biến (scope), và giảm thiểu việc cấp phát ô nhớ stack khi chưa cần thiết.
                        </p>
                        <p class="text-zinc-700 mt-2">
                            <strong>Toán tử định phạm vi đơn nguyên (Unary Scope Resolution Operator <code class="inline-code">::</code>):</strong> Khi một biến cục bộ trùng tên (shadowing) với một biến toàn cục, trình biên dịch mặc định phân giải tên biến theo phạm vi hẹp nhất (inner-most scope). Toán tử <code class="inline-code">::x</code> chỉ định cho bộ phân tích ngữ nghĩa (semantic analyzer) bỏ qua symbol table cục bộ và tra cứu trực tiếp định danh <code class="inline-code">x</code> trong bảng ký hiệu phạm vi toàn cục (global namespace symbol table).
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP1-C to C++-New.pdf - Trang 2-7: Từ khóa, Chú thích, Biến & Toán tử định phạm vi]</span>
                </section>

                <!-- Theory Part 2 -->
                <section id="theory-casting" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">2. Hệ Thống Ép Kiểu: C-Style vs Modern C++ Casts</h3>
                    <p>
                        Trong C, ép kiểu sử dụng cú pháp <code class="inline-code">(new_type)expression</code>. C++ hỗ trợ thêm dạng cú pháp hàm <code class="inline-code">new_type(expression)</code>. Tuy nhiên, kiểu ép kiểu C-style này cực kỳ nguy hiểm vì nó có thể ép mọi con trỏ bất kể quan hệ kế thừa hay tính hằng, bỏ qua hoàn toàn sự kiểm tra của compiler. C++ giới thiệu 4 toán tử ép kiểu tường minh:
                    </p>
                    <ul class="list-disc pl-6 space-y-2 text-zinc-700">
                        <li><strong><code class="inline-code">static_cast&lt;T&gt;(v)</code>:</strong> Ép kiểu an toàn tại thời điểm biên dịch (compile-time). Dùng cho các kiểu cơ bản (int sang double), con trỏ trong cây kế thừa (upcast/downcast không kiểm tra runtime), hoặc gọi hàm tạo chuyển đổi tường minh.</li>
                        <li><strong><code class="inline-code">const_cast&lt;T&gt;(v)</code>:</strong> Thêm hoặc loại bỏ thuộc tính <code class="inline-code">const</code> hoặc <code class="inline-code">volatile</code> của con trỏ hoặc tham chiếu. Đây là toán tử duy nhất trong C++ có thể thay đổi tính hằng. Nếu ô nhớ gốc thực chất là hằng số nằm trong phân vùng nhớ Read-Only (RODATA) mà bị ghi đè thông qua <code class="inline-code">const_cast</code>, chương trình sẽ rơi vào <strong>Undefined Behavior (UB)</strong> (thường dẫn đến lỗi Access Violation / SIGSEGV).</li>
                        <li><strong><code class="inline-code">reinterpret_cast&lt;T&gt;(v)</code>:</strong> Ép kiểu thô ở mức bit (low-level reinterpretation). Bắt trình biên dịch diễn giải mẫu nhị phân của ô nhớ sang một kiểu hoàn toàn khác (ví dụ: con trỏ sang số nguyên hoặc giữa các con trỏ kiểu không liên quan). Không sinh mã máy chuyển đổi giá trị.</li>
                        <li><strong><code class="inline-code">dynamic_cast&lt;T&gt;(v)</code>:</strong> Ép kiểu an toàn trong cây kế thừa tại thời điểm thực thi (run-time) dựa trên bảng RTTI (Run-Time Type Information). Yêu cầu lớp cơ sở phải có ít nhất 1 hàm ảo (<code class="inline-code">virtual</code>).</li>
                    </ul>
                    <span class="citation-badge">[Nguồn: OOP1-C to C++-New.pdf - Trang 8 & 35: Casting & const_cast]</span>
                </section>

                <!-- Theory Part 3 -->
                <section id="theory-const-io" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">3. Hằng Số (#define vs const) & Thư Viện I/O Stream (<iostream>, <iomanip>)</h3>
                    <p>
                        Trong C, hằng số thường được định nghĩa bằng macro tiền xử lý <code class="inline-code">#define PI 3.14159</code>. Trong C++, chuẩn khuyến nghị sử dụng từ khóa <code class="inline-code">const</code>: <code class="inline-code">const double PI = 3.14159;</code> hoặc <code class="inline-code">double const PI = 3.14159;</code>.
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-memory"></i> Cơ chế biên dịch: Symbol Table & Internal Linkage của const</div>
                        <p class="text-zinc-700">
                            <strong>1. #define vs const:</strong> Bộ tiền xử lý (preprocessor) chỉ thực hiện thay thế chuỗi văn bản (textual substitution) một cách mù quáng, không có kiểm tra kiểu dữ liệu, không có phạm vi biến (scope), và không xuất hiện trong bảng ký hiệu của debugger. Ngược lại, biến <code class="inline-code">const</code> trong C++ được quản lý chặt chẽ theo hệ thống kiểu tĩnh và phạm vi khối lệnh.
                        </p>
                        <p class="text-zinc-700 mt-2">
                            <strong>2. Internal Linkage:</strong> Trong C, biến <code class="inline-code">const</code> ở phạm vi toàn cục mặc định có External Linkage. Nhưng trong C++, biến <code class="inline-code">const</code> toàn cục mặc định có <strong>Internal Linkage</strong> (tương đương với việc có từ khóa <code class="inline-code">static</code>). Trình biên dịch có thể thực hiện gập hằng số (Constant Folding) và không cần cấp phát ô nhớ trên RAM trừ khi ta cố tình lấy địa chỉ của nó (<code class="inline-code">&x</code>).
                        </p>
                        <p class="text-zinc-700 mt-2">
                            <strong>3. Thư viện <iomanip>:</strong> Khác với <code class="inline-code">printf</code>/<code class="inline-code">scanf</code> của C, C++ sử dụng các đối tượng luồng <code class="inline-code">std::cin</code>, <code class="inline-code">std::cout</code>, <code class="inline-code">std::cerr</code>. Các hàm định dạng luồng chia làm hai loại:
                            <br>- <em>Sticky Manipulators (Duy trì trạng thái):</em> <code class="inline-code">setprecision(p)</code>, <code class="inline-code">fixed</code>, <code class="inline-code">showpoint</code> duy trì hiệu lực cho toàn bộ các phép xuất tiếp theo cho đến khi bị ghi đè.
                            <br>- <em>Non-sticky Manipulators (Một lần):</em> <code class="inline-code">setw(k)</code> chỉ áp dụng hiệu lực cho duy nhất một giá trị in ra ngay sau nó, sau đó độ rộng trường tự động reset về 0.
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP1-C to C++-New.pdf - Trang 9-14: Khai báo hằng, cout, cin, setw, setiosflags]</span>
                </section>

                <!-- Theory Part 4 -->
                <section id="theory-reference" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">4. Bản Chất Dưới Gầm Máy Của Biến Tham Chiếu (References &)</h3>
                    <p>
                        Biến tham chiếu (Reference) là một bí danh (alias) đại diện cho một ô nhớ đã tồn tại. Cú pháp: <code class="inline-code">Type &ref = var;</code>.
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-diagram-project"></i> Cơ chế Trình biên dịch hiện thực Reference</div>
                        <ul class="list-disc pl-5 space-y-1.5 text-zinc-700">
                            <li><strong>Bản chất con trỏ hằng (Const Pointer):</strong> Ở mức mã máy assembly, trình biên dịch thực tế cài đặt biến tham chiếu dưới dạng một <strong>con trỏ hằng tự động giải con trỏ</strong> (<code class="inline-code">Type * const p</code>). Khi truy xuất <code class="inline-code">ref</code>, CPU tự động dereference <code class="inline-code">*p</code>.</li>
                            <li><strong>Không thể Re-bind:</strong> Tham chiếu bắt buộc phải được khởi tạo ngay khi khai báo. Khi đã liên kết với một ô nhớ, tham chiếu không bao giờ có thể liên kết sang ô nhớ khác. Phép gán <code class="inline-code">ref = other;</code> chỉ đơn thuần là gán giá trị của <code class="inline-code">other</code> vào ô nhớ mà <code class="inline-code">ref</code> đang trỏ tới.</li>
                            <li><strong>Không có mảng tham chiếu:</strong> Mảng trong C++ đòi hỏi các phần tử phải có ô nhớ độc lập liên tiếp nhau. Do tham chiếu không phải là một đối tượng có địa chỉ độc lập (lấy địa chỉ tham chiếu ra địa chỉ biến gốc), chuẩn C++ cấm hoàn toàn khai báo mảng tham chiếu (<code class="inline-code">int& arr[5];</code> là lỗi biên dịch).</li>
                            <li><strong>Hằng tham chiếu & Kéo dài vòng đời (Lifetime Extension):</strong> Tham chiếu không hằng (<code class="inline-code">int&</code>) không thể bind vào rvalue (giá trị tạm thời như hằng số <code class="inline-code">5</code> hoặc kết quả biểu thức <code class="inline-code">a + b</code>). Tuy nhiên, <strong>Hằng tham chiếu (<code class="inline-code">const int&</code>)</strong> có khả năng bind vào rvalue. Khi đó, trình biên dịch tạo ra một đối tượng tạm thời trên stack và kéo dài vòng đời của nó bằng với vòng đời của hằng tham chiếu!</li>
                            <li><strong>Bẫy Trả Về Tham Chiếu (Dangling Reference):</strong> Một hàm trả về tham chiếu (<code class="inline-code">Type& func()</code>) tuyệt đối không được trả về biến cục bộ tự động trên stack. Khi hàm kết thúc, stack frame bị hủy, vùng nhớ bị giải phóng, tham chiếu trả về trở thành con trỏ rác (Dangling reference). Biến trả về phải là biến toàn cục, biến <code class="inline-code">static</code>, hoặc thuộc tính của đối tượng tồn tại lâu hơn lời gọi hàm.</li>
                        </ul>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP1-C to C++-New.pdf - Trang 15-26: Biến tham chiếu, Hằng tham chiếu, Hàm trả về tham chiếu]</span>
                </section>

                <!-- Theory Part 5 -->
                <section id="theory-func-inline" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">5. Tham Số Mặc Định (Default Arguments) & Hàm Nội Tuyến (Inline)</h3>
                    <p>
                        C++ cho phép gán giá trị mặc định cho tham số hàm: <code class="inline-code">void display(int x, int y = 10, int z = 20);</code>.
                    </p>
                    <ul class="list-disc pl-6 space-y-2 text-zinc-700">
                        <li><strong>Quy tắc từ phải qua trái:</strong> Các đối số mặc định bắt buộc phải nằm liên tục ở cuối danh sách tham số (tính từ phải qua trái). Không được phép khai báo tham số không mặc định nằm sau tham số mặc định (ví dụ: <code class="inline-code">void f(int x = 1, int y);</code> là lỗi biên dịch).</li>
                        <li><strong>Vị trí khai báo:</strong> Giá trị mặc định chỉ được phép khai báo một lần duy nhất, thường là trong nguyên mẫu hàm (function prototype trong header file). Tuyệt đối không lặp lại giá trị mặc định trong định nghĩa hàm (function definition) nếu đã khai báo ở prototype.</li>
                    </ul>

                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-bolt"></i> Cơ chế Dưới Gầm Máy của Hàm Inline</div>
                        <p class="text-zinc-700">
                            <strong>Chi phí gọi hàm thông thường:</strong> Khi gọi một hàm chuẩn, CPU phải thực hiện các thủ tục: đẩy thanh ghi và tham số lên Stack (push stack), nhảy lệnh con trỏ chỉ lệnh <code class="inline-code">EIP/RIP</code> sang địa chỉ hàm, khởi tạo Stack Frame, thực thi thân hàm, dọn dẹp frame (pop stack) và nhảy ngược trở về địa chỉ gọi (<code class="inline-code">RET</code>). Đối với các hàm cực ngắn (1-2 dòng) được gọi hàng triệu lần trong vòng lặp, overhead này chiếm tỷ trọng thời gian đáng kể.
                        </p>
                        <p class="text-zinc-700 mt-2">
                            <strong>Hàm <code class="inline-code">inline</code>:</strong> Báo hiệu cho trình biên dịch thay thế trực tiếp mã máy của thân hàm ngay tại vị trí gọi hàm (Code expansion). Từ khóa <code class="inline-code">inline</code> chỉ là một <em>gợi ý (compiler hint)</em>, trình biên dịch có quyền từ chối inline nếu hàm chứa vòng lặp phức tạp, đệ quy, hoặc kích thước quá lớn để tránh hiện tượng phình to kích thước file thực thi (<strong>Code Bloat</strong>) gây tràn Instruction Cache (I-Cache).
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP1-C to C++-New.pdf - Trang 22-28: Đối số mặc định, Hàm nội tuyến inline]</span>
                </section>

                <!-- Theory Part 6 -->
                <section id="theory-pointer-mem" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">6. Con Trỏ, Mảng Đa Chiều, Con Trỏ Hàm & Cấp Phát Động</h3>
                    <p>
                        Con trỏ lưu địa chỉ ô nhớ. Phân biệt rõ ràng 3 vị trí của từ khóa <code class="inline-code">const</code>:
                    </p>
                    <div class="overflow-x-auto my-3">
                        <table class="w-full text-sm border-collapse border border-zinc-300">
                            <thead class="bg-zinc-100 font-sans">
                                <tr>
                                    <th class="border border-zinc-300 p-2 text-left">Cú pháp</th>
                                    <th class="border border-zinc-300 p-2 text-left">Tên gọi</th>
                                    <th class="border border-zinc-300 p-2 text-center">Thay đổi *p (giá trị)</th>
                                    <th class="border border-zinc-300 p-2 text-center">Thay đổi p (địa chỉ)</th>
                                </tr>
                            </thead>
                            <tbody class="font-mono text-xs">
                                <tr>
                                    <td class="border p-2">const int *p;</td>
                                    <td class="border p-2 font-sans">Con trỏ tới hằng (Pointer to const)</td>
                                    <td class="border p-2 text-center text-red-600 font-bold">KHÔNG</td>
                                    <td class="border p-2 text-center text-green-600 font-bold">CÓ</td>
                                </tr>
                                <tr>
                                    <td class="border p-2">int* const p;</td>
                                    <td class="border p-2 font-sans">Hằng con trỏ (Const pointer)</td>
                                    <td class="border p-2 text-center text-green-600 font-bold">CÓ</td>
                                    <td class="border p-2 text-center text-red-600 font-bold">KHÔNG</td>
                                </tr>
                                <tr>
                                    <td class="border p-2">const int* const p;</td>
                                    <td class="border p-2 font-sans">Hằng con trỏ tới hằng</td>
                                    <td class="border p-2 text-center text-red-600 font-bold">KHÔNG</td>
                                    <td class="border p-2 text-center text-red-600 font-bold">KHÔNG</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-cubes-stacked"></i> Mảng 2 Chiều & Bố Cục Bộ Nhớ RAM</div>
                        <p class="text-zinc-700">
                            Cho khai báo mảng 2 chiều tĩnh <code class="inline-code">int A[3][4];</code>:
                            <br>- Về mặt vật lý trên RAM, toàn bộ 12 phần tử được xếp liên tục trong bộ nhớ theo thứ tự hàng ưu tiên (Row-Major Order).
                            <br>- Kiểu dữ liệu của <code class="inline-code">A</code> khi decay là con trỏ trỏ tới mảng 4 phần tử: <code class="inline-code">int (*)[4]</code>.
                            <br>- Biểu thức địa chỉ: <code class="inline-code">&A[i][j] == (*(A + i)) + j</code>.
                            <br>- Biểu thức giá trị: <code class="inline-code">A[i][j] == *(*(A + i) + j)</code>.
                            <br>- Khi tăng <code class="inline-code">A + 1</code>, địa chỉ nhảy một đoạn bằng <code class="inline-code">4 * sizeof(int) = 16</code> bytes. Khi tăng <code class="inline-code">*A + 1</code>, địa chỉ chỉ nhảy <code class="inline-code">1 * sizeof(int) = 4</code> bytes.
                        </p>
                        <p class="text-zinc-700 mt-2">
                            <strong>Cấp Phát Động (Heap Memory Management):</strong>
                            <br>- <code class="inline-code">new</code> vs <code class="inline-code">malloc</code>: <code class="inline-code">new</code> tự động tính toán kích thước kiểu, gọi Constructor của lớp, và ném ngoại lệ <code class="inline-code">std::bad_alloc</code> nếu hết bộ nhớ (thay vì trả về <code class="inline-code">NULL</code> như <code class="inline-code">malloc</code>).
                            <br>- <code class="inline-code">delete[]</code> vs <code class="inline-code">delete</code>: Khi cấp phát mảng bằng <code class="inline-code">new T[N]</code>, bộ quản lý heap ghi thêm một giá trị header ẩn (gọi là <em>cookie / overhead metadata</em>) ngay trước địa chỉ con trỏ trả về để lưu kích thước <code class="inline-code">N</code>. Toán tử <code class="inline-code">delete[]</code> đọc cookie này để gọi đúng <code class="inline-code">N</code> lần Destructor rồi giải phóng toàn bộ block. Dùng <code class="inline-code">delete</code> trần cho con trỏ mảng dẫn đến Undefined Behavior và rò rỉ bộ nhớ (Memory Leak).
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP1-C to C++-New.pdf - Trang 29-57: Con trỏ, Mảng 1D, 2D, Con trỏ hàm, Cấp phát động, Rò rỉ bộ nhớ]</span>
                </section>

                <!-- Theory Part 7 -->
                <section id="theory-overloading" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">7. Cơ Chế Đa Năng Hóa (Overloading) Hàm & Toán Tử</h3>
                    <p>
                        Trong ngôn ngữ C, mỗi hàm phải có một tên duy nhất (ví dụ hàm lấy trị tuyệt đối phải tách thành <code class="inline-code">abs</code>, <code class="inline-code">labs</code>, <code class="inline-code">fabs</code>). Trong C++, kỹ thuật <strong>Function Overloading</strong> cho phép nhiều hàm có cùng tên trong cùng một phạm vi scope.
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-gears"></i> Name Mangling & Giới hạn Toán Tử</div>
                        <p class="text-zinc-700">
                            <strong>Name Mangling:</strong> Trình biên dịch C++ mã hóa tên hàm và danh sách kiểu tham số thành một chuỗi duy nhất trong bảng ký hiệu (ví dụ <code class="inline-code">_Z5MyAbsi</code> cho <code class="inline-code">MyAbs(int)</code>, <code class="inline-code">_Z5MyAbsd</code> cho <code class="inline-code">MyAbs(double)</code>). Do đó:
                            <br>- Việc đa năng hóa hàm <strong>CHỈ</strong> dựa vào số lượng, thứ tự và kiểu của tham số.
                            <br>- <strong>KHÔNG THỂ</strong> đa năng hóa nếu hai hàm chỉ khác nhau về kiểu trả về (Return Type)!
                        </p>
                        <p class="text-zinc-700 mt-2">
                            <strong>Giới hạn của Đa năng hóa toán tử (Operator Overloading):</strong>
                            <br>1. Không thể tự tạo toán tử mới (như <code class="inline-code">**</code> hoặc <code class="inline-code">&lt;&gt;</code>).
                            <br>2. Không thay đổi được độ ưu tiên và số ngôi (arity) của toán tử gốc.
                            <br>3. <strong>5 toán tử KHÔNG ĐƯỢC PHÉP overload trong C++:</strong>
                            <br>&nbsp;&nbsp;&nbsp;&bull; Toán tử định phạm vi: <code class="inline-code">::</code>
                            <br>&nbsp;&nbsp;&nbsp;&bull; Toán tử truy cập thành viên trực tiếp: <code class="inline-code">.</code>
                            <br>&nbsp;&nbsp;&nbsp;&bull; Toán tử con trỏ tới thành viên: <code class="inline-code">.*</code>
                            <br>&nbsp;&nbsp;&nbsp;&bull; Toán tử điều kiện ba ngôi: <code class="inline-code">?:</code>
                            <br>&nbsp;&nbsp;&nbsp;&bull; Toán tử kích thước và kiểu: <code class="inline-code">sizeof</code>, <code class="inline-code">typeid</code>
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP1-C to C++-New.pdf - Trang 58-64: Đa năng hóa hàm & Đa năng hóa toán tử]</span>
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
                            50 Câu Trắc Nghiệm Code & Bẫy C++11 Chuyên Sâu
                        </h2>
                        <p class="text-xs text-zinc-500 mt-1">
                            100% dựa trên các đoạn code thực tế, bẫy rò rỉ bộ nhớ, UB, con trỏ và chuẩn C++11
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

print("Writing generator script...")

