#!/usr/bin/env python3
# fileencoding=utf-8


class Estring:
    def char_width(self, char):
        # For japanese.
        if len(char) == 1:
            return 1
        else:
            return 2

    def string_width(self, _string):
        char_width_list = []
        for c in _string.decode('utf-8'):
            char_width_list.append(self.char_width(c))
        return char_width_list

    def add_space(self, _string, num):
        return _string+' '*num

    def constant_width(self, _string, width):
        out = ''
        char_width_list = self.string_width(_string)
        width_sum = 0
        _end = 0
        if sum(char_width_list) < width:
            return self.add_space(_string, width - sum(char_width_list))
    
        for i, val in enumerate(char_width_list):
            width_sum += val
            if width_sum > width:
                _end = i
            break
        ustring = _string
        out = _string.decode('utf-8')[:_end]
        return out
