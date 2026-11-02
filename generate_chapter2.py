# -*- coding: utf-8 -*-
"""
Script to generate the complete standalone HTML for Chapter 2:
'OOP2-introduction_new.pdf' - Khái Niệm Lập Trình Hướng Đối Tượng (OOP Concepts & Paradigms)
Style: MOSTest5_2 (Minimalist Academic Brutalism, Red-800 Tor-sur-ton, Lora / Inter / JetBrains Mono)
"""

import json

html_template = """<!DOCTYPE html>
<html lang="vi" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chương 2: Khái Niệm Lập Trình Hướng Đối Tượng (OOP Deep Dive) - MOSTest5_2</title>

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
                    OOP
                </div>
                <div>
                    <h1 class="font-bold text-lg leading-tight tracking-tight">Chương 2: Khái Niệm Lập Trình Hướng Đối Tượng</h1>
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
                        <a href="#theory-section" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">1. Tiến trình tiến hóa phương pháp</a>
                        <a href="#theory-paradigm-shift" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">2. Tiếp cận Hướng Đối Tượng</a>
                        <a href="#theory-object-class" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">3. Đối tượng & Lớp (Identity/State)</a>
                        <a href="#theory-message-passing" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">4. Thông điệp & Phương thức</a>
                        <a href="#theory-four-pillars" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">5. 4 Trụ Cột của OOP</a>
                    </nav>
                </div>

                <div class="pt-4 border-t border-zinc-200">
                    <div class="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-zinc-500 mb-3">
                        <i class="fa-solid fa-list-check text-[#991b1b]"></i> Quiz Bẫy Code (50 Câu)
                    </div>
                    <nav class="space-y-1 text-xs border-l-2 border-zinc-200 pl-3">
                        <a href="#q-group-1" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 1: Tiến hóa & Toàn vẹn (1-5)</a>
                        <a href="#q-group-2" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 2: Đối tượng & Bố cục RAM (6-12)</a>
                        <a href="#q-group-3" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 3: Đóng gói & Information Hiding (13-18)</a>
                        <a href="#q-group-4" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 4: Lớp & Vòng đời Thể hiện (19-25)</a>
                        <a href="#q-group-5" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 5: Thông điệp & Con trỏ this (26-30)</a>
                        <a href="#q-group-6" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 6: Kế thừa & IS-A vs HAS-A (31-38)</a>
                        <a href="#q-group-7" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 7: Đa hình & Virtual Table (39-46)</a>
                        <a href="#q-group-8" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 8: Kiến trúc & Tổng hợp (47-50)</a>
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
                        Chuyên khảo Lý thuyết OOP C++11 & Bản đồ Kiến trúc
                    </div>
                    <h2 class="text-3xl font-extrabold text-zinc-900 tracking-tight font-sans">
                        Chương 2: Khái Niệm Lập Trình Hướng Đối Tượng
                    </h2>
                    <p class="text-sm text-zinc-500 mt-1">
                        Trích xuất toàn diện từ giáo trình <code class="inline-code">OOP2-introduction_new.pdf</code> | Phân tích sâu sắc cơ chế hướng đối tượng và kiến trúc bộ nhớ
                    </p>
                </div>

                <!-- Theory Part 1 -->
                <section class="theory-content space-y-4">
                    <h3 class="text-xl">1. Tiến Trình Tiến Hóa Của Các Phương Pháp Lập Trình</h3>
                    <p>
                        Lịch sử phát triển phần mềm là một chuỗi nỗ lực không ngừng để giải quyết "Cuộc khủng hoảng phần mềm" (Software Crisis) — khi độ phức tạp của bài toán vượt quá khả năng kiểm soát của con người.
                    </p>
                    <ul class="list-disc pl-6 space-y-2 text-zinc-700">
                        <li><strong>Lập trình không có cấu trúc (Non-structured Programming):</strong> Xuất hiện đầu tiên trong thời kỳ sơ khai (Assembly, Fortran/BASIC ban đầu). Toàn bộ chương trình sử dụng chung một không gian biến tổng thể (Global variables). Dòng điều khiển dựa vào lệnh nhảy không điều kiện <code class="inline-code">GOTO</code> hoặc <code class="inline-code">GOSUB</code>. Kết quả tạo nên <em>Mã Spaghetti</em> (Spaghetti Code) rối rắm, cực kỳ khó đọc, không thể tái sử dụng và chi phí bảo trì khổng lồ.</li>
                        <li><strong>Lập trình có cấu trúc / hướng thủ tục (Structured / Procedural Programming):</strong> Xuất hiện với Pascal, C. Chương trình được module hóa thành các hàm/thủ tục độc lập. Công thức kinh điển của Niklaus Wirth: <code class="inline-code">Chương trình = Cấu trúc dữ liệu + Giải thuật</code>.</li>
                    </ul>

                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-triangle-exclamation"></i> Cơ chế dưới gầm máy: Hạn chế chí tử của Lập trình hướng thủ tục</div>
                        <p class="text-zinc-700">
                            <strong>1. Sự tách rời giữa Dữ liệu và Hành vi:</strong> Trong C, dữ liệu nằm trong <code class="inline-code">struct</code> hoàn toàn thụ động và phơi bày công khai, trong khi các hàm xử lý lại nằm rải rác bên ngoài. Khi một cấu trúc dữ liệu bị sửa đổi (ví dụ đổi <code class="inline-code">int day, month, year;</code> sang <code class="inline-code">time_t timestamp;</code>), hàng trăm hàm xử lý liên quan trên toàn bộ dự án sẽ bị gãy và phải viết lại toàn bộ.
                        </p>
                        <p class="text-zinc-700 mt-2">
                            <strong>2. Không bảo vệ được tính toàn vẹn (Data Invariants):</strong> Bất kỳ đoạn mã nào trong dự án cũng có thể gán <code class="inline-code">date.day = 32; date.month = 13;</code> mà không có bất kỳ cơ chế kiểm soát nào ngăn chặn tại thời điểm gán.
                        </p>
                        <p class="text-zinc-700 mt-2">
                            <strong>3. Không tự động khởi tạo hay giải phóng tài nguyên:</strong> Biến trong C có thể bị sử dụng trước khi khởi tạo (chứa rác) hoặc bị rò rỉ vùng nhớ heap do lập trình viên quên gọi hàm giải phóng thủ công.
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP2-introduction_new.pdf - Trang 3-12: Lập trình không cấu trúc vs Hướng thủ tục]</span>
                </section>

                <!-- Theory Part 2 -->
                <section id="theory-paradigm-shift" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">2. Tiếp Cận Hướng Đối Tượng: Đóng Gói & Tái Sử Dụng Mã Nguồn</h3>
                    <p>
                        Tiếp cận hướng đối tượng (Object-Oriented Approach) ra đời để khắc phục triệt để 2 vấn đề lớn:
                    </p>
                    <ul class="list-disc pl-6 space-y-2 text-zinc-700">
                        <li><strong>Đóng gói (Encapsulation):</strong> Gom chung dữ liệu và mã xử lý vào trong một thực thể thống nhất gọi là Đối tượng. Che giấu cấu trúc dữ liệu bên trong (Data Hiding), chỉ cho phép bên ngoài tương tác thông qua một giao diện xác định (Public Interface). Nhờ đó, việc thay đổi cấu trúc bên trong hoàn toàn không làm ảnh hưởng đến mã nguồn của các module khác.</li>
                        <li><strong>Tái sử dụng mã nguồn (Code Reusability):</strong> Thông qua cơ chế Kế thừa (Inheritance) và Đa hình (Polymorphism), các lớp mới có thể tái sử dụng các thuộc tính và phương thức đã có mà không cần sao chép mã nguồn thô.</li>
                    </ul>
                    <span class="citation-badge">[Nguồn: OOP2-introduction_new.pdf - Trang 13-16: Tiếp cận hướng đối tượng & Ưu điểm]</span>
                </section>

                <!-- Theory Part 3 -->
                <section id="theory-object-class" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">3. Đối Tượng (Object) & Lớp (Class): Định Danh, Trạng Thái, Hành Vi</h3>
                    <p>
                        Hệ thống hướng đối tượng xem chương trình là một tập hợp các đối tượng cộng tác với nhau.
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-cube"></i> Ba yếu tố cấu thành một Đối tượng (Object) trong RAM</div>
                        <ul class="list-disc pl-5 space-y-2 text-zinc-700">
                            <li><strong>1. Định danh (Identity):</strong> Yếu tố phân biệt đối tượng này với tất cả các đối tượng khác trong toàn hệ thống. Trong C++, định danh chính là <strong>địa chỉ ô nhớ duy nhất</strong> của đối tượng (<code class="inline-code">&object</code> hoặc con trỏ <code class="inline-code">this</code>). Hai đối tượng có thể có toàn bộ giá trị thuộc tính giống hệt nhau, nhưng chúng vẫn là 2 thực thể độc lập vì chúng chiếm 2 ô nhớ khác nhau.</li>
                            <li><strong>2. Trạng thái (State / Attributes):</strong> Tập hợp các giá trị của các thuộc tính (biến thành viên dữ liệu) nội tại của đối tượng tại một thời điểm nhất định.</li>
                            <li><strong>3. Hành vi (Behavior / Methods):</strong> Tập hợp các thao tác, hành động mà đối tượng có thể thực hiện hoặc phản hồi khi nhận được thông điệp từ bên ngoài.</li>
                        </ul>
                        <p class="text-zinc-700 mt-2">
                            <strong>Khái niệm Lớp (Class):</strong> Lớp là một mô tả trừu tượng (khuôn mẫu / blueprint) xác định cấu trúc dữ liệu và hành vi chung cho một tập hợp các đối tượng cùng loại. Trong C++, Class là một <em>Kiểu dữ liệu do người dùng định nghĩa (User-defined Type)</em>, còn Object là một <em>Biến thể hiện cụ thể (Instance)</em> của kiểu dữ liệu đó.
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP2-introduction_new.pdf - Trang 22-34: Định nghĩa Đối tượng và Lớp]</span>
                </section>

                <!-- Theory Part 4 -->
                <section id="theory-message-passing" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">4. Cơ Chế Truyền Thông Điệp (Message Passing) & Con Trỏ this</h3>
                    <p>
                        Trong mô hình OOP lý thuyết, các đối tượng tương tác bằng cách <strong>gửi thông điệp</strong> (Message Passing). Thông điệp gồm 3 thành phần: Đối tượng nhận (Receiver), Tên hành động cần thực thi (Method Selector), và Các tham số đi kèm (Arguments).
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-microchip"></i> Hiện thực mức mã máy: Lời gọi hàm thành viên & Con trỏ this</div>
                        <p class="text-zinc-700">
                            Trong C++, việc gửi thông điệp <code class="inline-code">obj.deposit(500);</code> thực chất được trình biên dịch biên dịch thành một lời gọi hàm thông thường: <code class="inline-code">Account_deposit(&obj, 500);</code>.
                            <br>- Trình biên dịch ngầm chèn thêm một tham số đầu tiên bí mật: <strong>con trỏ hằng <code class="inline-code">this</code></strong> chứa địa chỉ ô nhớ của đối tượng gọi hàm.
                            <br>- Trên kiến trúc x86 với quy ước gọi <code class="inline-code">__thiscall</code>, con trỏ <code class="inline-code">this</code> được nạp trực tiếp vào thanh ghi <code class="inline-code">ECX</code> để tối ưu tốc độ truy xuất thuộc tính của đối tượng.
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP2-introduction_new.pdf - Trang 35: Thông điệp (Message)]</span>
                </section>

                <!-- Theory Part 5 -->
                <section id="theory-four-pillars" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">5. Bốn Trụ Cột Nền Tảng Của Lập Trình Hướng Đối Tượng</h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-4">
                        <div class="border border-zinc-200 p-4 rounded-lg bg-zinc-50 font-sans">
                            <h4 class="text-sm font-bold text-[#991b1b] uppercase flex items-center gap-2 mb-2">
                                <i class="fa-solid fa-shield-halved"></i> 1. Tính Đóng Gói (Encapsulation)
                            </h4>
                            <p class="text-xs text-zinc-600 leading-relaxed font-serif">
                                Cơ chế giấu nhẹm chi tiết cài đặt và cấu trúc dữ liệu bên trong đối tượng (Information Hiding). Các trường dữ liệu được bảo vệ bằng phạm vi <code class="inline-code">private</code>, việc truy xuất và chỉnh sửa bắt buộc phải thông qua các phương thức giao diện <code class="inline-code">public</code> đã được kiểm duyệt điều kiện toàn vẹn.
                            </p>
                        </div>
                        <div class="border border-zinc-200 p-4 rounded-lg bg-zinc-50 font-sans">
                            <h4 class="text-sm font-bold text-[#991b1b] uppercase flex items-center gap-2 mb-2">
                                <i class="fa-solid fa-sitemap"></i> 2. Tính Kế Thừa (Inheritance)
                            </h4>
                            <p class="text-xs text-zinc-600 leading-relaxed font-serif">
                                Mối quan hệ phân cấp biểu thị liên kết IS-A giữa các lớp. Lớp con (Derived class) tự động thừa hưởng thuộc tính và phương thức của lớp cha (Base class), cho phép tái sử dụng mã nguồn và thiết lập nền tảng đa hình.
                            </p>
                        </div>
                        <div class="border border-zinc-200 p-4 rounded-lg bg-zinc-50 font-sans">
                            <h4 class="text-sm font-bold text-[#991b1b] uppercase flex items-center gap-2 mb-2">
                                <i class="fa-solid fa-shapes"></i> 3. Tính Đa Hình (Polymorphism)
                            </h4>
                            <p class="text-xs text-zinc-600 leading-relaxed font-serif">
                                Khả năng các đối tượng thuộc các kiểu lớp khác nhau có thể phản hồi theo các cách riêng biệt trước cùng một thông điệp. Hiện thực thông qua hàm ảo (<code class="inline-code">virtual</code>) và cơ chế liên kết động tại runtime (Dynamic Binding qua VTable).
                            </p>
                        </div>
                        <div class="border border-zinc-200 p-4 rounded-lg bg-zinc-50 font-sans">
                            <h4 class="text-sm font-bold text-[#991b1b] uppercase flex items-center gap-2 mb-2">
                                <i class="fa-solid fa-filter"></i> 4. Tính Trừu Tượng (Abstraction)
                            </h4>
                            <p class="text-xs text-zinc-600 leading-relaxed font-serif">
                                Tập trung vào các đặc tính cốt lõi của bài toán, loại bỏ các chi tiết kỹ thuật phức tạp hoặc không cần thiết. Hiện thực trong C++ thông qua Lớp trừu tượng (Abstract Class) chứa các hàm thuần ảo (Pure Virtual Function).
                            </p>
                        </div>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP2-introduction_new.pdf - Trang 36-48: Đóng gói, Kế thừa, Đa hình, Trừu tượng]</span>
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
                            50 Câu Trắc Nghiệm Code & Bẫy OOP C++11 Chuyên Sâu
                        </h2>
                        <p class="text-xs text-zinc-500 mt-1">
                            100% dựa trên các đoạn code thực tế: bẫy bố cục bộ nhớ, con trỏ this, phá vỡ đóng gói, VTable và chuẩn C++11
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

print("Writing template for Chapter 2...")

