#!/usr/bin/env python3
# _*_ coding=utf-8 _*_

import argparse
import code
import signal
import sys
# import numpy as np
import matplotlib.pyplot as plt
import pywt
import pywt.data


def SigHandler_SIGINT(signum, frame):
    print()
    sys.exit(0)


class Argparser(object):
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--string", type=str, help="string")
        parser.add_argument("--bool", action="store_true",
                            help="bool", default=False)
        parser.add_argument("--dbg", action="store_true",
                            help="debug", default=False)
        self.args = parser.parse_args()

# write code here


def premain(argparser):
    signal.signal(signal.SIGINT, SigHandler_SIGINT)
    # here
    original = pywt.data.camera()

    titles = ["approximation", "horizontal detail",
              "vertical detail", "diagonal detail"]
    coeffs2 = pywt.dwt2(original, "bior1.3")
    LL, (LH, HL, HH) = coeffs2
    fig = plt.figure(figsize=(12, 3))

    for i, a in enumerate([LL, LH, HL, HH]):
        ax = fig.add_subplot(1, 4, i+1)
        ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
        ax.set_title(titles[i], fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])

    fig.tight_layout()
    plt.show()


def main():
    argparser = Argparser()
    if argparser.args.dbg:
        try:
            premain(argparser)
        except Exception as e:
            if hasattr(e, "__doc__"):
                print(e.__doc__)
            if hasattr(e, "message"):
                print(e.message)
            variables = globals().copy()
            variables.update(locals())
            shell = code.InteractiveConsole(variables)
            shell.interact(banner="DEBUG REPL")
    else:
        premain(argparser)


if __name__ == "__main__":
    main()
