#!/usr/local/bin/python3
from __future__ import print_function, unicode_literals


# Standard library modules.      
import  sys
            
# Other library modules.
from    columnar import columnar    # used to print columnar layouts
import  clr                         # https://pypi.org/project/clr/


# Local libray modules.
from whaaaaat import style_from_dict, Token, prompt, print_json, Separator

from utils import Usage
from utils import ThrowError
from search import Find
from utils import mykwargs
from results import Results

if sys.platform.lower() == "win32":
    os.system('color')


# TEMPORARY
class Interactive(Find):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.find()
        self.what_now()
        self.save_results()

    def what_now(self):
        print(self.counts)

        style = style_from_dict({
            Token.Separator: '#6C6C6C',
            Token.QuestionMark: '#FF9D00 bold',
            #Token.Selected: '',  # default
            Token.Selected: '#5F819D',
            Token.Pointer: '#FF9D00 bold',
            Token.Instruction: '',  # default
            Token.Answer: '#5F819D bold',
            Token.Question: '',
        })


        questions = [
            {
                'type': 'confirm',
                'message': f"Save results to: {self.out_filename}: ",
                'name': 'save',
                'default': 'True'
            }
        ]
    
    def save_results(self):
        style = style_from_dict({
            Token.Separator: '#6C6C6C',
            Token.QuestionMark: '#FF9D00 bold',
            #Token.Selected: '',  # default
            Token.Selected: '#5F819D',
            Token.Pointer: '#FF9D00 bold',
            Token.Instruction: '',  # default
            Token.Answer: '#5F819D bold',
            Token.Question: '',
        })

        if self.out_filename != None:

            questions = [
                {
                    'type': 'confirm',
                    'message': f"Save results to: {self.out_filename}: ",
                    'name': 'save',
                    'default': 'True'
                }
            ]
        else: # NOT DONE

            questions = [
                {
                    'type': 'expand',
                    'message': 'Save file on `file.js`: ',
                    'name': 'overwrite',
                    'default': 'a',
                    'choices': [
                        {
                            'key': 'y',
                            'name': 'Overwrite',
                            'value': 'overwrite'
                        },
                        {
                            'key': 'a',
                            'name': 'Overwrite this one and all next',
                            'value': 'overwrite_all'
                        },
                        {
                            'key': 'd',
                            'name': 'Show diff',
                            'value': 'diff'
                        },
                        Separator(),
                        {
                            'key': 'x',
                            'name': 'Abort',
                            'value': 'abort'
                        }
                    ]
                }
            ]

        answer = prompt(questions, style=style)
        if answer['save']:
            self.save_json()

    def move_file(self,src, dest):
        """ Move a given file from `src` to `dst`

            Params:
            ---------
            src [string]  : path to source file
            dest [string] : path to new location

            Returns:
            ---------
            bool success
        """
        pass


    def delete_file(self,src, ask=True):
        """ Delete a file from disk

            Params:
            ----------
            src [string]  : path to file
            ask [bool] : True = prompt user before deleting

            Returns:
            -----------
            bool success
        """
        pass


def main(*args,**kwargs):
    valid_commands = {
        'fin': "Find files or directories.",
        'com': "Compare files or directories.",
        'sum': "Summarize files or directories.",
        'mov': "Move files or directories.",
        'del': "Delete files or directories."
    }

    if len(args) < 2:
        print("Missing one of the following from your command: ")
        print(Usage.print('main',valid_commands))
        return
    elif not args[1] in valid_commands:
        print("Command not known: ")
        print(Usage.print('main',valid_commands))
    else:
        if args[1] == 'fin':
            f = Find(**kwargs)
            res = f.find()
            files = Results.get_files(res)
            print(files)
        elif args[1] == 'com':
            CompareFiles(**kwargs)


if __name__ == '__main__':

    kwargs, args = mykwargs(sys.argv)

    f = main(*args,**kwargs)

    



 
