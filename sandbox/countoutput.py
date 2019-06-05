import sys
import os

os.chdir('/Users/griffin/Dropbox/projects/filefoo/playground')

filepath = 'lsinodeinfo.out'

dirs = {}
files = []
with open(filepath) as fp:
    line = fp.readline()
    while line:
        if '/' in line:
            if not line in dirs:
                dirs[line] = 1
        else:
            files.append(line)
    line = fp.readline()

print(f"dirs: {len(dirs)} files: {len(files)}")
