# -*- coding: utf-8 -*-
"""
Script to generate the complete standalone HTML for Chapter 4:
'OOP4-OperatorOverloading_new.pdf' - Đa Năng Hóa Toán Tử (Operator Overloading Deep Dive)
Style: MOSTest5_2 (Minimalist Academic Brutalism, Red-800 Tor-sur-ton, Lora / Inter / JetBrains Mono)
"""

import json

html_template = """<!DOCTYPE html>
<html lang="vi" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chương 4: Đa Năng Hóa Toán Tử (Operator Overloading) - MOSTest5_2</title>

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
                    <h1 class="font-bold text-lg leading-tight tracking-tight">Chương 4: Đa Năng Hóa Toán Tử (Operator Overloading)</h1>
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
                        <a href="#theory-section" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">1. Bản chất & Giới hạn Toán tử</a>
                        <a href="#theory-member-vs-friend" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">2. Member vs Friend Function</a>
                        <a href="#theory-stream-io" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">3. Toán tử Nhập/Xuất <<, >></a>
                        <a href="#theory-subscript-functor" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">4. Chỉ số [] & Functor ()</a>
                        <a href="#theory-conversion" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">5. Chuyển đổi Kiểu & explicit</a>
                        <a href="#theory-assignment" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">6. Toán tử Gán = & Tự Gán</a>
                        <a href="#theory-inc-dec" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">7. Tiền tố ++x vs Hậu tố x++</a>
                        <a href="#theory-new-delete" class="block py-1 text-zinc-700 hover:text-[#991b1b] font-medium transition">8. Quản lý Heap new & delete</a>
                    </nav>
                </div>

                <div class="pt-4 border-t border-zinc-200">
                    <div class="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-zinc-500 mb-3">
                        <i class="fa-solid fa-list-check text-[#991b1b]"></i> Quiz Bẫy Code (50 Câu)
                    </div>
                    <nav class="space-y-1 text-xs border-l-2 border-zinc-200 pl-3">
                        <a href="#q-group-1" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 1: Giới hạn & Cốt lõi (1-6)</a>
                        <a href="#q-group-2" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 2: Member vs Friend (7-12)</a>
                        <a href="#q-group-3" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 3: Nhập/Xuất <<, >> (13-18)</a>
                        <a href="#q-group-4" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 4: Chỉ số [] & Functor (19-24)</a>
                        <a href="#q-group-5" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 5: Chuyển kiểu (25-30)</a>
                        <a href="#q-group-6" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 6: Toán tử gán = (31-36)</a>
                        <a href="#q-group-7" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 7: Tiền tố vs Hậu tố ++ (37-42)</a>
                        <a href="#q-group-8" class="block py-1 text-zinc-600 hover:text-[#991b1b] transition">Nhóm 8: new/delete & So sánh (43-50)</a>
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
                        Chương 4: Đa Năng Hóa Toán Tử (Operator Overloading)
                    </h2>
                    <p class="text-sm text-zinc-500 mt-1">
                        Trích xuất toàn diện từ giáo trình <code class="inline-code">OOP4-OperatorOverloading_new.pdf</code> | Phân tích sâu sắc cơ chế phân giải toán tử và bảng mã máy
                    </p>
                </div>

                <!-- Theory Part 1 -->
                <section class="theory-content space-y-4">
                    <h3 class="text-xl">1. Khái Niệm, Bản Chất & Các Giới Hạn Bất Khả Xâm Phạm</h3>
                    <p>
                        Trong ngôn ngữ C, khi tạo ra một kiểu dữ liệu mới (ví dụ <code class="inline-code">Complex</code>), để thực hiện các phép toán cộng, trừ ta buộc phải viết các hàm rườm rà như <code class="inline-code">AddComplex(c1, c2)</code>. C++ cho phép ta định nghĩa lại ý nghĩa của các toán tử có sẵn cho các kiểu dữ liệu người dùng, giúp biểu thức trở nên tự nhiên và trực quan (<code class="inline-code">c3 = c1 + c2;</code>).
                    </p>
                    
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-ban"></i> Các giới hạn bất khả xâm phạm của Operator Overloading</div>
                        <ul class="list-disc pl-5 space-y-2 text-zinc-700">
                            <li><strong>1. Không thể định nghĩa toán tử mới:</strong> Không thể tự sáng tạo các ký hiệu không có trong tập toán tử C++ như <code class="inline-code">**</code>, <code class="inline-code">&lt;&gt;</code>, <code class="inline-code">@</code>.</li>
                            <li><strong>2. Không thể thay đổi số toán hạng (Arity):</strong> Toán tử một ngôi (Unary) mãi mãi là một ngôi; toán tử hai ngôi (Binary) mãi mãi là hai ngôi.</li>
                            <li><strong>3. Không thể thay đổi độ ưu tiên và thứ tự kết hợp (Precedence & Associativity):</strong> Phép nhân <code class="inline-code">*</code> luôn có độ ưu tiên cao hơn phép cộng <code class="inline-code">+</code>.</li>
                            <li><strong>4. Danh sách 5 toán tử CẤM OVERLOAD:</strong>
                                <br>&nbsp;&nbsp;&bull; Toán tử định phạm vi: <code class="inline-code">::</code>
                                <br>&nbsp;&nbsp;&bull; Toán tử truy cập thành viên trực tiếp: <code class="inline-code">.</code>
                                <br>&nbsp;&nbsp;&bull; Toán tử con trỏ tới thành viên: <code class="inline-code">.*</code>
                                <br>&nbsp;&nbsp;&bull; Toán tử điều kiện ba ngôi: <code class="inline-code">?:</code>
                                <br>&nbsp;&nbsp;&bull; Toán tử kích thước và kiểm tra kiểu: <code class="inline-code">sizeof</code>, <code class="inline-code">typeid</code>
                            </li>
                            <li><strong>5. Bốn toán tử BẮT BUỘC PHẢI LÀ HÀM THÀNH VIÊN:</strong> Toán tử gán <code class="inline-code">=</code>, toán tử chỉ số <code class="inline-code">[]</code>, toán tử gọi hàm <code class="inline-code">()</code>, và toán tử trỏ thành viên <code class="inline-code">-&gt;</code>.</li>
                        </ul>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 4-6: Đa năng hoá toán tử và các giới hạn]</span>
                </section>

                <!-- Theory Part 2 -->
                <section id="theory-member-vs-friend" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">2. Cài Đặt Toán Tử: Hàm Thành Viên vs Hàm Bạn (Friend)</h3>
                    <p>
                        C++ hỗ trợ 2 cơ chế chính để cài đặt một toán tử hai ngôi:
                    </p>
                    <div class="overflow-x-auto my-3">
                        <table class="w-full text-sm border-collapse border border-zinc-300 font-sans">
                            <thead class="bg-zinc-100">
                                <tr>
                                    <th class="border p-2 text-left">Đặc điểm</th>
                                    <th class="border p-2 text-left">Hàm Thành Viên (Member)</th>
                                    <th class="border p-2 text-left">Hàm Tự Do / Hàm Bạn (Friend)</th>
                                </tr>
                            </thead>
                            <tbody class="text-xs">
                                <tr>
                                    <td class="border p-2 font-bold">Cú pháp gọi ngầm</td>
                                    <td class="border p-2 font-mono">a.operator@(b)</td>
                                    <td class="border p-2 font-mono">operator@(a, b)</td>
                                </tr>
                                <tr>
                                    <td class="border p-2 font-bold">Toán hạng bên trái</td>
                                    <td class="border p-2">Bắt buộc phải là đối tượng của class (*this)</td>
                                    <td class="border p-2">Có thể là bất kỳ kiểu nào (int, float, ostream...)</td>
                                </tr>
                                <tr>
                                    <td class="border p-2 font-bold">Tính đối xứng (Symmetry)</td>
                                    <td class="border p-2 text-red-600 font-bold">Không (obj + 5 chạy, 5 + obj lỗi)</td>
                                    <td class="border p-2 text-green-600 font-bold">Có (hỗ trợ cả obj + 5 và 5 + obj)</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 7-14: Hàm thành viên vs friend function]</span>
                </section>

                <!-- Theory Part 3 -->
                <section id="theory-stream-io" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">3. Đa Năng Hóa Toán Tử Nhập / Xuất (>> và <<)</h3>
                    <p>
                        Để in hoặc nhập đối tượng qua luồng chuẩn <code class="inline-code">std::cout &lt;&lt; obj;</code> hoặc <code class="inline-code">std::cin &gt;&gt; obj;</code>, ta bắt buộc phải cài đặt dưới dạng hàm tự do (thường khai báo <code class="inline-code">friend</code>).
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-right-left"></i> Chữ ký chuẩn mực của Toán tử Chèn/Trích luồng</div>
                        <p class="text-zinc-700">
                            - <strong>Toán tử xuất:</strong> <code class="inline-code">std::ostream&amp; operator&lt;&lt;(std::ostream&amp; os, const ClassName&amp; obj);</code>
                            <br>- <strong>Toán tử nhập:</strong> <code class="inline-code">std::istream&amp; operator&gt;&gt;(std::istream&amp; is, ClassName&amp; obj);</code>
                            <br><br>
                            <strong>Tại sao bắt buộc phải trả về tham chiếu luồng (<code class="inline-code">ostream&amp;</code>)?</strong>
                            <br>Bởi vì toán tử chèn luồng có tính kết hợp từ trái qua phải. Biểu thức <code class="inline-code">cout &lt;&lt; a &lt;&lt; b;</code> được lượng giá thành <code class="inline-code">(cout &lt;&lt; a) &lt;&lt; b;</code>. Để toán tử tiếp theo có thể in được <code>b</code>, lời gọi đầu tiên bắt buộc phải trả về tham chiếu đến chính đối tượng <code class="inline-code">cout</code> đó (Stream Chaining). Hơn nữa, các lớp stream trong C++ cấm sao chép (Non-copyable), nên bắt buộc phải truyền và trả về bằng tham chiếu.
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 15-18: Đa năng hoá toán tử nhập >> và xuất <<]</span>
                </section>

                <!-- Theory Part 4 -->
                <section id="theory-subscript-functor" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">4. Toán Tử Chỉ Số [] & Toán Tử Gọi Hàm () (Functor)</h3>
                    <p>
                        Cả hai toán tử này đều bắt buộc phải là phương thức thành viên của lớp.
                    </p>
                    <ul class="list-disc pl-6 space-y-2 text-zinc-700">
                        <li><strong>Toán tử chỉ số <code class="inline-code">[]</code>:</strong> Thường được triển khai theo cặp (Overload by Constness):
                            <br>- Bản không-const: <code class="inline-code">T&amp; operator[](size_t index);</code> (trả về tham chiếu lvalue để vừa đọc vừa ghi giá trị: <code class="inline-code">arr[i] = 10;</code>).
                            <br>- Bản const: <code class="inline-code">const T&amp; operator[](size_t index) const;</code> (trả về hằng tham chiếu để đọc trên các đối tượng <code class="inline-code">const</code>).
                        </li>
                        <li><strong>Toán tử gọi hàm <code class="inline-code">()</code> (Functor / Function Object):</strong> Biến một thể hiện đối tượng thành một hàm có thể gọi được (<code class="inline-code">obj(arg1, arg2)</code>). Đây là toán tử duy nhất trong C++ cho phép nhận <strong>số lượng tham số tùy ý</strong> và có thể overload nhiều phiên bản nhận các bộ tham số khác nhau.</li>
                    </ul>
                    <span class="citation-badge">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 19-21: Toán tử chỉ số [] & toán tử gọi hàm ()]</span>
                </section>

                <!-- Theory Part 5 -->
                <section id="theory-conversion" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">5. Toán Tử Chuyển Đổi Kiểu (Type Conversion Operator) & explicit</h3>
                    <p>
                        Toán tử chuyển đổi kiểu cho phép một đối tượng lớp tự động hoặc tường minh ép kiểu sang một kiểu dữ liệu khác (ví dụ từ <code class="inline-code">Fraction</code> sang <code class="inline-code">double</code>).
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-arrows-split-up-and-left"></i> Cú pháp đặc thù & Từ khóa explicit trong C++11</div>
                        <p class="text-zinc-700">
                            Cú pháp: <code class="inline-code">operator DestinationType() const;</code>
                            <br>- <strong>Đặc điểm:</strong> Tuyệt đối không ghi kiểu trả về ở đầu hàm (vì kiểu trả về đã chính là tên của đích đến).
                            <br>- <strong>C++11 explicit conversion:</strong> Trước C++11, toán tử chuyển đổi kiểu luôn ngầm định, rất dễ gây ra các lỗi chuyển đổi kiểu ngoài ý muốn làm sai lệch kết quả tính toán. C++11 cho phép thêm từ khóa <code class="inline-code">explicit</code>: <code class="inline-code">explicit operator bool() const;</code> để chỉ cho phép ép kiểu trong ngữ cảnh tường minh (như trong điều kiện <code class="inline-code">if (obj)</code> hoặc dùng <code class="inline-code">static_cast</code>).
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 22-25: Toán tử chuyển đổi kiểu]</span>
                </section>

                <!-- Theory Part 6 -->
                <section id="theory-inc-dec" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">6. Toán Tử Tăng / Giảm Tiền Tố (++x) vs Hậu Tố (x++)</h3>
                    <p>
                        C++ phân biệt giữa toán tử tăng tiền tố (Prefix) và hậu tố (Postfix) bằng một quy ước chữ ký đặc biệt:
                    </p>
                    <div class="overflow-x-auto my-3">
                        <table class="w-full text-sm border-collapse border border-zinc-300 font-sans">
                            <thead class="bg-zinc-100">
                                <tr>
                                    <th class="border p-2 text-left">Đặc tính</th>
                                    <th class="border p-2 text-left">Tiền tố: ++obj</th>
                                    <th class="border p-2 text-left">Hậu tố: obj++</th>
                                </tr>
                            </thead>
                            <tbody class="text-xs">
                                <tr>
                                    <td class="border p-2 font-bold">Chữ ký hàm</td>
                                    <td class="border p-2 font-mono">ClassName&amp; operator++();</td>
                                    <td class="border p-2 font-mono">ClassName operator++(int);</td>
                                </tr>
                                <tr>
                                    <td class="border p-2 font-bold">Tham số 'int' bù nhìn</td>
                                    <td class="border p-2">Không có tham số</td>
                                    <td class="border p-2">Nhận một tham số <code class="inline-code">int</code> giả (dummy) để phân biệt chữ ký</td>
                                </tr>
                                <tr>
                                    <td class="border p-2 font-bold">Giá trị trả về</td>
                                    <td class="border p-2">Tham chiếu lvalue tới đối tượng đã tăng (<code class="inline-code">*this</code>)</td>
                                    <td class="border p-2">Bản sao tạm thời chứa giá trị cũ trước khi tăng</td>
                                </tr>
                                <tr>
                                    <td class="border p-2 font-bold">Hiệu năng</td>
                                    <td class="border p-2 text-green-600 font-bold">Nhanh hơn (không tốn chi phí sao chép)</td>
                                    <td class="border p-2 text-yellow-600 font-bold">Chậm hơn (phải tạo bản sao tạm trên stack)</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 31-34: Đa năng hoá toán tử ++ và --]</span>
                </section>

                <!-- Theory Part 7 -->
                <section id="theory-new-delete" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">7. Đa Năng Hóa Toán Tử Quản Lý Heap: operator new & delete</h3>
                    <p>
                        C++ cho phép lập trình viên thay thế thuật toán cấp phát heap mặc định của hệ điều hành bằng cách tự overload <code class="inline-code">operator new</code> và <code class="inline-code">operator delete</code> cho từng lớp cụ thể (Memory Pool Pattern).
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-memory"></i> Cơ chế 2 bước của biểu thức new</div>
                        <p class="text-zinc-700">
                            Khi lập trình viên viết: <code class="inline-code">MyClass* p = new MyClass(10);</code>, CPU thực hiện chính xác 2 bước:
                            <br>1. <strong>Bước 1 (Cấp phát thô):</strong> Gọi hàm <code class="inline-code">void* operator new(size_t size);</code> để lấy về một khối ô nhớ thô có kích thước bằng <code class="inline-code">sizeof(MyClass)</code>.
                            <br>2. <strong>Bước 2 (Khởi tạo đối tượng):</strong> Gọi Constructor <code class="inline-code">MyClass::MyClass(10)</code> ngay trên vùng nhớ vừa được cấp phát.
                            <br>Khi overload <code class="inline-code">operator new</code>, ta chỉ can thiệp vào Bước 1, Constructor ở Bước 2 vẫn tự động chạy.
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP4-OperatorOverloading_new.pdf - Trang 40-42: Đa năng hoá new và delete]</span>
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
                            50 Câu Trắc Nghiệm Code & Bẫy Operator Overloading C++11
                        </h2>
                        <p class="text-xs text-zinc-500 mt-1">
                            100% dựa trên các đoạn code thực tế: bẫy phân giải toán tử, toán tử bạn, luồng IO, Functor, new/delete và chuẩn C++11
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

print("Writing template for Chapter 4...")

