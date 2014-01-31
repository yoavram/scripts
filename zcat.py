import gzip
import sys
if len(sys.argv) != 2:
	print "Usage: python zcat.py <filename>\nwhere <filename> is name of a text file compressed with gzip"
	sys.exit(1)
fn = sys.argv[1]
with gzip.open(fn) as f:
	print f.read()
sys.exit(0)
