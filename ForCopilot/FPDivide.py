# FPDivide.py
# FlatsPlus用のMarkdown分割・画像パス変換などを自動化するスクリプト（中身はこれから実装）

import os
import shutil
import subprocess

# パス定義
DOCS_FLATSPLUS = os.path.join(os.path.dirname(__file__), '..', 'docs', 'flatsplus')
DOCS_ORIGINAL = os.path.join(os.path.dirname(__file__), '..', 'docs', 'original')
FLATSPLUS_MD = os.path.join(DOCS_ORIGINAL, 'FlatsPlus.md')
MD_DIVIDER = os.path.join(os.path.dirname(__file__), 'md_divider', 'md_divider.py')
OUTP_DIR = os.path.join(DOCS_ORIGINAL, 'Outp')

# 1. docs/flatsplus の全ファイル・サブフォルダ削除
if os.path.exists(DOCS_FLATSPLUS):
    for name in os.listdir(DOCS_FLATSPLUS):
        path = os.path.join(DOCS_FLATSPLUS, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

# 2. md_divider.py で分割
if os.path.exists(OUTP_DIR):
    shutil.rmtree(OUTP_DIR)
cmd = ['python', MD_DIVIDER, FLATSPLUS_MD]
print('分割コマンド:', ' '.join(cmd), flush=True)
subprocess.run(cmd, check=True)

# 3. Outp配下の全ファイル・サブフォルダをdocs/flatsplusへ移動
if os.path.exists(OUTP_DIR):
    for name in os.listdir(OUTP_DIR):
        src = os.path.join(OUTP_DIR, name)
        dst = os.path.join(DOCS_FLATSPLUS, name)
        if os.path.isdir(src):
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.move(src, dst)
        else:
            shutil.move(src, dst)
    shutil.rmtree(OUTP_DIR)

print('FlatsPlus.mdの分割・配置が完了しました。', flush=True)

