# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2018 by Paweł Tomulik <ptomulik@meil.pw.edu.pl>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

__docformat__ = "restructuredText"

"""
TODO: Write documentation
"""

import sys
import os
import TestSCons
_python_ = TestSCons._python_

if sys.platform == 'win32':
    test = TestSCons.TestSCons(program='scons.bat', interpreter=None)
else:
    test = TestSCons.TestSCons()

dvipdfm = test.where_is('dvipdfm')
if not dvipdfm:
    test.skip_test('dvipdfm not found, skipping test...\n')

tex = test.where_is('tex')
if not tex:
    test.skip_test('tex not found, skipping test...\n')

test.subdir(['site_scons'])
test.subdir(['site_scons', 'site_tools'])
test.subdir(['site_scons', 'site_tools', 'dvipdfm'])
test.file_fixture('../../../../__init__.py','site_scons/site_tools/dvipdfm/__init__.py')
test.file_fixture('../../../../about.py','site_scons/site_tools/dvipdfm/about.py')
test.file_fixture('../../../../dvipdfm.py','site_scons/site_tools/dvipdfm/dvipdfm.py')

test.write('SConstruct', """
import os
foo = Environment(ENV={'PATH': os.environ['PATH']},
                  tools=['default', 'dvipdfm'])
bar = Environment(ENV={'PATH': os.environ['PATH']},
                  tools=['default', 'dvipdfm'],
                  DVIPDFM=r'%(_python_)s wrapper.py %%s' %% foo['DVIPDFM'])
foo.DVIPDFM(target='foo.pdf',
            source=foo.DVI(target='foo.dvi', source='foo.tex'))
bar.DVIPDFM(target='bar.pdf',
            source=bar.DVI(target='bar.dvi', source='bar.tex'))
foo.DVIPDFM(target='xxx.pdf', source = 'xxx.tex')
""" % locals())

test.write('bar.tex', r"""
\documentclass{article}
\begin{document}
\begin{abstract}
This is the bar.tex TeX file.
\end{abstract}
\end{document}
""")

test.write('foo.tex', r"""
\documentclass{article}
\begin{document}
\begin{abstract}
This is the foo.tex TeX file.
\end{abstract}
\end{document}
""")

test.write('wrapper.py', r"""
import os
import sys
cmd = " ".join(sys.argv[1:])
open('wrapper.out', 'a').write("%s\n" % cmd)
os.system(cmd)
""")

test.write('xxx.tex', r"""
\documentclass{article}
\begin{document}
\begin{abstract}
This is the xxx.tex TeX file.
\end{abstract}
\end{document}
""")


test.run(arguments = 'foo.pdf', stderr=None)
test.must_not_exist('wrapper.out')
test.must_exist('foo.pdf')

test.run(arguments = 'xxx.pdf', stderr=None)
test.must_not_exist('wrapper.out')
test.must_exist('xxx.dvi')

test.run(arguments = 'bar.pdf', stderr=None)
test.must_exist('wrapper.out')
test.must_match('wrapper.out', "dvipdfm -o bar.pdf bar.dvi\n", 'r')
test.must_exist('bar.pdf')

test.pass_test()

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set syntax=python expandtab tabstop=4 shiftwidth=4:
