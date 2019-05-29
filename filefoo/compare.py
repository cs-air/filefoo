import  filecmp                     
import  itertools  

class CompareFiles(object):
    """
    https://pymotw.com/2/filecmp/
    """

    valid_commands = {
        'path': 'Start search here.',
        'deep': 'Do a deep compare',
        'type': 'Files or directories.',
    }

    def __init__(self,**kwargs):

        self.valid_commands = CompareFiles.valid_commads
        self._init(**kwargs)

    def _init(self,**kwargs):
        for k, v in kwargs.items():
            if not k in self.valid_commands:
                ThrowError(
                    message=f"{k}={v} is not a valid command parameter.", bail=False)
                ThrowError(message=self._usage(), error_keyword=False)

        self.path = kwargs.get('path', None)
        self.deep = kwargs.get('deep', False)
        self.type = kwargs.get('type', 'Files')

    def file_compare(self,path = None):
        if path == None:
            path = self.path

        # Still no path ?!?
        if path == None:
            ThrowError(message=self._usage(), error_keyword=False)

        files = os.listdir(self.path)

        for f1, f2 in itertools.combinations(files, 2):
            if filecmp.cmp(f1, f2):
                print(f1, f2)

    def directory_compare(self):
        c = filecmp.dircmp(filepath1, filepath2)
        _report_recursive(c)

    def _report_recursive(self,dcmp):
        for name in dcmp.diff_files:
            print("DIFF file %s found in %s and %s" % (name, 
                dcmp.left, dcmp.right))
        for name in dcmp.left_only:
            print("ONLY LEFT file %s found in %s" % (name, dcmp.left))
        for name in dcmp.right_only:
            print("ONLY RIGHT file %s found in %s" % (name, dcmp.right))
        for sub_dcmp in dcmp.subdirs.values():
            print_diff_files(sub_dcmp)
