"""
laylib-pygame usage example: rainy night no resources example.


Author: Amardjia Amine
Date: 02/08/2020
Github: -
"""
from laylib import Environment
from engine import Engine
import sys


def main():
    demo = Environment(600, 480, False, 'Rainy night')
    # with no resources, just call your main engine.
    demo.load_complete(Engine())
    # particles simulation
    demo.gInstance.main_loop()
    demo.destroy()


if __name__ == "__main__":
    sys.exit(main())
