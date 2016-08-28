#!/usr/bin/env python3
# fileencoding=utf-8

import time
import unittest
import easyutil

class TestCmdAnimation(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass
    
    def setUp(self):
        pass

    def test_spin_animation(self):
        print(dir(easyutil))
        string1 = 'あいうえおThread1あいつ'
        string2 = 'fjkdflajThread1あいつ'    

        self.assertEqual(string_width(string1),[2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2])
        self.assertEqual(string_width(string2),[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2])
        
        self.assertEqual(constant_width(string1, 10), 'あいうえお')
        self.assertEqual(constant_width(string2, 10), 'fjkdflajTh')

        self.assertEqual(constant_width(string1, 30), 'あいうえおThread1あいつ       ')
        self.assertEqual(constant_width(string2, 30), 'fjkdflajThread1あいつ         ')

        
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

if __name__ == '__main__':
    unittest.main()
        
    
