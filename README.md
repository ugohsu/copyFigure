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
