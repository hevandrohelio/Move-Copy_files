import os
import shutil
from pathlib import Path


class Mc_file:
    def __init__(self, dir, new_dir):
        self.dir = dir
        self.new_dir = new_dir
        self.usefull_dir = Path(dir)
        self.dir_files = os.listdir(dir)
        self.all_ex_files_dir = []
        for file_ex in self.usefull_dir.glob('*'):
            self.all_ex_files_dir.append(file_ex)
        self.extensions = {filepath.suffix[1:] for filepath in self.usefull_dir.glob('*')}

    def copy(self):
        if not os.path.isdir(self.new_dir):
            os.mkdir(self.new_dir)
        if os.path.isdir(self.dir):
            for e in self.extensions:
                os.mkdir(fr'{self.new_dir}\{e}_files')
                for f in self.dir_files:
                    if e in f:
                        shutil.copy(fr'{self.dir}\{f}', fr'{self.new_dir}\{e}_files')
        else:
            return 'Origin Directory not found.'

    def move(self):
        if not os.path.isdir(self.new_dir):
            os.mkdir(self.new_dir)
        if os.path.isdir(self.dir):
            for e in self.extensions:
                os.mkdir(fr'{self.new_dir}\{e}_files')
                for f in self.dir_files:
                    if e in f:
                        shutil.move(fr'{self.dir}\{f}', fr'{self.new_dir}\{e}_files')
        else:
            return 'Origin Directory not found.'