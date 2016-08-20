#!/usr/bin/env python3
# coding : utf-8
'''


'''
import sys
import time
import resource
import threading
import itertools


class Signal:
    go = True


class MemMenager:
    '''
    '''
    def __init__(self):
        self.maxsize = 16

    def setLimitMemory(self,maxsize):
        # set Max Memory size.
        # maxsize:unit is Gb.
        self.maxsize = 1024*1024*1024*maxsize
        soft, hard = resource.getrlimit(resource.RLIMIT_AS)
        resource.setrlimit(resource.RLIMIT_AS,(self.maxsize,hard))
        print('Set Memoy Limit\t:\t{}Gb;'.format(maxsize))


class CafepyStdout:
    '''
    '''
    def __init__(self):
        self.duration_time = 0
        self.signal = Signal()
        
    def start(self):
        msg = "Caluclating->\t: "
        self.spinner = threading.Thread(target=self.spin,args=(msg,self.signal))
        self.spinner.start()

    def spin(self,msg,signal):
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
        
    def end(self):
        self.signal.go = False
        self.spinner.join()


