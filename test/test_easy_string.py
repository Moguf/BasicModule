#!/usr/bin/env python3
# fileencoding=utf-8

import os
import sys
import time
import unittest

sys.path.append(os.path.abspath('../easyutil'))
import estring as es


class TestCmdAnimation(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass
    
    def setUp(self):
        pass

    def test_spin_animation(self):
        es = estring.Estring()
        print(dir(es))
        string1 = u'あいうえおThread1あいつ'.encode('utf-8')
        string2 = u'fjkdflajThread1あいつ'
                
        self.assertEqual(es.string_width(string1),[2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2])
        self.assertEqual(es.string_width(string2),[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2])
        
        self.assertEqual(es.constant_width(string1, 10), 'あいうえお')
        self.assertEqual(es.constant_width(string2, 10), 'fjkdflajTh')

        self.assertEqual(es.constant_width(string1, 30), 'あいうえおThread1あいつ       ')
        self.assertEqual(es.constant_width(string2, 30), 'fjkdflajThread1あいつ         ')

        
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

if __name__ == '__main__':
    unittest.main()
        
    
