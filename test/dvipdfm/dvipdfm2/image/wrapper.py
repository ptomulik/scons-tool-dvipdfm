import os
import sys
cmd = " ".join(sys.argv[1:])
open('wrapper.out', 'ab').write("%s\n" % cmd)
os.system(cmd)
