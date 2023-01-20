#!/usr/bin/env python

"""code template"""

from env import *


def main():

    view = Board()

    while view.win.isOpen():
        update(10)
        # uncomment to pause before action
        view.update()
        # view.pause()
    # pause until mouse clicked
    view.pause()


if __name__ == '__main__':
    main()
