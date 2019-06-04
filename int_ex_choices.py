# -*- coding: utf-8 -*-
"""
* Checkbox question example
* run example by typing `python example/checkbox.py` in your console
"""
from __future__ import print_function, unicode_literals

from whaaaaat import style_from_dict, Token, prompt, print_json, Separator


style = style_from_dict({
    Token.Separator: '#6C6C6C',
    Token.QuestionMark: '#FF9D00 bold',
    Token.Selected: '#5F819D',  # default
    Token.Pointer: '#FF9D00 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#5F819D bold',
    Token.Question: '',
})


questions = [
    {
        'type': 'checkbox',
        'message': 'Select files or folders',
        'name': 'Results',
        'choices': [
            Separator('= Folders ='),
            {
                'name': 'Documents'
            },
            {
                'name': 'Media'
            },
            {
                'name': 'Pictures'
            },
            Separator('= Files ='),
            {
                'name': '/Users/you/somefile.png',
                'checked': False
            },
            {
                'name': '/Users/you/somefile2.png',
            },
            {
                'name': '/Users/you/somefile3.jpg',
            },
            Separator('= Delete All='),
            {
                'name': 'Delete All'
            },
            Separator('= Move All ='),
            {
                'name': 'Move All'
            }
        ],
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 else True
    }
]

answers = prompt(questions, style=style)
print_json(answers)