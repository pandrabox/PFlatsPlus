"""
Markdown Divider - Docusaurus用分割＆サイドバー自動修正
"""

# BASEをリポジトリルートに修正
import os
import re
import shutil

# BASE: このスクリプトの親の親（docusaurusプロジェクトルート）
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
INPUT_PATH = os.path.join(BASE, 'docs', 'original.md')
DIVIDED_DIR = os.path.join(BASE, 'docs', 'divided')
SIDEBAR_PATH = os.path.join(BASE, 'sidebars.js')

# docs/dividedを全削除
if os.path.exists(DIVIDED_DIR):
    shutil.rmtree(DIVIDED_DIR)
os.makedirs(DIVIDED_DIR, exist_ok=True)

# original.md読み込み
with open(INPUT_PATH, 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

sections = []
current_section = None
current_title = None
current_folder = None

for line in lines:
    if line.startswith('# '):
        if current_section is not None and current_title is not None:
            sections.append((current_folder, current_title, current_section))
        match = re.match(r'^#\s*@([^@]+)@(.+)$', line)
        if match:
            current_folder = match.group(1).strip()
            current_title = match.group(2).strip()
            current_section = ['# ' + current_title]
        else:
            current_folder = None
            current_title = line[2:].strip()
            current_section = [line]
    else:
        if current_section is not None:
            current_section.append(line)
if current_section is not None and current_title is not None:
    sections.append((current_folder, current_title, current_section))

# 分割ファイル出力
sidebar_structure = {}
file_index = 1
for folder, title, content in sections:
    out_dir = DIVIDED_DIR
    sidebar_key = None
    if folder:
        safe_folder = folder.replace('/', os.path.sep)
        out_dir = os.path.join(DIVIDED_DIR, safe_folder)
        os.makedirs(out_dir, exist_ok=True)
        sidebar_key = safe_folder
    else:
        sidebar_key = 'root'
    file_name = f"{file_index:03d}.md"
    out_path = os.path.join(out_dir, file_name)
    # slug生成: 最初の分割ファイル（file_index==1）は必ず'/'
    if file_index == 1:
        slug = '/'
    elif sidebar_key == 'root':
        slug = f'/divided/{file_name[:-3]}'
    else:
        slug = f'/divided/{sidebar_key}/{file_name[:-3]}'
    # frontmatter
    header = f"---\ntitle: {title}\nsidebar_position: {file_index}\nslug: {slug}\n---\n"
    with open(out_path, 'w', encoding='utf-8') as out_file:
        out_file.write(header)
        out_file.write('\n'.join(content))
        out_file.write('\n')
    # サイドバー構造
    if sidebar_key not in sidebar_structure:
        sidebar_structure[sidebar_key] = []
    sidebar_structure[sidebar_key].append((file_name, title))
    file_index += 1

# sidebars.js自動生成
sidebar_lines = [
    '// 自動生成: md_divider.py',
    'const sidebars = {',
    '  dividedSidebar: [',
]
for key, items in sidebar_structure.items():
    if key == 'root':
        for file_name, title in items:
            sidebar_lines.append(f"    'divided/{file_name[:-3]}', // {title}")
    else:
        sidebar_lines.append(f"    {{ type: 'category', label: '{key}', collapsed: false, items: [")
        for file_name, title in items:
            sidebar_lines.append(f"      'divided/{key}/{file_name[:-3]}', // {title}")
        sidebar_lines.append('    ] },')
sidebar_lines.append('  ],')
sidebar_lines.append('};\nexport default sidebars;')
with open(SIDEBAR_PATH, 'w', encoding='utf-8') as f:
    f.write('\n'.join(sidebar_lines))

print(f"分割・サイドバー自動生成完了: {file_index-1}ファイル", flush=True)
