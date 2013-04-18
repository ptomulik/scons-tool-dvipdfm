import os
import sys
import getopt
cmd_opts, arg = getopt.getopt(sys.argv[1:], 'io:r:', [])
infile = open(arg[0], 'rb')
out_file_name = None
for o,a in cmd_opts:
    if o == '-o':
        out_file_name = a
if out_file_name:
    out_file = open(out_file_name, 'wb')
else:
    out_file = sys.stdout
for l in infile.readlines():
    if l[:8] != '#dvipdfm':
        out_file.write(l)
sys.exit(0)
