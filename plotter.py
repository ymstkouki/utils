#ファイルから読み込んだデータのうち指定された列をプロット


import os
import csv
import argparse

import numpy as np
import matplotlib.pyplot as plt


#ファイルからデータの読み込み
#最初が#で始まる行はコメントとして読み飛ばす
def readfile(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == '#':
                continue
            else:
                d = [float(val) for val in row if val != '']
                data.append(d)
    data = np.array(data)

    return data

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
    print(args.filename)

    filename = os.path.expanduser(args.filename)
    ch = args.ch
    plotter(filename, ch)


if __name__ == '__main__':
    main()


"""
ipythonで実行する例
ipython plotter.py {filename} {ch1} {ch2}...
"""
