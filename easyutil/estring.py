#!/usr/bin/env python3
# fileencoding=utf-8

def char_width(char):
    # For japanese.
    if len(char) == 1:
        return 1
    else:
        return 2

def string_width(_string):
    char_width_list = []
    for c in _string.decode('utf-8'):
        char_width_list.append(char_width(c))
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
    ustring = _str
    return out
