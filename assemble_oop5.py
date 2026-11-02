# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Import questions from build_oop5_quiz
import build_oop5_quiz
questions = build_oop5_quiz.questions

assert len(questions) == 50, f"Expected 50 questions, got {len(questions)}"

html_head_and_theory = """<!DOCTYPE html>
<html lang="vi" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chương 5: Kế Thừa (Inheritance) - MOSTest5_2</title>

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
                <i class="fa-solid fa-sitemap text-2xl text-red-200"></i>
                <div>
                    <h1 class="text-lg font-bold tracking-tight">C++11 Academic Masterclass</h1>
                    <p class="text-xs text-red-200 font-mono">Chương 5: Kế Thừa (Inheritance) & Cơ Chế Dưới Gầm Máy</p>
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
                        <a href="#theory-concept" class="block py-1.5 px-2.5 rounded hover:bg-red-50 hover:text-[#991b1b] transition text-zinc-700">1. Bản Chất Kế Thừa & IS-A vs HAS-A</a>
                        <a href="#theory-access" class="block py-1.5 px-2.5 rounded hover:bg-red-50 hover:text-[#991b1b] transition text-zinc-700">2. Quyền Truy Cập (public/protected/private)</a>
                        <a href="#theory-lifecycle" class="block py-1.5 px-2.5 rounded hover:bg-red-50 hover:text-[#991b1b] transition text-zinc-700">3. Vòng Đời Ctor / Dtor & Bài Tập Slide</a>
                        <a href="#theory-hiding" class="block py-1.5 px-2.5 rounded hover:bg-red-50 hover:text-[#991b1b] transition text-zinc-700">4. Che Khuất Tên (Name Hiding) & Overriding</a>
                        <a href="#theory-casting" class="block py-1.5 px-2.5 rounded hover:bg-red-50 hover:text-[#991b1b] transition text-zinc-700">5. Upcast, Downcast & Bẫy Slicing</a>
                        <a href="#theory-multiple" class="block py-1.5 px-2.5 rounded hover:bg-red-50 hover:text-[#991b1b] transition text-zinc-700">6. Đa Kế Thừa & Kế Thừa Ảo (Diamond)</a>
                    </nav>
                </div>

                <!-- TOC Quiz -->
                <div class="bg-white border border-zinc-200 rounded-lg p-5 shadow-sm">
                    <h2 class="text-xs font-bold uppercase tracking-wider text-[#991b1b] font-mono mb-3 flex items-center gap-2">
                        <i class="fa-solid fa-vial-circle-check"></i> 50 Câu Trắc Nghiệm Code
                    </h2>
                    <nav class="space-y-1 text-xs font-mono text-zinc-600">
                        <a href="#q-group-1" class="block py-1 px-2 rounded hover:bg-red-50 hover:text-[#991b1b] transition">Câu 01 - 08: Bố Cục Bộ Nhớ & Ctor/Dtor</a>
                        <a href="#q-group-2" class="block py-1 px-2 rounded hover:bg-red-50 hover:text-[#991b1b] transition">Câu 09 - 16: Quyền Truy Cập public/pro/pri</a>
                        <a href="#q-group-3" class="block py-1 px-2 rounded hover:bg-red-50 hover:text-[#991b1b] transition">Câu 17 - 24: Che Khuất Tên & Overriding</a>
                        <a href="#q-group-4" class="block py-1 px-2 rounded hover:bg-red-50 hover:text-[#991b1b] transition">Câu 25 - 34: Upcast, Downcast & Slicing</a>
                        <a href="#q-group-5" class="block py-1 px-2 rounded hover:bg-red-50 hover:text-[#991b1b] transition">Câu 35 - 44: Đa Kế Thừa & Kế Thừa Ảo</a>
                        <a href="#q-group-6" class="block py-1 px-2 rounded hover:bg-red-50 hover:text-[#991b1b] transition">Câu 45 - 50: C++11 Inheriting & Nâng Cao</a>
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
                        Chương 5: Cơ Chế Kế Thừa (Inheritance) & Kiến Trúc Dưới Gầm Máy
                    </h2>
                    <p class="text-sm text-zinc-500 font-serif italic mt-1">
                        Trích xuất toàn diện từ slide bài giảng OOP5-Inheritance_new.pdf (81 trang) và OOP5-Inheritance_Baitap.pdf (6 trang)
                    </p>
                </div>

                <!-- Theory Part 1 -->
                <section id="theory-concept" class="theory-content space-y-4">
                    <h3 class="text-xl">1. Bản Chất Kế Thừa & Cơ Chế Tái Sử Dụng Mã Nguồn</h3>
                    <p>
                        Trong kỹ nghệ phần mềm, sao chép mã nguồn (copy-paste) dẫn tới sự phình to kích thước chương trình, khó khăn khi bảo trì và chi phí nâng cấp tốn kém. Hiện tượng trùng lặp thông tin thường xuất hiện ở 2 dạng:
                        <br><strong>- Dạng chia sẻ:</strong> Hai thực thể có phần chung giao nhau ($A \cap B \neq \emptyset$).
                        <br><strong>- Dạng mở rộng:</strong> Thực thể $B$ bao hàm trọn vẹn $A$ và bổ sung thêm các đặc tính riêng ($B = A + \epsilon$).
                    </p>
                    <p>
                        Kế thừa giải quyết bài toán trên bằng cách cho phép một lớp dẫn xuất (Derived Class) thừa hưởng các thuộc tính và phương thức của lớp cơ sở (Base Class). Tuy nhiên, cần phân biệt rõ hai mối quan hệ nền tảng:
                        <br><strong>- IS-A (Kế Thừa):</strong> Thể hiện mối quan hệ bản chất chủng loại. Ví dụ: <code>Car IS-A MotorVehicle</code> (Ô tô là một loại phương tiện cơ giới). Dùng <code>public inheritance</code>.
                        <br><strong>- HAS-A (Bao Đóng / Composition):</strong> Thể hiện mối quan hệ sở hữu. Ví dụ: <code>Car HAS-A Engine</code> (Xe ô tô có một động cơ). Luôn ưu tiên dùng biến thành viên thay vì kế thừa.
                    </p>

                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-microchip"></i> Cơ Chế Dưới Gầm Máy: Bố Cục Bộ Nhớ Của Đối Tượng Kế Thừa (Memory Layout)</div>
                        <p class="text-sm text-zinc-700 font-sans leading-relaxed">
                            Khi một lớp dẫn xuất được cấp phát trong RAM, trình biên dịch bố trí <strong>Base Class Subobject nằm ngay ở phần đầu (offset 0)</strong> của cấu trúc bộ nhớ. Ngay sau Base Subobject là các trường dữ liệu riêng của lớp dẫn xuất theo thứ tự khai báo.
                            <br>- Do đó, địa chỉ raw của đối tượng <code>Derived</code> trùng khớp hoàn toàn với địa chỉ của <code>Base</code> subobject trong đơn kế thừa, cho phép phép toán Upcasting diễn ra với chi phí CPU bằng 0 (Zero-overhead conversion).
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP5-Inheritance_new.pdf - Trang 2-15 & 47-49: Khái niệm & Quan hệ IS-A vs HAS-A]</span>
                </section>

                <!-- Theory Part 2 -->
                <section id="theory-access" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">2. Cú Pháp & Bảng Quyền Truy Cập (public, protected, private)</h3>
                    <p>
                        C++ cung cấp 3 từ khóa định nghĩa kiểu thừa kế: <code class="inline-code">class Derived : [access-specifier] Base</code>. Ma trận biến đổi quyền truy cập như sau:
                    </p>
                    <div class="overflow-x-auto my-3">
                        <table class="min-w-full text-xs font-sans border border-zinc-200 text-left">
                            <thead class="bg-zinc-100 font-bold text-zinc-700">
                                <tr>
                                    <th class="p-2 border">Quyền ở Lớp Cơ Sở (Base)</th>
                                    <th class="p-2 border">Thừa Kế Public</th>
                                    <th class="p-2 border">Thừa Kế Protected</th>
                                    <th class="p-2 border">Thừa Kế Private</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="p-2 border font-mono text-emerald-700">public</td>
                                    <td class="p-2 border font-semibold text-emerald-700">public</td>
                                    <td class="p-2 border font-semibold text-amber-700">protected</td>
                                    <td class="p-2 border font-semibold text-rose-700">private</td>
                                </tr>
                                <tr>
                                    <td class="p-2 border font-mono text-amber-700">protected</td>
                                    <td class="p-2 border font-semibold text-amber-700">protected</td>
                                    <td class="p-2 border font-semibold text-amber-700">protected</td>
                                    <td class="p-2 border font-semibold text-rose-700">private</td>
                                </tr>
                                <tr>
                                    <td class="p-2 border font-mono text-rose-700">private</td>
                                    <td class="p-2 border text-zinc-400 italic">Không truy cập được</td>
                                    <td class="p-2 border text-zinc-400 italic">Không truy cập được</td>
                                    <td class="p-2 border text-zinc-400 italic">Không truy cập được</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-shield-halved"></i> Cơ Chế Dưới Gầm Máy: Compile-time Access Checking</div>
                        <p class="text-sm text-zinc-700 font-sans leading-relaxed">
                            Từ khóa bảo vệ (<code>public</code>, <code>protected</code>, <code>private</code>) chỉ là một cơ chế kiểm tra tính hợp lệ tại <strong>thời điểm biên dịch (Compile-time)</strong>. Chúng hoàn toàn biến mất trong file nhị phân (Binary) sau khi biên dịch và không hề tiêu tốn một byte RAM nào.
                            <br>- Trong C++, <code>struct</code> mặc định kế thừa <code>public</code>, còn <code>class</code> mặc định kế thừa <code>private</code>.
                            <br>- Lớp dẫn xuất có thể sử dụng chỉ thị <code class="inline-code">using Base::member;</code> để tái công khai (unhide hoặc promote) một thành viên từ protected lên public.
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP5-Inheritance_new.pdf - Trang 31-40: Quyền truy nhập public, protected, private]</span>
                </section>

                <!-- Theory Part 3 -->
                <section id="theory-lifecycle" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">3. Vòng Đời Đối Tượng: Trình Tự Thực Thi Constructor & Destructor</h3>
                    <p>
                        Quy tắc bất biến trong C++: <strong>Xây nền tảng trước, xây tầng trên sau; Hủy tầng trên trước, dỡ nền tảng sau</strong>.
                        <br><strong>- Quá trình Khởi tạo (Construction):</strong>
                        1. Khởi tạo Base Class Subobject (thông qua Member Initializer List của Derived).
                        2. Khởi tạo các biến thành viên của Derived theo đúng <em>thứ tự khai báo</em> trong định nghĩa class.
                        3. Thực thi thân hàm Constructor của Derived.
                        <br><strong>- Quá trình Hủy (Destruction):</strong>
                        Diễn ra theo thứ tự ngăn xếp LIFO hoàn toàn ngược lại. Thân Destructor của Derived chạy trước, rồi giải phóng các thành viên riêng, cuối cùng gọi Base Destructor.
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-code-branch"></i> Bẫy Lập Trình: Side-effects trong Constructor Chaining (Bài Tập 1 Slide)</div>
                        <p class="text-sm text-zinc-700 font-sans leading-relaxed">
                            Xét ví dụ bài tập trang 2 slide OOP5-Baitap: <code class="inline-code">Z(int i) : Y(i++) {}</code>.
                            <br>- Constructor của <code>Y</code> nhận giá trị cũ của <code>i</code> trước khi tăng (do toán tử hậu tố <code>i++</code>).
                            <br>- Sau khi hoàn thành khởi tạo cho <code>Y</code>, biến <code>i</code> của <code>Z</code> mới mang giá trị mới.
                            <br>- Nếu lớp dẫn xuất tự định nghĩa <strong>Copy Constructor</strong> mà quên gọi tường minh <code>Base(other)</code> trong danh sách khởi tạo, trình biên dịch sẽ tự động gọi <em>Default Constructor</em> của Base, làm mất sạch dữ liệu sao chép của lớp cha!
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP5-Inheritance_new.pdf - Trang 29-30 & OOP5-Inheritance_Baitap.pdf - Trang 2: Thứ tự gọi hàm dựng]</span>
                </section>

                <!-- Theory Part 4 -->
                <section id="theory-hiding" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">4. Hiện Tượng Che Khuất Tên (Name Hiding) & Tái Định Nghĩa (Overriding)</h3>
                    <p>
                        Một lỗi hiểu lầm nghiêm trọng của người học C++ là cho rằng Function Overloading có thể diễn ra xuyên suốt cây kế thừa giữa Base và Derived.
                        <br><strong>Quy tắc Name Lookup:</strong> Nếu lớp dẫn xuất khai báo bất kỳ hàm nào trùng tên với hàm của lớp cha (bất kể danh sách tham số và kiểu trả về có khác biệt hay không), toàn bộ các hàm cùng tên ở lớp cha sẽ bị <strong>CHE KHUẤT (Shadowed / Hidden)</strong> hoàn toàn khỏi scope của lớp dẫn xuất.
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-eye-slash"></i> Cơ Chế Dưới Gầm Máy: Name Lookup vs Overload Resolution</div>
                        <p class="text-sm text-zinc-700 font-sans leading-relaxed">
                            Trình biên dịch thực hiện tìm kiếm tên (Name Lookup) từ scope hiện tại trước. Ngay khi tìm thấy tên hàm trong <code>Derived</code>, quá trình tìm kiếm dừng lại và chuyển sang bước kiểm tra kiểu (Type Checking). Nó không bao giờ tìm kiếm tiếp lên scope của <code>Base</code>.
                            <br>- Để khôi phục các hàm của Base vào bộ nạp chồng của Derived, ta phải sử dụng chỉ thị: <code class="inline-code">using Base::func_name;</code>.
                            <br>- Biến thành viên trùng tên giữa Base và Derived cũng bị che khuất tương tự: cả hai biến đều cùng tồn tại trong RAM ở các offset khác nhau, truy cập bằng cú pháp <code class="inline-code">Base::variable</code>.
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP5-Inheritance_new.pdf - Trang 41-46: Overriding & Name Hiding]</span>
                </section>

                <!-- Theory Part 5 -->
                <section id="theory-casting" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">5. Chuyển Kiểu Trong Kế Thừa: Upcasting, Downcasting & Bẫy Cắt Xén (Object Slicing)</h3>
                    <p>
                        Kế thừa công khai tạo ra mối quan hệ subtype tự nhiên:
                        <br><strong>- Upcasting (Ép kiểu lên):</strong> Chuyển con trỏ hoặc tham chiếu từ <code>Derived* / Derived&</code> thành <code>Base* / Base&</code>. Đây là phép biến đổi hoàn toàn an toàn, ngầm định (implicit) và không mất chi phí runtime.
                        <br><strong>- Downcasting (Ép kiểu xuống):</strong> Chuyển từ <code>Base*</code> thành <code>Derived*</code>. Đây là phép toán nguy hiểm vì con trỏ Base có thể không thực sự trỏ tới một đối tượng Derived hoàn chỉnh. Phải dùng <code class="inline-code">dynamic_cast</code> (đòi hỏi lớp phải có ít nhất 1 hàm virtual để sinh RTTI) hoặc <code class="inline-code">static_cast</code> (nếu chắc chắn 100% để tránh chi phí RTTI).
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-scissors"></i> Bẫy Tử Thần: Object Slicing (Cắt Xén Đối Tượng)</div>
                        <p class="text-sm text-zinc-700 font-sans leading-relaxed">
                            Hiện tượng <strong>Object Slicing</strong> xảy ra khi truyền tham trị một đối tượng Derived vào một biến nhận kiểu Base: <code class="inline-code">Base b = derivedObj;</code> hoặc <code class="inline-code">void func(Base b);</code>.
                            <br>- Khi đó, hàm khởi tạo sao chép <code>Base::Base(const Base&)</code> được gọi, nó CHỈ sao chép phần Base subobject, toàn bộ dữ liệu thành viên mở rộng và con trỏ ảo của Derived bị "cắt phăng" hoàn toàn!
                            <br>- Đối tượng <code>b</code> trở thành một Base nguyên thủy, mất hoàn toàn tính đa hình động. <em>Quy tắc vàng: Luôn truyền đối tượng đa hình qua Con trỏ (Pointer) hoặc Tham chiếu hằng (Const Reference)!</em>
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP5-Inheritance_new.pdf - Trang 50-70: Upcast, Downcast và Object Slicing]</span>
                </section>

                <!-- Theory Part 6 -->
                <section id="theory-multiple" class="theory-content space-y-4 pt-6 border-t border-zinc-200">
                    <h3 class="text-xl">6. Đa Kế Thừa & Kế Thừa Ảo (The Diamond Problem)</h3>
                    <p>
                        C++ hỗ trợ đa kế thừa (Multiple Inheritance), cho phép một lớp dẫn xuất từ nhiều lớp cơ sở: <code class="inline-code">class C : public A, public B</code>.
                        <br>Mô hình này tiềm ẩn hiểm họa <strong>Vấn Đề Hình Thoi (The Diamond Problem)</strong>: Khi cả $B$ và $C$ đều kế thừa từ $A$, và lớp $D$ kế thừa cả $B$ và $C$.
                        <br>- Trong bộ nhớ của $D$, sẽ tồn tại <strong>HAI bản sao độc lập của $A$</strong>. Bất kỳ thao tác truy cập nào tới thành viên của $A$ qua $D$ sẽ bị compiler báo lỗi mơ hồ (Ambiguous member).
                    </p>
                    <div class="under-the-hood">
                        <div class="under-the-hood-title"><i class="fa-solid fa-gem"></i> Cơ Chế Dưới Gầm Máy: Kế Thừa Ảo (Virtual Inheritance) & vbptr</div>
                        <p class="text-sm text-zinc-700 font-sans leading-relaxed">
                            Để giải quyết vấn đề hình thoi, C++ đưa ra <strong>Kế Thừa Ảo</strong>: <code class="inline-code">class B : virtual public A</code> và <code class="inline-code">class C : virtual public A</code>.
                            <br>1. <strong>Đồng nhất Subobject:</strong> Trình biên dịch hợp nhất 2 bản sao thành duy nhất MỘT subobject $A$ dùng chung trong lòng đối tượng $D$.
                            <br>2. <strong>Trách nhiệm của Most-Derived Class:</strong> Lớp dẫn xuất xa nhất ($D$) chịu trách nhiệm trực tiếp gọi Constructor của Virtual Base ($A$), bỏ qua mọi lời gọi tới $A$ từ $B$ và $C$.
                            <br>3. <strong>Chi phí bộ nhớ:</strong> Để định vị được subobject $A$ ảo trong thời gian chạy, trình biên dịch phải chèn thêm một con trỏ cơ sở ảo (<strong>vbptr</strong> - Virtual Base Pointer) hoặc lưu offset trong VTable, làm tăng kích thước của đối tượng thêm 8-16 bytes trên kiến trúc 64-bit.
                        </p>
                    </div>
                    <span class="citation-badge">[Nguồn: OOP5-Inheritance_new.pdf - Trang 71-76: Đa thừa kế, Sự mơ hồ & Lớp cơ sở ảo]</span>
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
                            50 Câu Trắc Nghiệm Code & Bẫy Kế Thừa C++11 Chuyên Sâu
                        </h2>
                        <p class="text-xs text-zinc-500 mt-1">
                            100% dựa trên các đoạn code thực tế: bẫy Slicing, Downcast UB, Name Hiding, Diamond Problem, EBO và C++11 Inheriting Ctor
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
root_path = "c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/OOP5-Inheritance_new.html"
baitap_path = "c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/Bài tập/OOP5-Inheritance_new.html"

with open(root_path, "w", encoding="utf-8") as f:
    f.write(html_head_and_theory)

with open(baitap_path, "w", encoding="utf-8") as f:
    f.write(html_head_and_theory)

print(f"Chapter 5 standalone HTML successfully written to:\n  - {root_path}\n  - {baitap_path}\nSize: {len(html_head_and_theory)} bytes.")

