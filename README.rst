Easy_utill (Python3 scripts)
============================

Easy utill provide memory usage, flush animation during calculation and so on.

Requirements
------------

* Python > 3.5.1

Set Up
------

Install virtualenv. (for protecting your Home environment.)

.. code-block:: bash
   
   python3 -m pip install -U pip setuptools
   python3 -m pip install virtualenv
   # or
   pip3 install virtualenv

activate virtualenv

.. code-block:: bash
   
   virtualenv -p python3 venv
   source venv/bin/activate
   # Removing virtual environment
   # (venv) deactivate 

build & install
---------------

.. code-block:: bash
   
   pip install git+https://github.com/Moguf/easy_utill.git
   # or 
   git clone https://github.com/Moguf/easy_utill.git
   cd easy_utill
   python setup.py build
   python setup.py install
   
   

How to use
----------

.. code-block:: python
   
   from easyutill import CmdAnimation, MemLimit
   
   ## For Command Line Animation. 
   anm = CmdAnimation()
   anm.start()
   # Your function here.
   anm.end()
   
   ## For Memory Limit 
   memutl = MemUtill()
   memutl.set(8)
   # Memory Limit is 8Gb.

When you want to get a big data from web server and know download progress, you have better to use progress-mode.

.. code-block:: python
                
   from urllib.request import urlopen, urlretrieve
   from easyutill import CmdAnimation
   
   ## For Command Line Animation.
   url = "http\://hoge.com/target.html"
   filename = "target.html"
   meta = urlopen(url).info()
   size = int(meta.get_all("Content-Length")[0])
   anm = CmdAnimation('progress', filename=filename, size=size)
   anm.start()
   urlretrieve(url, filename)

   """ 
   ex)
   [======>                       ] 12.01%
   """



