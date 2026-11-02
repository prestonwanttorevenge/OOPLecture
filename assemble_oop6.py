# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Import questions from build_oop6_quiz
import build_oop6_quiz
questions = build_oop6_quiz.questions

assert len(questions) == 50, f"Expected 50 questions, got {len(questions)}"

html_head_and_theory = """<!DOCTYPE html>
<html lang="vi" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chương 6: Đa Hình (Polymorphism) - MOSTest5_2</title>

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
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.75rem;
            color: #991b1b;
            background-color: #fef2f2;
            border: 1px solid #fecaca;
            padding: 0.15rem 0.5rem;
            border-radius: 0.25rem;
            margin-top: 0.5rem;
        }

        pre[class*="language-"] {
            border-radius: 0.5rem;
            margin: 1rem 0;
            border: 1px solid #27272a;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.875rem;
        }

        .quiz-btn {
            transition: all 0.15s ease-in-out;
        }

        .quiz-btn.selected-correct {
            background-color: #059669 !important;
            color: #ffffff !important;
            border-color: #047857 !important;
        }

        .quiz-btn.selected-wrong {
            background-color: #dc2626 !important;
            color: #ffffff !important;
            border-color: #b91c1c !important;
        }

        .quiz-btn.show-correct {
            background-color: #10b981 !important;
            color: #ffffff !important;
            border-color: #059669 !important;
        }

        .answer-block {
            display: none;
        }

        .answer-block.show {
            display: block;
            animation: fadeIn 0.3s ease-in;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-4px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .inline-code {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.875em;
            background-color: #f4f4f5;
            padding: 0.15em 0.4em;
            border-radius: 0.25rem;
            color: #991b1b;
            border: 1px solid #e4e4e7;
        }
    </style>
</head>
<body class="antialiased min-h-screen flex flex-col">

    <!-- Top Sticky Header -->
    <header class="sticky top-0 z-50 bg-[#991b1b] text-white shadow-md border-b border-red-900">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <i class="fa-solid fa-shapes text-2xl text-red-200"></i>
                <div>
                    <h1 class="text-lg font-bold tracking-tight">C++11 Academic Masterclass</h1>
                    <p class="text-xs text-red-200 font-mono">Chương 6: Đa Hình (Polymorphism) & Cơ Chế VTable Dưới Gầm Máy</p>
                </div>
            </div>
            <div class="flex items-center space-x-4">
                <div class="text-right hidden sm:block">
                    <span id="score-display" class="font-mono text-sm font-semibold bg-red-900/60 px-3 py-1.5 rounded border border-red-700/50">Điểm: 0/50</span>
                </div>
                <button onclick="resetQuiz()" class="px-3 py-1.5 text-xs font-semibold bg-red-700 hover:bg-red-600 rounded transition flex items-center gap-1.5 shadow-sm">
                    <i class="fa-solid fa-rotate-right"></i> Làm lại
                </button>
            </div>
        </div>
    </header>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 flex-1 flex flex-col lg:flex-row gap-8 w-full">

        <!-- Sticky Sidebar Navigation (TOC) -->
        <aside class="w-full lg:w-72 shrink-0">
            <div class="sticky top-24 space-y-6">
                <!-- TOC Theory -->
                <div class="bg-white border border-zinc-200 rounded-lg p-5 shadow-sm">
                    <h2 class="text-xs font-bold uppercase tracking-wider text-[#991b1b] font-mono mb-3 flex items-center gap-2">
                        <i class="fa-solid fa-book-open"></i> Mục Lục Lý Thuyết
                    </h2>
                    <nav class="space-y-1 text-sm font-medium">
                        <a href="#theory-concept" class="block py-1.5 px-2.5 rounded hover:bg-red-50 hover:text-[#991b1b] transition text-zinc-700">1. Bản Chất Đa Hình & Phân Loại Liên Kết</a>
                        <a href="#theory-override" class="block py-1.5 px-2.5 rounded hover:bg-red-50 hover:text-[#991b1b] transition text-zinc-700">2. Overloading vs Overriding & C++11 override/final</a>
                        <a href="#theory-vtable" class="block py-1.5 px-2.5 rounded hover:bg-red-50 hover:text-[#991b1b] transition text-zinc-700">3. Bảng Ảo (VTable) & Con Trỏ Ảo (vptr)</a>
                        <a href="#theory-vdtor" class="block py-1.5 px-2.5 rounded hover:bg-red-50 hover:text-[#991b1b] transition text-zinc-700">4. Destructor Ảo & Quy Tắc Vàng Bộ Nhớ</a>
                        <a href="#theory-abstract" class="block py-1.5 px-2.5 rounded hover:bg-red-50 hover:text-[#991b1b] transition text-zinc-700">5. Lớp Trừu Tượng & Hàm Thuần Ảo</a>
                        <a href="#theory-ctor-trap" class="block py-1.5 px-2.5 rounded hover:bg-red-50 hover:text-[#991b1b] transition text-zinc-700">6. Bẫy Tử Thần: Hàm Ảo trong Ctor / Dtor</a>
                    </nav>
                </div>

                <!-- TOC Quiz -->
                <div class="bg-white border border-zinc-200 rounded-lg p-5 shadow-sm">
                    <h2 class="text-xs font-bold uppercase tracking-wider text-[#991b1b] font-mono mb-3 flex items-center gap-2">
                        <i class="fa-solid fa-vial-circle-check"></i> 50 Câu Trắc Nghiệm Code
                    </h2>
                    <nav class="space-y-1 text-xs font-mono text-zinc-600">
                        <a href="#q-group-1" class="block py-1 px-2 rounded hover:bg-red-50 hover:text-[#991b1b] transition">Câu 01 - 08: VTable & vptr Dưới Gầm Máy</a>
                        <a href="#q-group-2" class="block py-1 px-2 rounded hover:bg-red-50 hover:text-[#991b1b] transition">Câu 09 - 16: Overriding, override & final</a>
                        <a href="#q-group-3" class="block py-1 px-2 rounded hover:bg-red-50 hover:text-[#991b1b] transition">Câu 17 - 24: Virtual Destructor & Vùng Heap</a>
                        <a href="#q-group-4" class="block py-1 px-2 rounded hover:bg-red-50 hover:text-[#991b1b] transition">Câu 25 - 34: Lớp Trừu Tượng & Hàm Thuần Ảo</a>
                        <a href="#q-group-5" class="block py-1 px-2 rounded hover:bg-red-50 hover:text-[#991b1b] transition">Câu 35 - 42: Bẫy Hàm Ảo trong Ctor / Dtor</a>
                        <a href="#q-group-6" class="block py-1 px-2 rounded hover:bg-red-50 hover:text-[#991b1b] transition">Câu 43 - 50: Đa Hình Nâng Cao, RTTI & CRTP</a>
                    </nav>
                </div>
            </div>
        </aside>

        <!-- Main Content Area -->
        <main class="flex-1 space-y-10 min-w-0">

            <!-- THEORY SECTION -->
            <article class="bg-white border border-zinc-200 rounded-lg p-6 sm:p-10 shadow-sm space-y-8">
                <div class="border-b-2 border-[#991b1b] pb-4">
                    <div class="flex items-center gap-2 text-xs font-mono font-bold text-[#991b1b] uppercase tracking-wider mb-1">
                        Tài Liệu Học Thuật Chuyên Sâu C++11
                    </div>
                    <h2 class="text-3xl font-black text-zinc-900 tracking-tight font-sans uppercase">
                        Chương 6: Tính Đa Hình (Polymorphism) & Cơ Chế VTable Dưới Gầm Máy
                    </h2>
                    <p class="text-sm text-zinc-500 font-serif italic mt-1">
                        Trích xuất toàn diện từ slide bài giảng OOP6-Polymorphism_new.pdf (45 trang)
                    </p>
                </div>

                <!-- Theory Part 1 -->
                <section id="theory-concept" class="theory-content space-y-4">
                    <h3 class="text-xl">1. Bản Chất Đa Hình & Phân Loại Liên Kết (Binding Classification)</h3>
                    <p>
                        Thuật ngữ <strong>Polymorphism</strong> có nguồn gốc từ tiếng Hy Lạp, mang nghĩa là 'nhiều hình thức' hay 'nhiều dạng sống'. Trong lập trình hướng đối tượng, đa hình là khả năng các đối tượng thuộc các lớp khác nhau phản hồi cùng một thông điệp (lời gọi hàm) theo các cách xử lý đặc thù khác nhau.
                    </p>
                    <p>
                        Hai hình thức liên kết hàm cốt lõi trong C++:
                        <br><strong>- Liên kết tĩnh (Static Binding / Early Binding):</strong> Quá trình liên kết một lời gọi hàm với một định nghĩa cụ thể được trình biên dịch thực hiện ngay tại thời điểm biên dịch (Compile-time). Áp dụng cho: hàm thông thường, hàm quá tải (Function Overloading), hàm mẫu (Templates).
                        <br><strong>- Liên kết động (Dynamic Binding / Late Binding):</strong> Quá trình liên kết được trì hoãn đến tận thời điểm thực thi chương trình (Runtime). Áp dụng cho các <strong>Hàm ảo (Virtual Functions)</strong> được gọi qua Con trỏ (<code>Base*</code>) hoặc Tham chiếu (<code>Base&</code>).
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-microchip"></i> Cơ Chế Dưới Gầm Máy: Static Binding vs Dynamic Binding</div>
                        <p class="text-sm text-zinc-700 font-sans leading-relaxed">
                            - <strong>Static Binding:</strong> Compiler phát sinh chỉ lệnh hợp ngữ gọi trực tiếp địa chỉ nhãn hàm cố định (<code>call _ZN4Base4drawEv</code>). Không tốn chi phí gián tiếp, trình tối ưu hóa có thể inline mã nguồn.
                            <br>- <strong>Dynamic Binding:</strong> Compiler phát sinh mã tra cứu con trỏ qua 2 bước gián tiếp (Double Indirection): Lấy địa chỉ bảng VTable từ con trỏ <code>vptr</code> trong đối tượng, tra cứu index tương ứng trong VTable, và thực hiện lệnh gọi gián tiếp (<code>call qword ptr [rax+offset]</code>).
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 2-7 & 13-20: Đa hình là gì & Phân loại liên kết]</span>
                </section>

                <!-- Theory Part 2 -->
                <section id="theory-override" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">2. Overloading vs Overriding & Bộ Từ Khóa C++11 (override, final)</h3>
                    <p>
                        Sự phân biệt rõ ràng giữa hai khái niệm dễ nhầm lẫn nhất:
                        <br><strong>- Overloading (Nạp chồng hàm):</strong> Cùng nằm trong một phạm vi (scope), tên hàm giống nhau nhưng <em>danh sách tham số bắt buộc phải khác nhau</em>. Phân giải lúc biên dịch.
                        <br><strong>- Overriding (Ghi đè phương thức):</strong> Diễn ra giữa lớp cha và lớp con trong cây kế thừa. Hàm ở lớp con ghi đè một hàm ảo của lớp cha với <em>chữ ký hàm (signature) giống hệt nhau</em>. Phân giải lúc chạy.
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-shield-halved"></i> C++11 Contextual Keywords: override & final</div>
                        <p class="text-sm text-zinc-700 font-sans leading-relaxed">
                            - <code class="inline-code">override</code>: Chỉ thị cho trình biên dịch kiểm tra tính hợp lệ của việc ghi đè. Nếu lớp cha không có hàm ảo nào khớp 100% chữ ký (kể cả thuộc tính <code>const</code>, kiểu tham số), trình biên dịch sẽ chặn lỗi ngay lập tức.
                            <br>- <code class="inline-code">final</code>:
                            <br>&nbsp;&nbsp;+ Đặt sau hàm ảo: Cấm mọi lớp con kế tiếp ghi đè hàm này.
                            <br>&nbsp;&nbsp;+ Đặt sau tên lớp: Cấm bất kỳ lớp nào kế thừa từ lớp này. Cho phép compiler thực hiện tối ưu hóa <strong>Devirtualization</strong> (loại bỏ tra cứu VTable để gọi thẳng).
                            <br>- <strong>Covariant Return Types (Kiểu trả về đồng biến):</strong> Ngoại lệ duy nhất cho phép hàm override có kiểu trả về khác lớp cha nếu kiểu trả về là con trỏ/tham chiếu tới lớp con của kiểu trả về ở lớp cha.
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 6-12: Overloading vs Overriding]</span>
                </section>

                <!-- Theory Part 3 -->
                <section id="theory-vtable" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">3. Bảng Ảo (VTable) & Con Trỏ Ảo (vptr) Dưới Gầm Máy</h3>
                    <p>
                        Để hiện thực hóa tính đa hình động với chi phí tối ưu, C++ triển khai kiến trúc <strong>VTable / vptr</strong>:
                        <br><strong>1. Bảng VTable (Virtual Method Table):</strong> Là một mảng tĩnh chứa các con trỏ hàm được trình biên dịch tạo ra cho mỗi Class có hàm ảo và đặt trong phân vùng Read-Only Data (<code>.rodata</code>). Mỗi lớp chỉ có 1 bảng VTable duy nhất.
                        <br><strong>2. Con trỏ vptr (Virtual Table Pointer):</strong> Mỗi đối tượng thuộc lớp đó sẽ được chèn thêm một con trỏ bí mật ở 8 bytes đầu tiên (trên kiến trúc 64-bit), trỏ thẳng vào VTable của lớp tương ứng.
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-table"></i> Giải Mã Tiến Trình Dispatch Hàm Ảo (Step-by-Step)</div>
                        <p class="text-sm text-zinc-700 font-sans leading-relaxed">
                            Khi gặp lệnh gọi hàm ảo: <code class="inline-code">pBase->draw();</code>
                            <br>1. CPU đọc con trỏ <code>pBase</code> để lấy địa chỉ của đối tượng trong RAM.
                            <br>2. CPU giải tham chiếu 8 bytes đầu tiên của đối tượng để lấy giá trị con trỏ <code>vptr</code>.
                            <br>3. CPU cộng thêm offset cố định của hàm <code>draw()</code> trong VTable (ví dụ: <code>vptr + 0</code> cho slot đầu tiên).
                            <br>4. CPU nhảy tới địa chỉ hàm được lưu trong slot đó và truyền con trỏ <code>this</code> làm tham số đầu tiên.
                            <br><em>Chi phí: 1 bước truy cập bộ nhớ gián tiếp và không thể inline mã nguồn thông thường.</em>
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 21-26: Hàm ảo & Cơ chế liên kết động]</span>
                </section>

                <!-- Theory Part 4 -->
                <section id="theory-vdtor" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">4. Destructor Ảo (Virtual Destructor) - Quy Tắc Vàng Quản Lý Bộ Nhớ</h3>
                    <p>
                        Slide trang 27-30 nhấn mạnh một trong những quy tắc kiến trúc quan trọng nhất của C++: <strong>Mỗi khi tạo một lớp để được dùng làm lớp cơ sở, ta luôn luôn phải khai báo Destructor là hàm ảo!</strong>
                    </p>
                    <p>
                        Nếu Destructor của lớp cơ sở không phải là hàm ảo: Khi một đối tượng lớp dẫn xuất được cấp phát trên heap và quản lý qua con trỏ lớp cơ sở (<code class="inline-code">Base* p = new Derived(); delete p;</code>):
                        <br>- Trình biên dịch sử dụng liên kết tĩnh, chỉ gọi duy nhất Destructor của lớp cơ sở (<code class="inline-code">Base::~Base()</code>).
                        <br>- Thân hàm Destructor của lớp dẫn xuất (<code class="inline-code">Derived::~Derived()</code>) bị <strong>BỎ QUA HOÀN TOÀN</strong>.
                        <br>- Dẫn tới rò rỉ bộ nhớ (Memory Leak) nghiêm trọng cho mọi tài nguyên heap do lớp dẫn xuất nắm giữ và kích hoạt <strong>Hành Vi Không Xác Định (Undefined Behavior - UB)</strong> theo chuẩn ISO C++.
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-broom"></i> Cơ Chế Dưới Gầm Máy: Virtual Destructor Dispatch</div>
                        <p class="text-sm text-zinc-700 font-sans leading-relaxed">
                            Khi khai báo <code class="inline-code">virtual ~Base() = default;</code>, destructor của Derived được tự động chèn vào VTable. Lệnh <code>delete p;</code> sẽ tra cứu VTable để gọi <code>~Derived()</code> trước, rồi sau đó chuỗi hủy tự động dỡ ngược về <code>~Base()</code>, giải phóng trọn vẹn 100% tài nguyên.
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 27-30: Destructor ảo & Quản lý bộ nhớ]</span>
                </section>

                <!-- Theory Part 5 -->
                <section id="theory-abstract" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">5. Lớp Trừu Tượng (Abstract Class) & Hàm Thuần Ảo (Pure Virtual Function)</h3>
                    <p>
                        Một <strong>Hàm Thuần Ảo (Pure Virtual Function)</strong> là một hàm ảo được khai báo với cú pháp đặc biệt: <code class="inline-code">virtual void func() = 0;</code>.
                        <br>Bất kỳ lớp nào chứa ít nhất một hàm thuần ảo sẽ tự động trở thành <strong>Lớp Trừu Tượng (Abstract Class)</strong>.
                    </p>
                    <p>
                        <strong>Các Quy Tắc Vàng Của Lớp Trừu Tượng:</strong>
                        <br>1. <strong>Cấm Khởi Tạo Đối Tượng:</strong> Không thể tạo thể hiện trực tiếp từ lớp trừu tượng (<code class="inline-code">AbstractBase b;</code> -> Lỗi biên dịch).
                        <br>2. <strong>Hỗ Trợ Con Trỏ & Tham Chiếu:</strong> Hoàn toàn có thể khai báo con trỏ (<code class="inline-code">AbstractBase* ptr;</code>) và tham chiếu để trỏ tới các lớp con cụ thể.
                        <br>3. <strong>Ràng Buộc Lớp Con:</strong> Lớp con bắt buộc phải override TẤT CẢ các hàm thuần ảo, nếu không nó sẽ tiếp tục là một lớp trừu tượng.
                        <br>4. <strong>Định Nghĩa Hàm Thuần Ảo:</strong> C++ vẫn cho phép cung cấp phần thân định nghĩa cho hàm thuần ảo ở <em>bên ngoài khai báo class</em> để làm mã cài đặt mặc định cho các lớp con tái sử dụng qua <code class="inline-code">Base::func()</code>.
                    </p>
                    <span class="citation-badge">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 31-43: Lớp trừu tượng & Hàm thuần ảo]</span>
                </section>

                <!-- Theory Part 6 -->
                <section id="theory-ctor-trap" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">6. Bẫy Tử Thần: Gọi Hàm Ảo Trong Constructor & Destructor</h3>
                    <p>
                        Một trong những cạm bẫy kiến trúc nguy hiểm bậc nhất trong C++ là việc gọi hàm ảo từ bên trong Constructor hoặc Destructor của lớp cơ sở.
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-triangle-exclamation"></i> Cơ Chế Vô Hiệu Hóa Đa Hình Trong Constructor / Destructor</div>
                        <p class="text-sm text-zinc-700 font-sans leading-relaxed">
                            - <strong>Trong Constructor:</strong> Khi Constructor của <code>Base</code> đang chạy, phần <code>Derived</code> chưa hề được cấp phát và khởi tạo. Để đảm bảo an toàn bộ nhớ, trình biên dịch thiết lập <code>vptr</code> trỏ vào <strong>VTable của Base</strong>. Do đó, lời gọi hàm ảo sẽ gọi phiên bản của <code>Base</code>, KHÔNG PHẢI của <code>Derived</code>!
                            <br>- <strong>Hiểm Họa Pure Virtual Crash:</strong> Nếu hàm ảo trong Base là hàm thuần ảo (<code>= 0</code>) và bị gọi gián tiếp trong Constructor, con trỏ VTable trỏ tới hàm báo lỗi hệ thống <code>__cxa_pure_virtual()</code>, khiến chương trình <strong>SẬP TỨC THÌ (Crash / Abort)</strong> tại runtime!
                            <br>- <strong>Trong Destructor:</strong> Khi <code>Derived</code> đã bị hủy xong, <code>vptr</code> bị hạ cấp (demoted) trỏ ngược về VTable của <code>Base</code>, lời gọi hàm ảo lại chỉ thực thi mã của Base.
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP6-Polymorphism_new.pdf - Trang 23-26 & 38-40: VTable trong vòng đời đối tượng]</span>
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
                            50 Câu Trắc Nghiệm Code & Bẫy Đa Hình C++11 Chuyên Sâu
                        </h2>
                        <p class="text-xs text-zinc-500 mt-1">
                            100% dựa trên các đoạn code thực tế: bẫy VTable, Virtual Dtor UB, Pure Virtual Crash, NVI Idiom, Covariant return và CRTP
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
        const quizData = """ + json.dumps(questions, ensure_ascii=False, indent=8) + """;

        let userAnswers = {};
        let score = 0;

        function renderQuiz() {
            const container = document.getElementById('quiz-container');
            container.innerHTML = '';

            let currentGroup = '';

            quizData.forEach((q, idx) => {
                if (q.group_name && q.group_name !== currentGroup) {
                    currentGroup = q.group_name;
                    const groupHeader = document.createElement('div');
                    groupHeader.id = q.group_id;
                    groupHeader.className = "pt-8 pb-3 border-b-2 border-zinc-300 text-[#991b1b] font-bold text-lg font-sans uppercase tracking-tight flex items-center gap-2";
                    groupHeader.innerHTML = `<i class="fa-solid fa-layer-group text-sm"></i> ${currentGroup}`;
                    container.appendChild(groupHeader);
                }

                const card = document.createElement('div');
                card.id = `q-${q.id}`;
                card.className = "p-5 border border-zinc-200 rounded-lg bg-zinc-50/50 space-y-4 hover:border-zinc-300 transition-colors";

                const header = document.createElement('div');
                header.className = "flex items-start justify-between gap-4";
                header.innerHTML = `
                    <div class="space-y-1">
                        <span class="inline-block text-xs font-mono font-bold text-white bg-[#991b1b] px-2 py-0.5 rounded">
                            Câu ${q.id.toString().padStart(2, '0')}/50
                        </span>
                        <h4 class="text-base font-bold text-zinc-900 font-sans">${q.title}</h4>
                    </div>
                    <div id="badge-status-${q.id}" class="text-xs font-mono shrink-0"></div>
                `;
                card.appendChild(header);

                if (q.code) {
                    const codeBlock = document.createElement('pre');
                    codeBlock.className = "language-cpp";
                    const code = document.createElement('code');
                    code.className = "language-cpp";
                    code.textContent = q.code;
                    codeBlock.appendChild(code);
                    card.appendChild(codeBlock);
                }

                const optionsGrid = document.createElement('div');
                optionsGrid.className = "grid grid-cols-1 gap-2 pt-2";

                q.options.forEach((opt, optIdx) => {
                    const btn = document.createElement('button');
                    btn.id = `btn-${q.id}-${optIdx}`;
                    btn.type = "button";
                    btn.className = "quiz-btn text-left p-3 text-sm rounded border border-zinc-300 bg-white hover:bg-zinc-100 text-zinc-800 font-sans transition-all flex items-start gap-2.5";
                    btn.innerHTML = `<span class="font-mono font-bold text-zinc-500 shrink-0">${String.fromCharCode(65 + optIdx)}.</span> <span>${opt.substring(3)}</span>`;
                    btn.onclick = () => selectOption(q.id, optIdx);
                    optionsGrid.appendChild(btn);
                });
                card.appendChild(optionsGrid);

                const answerBlock = document.createElement('div');
                answerBlock.id = `answer-${q.id}`;
                answerBlock.className = "answer-block mt-4 p-4 rounded bg-white border-l-4 border-emerald-600 shadow-sm text-sm text-zinc-800";
                answerBlock.innerHTML = `
                    <div class="font-bold text-emerald-800 font-sans mb-1 flex items-center gap-1.5">
                        <i class="fa-solid fa-circle-check"></i> GIẢI THÍCH CHUYÊN SÂU
                    </div>
                    <div class="text-xs sm:text-sm font-sans leading-relaxed text-zinc-700">
                        ${q.explanation}
                    </div>
                `;
                card.appendChild(answerBlock);

                container.appendChild(card);
            });

            Prism.highlightAll();
        }

        function selectOption(qId, selectedIdx) {
            if (userAnswers[qId] !== undefined) return;

            userAnswers[qId] = selectedIdx;
            const q = quizData.find(item => item.id === qId);
            const isCorrect = (selectedIdx === q.correct);

            if (isCorrect) {
                score++;
            }

            updateScoreDisplay();

            q.options.forEach((_, idx) => {
                const btn = document.getElementById(`btn-${qId}-${idx}`);
                btn.disabled = true;

                if (idx === q.correct) {
                    btn.classList.add('show-correct');
                }
            });

            const clickedBtn = document.getElementById(`btn-${qId}-${selectedIdx}`);
            if (isCorrect) {
                clickedBtn.classList.remove('show-correct');
                clickedBtn.classList.add('selected-correct');
            } else {
                clickedBtn.classList.add('selected-wrong');
            }

            const statusBadge = document.getElementById(`badge-status-${qId}`);
            if (isCorrect) {
                statusBadge.innerHTML = '<span class="text-emerald-700 font-bold"><i class="fa-solid fa-check"></i> Đúng</span>';
            } else {
                statusBadge.innerHTML = '<span class="text-rose-700 font-bold"><i class="fa-solid fa-xmark"></i> Sai</span>';
            }

            const ansBlock = document.getElementById(`answer-${qId}`);
            ansBlock.classList.add('show');
        }

        function updateScoreDisplay() {
            const total = quizData.length;
            const answeredCount = Object.keys(userAnswers).length;
            document.getElementById('score-display').innerText = `Điểm: ${score}/${total}`;
            document.getElementById('answered-count').innerText = `${answeredCount}/${total}`;
        }

        function resetQuiz() {
            if (!confirm('Bạn có chắc chắn muốn làm lại bài kiểm tra từ đầu?')) return;
            userAnswers = {};
            score = 0;
            updateScoreDisplay();
            renderQuiz();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        document.addEventListener('DOMContentLoaded', () => {
            renderQuiz();
            updateScoreDisplay();
        });
    </script>
</body>
</html>
"""

# Output paths
root_path = "c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/OOP6-Polymorphism_new.html"
baitap_path = "c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/Bài tập/OOP6-Polymorphism_new.html"

with open(root_path, "w", encoding="utf-8") as f:
    f.write(html_head_and_theory)

with open(baitap_path, "w", encoding="utf-8") as f:
    f.write(html_head_and_theory)

print(f"Chapter 6 standalone HTML successfully written to:\n  - {root_path}\n  - {baitap_path}\nSize: {len(html_head_and_theory)} bytes.")

