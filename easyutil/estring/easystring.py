# fileencoding=utf-8

__all__ = ['char_width', 'string_width', 'add_space', 'constant_width']

def char_width(char):
    # For japanese.
    if len(char) == 1:
        return 1
    else:
        return 2

def string_width(_string):
    char_width_list = []
    for c in _string:
        char_width_list.append(char_width(c.encode('utf-8')))
    return char_width_list

def add_space(_string, num):
    return _string+' '*num

def constant_width(_string, width):
    out = ''
    char_width_list = string_width(_string)
    width_sum = 0
    _end = 0
    if sum(char_width_list) < width:
        return add_space(_string, width - sum(char_width_list))
    
    for i, val in enumerate(char_width_list):
        width_sum += val
        if width_sum > width:
            _end = i
            break
    ustring = _string
    out = _string.decode('utf-8')[:_end]
    return out
