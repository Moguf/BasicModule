#!/usr/bin/env python3
# coding : utf-8
'''
This file contains Memory manager Class. Python don't set Memory Limit.We need 
to set Memory Limit to protect our Machine from a pending state.

:Author:  Mogu 

Environment
-----------

    Python3.5.1

Requirements
------------

References
------------

    1) in Ch13.4 Python Coookbook,Third edition [By David Beazley,Brian K. Jones], 2013.

'''
import resource


class Limit:
    """ basic description """
    __doc__ = "here"
    __all__ = ["set","show","__init__"]
    
    def __init__(self):
        self.maxsize = 16

    def set(self, maxsize):
        '''
        Set Memory Limit.
        
        :maxsize: int
        :return: void
        '''

        self.maxsize = 1024*1024*1024*maxsize
        soft, hard = resource.getrlimit(resource.RLIMIT_AS)
        resource.setrlimit(resource.RLIMIT_AS,(self.maxsize,hard))
        print('Set Memoy Limit\t:\t{}Gb;'.format(maxsize))

    def show(self):
        '''
        Show current setting.

        :maxsize: int
        :return: void

        '''

        

        

