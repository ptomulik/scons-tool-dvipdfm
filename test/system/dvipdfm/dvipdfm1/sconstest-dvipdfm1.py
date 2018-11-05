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
import TestSCons
_python_ = TestSCons._python_

if sys.platform == 'win32':
    test = TestSCons.TestSCons(program='scons.bat', interpreter=None)
else:
    test = TestSCons.TestSCons()

test.write('SConstruct', """\
env = Environment(TEX = r'%(_python_)s mytex.py',
                  LATEX = r'%(_python_)s mylatex.py',
                  DVIPDFM = r'%(_python_)s mydvipdfm.py',
                  tools=['dvipdfm', 'latex', 'tex'])
dvi = env.DVI(target='test1.dvi', source='test1.tex')
env.DVI(target='test2.dvi', source='test2.tex')
env.DVIPDFM(target='test1.pdf', source=dvi)
env.DVIPDFM(target='test2.pdf', source='test2.dvi')
""" % locals())

test.write('mydvipdfm.py', """\
import os
import sys
import getopt
cmd_opts, arg = getopt.getopt(sys.argv[1:], 'io:r:', [])
infile = open(arg[0], 'r')
out_file_name = None
for o,a in cmd_opts:
    if o == '-o':
        out_file_name = a
if out_file_name:
    out_file = open(out_file_name, 'w')
else:
    out_file = sys.stdout
for l in infile.readlines():
    if l[:8] != '#dvipdfm':
        out_file.write(l)
sys.exit(0)
""")

test.write('mylatex.py', """\
import os
import sys
import getopt
cmd_opts, arg = getopt.getopt(sys.argv[1:], 'i:r:', [])
base_name = os.path.splitext(arg[0])[0]
infile = open(arg[0], 'r')
out_file = open(base_name+'.dvi', 'w')
for l in infile.readlines():
    if l[:6] != '#latex':
        out_file.write(l)
sys.exit(0)
""")

test.write('mytex.py', """\
import os
import sys
import getopt
cmd_opts, arg = getopt.getopt(sys.argv[1:], 'i:r:', [])
base_name = os.path.splitext(arg[0])[0]
infile = open(arg[0], 'r')
out_file = open(base_name+'.dvi', 'w')
for l in infile.readlines():
    if l[:4] != '#tex':
        out_file.write(l)
sys.exit(0)
""")

test.write('test1.tex', """\
This is a .dvi test.
#tex
#dvipdfm
""")

test.write('test2.tex', """\
This is a .tex test.
#tex
#dvipdfm
""")


test.subdir(['site_scons'])
test.subdir(['site_scons', 'site_tools'])
test.subdir(['site_scons', 'site_tools', 'dvipdfm'])
test.file_fixture('../../../../__init__.py','site_scons/site_tools/dvipdfm/__init__.py')
test.file_fixture('../../../../about.py','site_scons/site_tools/dvipdfm/about.py')
test.file_fixture('../../../../dvipdfm.py','site_scons/site_tools/dvipdfm/dvipdfm.py')

test.run(arguments = [], stderr = None)

test.must_exist('test1.pdf')
test.must_exist('test2.pdf')
test.must_match('test1.pdf', "This is a .dvi test.\n", 'r')
test.must_match('test2.pdf', "This is a .tex test.\n", 'r')

test.pass_test()

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set syntax=python expandtab tabstop=4 shiftwidth=4:
