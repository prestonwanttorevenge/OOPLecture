# -*- coding: utf-8 -*-
"""
Builder for Master Curriculum Dashboard: index.html
Style: MOSTest5_2 (Academic Minimalist Brutalism, Red-800 Tor-sur-ton)
"""
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_content = """<!DOCTYPE html>
<html lang="vi" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>C++11 OOP Academic Masterclass - Cổng Học Tập & Khảo Thí Toàn Diện</title>

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

    <style>
        body {
            background-color: #fafafa;
            color: #18181b;
            font-family: 'Inter', sans-serif;
        }

        .chapter-card {
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .chapter-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 25px -5px rgba(153, 27, 27, 0.12), 0 8px 10px -6px rgba(153, 27, 27, 0.08);
            border-color: #b91c1c;
        }
    </style>
</head>
<body class="antialiased min-h-screen flex flex-col">

    <!-- Top Navigation Header -->
    <header class="sticky top-0 z-50 bg-[#991b1b] text-white shadow-md border-b border-red-900">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <i class="fa-solid fa-graduation-cap text-2xl text-red-200"></i>
                <div>
                    <h1 class="text-lg font-bold tracking-tight">C++11 OOP Academic Masterclass</h1>
                    <p class="text-xs text-red-200 font-mono">Hệ Thống Lý Thuyết Chuyên Sâu & 400 Câu Khảo Thí Code Dưới Gầm Máy</p>
                </div>
            </div>
            <div class="flex items-center space-x-4">
                <span class="text-xs font-mono bg-red-900/70 border border-red-700/60 px-3 py-1.5 rounded text-red-100 font-semibold">
                    <i class="fa-solid fa-shield-halved text-emerald-400 mr-1"></i> Chuẩn MOSTest5_2
                </span>
            </div>
        </div>
    </header>

    <!-- Hero Banner -->
    <div class="bg-gradient-to-b from-red-50 to-transparent border-b border-zinc-200 py-12 px-4 sm:px-6 lg:px-8 text-center">
        <div class="max-w-4xl mx-auto space-y-4">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-mono font-bold bg-red-100 text-[#991b1b] border border-red-200">
                <i class="fa-solid fa-bolt"></i> 8 CHƯƠNG TOÀN DIỆN • 400 BẪY CODE C++11 • 100% CƠ CHẾ DƯỚI GẦM MÁY
            </div>
            <h2 class="text-3xl sm:text-5xl font-black text-zinc-900 tracking-tight font-sans uppercase">
                Giáo Trình C++11 Hướng Đối Tượng & Trắc Nghiệm Chuyên Sâu
            </h2>
            <p class="text-base sm:text-lg text-zinc-600 font-serif max-w-3xl mx-auto leading-relaxed">
                Hệ thống học tập và khảo thí học thuật toàn diện được trích xuất trực tiếp từ toàn bộ slide bài giảng OOP Bách Khoa Đà Nẵng, kết hợp phân tích sâu sắc cấu trúc bộ nhớ RAM, phân mảnh Heap, VTable/vptr, Stack Unwinding và tiêu chuẩn ISO C++11.
            </p>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 max-w-2xl mx-auto pt-4 text-center font-mono">
                <div class="p-3 bg-white border border-zinc-200 rounded-lg shadow-sm">
                    <div class="text-2xl font-black text-[#991b1b]">8</div>
                    <div class="text-xs text-zinc-500 uppercase">Chương Học</div>
                </div>
                <div class="p-3 bg-white border border-zinc-200 rounded-lg shadow-sm">
                    <div class="text-2xl font-black text-[#991b1b]">400</div>
                    <div class="text-xs text-zinc-500 uppercase">Câu Trắc Nghiệm Code</div>
                </div>
                <div class="p-3 bg-white border border-zinc-200 rounded-lg shadow-sm">
                    <div class="text-2xl font-black text-[#991b1b]">100%</div>
                    <div class="text-xs text-zinc-500 uppercase">Giải Thích Gầm Máy</div>
                </div>
                <div class="p-3 bg-white border border-zinc-200 rounded-lg shadow-sm">
                    <div class="text-2xl font-black text-[#991b1b]">C++11</div>
                    <div class="text-xs text-zinc-500 uppercase">Chuẩn Học Thuật</div>
                </div>
            </div>
        </div>
    </div>

    <!-- Main Modules Grid -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 flex-1 w-full">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">

            <!-- Module 1 -->
            <div class="chapter-card bg-white border border-zinc-200 rounded-lg p-6 flex flex-col justify-between shadow-sm">
                <div class="space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-mono font-bold text-white bg-[#991b1b] px-2.5 py-0.5 rounded">
                            CHƯƠNG 01
                        </span>
                        <span class="text-xs font-mono text-zinc-500">50 MCQs • 120 KB</span>
                    </div>
                    <h3 class="text-xl font-bold text-zinc-900 font-sans tracking-tight">
                        Từ C Sang C++ & Các Mở Rộng Cơ Bản
                    </h3>
                    <p class="text-xs text-zinc-600 font-serif leading-relaxed">
                        Tham chiếu (References), Khác biệt với Con trỏ, Toán tử new/delete vs malloc/free, Ép kiểu C++11 (static_cast, const_cast, reinterpret_cast), Inline functions, Con trỏ hàm và Nạp chồng hàm.
                    </p>
                    <div class="text-xs font-mono text-zinc-500 pt-1">
                        <span class="text-[#991b1b] font-semibold"><i class="fa-solid fa-file-pdf mr-1"></i> Nguồn:</span> OOP1-C to C++-New.pdf (70 trang)
                    </div>
                </div>
                <div class="pt-5 mt-4 border-t border-zinc-100 flex items-center justify-between">
                    <span class="text-xs font-mono text-emerald-700 font-bold"><i class="fa-solid fa-circle-check"></i> Đầy đủ Lý Thuyết & 50 Quiz</span>
                    <a href="OOP1-C_to_C++.html" class="px-4 py-2 bg-[#991b1b] hover:bg-red-700 text-white text-xs font-bold font-sans rounded transition shadow-sm flex items-center gap-1.5">
                        Khám Phá <i class="fa-solid fa-arrow-right"></i>
                    </a>
                </div>
            </div>

            <!-- Module 2 -->
            <div class="chapter-card bg-white border border-zinc-200 rounded-lg p-6 flex flex-col justify-between shadow-sm">
                <div class="space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-mono font-bold text-white bg-[#991b1b] px-2.5 py-0.5 rounded">
                            CHƯƠNG 02
                        </span>
                        <span class="text-xs font-mono text-zinc-500">50 MCQs • 113 KB</span>
                    </div>
                    <h3 class="text-xl font-bold text-zinc-900 font-sans tracking-tight">
                        Tổng Quan Lập Trình Hướng Đối Tượng (OOP)
                    </h3>
                    <p class="text-xs text-zinc-600 font-serif leading-relaxed">
                        Tiến hóa từ Lập trình thủ tục sang Hướng đối tượng, 3 đặc trưng cốt lõi của Object (Identity, State, Behavior), Tính đóng gói (Encapsulation), Cơ chế truyền thông điệp (Message Passing) và 4 Trụ cột OOP.
                    </p>
                    <div class="text-xs font-mono text-zinc-500 pt-1">
                        <span class="text-[#991b1b] font-semibold"><i class="fa-solid fa-file-pdf mr-1"></i> Nguồn:</span> OOP2-introduction_new.pdf (48 trang)
                    </div>
                </div>
                <div class="pt-5 mt-4 border-t border-zinc-100 flex items-center justify-between">
                    <span class="text-xs font-mono text-emerald-700 font-bold"><i class="fa-solid fa-circle-check"></i> Đầy đủ Lý Thuyết & 50 Quiz</span>
                    <a href="OOP2-introduction_new.html" class="px-4 py-2 bg-[#991b1b] hover:bg-red-700 text-white text-xs font-bold font-sans rounded transition shadow-sm flex items-center gap-1.5">
                        Khám Phá <i class="fa-solid fa-arrow-right"></i>
                    </a>
                </div>
            </div>

            <!-- Module 3 -->
            <div class="chapter-card bg-white border border-zinc-200 rounded-lg p-6 flex flex-col justify-between shadow-sm">
                <div class="space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-mono font-bold text-white bg-[#991b1b] px-2.5 py-0.5 rounded">
                            CHƯƠNG 03
                        </span>
                        <span class="text-xs font-mono text-zinc-500">50 MCQs • 109 KB</span>
                    </div>
                    <h3 class="text-xl font-bold text-zinc-900 font-sans tracking-tight">
                        Lớp & Đối Tượng (Class & Objects)
                    </h3>
                    <p class="text-xs text-zinc-600 font-serif leading-relaxed">
                        Khai báo Header vs Source, Con trỏ this và tối ưu hóa con trỏ vô hình, Constructors & Destructors, Copy Constructor & Bẫy Deep/Shallow Copy, Hàm bạn (friend), Thành viên static/const, Hợp thành (Composition).
                    </p>
                    <div class="text-xs font-mono text-zinc-500 pt-1">
                        <span class="text-[#991b1b] font-semibold"><i class="fa-solid fa-file-pdf mr-1"></i> Nguồn:</span> OOP3-Class&Objec_new.pdf (78 trang)
                    </div>
                </div>
                <div class="pt-5 mt-4 border-t border-zinc-100 flex items-center justify-between">
                    <span class="text-xs font-mono text-emerald-700 font-bold"><i class="fa-solid fa-circle-check"></i> Đầy đủ Lý Thuyết & 50 Quiz</span>
                    <a href="OOP3-Class&Objec_new.html" class="px-4 py-2 bg-[#991b1b] hover:bg-red-700 text-white text-xs font-bold font-sans rounded transition shadow-sm flex items-center gap-1.5">
                        Khám Phá <i class="fa-solid fa-arrow-right"></i>
                    </a>
                </div>
            </div>

            <!-- Module 4 -->
            <div class="chapter-card bg-white border border-zinc-200 rounded-lg p-6 flex flex-col justify-between shadow-sm">
                <div class="space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-mono font-bold text-white bg-[#991b1b] px-2.5 py-0.5 rounded">
                            CHƯƠNG 04
                        </span>
                        <span class="text-xs font-mono text-zinc-500">50 MCQs • 102 KB</span>
                    </div>
                    <h3 class="text-xl font-bold text-zinc-900 tracking-tight font-sans">
                        Quá Tải Toán Tử (Operator Overloading)
                    </h3>
                    <p class="text-xs text-zinc-600 font-serif leading-relaxed">
                        Giới hạn ngôn ngữ (5 toán tử cấm nạp chồng), Member vs Non-member/Friend, Toán tử nhập xuất (&lt;&lt;, &gt;&gt;), Chỉ mục mảng [], Lời gọi hàm (), Chuyển đổi kiểu (Conversion Operators), Tiền tố/Hậu tố ++/--, Toán tử gán =.
                    </p>
                    <div class="text-xs font-mono text-zinc-500 pt-1">
                        <span class="text-[#991b1b] font-semibold"><i class="fa-solid fa-file-pdf mr-1"></i> Nguồn:</span> OOP4-OperatorOverloading_new.pdf (47 trang)
                    </div>
                </div>
                <div class="pt-5 mt-4 border-t border-zinc-100 flex items-center justify-between">
                    <span class="text-xs font-mono text-emerald-700 font-bold"><i class="fa-solid fa-circle-check"></i> Đầy đủ Lý Thuyết & 50 Quiz</span>
                    <a href="OOP4-OperatorOverloading_new.html" class="px-4 py-2 bg-[#991b1b] hover:bg-red-700 text-white text-xs font-bold font-sans rounded transition shadow-sm flex items-center gap-1.5">
                        Khám Phá <i class="fa-solid fa-arrow-right"></i>
                    </a>
                </div>
            </div>

            <!-- Module 5 -->
            <div class="chapter-card bg-white border border-zinc-200 rounded-lg p-6 flex flex-col justify-between shadow-sm">
                <div class="space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-mono font-bold text-white bg-[#991b1b] px-2.5 py-0.5 rounded">
                            CHƯƠNG 05
                        </span>
                        <span class="text-xs font-mono text-zinc-500">50 MCQs • 118 KB</span>
                    </div>
                    <h3 class="text-xl font-bold text-zinc-900 tracking-tight font-sans">
                        Tính Kế Thừa (Inheritance)
                    </h3>
                    <p class="text-xs text-zinc-600 font-serif leading-relaxed">
                        Quan hệ IS-A vs HAS-A, Quyền truy cập (public, protected, private), Trình tự thực thi Ctor/Dtor, Che khuất tên (Name Hiding), Upcasting & Bẫy Cắt Xén (Object Slicing), Đa kế thừa & Vấn đề hình thoi (Virtual Base Class).
                    </p>
                    <div class="text-xs font-mono text-zinc-500 pt-1">
                        <span class="text-[#991b1b] font-semibold"><i class="fa-solid fa-file-pdf mr-1"></i> Nguồn:</span> OOP5-Inheritance_new.pdf (81 trang) + Bài tập (6 trang)
                    </div>
                </div>
                <div class="pt-5 mt-4 border-t border-zinc-100 flex items-center justify-between">
                    <span class="text-xs font-mono text-emerald-700 font-bold"><i class="fa-solid fa-circle-check"></i> Đầy đủ Lý Thuyết & 50 Quiz</span>
                    <a href="OOP5-Inheritance_new.html" class="px-4 py-2 bg-[#991b1b] hover:bg-red-700 text-white text-xs font-bold font-sans rounded transition shadow-sm flex items-center gap-1.5">
                        Khám Phá <i class="fa-solid fa-arrow-right"></i>
                    </a>
                </div>
            </div>

            <!-- Module 6 -->
            <div class="chapter-card bg-white border border-zinc-200 rounded-lg p-6 flex flex-col justify-between shadow-sm">
                <div class="space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-mono font-bold text-white bg-[#991b1b] px-2.5 py-0.5 rounded">
                            CHƯƠNG 06
                        </span>
                        <span class="text-xs font-mono text-zinc-500">50 MCQs • 118 KB</span>
                    </div>
                    <h3 class="text-xl font-bold text-zinc-900 tracking-tight font-sans">
                        Tính Đa Hình (Polymorphism)
                    </h3>
                    <p class="text-xs text-zinc-600 font-serif leading-relaxed">
                        Static vs Dynamic Polymorphism, Overloading vs Overriding, C++11 override & final, Cơ chế Bảng Ảo (VTable) & Con trỏ vptr, Destructor Ảo ngăn chặn rò rỉ heap, Lớp Trừu Tượng & Pure Virtual, Bẫy hàm ảo trong Constructor.
                    </p>
                    <div class="text-xs font-mono text-zinc-500 pt-1">
                        <span class="text-[#991b1b] font-semibold"><i class="fa-solid fa-file-pdf mr-1"></i> Nguồn:</span> OOP6-Polymorphism_new.pdf (45 trang)
                    </div>
                </div>
                <div class="pt-5 mt-4 border-t border-zinc-100 flex items-center justify-between">
                    <span class="text-xs font-mono text-emerald-700 font-bold"><i class="fa-solid fa-circle-check"></i> Đầy đủ Lý Thuyết & 50 Quiz</span>
                    <a href="OOP6-Polymorphism_new.html" class="px-4 py-2 bg-[#991b1b] hover:bg-red-700 text-white text-xs font-bold font-sans rounded transition shadow-sm flex items-center gap-1.5">
                        Khám Phá <i class="fa-solid fa-arrow-right"></i>
                    </a>
                </div>
            </div>

            <!-- Module 7 -->
            <div class="chapter-card bg-white border border-zinc-200 rounded-lg p-6 flex flex-col justify-between shadow-sm">
                <div class="space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-mono font-bold text-white bg-[#991b1b] px-2.5 py-0.5 rounded">
                            CHƯƠNG 07
                        </span>
                        <span class="text-xs font-mono text-zinc-500">50 MCQs • 114 KB</span>
                    </div>
                    <h3 class="text-xl font-bold text-zinc-900 tracking-tight font-sans">
                        Khuôn Mẫu (Templates & Generic Programming)
                    </h3>
                    <p class="text-xs text-zinc-600 font-serif leading-relaxed">
                        Lập trình tổng quát C vs C++, Function Templates & Suy diễn kiểu, Class Templates & Template Stack, Non-Type Template Parameters (NTTP), Template Specialization (Full & Partial), Variadic Templates & SFINAE trong C++11.
                    </p>
                    <div class="text-xs font-mono text-zinc-500 pt-1">
                        <span class="text-[#991b1b] font-semibold"><i class="fa-solid fa-file-pdf mr-1"></i> Nguồn:</span> OOP7-Template.pdf (37 trang)
                    </div>
                </div>
                <div class="pt-5 mt-4 border-t border-zinc-100 flex items-center justify-between">
                    <span class="text-xs font-mono text-emerald-700 font-bold"><i class="fa-solid fa-circle-check"></i> Đầy đủ Lý Thuyết & 50 Quiz</span>
                    <a href="OOP7-Template.html" class="px-4 py-2 bg-[#991b1b] hover:bg-red-700 text-white text-xs font-bold font-sans rounded transition shadow-sm flex items-center gap-1.5">
                        Khám Phá <i class="fa-solid fa-arrow-right"></i>
                    </a>
                </div>
            </div>

            <!-- Module 8 -->
            <div class="chapter-card bg-white border border-zinc-200 rounded-lg p-6 flex flex-col justify-between shadow-sm">
                <div class="space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-mono font-bold text-white bg-[#991b1b] px-2.5 py-0.5 rounded">
                            CHƯƠNG 08
                        </span>
                        <span class="text-xs font-mono text-zinc-500">50 MCQs • 102 KB</span>
                    </div>
                    <h3 class="text-xl font-bold text-zinc-900 tracking-tight font-sans">
                        Xử Lý Ngoại Lệ (Exception Handling)
                    </h3>
                    <p class="text-xs text-zinc-600 font-serif leading-relaxed">
                        Mã lỗi truyền thống vs Ngoại lệ, Cơ chế throw & try-catch, Stack Unwinding tự động hủy đối tượng LIFO, Bẫy Slicing trong catch, Cây phân cấp std::exception, Từ khóa noexcept trong C++11, Ngoại lệ trong Constructor và Destructor.
                    </p>
                    <div class="text-xs font-mono text-zinc-500 pt-1">
                        <span class="text-[#991b1b] font-semibold"><i class="fa-solid fa-file-pdf mr-1"></i> Nguồn:</span> OOP8-Exception.pdf (44 trang)
                    </div>
                </div>
                <div class="pt-5 mt-4 border-t border-zinc-100 flex items-center justify-between">
                    <span class="text-xs font-mono text-emerald-700 font-bold"><i class="fa-solid fa-circle-check"></i> Đầy đủ Lý Thuyết & 50 Quiz</span>
                    <a href="OOP8-Exception.html" class="px-4 py-2 bg-[#991b1b] hover:bg-red-700 text-white text-xs font-bold font-sans rounded transition shadow-sm flex items-center gap-1.5">
                        Khám Phá <i class="fa-solid fa-arrow-right"></i>
                    </a>
                </div>
            </div>

        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-zinc-900 text-zinc-400 py-8 border-t border-zinc-800 text-center font-sans text-xs space-y-2">
        <div class="max-w-7xl mx-auto px-4">
            <p class="text-zinc-300 font-medium font-serif">
                Hệ Thống Khảo Thí & Học Liệu C++11 Hướng Đối Tượng - Khoa Công Nghệ Thông Tin
            </p>
            <p class="font-mono text-zinc-500 text-[11px]">
                Kiến trúc chuẩn MOSTest5_2 • Brutalist Minimalist • C++11 ISO/IEC 14882:2011 Standard Compliant
            </p>
        </div>
    </footer>

</body>
</html>
"""

# Write to root and Bai tap
with open("c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

try:
    with open("c:/Users/LAPTOP/Desktop/Tài liệu học tập/OOP Lecture/Bài tập/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
except Exception:
    pass

print(f"Master index.html generated successfully! Size: {len(html_content)} bytes.")

