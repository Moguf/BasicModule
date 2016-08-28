#!/usr/bin/env python3
# coding : utf-8
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


class easyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.value = None
        
    def run(self):
        self.value =  self.target(self.args[2])
        
    def get_value():
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
            out = "{}\t{}{}{}{}\n".format(msg2, spins[i], spins2[i], spins3[i], spins4[i])
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


class MultiCmdAnimation:
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
        self.types = {"progress": self._progress}
        self.func = self.types[anim_type]
        self.filenames = filenames
        self.msg = msgs
        self.msg2 = msgs2
        self.signal = Signal()
        
    def _check(self):
        pass

    def _progress(self):
        pass
    
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

    def start(self):
        '''
        start() starts animation. 
        '''
        self.anim = threading.Thread(target=self.func, args=(self.msg, self.msg2, self.signal))
        self.anim.start()

    def _progress(self, msg, msg2, signal):
        while True:
            _msg = ' '
            print(self.filenames)
            get_names = [ easyThread(target=self._get_size, args=(_msg, filename))
                          for filename in self.filenames ]
            [ get_names[i].start() for i in len(get_names) ]
            [ get_names[i].join() for i in len(get_names) ]
            now_size = [ get_names[i].get_value() for i in len(get_names) ]
            print(now_size)
            break
            '''
            self._showProgress(msg2, now_size)
            if self.full_size == now_size:
                break
            '''
            
    def _get_size(self, msg, filename):
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
        
if __name__ == "__main__":
    msgs  = ["msg:hello"+str(i) for i in range(4)]
    msgs2 = ["msg2:hello"+str(i) for i in range(4)]
    files = ["hello"+str(i)+'.txt' for i in range(4)]
    sizes = [10*4 for i in range(4)]
    anm = MultiCmdAnimation("progress", filenames=files, msgs=msgs, msgs2=msgs2, sizes=sizes)
    anm.start()
    anm.end()
