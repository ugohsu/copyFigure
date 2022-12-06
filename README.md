# cf

画像ファイルをクリップボードにコピーする関数 (とくに、LaTeX でタイプセットした数式を SVG 形式でクリップボードにコピーする)

## Dependency

- Python 3.5
- xclip
- pdftocairo (poppler-utils)

## Installation

```
# python3 setup.py install
```

## Usage

- mathpdf
    - `mathpdf [FILE]`
    - [FILE] に所定のプリアンブル等を付け加えて、upLaTeX でタイプセット
- cf
    - `cf [FILE]`
    - [FILE] で指定された画像ファイル (PDF, SVG, PNG, JPG のみ) をクリップボードにコピー

## Notation

複数行の数式をあつかいたい場合には、https://okumuralab.org/tex/mod/forum/discuss.php?d=2875 にならい、

```{tex}
\documentclass[varwidth, crop]{standalone}
\usepackage{svg} % svg ファイルを読み込む場合
\usepackage{amsmath, amssymb, amsfonts, newtxtext, newtxmath} % 数式関係
\usepackage{luatexja} % LuaLaTeX でタイプセットする場合
\usepackage{threeparttable} % 以下、テーブル関係
\usepackage{dcolumn}
\usepackage{longtable}
\usepackage{booktabs}
\begin{document}
    % https://okumuralab.org/tex/mod/forum/discuss.php?d=2875
    \[
        \begin{aligned}
            &\mathit{lnBAS}_{i, -2} = \notag \\
            &\beta_0 + \mathit{Others} \notag
        \end{aligned}
    \]
\end{document}
```

のようなコードにして、lualatex を実行するのがよいかも。
