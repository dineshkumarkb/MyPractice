import re

n =  input()
for i in range(n):
    s = raw_input()
    if re.search(r'^[+-]?\d*\.\d+$',s):
       print True
    else:
       print False

"""
^ -  Beginning of a line
[+-] -  Match any of the characters either + or -
? -  0 or 1 occurence. The string may or may not start with +/-. It may start with . as well.
\d -  digit may come before dot or may be not. 
* - 0 or more occurence of prev expression
\. -  Match "." character literal
\d+ - digit one or more times
$ - End of a line

"""