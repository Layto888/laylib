"""
laylib-pygame usage example: no resources example with a particle system.
Use the mouse to control particles.

Author: Amardjia Amine
Date: 24/10/2018
Github: -
"""
from laylib import Environment
from engine import Engine
import sys


def main():
    demo = Environment(1024, 720, False, 'No resources demo')
    # with no resources, just call your main engine.
    demo.load_complete(Engine())
    # particles simulation
    demo.gInstance.main_loop()
    demo.destroy()


if __name__ == "__main__":
    sys.exit(main())
