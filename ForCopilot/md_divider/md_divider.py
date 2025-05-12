"""
Markdown Divider - Markdownファイルを分割するツール

使い方:
python md_divider.py <入力Markdownファイルパス>

機能:
- 大きなMarkdownファイルを複数の小さなファイルに分割する
- H1見出し(#で始まる行)ごとに分割
- Docusaurusのフロントマターを各ファイルに追加
- @フォルダ名@タイトル形式でフォルダ指定可能
- 連番(001.md, 002.md, ...)のファイルに出力
"""

import os
import sys
import re

def main():
    try:
        if len(sys.argv) < 2 or not os.path.exists(sys.argv[1]):
            print("mdファイルをパラメータとして指定してください。", flush=True)
            print("使用方法: python md_divider.py <Markdownファイルパス>", flush=True)
            return

        input_path = sys.argv[1]
        print(f"入力ファイル: {input_path}", flush=True)
        
        out_dir = os.path.join(os.path.dirname(input_path), "Outp")
        os.makedirs(out_dir, exist_ok=True)
        print(f"出力ディレクトリ: {out_dir}", flush=True)

        # UTF-8でファイルを読み込み、BOMを適切に処理
        with open(input_path, 'rb') as f:
            content = f.read()
            if content.startswith(b'\xef\xbb\xbf'):  # BOM付きUTF-8
                content = content[3:]
                print("BOM付きUTF-8ファイルを検出しました。BOMを取り除きます。", flush=True)
            
            # バイナリデータをUTF-8としてデコード
            text = content.decode('utf-8', errors='replace')
            lines = text.splitlines()
        
        print(f"入力ファイルを読み込みました: {len(lines)}行", flush=True)

        sections = []
        current_section = None
        current_title = None
        current_folder = None

        for line in lines:
            if line.startswith('# '):
                if current_section is not None and current_title is not None:
                    sections.append((current_folder, current_title, current_section))

                # H1行から@...@を抽出
                match = re.match(r'^#\s*@([^@]+)@(.+)$', line)
                if match:
                    current_folder = match.group(1).strip()
                    current_title = match.group(2).strip()
                    # H1行から@...@を除去
                    current_section = ["# " + current_title]
                else:
                    current_folder = None
                    current_title = line[2:].strip()
                    current_section = [line]
            else:
                if current_section is not None:
                    current_section.append(line)

        # 最後のセクションを追加
        if current_section is not None and current_title is not None:
            sections.append((current_folder, current_title, current_section))

        file_index = 1
        for folder, title, content in sections:
            output_dir = out_dir
            if folder:
                # フォルダ名のスラッシュをOSに合わせたパス区切り文字に変換
                safe_folder = folder.replace('/', os.path.sep)
                output_dir = os.path.join(out_dir, safe_folder)
                os.makedirs(output_dir, exist_ok=True)
            
            # 連番ファイル名（0埋め3桁）
            file_name = f"{file_index:03d}.md"
            out_path = os.path.join(output_dir, file_name)

            # Docusaurusフロントマターを作成
            header = f"---\ntitle: {title}\nsidebar_position: {file_index}\n---\n"
            
            # ヘッダ + 本文を書き込み
            with open(out_path, 'w', encoding='utf-8') as out_file:
                out_file.write(header)
                out_file.write('\n'.join(content))
                out_file.write('\n')
            
            file_index += 1

        print(f"分割完了: {len(sections)}個のファイルを{out_dir}以下に出力しました。", flush=True)
        
    except Exception as e:
        print(f"エラーが発生しました: {e}", flush=True)
        import traceback
        print(traceback.format_exc(), flush=True)

if __name__ == "__main__":
    main()
