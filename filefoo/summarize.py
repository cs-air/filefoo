from os import listdir
from os.path import isfile, isdir, join
from abspath import abs_path
import pprint as pp

class SummaryCounts:
    def __init__(self):
        self.dir_count = 0
        self.file_count = 0

    def __str__(self):
        return f"Dirs: {self.dir_count} Files: {self.file_count}"
    
    def __repr__(self):
        return self.__str__()


class Summary(object):
    """Used right now to get dir and file counts to be used in a 'time left' type output."""
    def __init__(self,**kwargs):
        self.path = kwargs.get('path', '.')
        self.recurse = kwargs.get('recurse', False)
        self.depth = kwargs.get('depth', 1)
        self.counts = SummaryCounts()
        self.dirs = {
            0 : [self.path]
            }
        self.level = 0

        if not isdir(self.path):
            raise(f"Error: {self.path} is not a directory in class Summary init method.")
    
    def get_counts(self):
        for i in range(self.depth):
            self.dirs[i+1] = []
            for d in self.dirs[i]:
                for entry in listdir(d):
                    item = join(d,entry)
                    if isdir(item):
                        self.dirs[i+1].append(item)
                        self.counts.dir_count += 1
                    else:
                        self.counts.file_count += 1
        return self.counts
            

    def get_dirs(self):
        return self.dirs
   
    def __str__(self):
        return f"Dirs: {self.dir_count} Files:{self.file_count}"

    def __repr__(self):
        return self.__str__()



if __name__=='__main__':
    S = Summary(path=abs_path('~/Dropbox'),depth=3)
    counts = S.get_counts()
    print(counts)
    pp.pprint(S.get_dirs())

        