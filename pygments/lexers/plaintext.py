# -*- coding: utf-8 -*-
"""
    pygments.lexers.plaintext
    ~~~~~~~~~~~~~~~~~~~~

    Lexers for plain text formats.

    :copyright: Copyright 2006-2019 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import RegexLexer, include, bygroups
from pygments.token import Generic

__all__ = ['PlainTextLexer']


class PlainTextLexer(RegexLexer):
    """
    Lexer for plain text forcing it to have a certain color.
    """

    name = 'PlainText'
    aliases = ['plaintext', 'plainconsole']
    filenames = ['*.txt']
    mimetypes = ['text/plain']

    tokens = {
        'root': [
            (r'.*\n', Generic),
        ]
    }

    def analyse_text(text):
        # Only use this if explicitly called for.
        pass

