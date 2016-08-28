#!/usr/bin/env python3
# fileencoding=utf-8
'''
cmdanime.py
~~~~~~~~~~~

cmdanime.py provides command-line animation. When yor start to run a long calculation in python, 
if there is no output in command-line, you are warried about whichever the program starts or not. 
In that case, cmdanime.CmdAnimation show animation in command-line.

.. code-block:: python
   
   from easyutil import CmdAnimation
   
   ## For Command Line Animation. 
   anm = CmdAnimation()
   anm.start()
   # Your function here.
   anm.end()


.. autoclass:: easyutil.Signal
    :members:

.. autoclass:: easyutil.CmdAnimation
    :members:


'''
import os
import sys
import time
import threading
import itertools
from easy_string import *

class easyThread(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.value = 0
        self.func = func
        self.args = args
        
    def run(self):
        self.value =  self.func(self.args[1])
        
    def get_value(self):
        return self.value
    

class Signal:
    go = True


class CmdAnimation:
    '''
    .. code-block::python 
       :emphasize-lines: 3,5

    '''
    def __init__(self, anim_type='spin', filename='', size=0, msg='', msg2=''):
        """ 
        :anim_type[str]:  [spin, progress]
        :filename[str]:   for showing progress bar.
        :full_size[int]:  for showing progress bar. 
        """
        self.full_size = size
        self.signal = Signal()
        self.duration_time = 0
        self.filename = filename
        self.types = {"spin": self._spin, "progress": self._progress}
        self.func = self.types[anim_type]
        self.msg = msg
        self.msg2 = msg2
        self.msg2_size = 20
        
    def start(self):
        '''
        start() starts animation. 
        '''
        self.anim = threading.Thread(target=self.func, args=(self.msg, self.msg2, self.signal))
        self.anim.start()
        
    def _spin(self, msg, msg2, signal):
        # Show Spin.
        spins  = '|/-\\'
        spins2 = '/-\\|'
        spins3 = '-\\|/'
        spins4 = '\\|/-'
        sys.stdout.write(msg)
        for i in itertools.cycle(range(4)):
            out = "{}\t{}{}{}{}".format(msg2, spins[i], spins2[i], spins3[i], spins4[i])
            sys.stdout.write(out)
            sys.stdout.flush()
            sys.stdout.write('\x08'*len(out))
            time.sleep(.1)
            if not signal.go:
                break
        sys.stdout.write('\x08'*(4+len(msg)))

    def _progress(self, msg, msg2, signal):
        sys.stdout.write(msg)
        while True:
            try:
                now_size = self._get_size(self.filename)
            except:
                continue
            self._showProgress(msg2, now_size)
            if self.full_size == now_size:
                break
            
    def _showProgress(self, msg2, now_size):
        # Show progress bar.
        out = msg2 + self._get_bar(now_size)
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
        
    def _get_size(self, filename):
        '''
        _get_size():    get a filesize form a filename and return the filsesize.
        '''
        return os.path.getsize(os.path.abspath(filename))
        
    def end(self):
        '''
        end() stop animation. 
        '''
        self.signal.go = False
        self.anim.join()


class MultiCmdAnimation(CmdAnimation):
    '''
    This class is an extension of CmdAnimation and provide a command-line animation in multipule line.

    .. code-block::python 
       :emphasize-lines: 3,5

    '''
    def __init__(self, anim_type='progress', filenames=[], sizes=[], msgs=[], msgs2=[]):
        """ 
        Now only suppoting progress mode.
        
        :anim_type[str]:  [spin, progress]
        :filenames[str list]:   for showing progress bar.
        :full_sizes[int list]:  for showing progress bar. 
        :full_sizes[int list]:  for showing progress bar. 
        """
        CmdAnimation.__init__(self)
        self.types = {"progress": self._progress}
        self.func = self.types[anim_type]
        self.filenames = filenames
        self.msg = ['' for i in range(len(msgs2))]
        self.msg2 = msgs2
        self.signal = Signal()
        self.full_sizes = sizes

    def start(self):
        '''
        start() starts animation. 
        '''
        self.anim = threading.Thread(target=self.func, args=(self.msg, self.msg2, self.signal))
        self.anim.start()

    def _progress(self, msg, msg2, signal):
        _msg = ' '
        get_names = [ easyThread(func=self._get_size, args=(_msg, filename))
                      for filename in self.filenames ]
        [ get_names[i].start() for i, dump in enumerate(get_names) ]
        while True:
            now_sizes = [ get_names[i].get_value() for i, _dump in enumerate(get_names) ]
            self._showProgress(msg2, now_sizes)
            [ get_names[i].join() for i, dump in enumerate(get_names) if now_sizes[i] == self.full_sizes[i]]
        
    def _showProgress(self, msg2, now_sizes):
        # Show progress bar.
        out = ''
        for i, now_size in enumerate(now_sizes):
            header = constant_width(msg2[i], 50)
            out += header + self._get_bar(now_size, self.full_sizes[i])
        sys.stdout.write(out)
        time.sleep(.3)
        sys.stdout.flush()
        sys.stdout.write('\x08'*(len(out)))
        time.sleep(.1)        

    def _get_bar(self, now_size, full_size):
        _space = ' '
        _bar = '='
        _arrow = '>'
        bar_size = 60
        ratio = now_size / full_size
        arrow = _bar * (int((ratio) * bar_size) - 1) + _arrow
        space = _space * (bar_size - len(arrow))
        percent = '{0:5.2f}%   |'.format(ratio * 100)
        out = '['+ arrow + space + ']' + percent
        return out

    
if __name__ == "__main__":

    msgs  = ["msg:hello"+str(i) for i in range(4)]
    msgs2 = [u"msg2:helloあ" for i in range(4)]
    files = ["hello"+str(i)+'.txt' for i in range(4)]
    sizes = [10*4 for i in range(4)]
    anm = MultiCmdAnimation("progress", filenames=files, msgs2=msgs2, sizes=sizes)
    anm.start()
    anm.end()

    
