s= input()
def pel(s):
    if len(s) <=1:
        return print(1)
    else:
        if s[0] ==s[-1]:
            return pel(s[1:-1])
        else:
            return print(0)
pel(s)