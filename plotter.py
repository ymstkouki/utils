#ファイルから読み込んだデータのうち指定された列をプロット


import os
import csv
import argparse

import numpy as np
import matplotlib.pyplot as plt

from readfile import *


#指定されたchのデータをプロット
def plotter(filename, ch):
    data = readfile(filename)
    for i in ch:
        x = list(range(len(data[:, i])))
        plt.plot(x, data[:, i], label=f'ch{i}')
    plt.legend()
    plt.show()

#filenameとchをコマンドラインから受け取る
def main():
    parser = argparse.ArgumentParser(description="Plot selected data")
    parser.add_argument('filename', type=str, help='data file')
    parser.add_argument('ch', nargs='+', type=int, help='selected channels')
    args = parser.parse_args()
    filename = os.path.expanduser(args.filename)
    ch = args.ch
    plotter(filename, ch)


if __name__ == '__main__':
    main()


"""
ipythonで実行する例
ipython plotter.py {filename} {ch1} {ch2}...
"""
