#!/usr/bin/env python3
# coding:utf-8

import time
import unittest
from easyutil import CmdAnimation

class TestCmdAnimation(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass
    
    def setUp(self):
        pass

    def test_spin_animation(self):
        self.tclass = CmdAnimation()
        self.tclass.start()
        time.sleep(2.)
        self.tclass.end()
        
    def test_progress_animation(self):
        self.tclass = CmdAnimation(anim_type="progress", filename="test_cmdanime.py", size=100)
        self.tclass.start()
        time.sleep(3.)
        self.tclass.end()        
        
    def test_get_size(self):
        self.tclass = CmdAnimation()
        raise Exception(str(self.tclass.get_size('test_cmdanime.py')))
        
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

if __name__ == '__main__':
    unittest.main()
        
    
