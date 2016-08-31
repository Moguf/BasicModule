
def getValName(value):
    '''
    get value name in str format, and return the str.
    '''
    for k, v in zip(globals().keys(),globals().values()):
        if v == value:
            return k

