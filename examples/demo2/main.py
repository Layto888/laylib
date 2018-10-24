"""
laylib-pygame usage example: no resources example
Author: Amardjia Amine
Date: 01/08/18
Github: ---
"""
from laylib import Environment
from engine import Engine, WIDTH, HEIGHT


def main():
    # init global environment
    demo = Environment(WIDTH, HEIGHT, False, 'No resources demo')
    # with no resources, just call your main engine.
    demo.load_complete(Engine())
    # play
    demo.gInstance.main_loop()
    # quit the game
    demo.destroy()


if __name__ == "__main__":
    main()
