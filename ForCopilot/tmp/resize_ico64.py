import os
from PIL import Image

# 入力・出力ディレクトリ
SRC_DIR = r'c:/P/docusaurus/docusaurus/ForCopilot/tmp/MenuIco_result'
DST_DIR = r'c:/P/docusaurus/docusaurus/static/img/icos'
SIZE = (32, 32)

os.makedirs(DST_DIR, exist_ok=True)

for filename in os.listdir(SRC_DIR):
    if filename.lower().endswith('.png'):
        src_path = os.path.join(SRC_DIR, filename)
        dst_path = os.path.join(DST_DIR, filename)
        try:
            with Image.open(src_path) as img:
                img = img.convert('RGBA')
                img = img.resize(SIZE, Image.LANCZOS)
                img.save(dst_path)
                print(f'Saved: {dst_path}')
        except Exception as e:
            print(f'Error processing {filename}: {e}')
