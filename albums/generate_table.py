#!/usr/bin/python

import os

table_str = "\
<table>\n\
    <thead>\n\
        <tr>\n\
            <th>專輯</th>\n\
            <th>曲目</th>\n\
        </tr>\n\
    </thead>\n\
    <tbody>\n"

for root, dirs, files in os.walk("."):
    path = root.split(os.sep)
    if len(path) == 1: continue
    album_length = len(files)

    album_str = f"\
        <tr>\n\
            <td rowspan={album_length}>{path[-1]}</td>\n\
            <td>\n\n[{files[0].replace('.pdf', '')}](albums/{path[-1].replace(' ', '%20')}/{files[0].replace(' ', '%20')})</td>\n\
        </tr>\n"

    for file in files[1:]:
        album_str += f"\
        <tr>\n\
            <td>\n\n[{file.replace('.pdf', '')}](albums/{path[-1].replace(' ', '%20')}/{file.replace(' ', '%20')})</td>\n\
        </tr>\n"

    table_str += album_str

table_str += "\
    </tbody>\n\
</table>"