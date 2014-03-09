#!/bin/sh
# links for documentation:
# http://www.howtogeek.com/howto/ubuntu/display-number-of-processors-on-linux/

cat /proc/cpuinfo | grep processor | wc -l
