laylib package for pygame
=========================

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
	:target: https://opensource.org/licenses/MIT

.. image:: https://img.shields.io/badge/version-1.1.4-red.svg
	:target: https://pypi.org/project/laylib
 


This package is made to fast prototype your multimedia applications like games on pygame. 
Write clean and pragmatic design. It lets you focus on the game engine itself, so you dont have
to take care about several details like setting up the window, loading and cheking data (images,
sound, font, fx, music, resources names...).
All you need to do is to put your resources into a specific data folder and use them 
in your game class 'MyEngine()'.

You don't need to reinvent the wheel, some repetitive parts of code (main loop, getting the delta time, 
closing the window, drawing text...) are already described and ready to use in the 
default engine.

    
Usage example
-------------

.. code-block:: python

    from laylib import Environment
    from engine import Engine

    def main():
	demo = Environment(800, 600, False, 'My game')
	demo.load_complete(Engine(), 'data', 'resources.res')
	demo.gInstance.main_loop()
	demo.destroy()

    if __name__ == "__main__":
	main()

	
INSTALLATION
------------

First, install the dependencies:
- Python3 (3.1 or later) <http://www.python.org>
- Pygame 1.9.1 or later <http://pygame.org/download.shtml>
Or run in terminal:

.. code-block:: bash

    $ pip install -r requirements.txt

Then install laylib: 

.. code-block:: bash

    $ pip install laylib

Or alternatively, you can just copy the "laylib" folder into the same
directory as the Python program that uses it.

USAGE
-----
For usage see examples provided with laylib. 
For more details, all other parts of documentation are described in the source file.

TODO
----
# [checkbox:unchecked]
 - [x] add test module for laylib.
 - []  more automation for resources management
 - [x] improve util.py module
 - [x] add more examples for demo

Release History
---------------

* 1.1.4
    * bug fix rotate function util.py file
    * changed value 3.14 to math.pi deg2rad function util.py
    * add complete test module
    * changed README.md to README.rst
* 1.1.3
    * Bug version package fix (init.py file).
* 1.1.2
    * Removed functions: `load_global()`/`destroy_global()` from Resources class.
    * Bug version fix (setup.py file).
* 1.1.1
    * Now we can set the 'time_unit' to change the delta_time unit.
    * Minor bugs fix on util.py
* 0.1.0
    * The first proper release
* 0.0.1
    * Work in progress

Meta
----
Amardjia Amine – amardjia.amine@gmail.com
Distributed under the MIT license.
[https://github.com/Layto888]ok



