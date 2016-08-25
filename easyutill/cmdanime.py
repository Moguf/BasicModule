#!/usr/bin/env python3
# coding : utf-8
'''

'''
import os
import sys
import time
import threading
import itertools


class Signal:
    go = True


class CmdAnimation:
    '''
    .. code-block::python 
       :emphasize-lines: 3,5
    '''
    def __init__(self, anim_type='spin', filename='', size=0, msg=""):
        """ 
        :signal:     terminate threading
        :anim_type:  [spin, progress]
        :filename:   for showing progress bar.
        :full_size:  for showing progress bar. 
        """
        self.full_size = size
        self.signal = Signal()
        self.duration_time = 0
        self.filename = filename
        self.types = {"spin": self._spin, "progress": self._progress}
        self.func = self.types[anim_type]
        self.msg = msg

    def start(self):
        self.anim = threading.Thread(target=self.func, args=(self.msg, self.signal))
        self.anim.start()
        
    def _spin(self, msg, signal):
        # Show Spin.
        spins  = '|/-\\'
        spins2 = '/-\\|'
        spins3 = '-\\|/'
        spins4 = '\\|/-'
        sys.stdout.write(msg)
        for i in itertools.cycle(range(4)):
            out = "\t{}{}{}{}".format(spins[i],spins2[i],spins3[i],spins4[i])
            sys.stdout.write(out)
            sys.stdout.flush()
            sys.stdout.write('\x08'*len(out))
            time.sleep(.1)
            if not signal.go:
                break
        sys.stdout.write('\x08'*(4+len(msg)))

    def _progress(self, msg, signal):
        sys.stdout.write(msg)
        while True:
            try:
                now_size = self.get_size(self.filename)
            except:
                continue
            
            self._showProgress(now_size)
            if self.full_size == now_size:
                break
        
    def _showProgress(self, now_size):
        # Show progress bar.
        out = self._get_bar(now_size)
        sys.stdout.write(out)
        time.sleep(.2)
        sys.stdout.flush()
        sys.stdout.write('\x08'*len(out))
        time.sleep(.1)        

    def _get_bar(self, now_size):
        _space = ' '
        _bar = '='
        _arrow = '>'
        bar_size = 60
        ratio = now_size / self.full_size
        arrow = _bar * (int((ratio) * bar_size) - 1) + _arrow
        space = _space * (bar_size - len(arrow))
        percent = '{0:5.2f}%'.format(ratio * 100)
        out = '['+ arrow + space + ']' + percent
        return out
        
    def get_size(self, filename):
        #:size:   byte.
        return os.path.getsize(os.path.abspath(filename))
        
    def end(self):
        self.signal.go = False
        self.anim.join()

    
