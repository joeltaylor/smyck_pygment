# -*- coding: utf-8 -*-
"""
    Smyck Colorscheme
    ~~~~~~~~~~~~~~~~~

    Converted by Vim Colorscheme Converter
"""
from pygments.style import Style
from pygments.token import Token, Comment, Name, Keyword, Generic, Number, Operator, String

class SmyckStyle(Style):

    background_color = '#282828'
    styles = {
        Token:              'noinherit #F7F7F7 bg:#282828',
        Comment:            'noinherit #8F8F8F',
        Generic.Error:      'noinherit #F7F7F7 bg:#c00000',
        Name.Entity:        'noinherit #d7d7d7',
        Comment.Preproc:    'noinherit #D1FA71',
        Keyword:            'noinherit #D1FA71',
        Name.Tag:           'noinherit #D1FA71',
        Generic.Inserted:   '#ffffff bg:#008000 bold',
        Number:             'noinherit #F6DC69',
        String:             'noinherit #F6DC69',
        Generic.Traceback:  'noinherit #F7F7F7 bg:#c00000',
        Name.Variable:      'noinherit #96D9F1',
        Generic.Deleted:    '#ffffff bg:#c00000 bold',
        Generic.Subheading: 'noinherit #88CCE7',
        Generic.Heading:    'noinherit #88CCE7',
        Keyword.Type:       'noinherit #96D9F1',
        Name.Constant:      'noinherit #96D9F1',
        Generic.Output:     '#8F8F8F bold',
        Generic.Emph:       'noinherit #ff00ff bg:#272727 underline',
    }
