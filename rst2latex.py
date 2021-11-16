#!/usr/bin/env python3

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


"""
A customized front end to the Docutils Publisher, producing LaTeX with valid codeblocks using the listings package.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline
from docutils.parsers.rst import directives, Directive
from docutils import nodes


class CodeBlock(Directive):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}
    has_content = True

    rstlang_to_listingslang = {
        'text': '{}'
    }

    def run(self):
        language = self.rstlang_to_listingslang.get(self.arguments[0], self.arguments[0])
        content = '\n'.join(self.content)
        latex = '\\begin{{lstlisting}}[language={}]\n{}\n\\end{{lstlisting}}'.format(language, content)
        return [nodes.raw('', latex, format='latex')]


description = ('Generates LaTeX documents from standalone reStructuredText '
               'sources. '
               'Reads from <source> (default is stdin) and writes to '
               '<destination> (default is stdout).  See '
               '<http://docutils.sourceforge.net/docs/user/latex.html> for '
               'the full reference.')


for directive_name in ('code', 'code-block'):
    directives.register_directive(directive_name, CodeBlock)
publish_cmdline(writer_name='latex', description=description)
