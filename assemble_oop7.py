# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Import questions from build_oop7_quiz
import build_oop7_quiz
questions = build_oop7_quiz.questions

assert len(questions) == 50, f"Expected 50 questions, got {len(questions)}"

html_head_and_theory = """<!DOCTYPE html>
<html lang="vi" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chương 7: Khuôn Mẫu (Templates) - MOSTest5_2</title>

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
                <i class="fa-solid fa-cubes-stacked text-2xl text-red-200"></i>
                <div>
                    <h1 class="text-lg font-bold tracking-tight">C++11 Academic Masterclass</h1>
                    <p class="text-xs text-red-200 font-mono">Chương 7: Khuôn Mẫu (Templates) & Lập Trình Tổng Quát (Generic)</p>
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
                        <a href="#theory-concept" class="block py-1.5 px-2.5 rounded hover:bg-red-50 hover:text-[#991b1b] transition text-zinc-700">1. Lập Trình Tổng Quát & C++ Template</a>
                        <a href="#theory-function" class="block py-1.5 px-2.5 rounded hover:bg-red-50 hover:text-[#991b1b] transition text-zinc-700">2. Khuôn Mẫu Hàm & Suy Diễn Kiểu</a>
                        <a href="#theory-class" class="block py-1.5 px-2.5 rounded hover:bg-red-50 hover:text-[#991b1b] transition text-zinc-700">3. Khuôn Mẫu Lớp & Template Stack</a>
                        <a href="#theory-nttp" class="block py-1.5 px-2.5 rounded hover:bg-red-50 hover:text-[#991b1b] transition text-zinc-700">4. Non-Type Parameters & Template Parameters</a>
                        <a href="#theory-specialization" class="block py-1.5 px-2.5 rounded hover:bg-red-50 hover:text-[#991b1b] transition text-zinc-700">5. Đặc Tả (Full & Partial Specialization)</a>
                        <a href="#theory-modern" class="block py-1.5 px-2.5 rounded hover:bg-red-50 hover:text-[#991b1b] transition text-zinc-700">6. Kỹ Thuật C++11 (typename, Variadic, decltype)</a>
                    </nav>
                </div>

                <!-- TOC Quiz -->
                <div class="bg-white border border-zinc-200 rounded-lg p-5 shadow-sm">
                    <h2 class="text-xs font-bold uppercase tracking-wider text-[#991b1b] font-mono mb-3 flex items-center gap-2">
                        <i class="fa-solid fa-vial-circle-check"></i> 50 Câu Trắc Nghiệm Code
                    </h2>
                    <nav class="space-y-1 text-xs font-mono text-zinc-600">
                        <a href="#q-group-1" class="block py-1 px-2 rounded hover:bg-red-50 hover:text-[#991b1b] transition">Câu 01 - 08: Bản Chất Template & Instantiation</a>
                        <a href="#q-group-2" class="block py-1 px-2 rounded hover:bg-red-50 hover:text-[#991b1b] transition">Câu 09 - 16: Function Templates & Suy Diễn Kiểu</a>
                        <a href="#q-group-3" class="block py-1 px-2 rounded hover:bg-red-50 hover:text-[#991b1b] transition">Câu 17 - 24: Class Templates & Cấu Trúc Dữ Liệu</a>
                        <a href="#q-group-4" class="block py-1 px-2 rounded hover:bg-red-50 hover:text-[#991b1b] transition">Câu 25 - 34: Non-Type Parameters & Template Khác</a>
                        <a href="#q-group-5" class="block py-1 px-2 rounded hover:bg-red-50 hover:text-[#991b1b] transition">Câu 35 - 42: Đặc Tả Toàn Phần & Từng Phần</a>
                        <a href="#q-group-6" class="block py-1 px-2 rounded hover:bg-red-50 hover:text-[#991b1b] transition">Câu 43 - 50: C++11 Variadic, decltype & SFINAE</a>
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
                        Chương 7: Khuôn Mẫu (Templates) & Lập Trình Tổng Quát (Generic Programming)
                    </h2>
                    <p class="text-sm text-zinc-500 font-serif italic mt-1">
                        Trích xuất toàn diện từ slide bài giảng OOP7-Template.pdf (37 trang)
                    </p>
                </div>

                <!-- Theory Part 1 -->
                <section id="theory-concept" class="theory-content space-y-4">
                    <h3 class="text-xl">1. Khái Niệm Lập Trình Tổng Quát (Generic Programming) & Cơ Chế Template C++</h3>
                    <p>
                        Slide trang 2-10 định nghĩa: <strong>Lập trình tổng quát (Generic Programming)</strong> là phương pháp lập trình độc lập với chi tiết biểu diễn dữ liệu. Tư tưởng cốt lõi là định nghĩa một thuật toán hoặc cấu trúc dữ liệu không phụ thuộc vào một biểu diễn cụ thể nào, sau đó mới chỉ ra kiểu dữ liệu thích hợp làm tham số.
                    </p>
                    <p>
                        So sánh với các giải pháp truyền thống trong C:
                        <br><strong>- Tiền xử lý Macro (#define):</strong> Thay thế chuỗi văn bản đơn thuần trước khi dịch mã. Tiềm ẩn nguy cơ side-effects (ví dụ: <code>#define SWAP(a,b)</code>), không kiểm tra kiểu, cực kỳ khó gỡ lỗi (debug).
                        <br><strong>- Con trỏ vô kiểu (void*):</strong> Làm mất kiểm tra an toàn kiểu (Type Safety), đòi hỏi ép kiểu thủ công nguy hiểm, cản trở trình biên dịch tối ưu hóa inlining.
                        <br><strong>- C++ Template:</strong> Cơ chế sinh mã nguồn tĩnh tại thời điểm biên dịch (Compile-time code generation / Instantiation). Đạt được sự an toàn kiểu tuyệt đối (100% Type-safe) và hiệu năng thực thi tối đa (Zero-overhead abstraction).
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-microchip"></i> Cơ Chế Dưới Gầm Máy: Instantiation & Code Bloat</div>
                        <p class="text-sm text-zinc-700 font-sans leading-relaxed">
                            Bản thân một Template KHÔNG PHẢI là một hàm hay một lớp nhị phân! Nó là một công thức/bản vẽ thiết kế (Blueprint).
                            <br>- Khi trình biên dịch gặp một lời gọi cụ thể (ví dụ: <code>swap(a, b)</code> với <code>int</code>), nó tiến hành <strong>Instantiation</strong>: sinh ra một phiên bản hàm thực sự trong phân vùng mã lệnh (.text).
                            <br>- Nếu một template được sử dụng với 20 kiểu dữ liệu khác nhau, 20 phiên bản mã máy độc lập sẽ được tạo ra trong file đối tượng, dẫn đến hiện tượng <strong>Template Code Bloat</strong> (phình to kích thước file thực thi).
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP7-Template.pdf - Trang 2-10: Lập trình tổng quát & C++ Template]</span>
                </section>

                <!-- Theory Part 2 -->
                <section id="theory-function" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">2. Khuôn Mẫu Hàm (Function Templates) & Cơ Chế Suy Diễn Kiểu (Deduction)</h3>
                    <p>
                        Khuôn mẫu hàm cho phép định nghĩa một tập vô hạn các hàm nạp chồng với cùng một tên:
                        <br><code class="inline-code">template &lt;typename T&gt; void swap(T& a, T& b);</code>
                        <br><strong>Cơ chế phân giải của trình biên dịch:</strong>
                        <br>1. <strong>Suy Diễn Kiểu (Template Argument Deduction):</strong> Trình biên dịch tự động phân tích kiểu của các đối số truyền vào hàm để suy ra tham số kiểu <code>T</code>. <em>Quy tắc: Không có sự ép kiểu ngầm định khi suy diễn kiểu!</em> Nếu truyền <code>swap(5, 3.14)</code>, compiler sẽ báo lỗi xung đột suy diễn giữa <code>int</code> và <code>double</code>.
                        <br>2. <strong>Chỉ Định Tường Minh:</strong> Người dùng có thể ép kiểu cụ thể bằng cú pháp: <code class="inline-code">swap&lt;double&gt;(5, 3.14);</code>.
                        <br>3. <strong>Nạp Chồng Khuôn Mẫu Hàm:</strong> Khi có cả hàm non-template và hàm template cùng khớp hoàn hảo với tham số truyền vào, hàm <strong>Non-template luôn được ưu tiên lựa chọn</strong>.
                    </p>
                    <span class="citation-badge">[Nguồn: OOP7-Template.pdf - Trang 11-15: Khuôn mẫu hàm & Instantiation]</span>
                </section>

                <!-- Theory Part 3 -->
                <section id="theory-class" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">3. Khuôn Mẫu Lớp (Class Templates) & Cấu Trúc Template Stack</h3>
                    <p>
                        Tương tự khuôn mẫu hàm, khuôn mẫu lớp cho phép tạo ra các cấu trúc dữ liệu tổng quát:
                        <br><code class="inline-code">template &lt;typename T, typename U&gt; class Pair { T first; U second; };</code>
                        <br><strong>Các điểm kiến trúc đặc thù:</strong>
                        <br>- Không hề tồn tại struct nào tên là <code>Pair</code> trong file nhị phân, mà chỉ có các struct có tên cụ thể như <code>Pair&lt;int, int&gt;</code>, <code>Pair&lt;int, float&gt;</code>...
                        <br>- Trong chuẩn C++11, khi khai báo đối tượng bắt buộc phải dùng cặp dấu ngoặc nhọn: <code class="inline-code">Pair&lt;int, double&gt; p;</code>.
                        <br>- Khi định nghĩa phương thức của Class Template ở bên ngoài thân class, mỗi phương thức bắt buộc phải có tiền tố template riêng và tên lớp kèm tham số: <code class="inline-code">template &lt;typename T&gt; void Stack&lt;T&gt;::push(const T& val)</code>.
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-layer-group"></i> Bài Tập 7.1 Slide: Template Stack & Mảng Động Tổng Quát</div>
                        <p class="text-sm text-zinc-700 font-sans leading-relaxed">
                            Cấu trúc dữ liệu Stack tổng quát trong slide kết hợp quản lý bộ nhớ động <code>T* elements</code>, con trỏ quản lý chỉ mục <code>top</code>, và tuân thủ chặt chẽ mẫu thiết kế RAII. Destructor của Class Template tự động kích hoạt hủy từng phần tử và giải phóng vùng nhớ heap tương ứng với từng kiểu cụ thể.
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP7-Template.pdf - Trang 16-27: Khuôn mẫu lớp & Template Stack]</span>
                </section>

                <!-- Theory Part 4 -->
                <section id="theory-nttp" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">4. Non-Type Template Parameters (NTTP) & Tham Số Khuôn Mẫu Khác</h3>
                    <p>
                        Ngoài các tham số 'kiểu' (<code>typename T</code>), C++ hỗ trợ thêm 2 loại tham số cao cấp:
                        <br><strong>1. Non-Type Template Parameters (NTTP - Tham số phi kiểu):</strong>
                        <br>Cho phép truyền một giá trị hằng số biết trước tại thời điểm biên dịch làm tham số template: <code class="inline-code">template &lt;typename T, int Size&gt; class Stack;</code>.
                        <br>- <em>Ràng buộc C++11:</em> Chỉ nhận kiểu số nguyên (<code>int</code>, <code>long</code>), enum, hoặc con trỏ có static linkage. CẤM số thực <code>float/double</code> và chuỗi string literal!
                        <br>- <em>Hệ quả kiểu:</em> <code>Stack&lt;int, 10&gt;</code> và <code>Stack&lt;int, 20&gt;</code> là <strong>HAI KIỂU LỚP HOÀN TOÀN KHÁC BIỆT</strong> trong bộ nhớ và không thể gán cho nhau.
                        <br><strong>2. Template Template Parameters (Tham số khuôn mẫu là khuôn mẫu):</strong>
                        <br>Cho phép truyền một khuôn mẫu chưa cụ thể hóa làm tham số: <code class="inline-code">template &lt;typename T, template &lt;typename&gt; class Container&gt; class Map;</code>.
                    </p>
                    <span class="citation-badge">[Nguồn: OOP7-Template.pdf - Trang 28-36: Các tham số template khác & NTTP]</span>
                </section>

                <!-- Theory Part 5 -->
                <section id="theory-specialization" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">5. Đặc Tả Khuôn Mẫu (Template Specialization: Full vs Partial)</h3>
                    <p>
                        Khi một thuật toán tổng quát không tối ưu hoặc không áp dụng được cho một kiểu dữ liệu cụ thể (ví dụ: con trỏ hoặc kiểu <code>bool</code>), C++ cung cấp cơ chế <strong>Đặc Tả (Specialization)</strong>:
                        <br><strong>- Full Specialization (Đặc tả toàn phần):</strong> Thay thế toàn bộ định nghĩa template cho một kiểu cụ thể duy nhất. Cú pháp bắt đầu bằng <code class="inline-code">template &lt;&gt;</code>. Áp dụng cho cả Class Template và Function Template.
                        <br><strong>- Partial Specialization (Đặc tả từng phần):</strong> Tùy biến template cho một nhóm kiểu con (như mọi kiểu con trỏ <code>T*</code>, hoặc khi hai tham số kiểu trùng nhau <code>&lt;T, T&gt;</code>).
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-ban"></i> Cạm Bẫy Sống Còn: Function Templates Không Hỗ Trợ Partial Specialization!</div>
                        <p class="text-sm text-zinc-700 font-sans leading-relaxed">
                            Chuẩn ISO C++ <strong>CẤM TUYỆT ĐỐI</strong> đặc tả từng phần trên Function Template! Nếu muốn đặc tả từng phần cho hàm, lập trình viên bắt buộc phải sử dụng <em>Function Overloading</em> thông thường.
                            <br>- Lưu ý thứ tự ưu tiên (Sutter's Trap): Specialization của Function Template không tham gia vào quá trình Overload Resolution! Compiler luôn chọn Base Template tốt nhất trước rồi mới xét tới Specialization của chính Base Template đó.
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP7-Template.pdf - Trang 20-22 & ISO C++ Template Specialization rules]</span>
                </section>

                <!-- Theory Part 6 -->
                <section id="theory-modern" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">6. Kỹ Thuật Template Hiện Đại Trong Chuẩn C++11</h3>
                    <p>
                        Chuẩn C++11 đã nâng tầm Generic Programming lên một tầm cao mới với hàng loạt tính năng cách mạng:
                        <br><strong>1. Từ khóa typename cho Dependent Types:</strong> Bắt buộc dùng <code>typename T::subtype* ptr;</code> để thông báo cho compiler biết đó là một kiểu dữ liệu, giải quyết sự nhập nhằng cú pháp ở Phase 1.
                        <br><strong>2. Alias Templates (Bí danh khuôn mẫu):</strong> Thay thế <code>typedef</code> bằng cú pháp <code class="inline-code">template &lt;typename T&gt; using Vec = std::vector&lt;T&gt;;</code>.
                        <br><strong>3. Variadic Templates:</strong> Cho phép khuôn mẫu nhận số lượng tham số biến đổi (<code class="inline-code">typename... Args</code>) kết hợp toán tử đếm <code class="inline-code">sizeof...(Args)</code> và kỹ thuật đệ quy mở gói (Recursive Unpacking).
                        <br><strong>4. decltype & Trailing Return Type:</strong> Tự động suy diễn kiểu trả về của biểu thức: <code class="inline-code">auto add(T a, U b) -&gt; decltype(a + b);</code>.
                        <br><strong>5. Thư viện &lt;type_traits&gt; & SFINAE:</strong> Kiểm tra đặc tính kiểu lúc biên dịch và bật/tắt hàm có điều kiện bằng <code class="inline-code">std::enable_if</code>.
                    </p>
                    <span class="citation-badge">[Nguồn: C++11 Standard & OOP7-Template.pdf - Trang 28-36: Tính năng mở rộng hiện đại]</span>
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
                            50 Câu Trắc Nghiệm Code & Bẫy Khuôn Mẫu (Template) C++11 Chuyên Sâu
                        </h2>
                        <p class="text-xs text-zinc-500 mt-1">
                            100% dựa trên code thực tế: bẫy Two-Phase Lookup, Deduction Conflicts, NTTP restrictions, Sutter's Trap, SFINAE và Variadic
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
root_path = "c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/OOP7-Template.html"
baitap_path = "c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/Bài tập/OOP7-Template.html"

with open(root_path, "w", encoding="utf-8") as f:
    f.write(html_head_and_theory)

with open(baitap_path, "w", encoding="utf-8") as f:
    f.write(html_head_and_theory)

print(f"Chapter 7 standalone HTML successfully written to:\n  - {root_path}\n  - {baitap_path}\nSize: {len(html_head_and_theory)} bytes.")

