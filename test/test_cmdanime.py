#!/usr/bin/env python3
# fileencoding:utf-8

import os
import sys
import time
import unittest

sys.path.append(os.path.abspath('../easyutil'))
from cmdanime import CmdAnimation

class TestCmdAnimation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    
    def setUp(self):
        pass

    def test_spin_animation(self):
        self.tclass = CmdAnimation()
        self.tclass.start()
        time.sleep(2.)
        self.tclass.end()
        
    def test_progress_animation(self):
        self.tclass = CmdAnimation(anim_type="progress", filename="test_cmdanime.py", size=1000)
        self.tclass.start()
        self.assertEqual()
        time.sleep(3.)
        self.tclass.end()
        raise KeyboardInterrupt()
        
    def test_get_size(self):
        self.tclass = CmdAnimation()
        raise Exception(str(self.tclass.get_size('test_cmdanime.py')))
        
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
        
    
