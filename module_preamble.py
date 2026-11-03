# -*- coding: utf-8 -*-

preamble_text = r"""\documentclass[12pt,a4paper,oneside]{book}

% ==============================================================================
% GÓI HỆ THỐNG VÀ THIẾT LẬP PHÔNG CHỮ HỌC THUẬT
% ==============================================================================
\usepackage{fontspec}
\setmainfont{Latin Modern Roman}
\setsansfont{Latin Modern Sans}
\setmonofont[Scale=0.92]{Consolas}

\usepackage{amsmath, amssymb, amsthm}
\usepackage{graphicx}
\usepackage{adjustbox}
\usepackage[
    a4paper,
    top=2.5cm,
    bottom=2.5cm,
    left=3.0cm,
    right=2.5cm,
    headheight=26pt,
    footskip=1.5cm
]{geometry}

\usepackage{xcolor}
% Bảng màu học thuật Xanh Navy Oxford & Lam Nhạt Dịu Mắt (Gentle Academic Blue Palette)
\definecolor{primaryblue}{RGB}{24, 49, 83}      % Xanh Navy học thuật Oxford (#183153)
\definecolor{darkblue}{RGB}{15, 23, 42}         % Xanh sẫm tiêu đề và bìa (#0f172a)
\definecolor{accentblue}{RGB}{30, 64, 175}      % Lam hoàng gia tạo điểm nhấn viền (#1e40af)
\definecolor{softblue}{RGB}{59, 130, 246}       % Lam dịu cho thanh tiêu đề phụ (#3b82f6)
\definecolor{bgsoftblue}{RGB}{245, 248, 252}    % Lam nhạt pastel dịu mắt cho nền hộp lý thuyết (#f5f8fc)
\definecolor{bglighterblue}{RGB}{238, 244, 251} % Lam băng siêu dịu cho hộp chuyên sâu (#eef4fb)
\definecolor{codebg}{RGB}{248, 250, 252}        % Xám đá phiến siêu nhạt nền code (#f8fafc)
\definecolor{codeframe}{RGB}{226, 232, 240}     % Viền mã nguồn trung tính (#e2e8f0)
\definecolor{keywordblue}{RGB}{14, 65, 148}     % Xanh navy đậm cho từ khóa C++
\definecolor{commentgray}{RGB}{100, 116, 139}   % Xám tro cho chú thích code
\definecolor{stringblue}{RGB}{3, 105, 161}      % Lam biển cho chuỗi ký tự

\usepackage{parskip}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\itshape\color{darkblue}The OOP C++ Bible --- Giáo Trình Khoa Học Máy Tính Toàn Diện}
\fancyhead[R]{\small\bfseries\color{primaryblue}\thepage}
\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\headrule}{\hbox to\headwidth{\color{primaryblue}\leaders\hrule height \headrulewidth\hfill}}

\usepackage{titlesec}
\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries\color{primaryblue}}
  {\filleft\Large\textsf{\color{accentblue}CHƯƠNG}\ \Huge\thechapter}
  {1.5ex}
  {\titlerule[2pt]\vspace{1.5ex}\filright}
  [\vspace{1.5ex}{\color{primaryblue}\titlerule[0.8pt]}]

\titleformat{\section}
  {\normalfont\Large\bfseries\color{darkblue}}
  {\thesection}{1em}{}

\titleformat{\subsection}
  {\normalfont\large\bfseries\color{primaryblue}}
  {\thesubsection}{1em}{}

\titleformat{\subsubsection}
  {\normalfont\normalsize\bfseries\color{accentblue}}
  {\thesubsubsection}{1em}{}

% ==============================================================================
% CẤU HÌNH TRÍCH XUẤT MÃ NGUỒN (LISTINGS) VÀ HỖ TRỢ UNICODE
% ==============================================================================
\usepackage{listings}
\lstset{
    language=C++,
    basicstyle=\ttfamily\footnotesize,
    keywordstyle=\color{keywordblue}\bfseries,
    commentstyle=\color{commentgray}\itshape,
    stringstyle=\color{stringblue},
    backgroundcolor=\color{codebg},
    frame=single,
    rulecolor=\color{codeframe},
    breaklines=true,
    breakatwhitespace=false,
    showstringspaces=false,
    tabsize=4,
    numbers=left,
    numberstyle=\tiny\color{commentgray},
    numbersep=8pt,
    xleftmargin=16pt,
    xrightmargin=6pt,
    captionpos=b,
    columns=flexible,
    keepspaces=true,
    escapeinside={/*@}{@*/},
    morekeywords={nullptr, noexcept, constexpr, decltype, override, final, static_assert, alignas, alignof}
}

% ==============================================================================
% HỘP ĐỊNH NGHĨA VÀ PHÂN TÍCH CHUYÊN SÂU (TCOLORBOX)
% ==============================================================================
\usepackage{tcolorbox}
\tcbuselibrary{skins, breakable}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric, arrows.meta, positioning, calc}

\newtcolorbox{theorybox}[1][]{
    enhanced,
    colback=bgsoftblue,
    colframe=primaryblue,
    coltitle=white,
    fonttitle=\bfseries\sffamily,
    title={Tiên Đề / Định Nghĩa Pháp Lập: #1},
    boxrule=1.2pt,
    arc=2pt,
    left=12pt,
    right=12pt,
    top=9pt,
    bottom=9pt,
    before skip=14pt,
    after skip=14pt,
    breakable
}

\newtcolorbox{underhoodbox}[1][]{
    enhanced,
    colback=bglighterblue,
    colframe=accentblue,
    coltitle=white,
    fonttitle=\bfseries\sffamily,
    title={Khảo Sát Kiến Trúc Phần Cứng \& Trình Biên Dịch: #1},
    boxrule=1.4pt,
    arc=2pt,
    left=12pt,
    right=12pt,
    top=9pt,
    bottom=9pt,
    before skip=14pt,
    after skip=14pt,
    breakable
}

\newtcolorbox{warningbox}[1][]{
    enhanced,
    colback=white,
    colframe=accentblue!80!black,
    coltitle=white,
    fonttitle=\bfseries\sffamily,
    title={Cảnh Báo Kỹ Thuật \& Rủi Ro Biên Dịch: #1},
    boxrule=1.2pt,
    arc=2pt,
    left=12pt,
    right=12pt,
    top=9pt,
    bottom=9pt,
    before skip=14pt,
    after skip=14pt,
    breakable
}

\newtcolorbox{dangerbox}[1][]{
    enhanced,
    colback=bgsoftblue,
    colframe=darkblue,
    coltitle=white,
    fonttitle=\bfseries\sffamily,
    title={Hành Vi Không Xác Định (Undefined Behavior): #1},
    boxrule=1.6pt,
    arc=2pt,
    left=12pt,
    right=12pt,
    top=9pt,
    bottom=9pt,
    before skip=14pt,
    after skip=14pt,
    breakable
}

\usepackage{enumitem}
\usepackage{booktabs}
\usepackage[
    colorlinks=true,
    linkcolor=primaryblue,
    citecolor=primaryblue,
    urlcolor=accentblue,
    bookmarksnumbered=true,
    pdfstartview=FitH
]{hyperref}

% ==============================================================================
% PHẦN THÂN TÀI LIỆU (DOCUMENT BODY)
% ==============================================================================
\begin{document}

% Trang Bìa Học Thuật Oxford Style
\begin{titlepage}
    \centering
    \vspace*{1.5cm}
    
    {\Huge\bfseries\color{darkblue} THE OOP C++ BIBLE\par}
    \vspace{0.4cm}
    {\large\scshape\color{primaryblue} Giáo Trình Khoa Học Máy Tính \& Kiến Trúc Phần Mềm Hướng Đối Tượng\par}
    
    \vspace{1.2cm}
    {\color{primaryblue}\rule{0.85\textwidth}{1.8pt}}\par
    \vspace{0.6cm}
    
    {\LARGE\bfseries Phân Tích Chuyên Sâu C++11/14/17 Dưới Tầng Phần Cứng, Quản Trị Bộ Nhớ RAM, VTable \& Cơ Chế Trình Biên Dịch\par}
    
    \vspace{0.6cm}
    {\color{primaryblue}\rule{0.85\textwidth}{1.8pt}}\par
    
    \vspace{2.5cm}
    
    \begin{minipage}{0.85\textwidth}
        \centering
        \textbf{\large Chuyên Luận Đào Tạo Kỹ Sư Công Nghệ Thông Tin Cao Cấp}\\[0.3cm]
        \textit{\normalsize Tái hiện toàn diện cơ sở lý thuyết, mô hình kiến trúc bộ nhớ, các hệ hình lập trình, và giải thuật tối ưu hóa tài nguyên chuẩn mực quốc tế ISO/IEC 14882.}
    \end{minipage}
    
    \vfill
    
    {\large\bfseries Tủ Sách Kỹ Thuật Máy Tính \& Khoa Học Phần Mềm\par}
    {\normalsize Lưu Hành Học Thuật \& Nghiên Cứu Chuyên Sâu --- Năm 2026\par}
    \vspace*{1cm}
\end{titlepage}

\frontmatter
\tableofcontents
\mainmatter
"""
