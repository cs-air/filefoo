import json
from helper import ThrowError
import os

class Results(object):

    @staticmethod
    def get_files(results):
        """ Pulls out files from search results.
        """

        if not isinstance(results,dict):
            ThrowError(message="Argument: 'results' not a 'dict' type in 'get_files'")

        files_list = []
        count = 1
        for d, dd in results.items():
            if dd.size > 0:
                for f in dd.files:
                    files_list.append({
                        'id': count,
                        'path': f.base_dir,
                        'name': f.name,
                        'size': f.size,
                        'modify_date': f.mdate,
                        'ext': f.ftype
                    })
                    count += 1

        return files_list
        
    @staticmethod
    def save_json(files,file_name):
        """ Saves the list of found files to a json file.
        """

        if not isinstance(files,list):
            ThrowError(message="Argument: 'files' not a 'list' type in 'save_json'")

        if not isinstance(file_name,str):
            ThrowError(message="Argument: 'file_name' is not a 'str' type in 'save_json'")

        with open(out_filename, "w") as f:
            f.write(json.dumps(files_list))

        return os.path.isfile(file_name)