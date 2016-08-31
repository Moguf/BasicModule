
def getGvalName(value):
    '''
    get global value name in str format, and return the str.
    '''
    for k, v in zip(globals().keys(), globals().values()):
        if v == value:
            return k

def getLvalName(valuenames, value):
    '''
    Usage
    ~~~~~
    
    .. code-block:: python

        getLvalName(locals(), value)
    
    :value:    value is value you want to get the name.
    
    get local value name in str format, and return the str.
    
    '''
    for k, v in zip(valuenames.keys(), valuenames.values()):
        if v == value:
            return k

def getValNameFromClass(inclass, value):
    '''
    Dangerous code!!! This function uses eval(). 
    You have to use this function carefully.
    '''
    valuelists = [ ele for ele in dir(inclass) if ele[:2] != '__' ]
    out =[]
    for v in valuelists:
        instruction = 'inclass.' + str(v)
        if value == eval(instruction):
            out.append(str(v))
    if len(out) == 1:
        return out[0]
    else:            
        return out        



