scons-tool-dvipdfm
==================

This is dvipdfm tool for `SCons`_. It is derived from the ``dvipdf`` tool
present in `SCons`_ core. The code has been adapted to enable usage of
`dvipdfm`_ program.

INSTALLATION
------------

Copy the ``dvipdfm.py`` file to your project's ``site_scons/site_tools/``
(per-project installation) or to ``~/.scons/site_scons/site_tools/`` (per user
installation). See SCons manual for details about installation of tools.

USAGE EXAMPLES
--------------

Converting existing ``*.dvi`` file to ``*.pdf``::

    # SConstruct
    env = Environment(tools = ['dvipdfm'])
    env.DVIPDFM('foo.dvi')
    
Compiling ``LaTeX`` document to ``*.dvi`` and generating ``*.pdf`` file with
the ``DVIPDFM`` builder (note, the ``tex`` or ``default`` tool(s) must be
loaded)::

    # SConstruct
    env = Environment(tools = ['tex', 'dvipdfm'])
    env.DVIPDFM('foo.tex')

CONSTRUCTION VARIABLES
``````````````````````

The following construction variables may be used to configure the ``DVIPDFM``
builder:

============================== ==============================================
        Variable                                Description
============================== ==============================================
 ``DVIPDFM``                    the ``dvipdfm`` executable
------------------------------ ----------------------------------------------
 ``DVIPDFMFLAGS``               additional flags to ``dvipdfm``
------------------------------ ----------------------------------------------
 ``DVIPDFMCOM``                 complete commandline for ``dvipdfm``
------------------------------ ----------------------------------------------
 ``DVIPDFMSUFFIX``              suffix for target files, by default ``.pdf``
============================== ==============================================


DOWNLOADING TEST FRAMEWORK
--------------------------

To run tests you will need the `SCons test framework`_. On GNU systems you may quickly download it with the script ``bin/download-deps.sh``::

    bin/download-deps.sh

The development tree may be later cleaned-up from the downloaded files by::

    bin/delete-deps.sh

The script uses the `mercurial`_ VCS (hg) tools to download latest version.

If the above script does not work on your platform download the following files
from the `SCons test framework`_.

 ========================= ==================================================
  source file/directory                   target file/directory
 ========================= ==================================================
  ``QMTest/``               ``QMTest/``
 ------------------------- --------------------------------------------------
  ``runtest.py``            ``runtest.py``
 ========================= ==================================================

All downloaded files are ignored from the repository by ``.gitignore``, so you
don't have to worry about deleting them before doing commits.


RUNNING TESTS
-------------

To run all the tests type::
  
    python runtest.py -a

This requires the presence of the testing framework in the development tree.

LICENSE
-------
Copyright (c) 2013 by Pawel Tomulik

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE

.. _SCons: http://scons.org
.. _SCons test framework: https://bitbucket.org/dirkbaechle/scons_test_framework
.. _mercurial: http://mercurial.selenic.com/
.. _dvipdfm: http://gaspra.kettering.edu/dvipdfm/
