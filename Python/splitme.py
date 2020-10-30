def splitme(string,delimiter):

    l = []
    s = string
    pos = 0
    for i,j in enumerate(string):
        if j == delimiter:
            l.append(string[pos:i])
            pos = i+1
            s = string[pos:]
            if delimiter not in s:
                l.append(s)

    return l





print splitme("dinesh,kumar,",",")
