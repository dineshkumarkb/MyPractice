import sys

from time import sleep

def color():
           s=sys.stdout
           s.write('\033[32m\u25a0\033[m'*10)
           s.flush()
           sleep(2)
           s.write('\b\n')
           s.flush()
color()