from time import sleep, strftime, localtime
from sys import executable

import numpy

VERSION = '0.1.5'


def runner():
    print('{} {}'.format(VERSION, strftime('%Y-%m-%d %H:%M:%S', localtime())))
    print('Python: {} Numpy: {}'.format(executable, numpy.__version__))


if __name__ == '__main__':
    while True:
        runner()
        sleep(1)
