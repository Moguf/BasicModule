#!/usr/bin/env python3
# coding : utf-8
'''
'''

import resource


class Limit:
    '''
    '''
    def __init__(self):
        self.maxsize = 16

    def set(self, maxsize):
        '''
        # set Max Memory size.
        # maxsize:unit is Gb.
        '''
        self.maxsize = 1024*1024*1024*maxsize
        soft, hard = resource.getrlimit(resource.RLIMIT_AS)
        resource.setrlimit(resource.RLIMIT_AS,(self.maxsize,hard))
        print('Set Memoy Limit\t:\t{}Gb;'.format(maxsize))

    def show(self):
        pass
