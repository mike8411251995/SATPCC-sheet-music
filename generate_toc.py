#!/usr/bin/python

import os

# Header
toc_str = "# 樂譜目錄\n\n"
toc_str += "*點擊專輯名稱展開查看曲目*\n\n"

# Collect albums and their files from the albums directory
albums = []
albums_dir = "albums"

for root, dirs, files in os.walk(albums_dir, topdown=True):
    # Skip the albums root directory
    if root == albums_dir:
        continue
    
    path = root.split(os.sep)
    
    # Only process PDF files
    pdf_files = [f for f in files if f.endswith('.pdf')]
    if not pdf_files:
        continue
    
    album_name = path[-1]
    albums.append((album_name, sorted(pdf_files)))

# Sort albums by name
albums.sort(key=lambda x: x[0])

# Generate collapsible sections for each album
for album_name, files in albums:
    album_path = album_name.replace(' ', '%20')
    
    # Create details/summary collapsible section
    toc_str += f"<details>\n"
    toc_str += f"<summary><b>{album_name}</b> ({len(files)} 首)</summary>\n\n"
    
    # List songs
    for file in files:
        song_name = file.replace('.pdf', '')
        file_path = file.replace(' ', '%20')
        toc_str += f"- [{song_name}](albums/{album_path}/{file_path})\n"
    
    toc_str += f"\n</details>\n\n"

# Write to README.md with UTF-8 encoding
output_file = "README.md"
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(toc_str)

print(f"✓ 已生成目錄文件: {output_file}")
print(f"✓ 共有 {len(albums)} 個專輯")
