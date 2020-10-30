name = "Dinesh"

print name

print globals().items()

def family():

    global name
    name = "KTB"
    print name


family()


print globals().items()


