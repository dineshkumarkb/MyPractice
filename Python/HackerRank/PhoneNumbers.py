import re

def validate(s):
    print s
    patt = r'^[7-9][0-9]{9}$'
    if re.search(patt,s):
        print "YES"
    else:
        print "NO"





if __name__ == "__main__":
    n = raw_input()
    for i in range(int(n)):
        validate(raw_input())