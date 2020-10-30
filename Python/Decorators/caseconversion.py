def convert_to_upper(func):
    def convert(mystr):
        mystr_upper = mystr.upper()
        return func(mystr_upper)
    return convert




@convert_to_upper
def bold_me(str_bold):
    print(str_bold)

bold_me("dinesh")
#print(s)