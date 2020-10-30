#
# def call_me(l):
#     l = [0,1]
#     print l
#
# def myappend(l):
#     l.append(2)
#
#
# l = [0]
#
# call_me(l)
# myappend(l)
# print l

a = [0,1]
b = [2,3]
c = a
c.append(4)

print "a = " , a
print "b = ", b
print "c = ", c
print " a after modification ", a

print a is b
print b is c
print c is a
print a is c
