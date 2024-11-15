#ファイルから読み込んだデータを2次元上の点でプロット
#箱ひげ図などオプションで追加


import os
import argparse

import numpy as np
import matplotlib.pyplot as plt

from readfile import *


#データ点を散布
def scatter(data, i):
    length = len(data)
    noise = np.random.normal(0, 1, length)
    base = [i] * length + noise
    plt.scatter(base, data)

#箱ひげ図を描画
def boxplot(data, i):
    plt.boxplot([data], positions=[i], width=0.5)

#データの平均値を表示
def mean(data, i):
    m = np.mean(data)
    plt.scatter(i, m, marker='x', c='black')

#複数ファイルからデータを読み込み
#見やすいようにx軸の値にはノイズを付与
def scatterer(files, option=''):
    x = []

    #各ファイルからデータを読み込み，optionに応じてプロット
    for i, filename in enumerate(files):
        x = x.append(i)
        filename = os.path.expanduser(filename)
        data = readfile(filename)

        #optionごとの処理
        #散布図
        if 's' in option:
            scatter(data, i)
        #箱ひげ図
        if 'b' in option:
            boxplot(data, i)
        #平均値
        if 'm' in option:
            mean(data, i)
        
    #x軸のラベルをファイル名で置き換え
    plt.xticks(x, files)
    
    #グラフを表示
    plt.xlabel('filename')
    plt.ylabel('value')
    plt.legend()
    plt.show()

#optionとfilesをコマンドラインから受け取る     
def main():
    parser = argparse.ArgumentParser(description="Scatter data points")
    parser.add_argument('option', type=str, help='plot options')
    parser.add_argument('files', nargs='+', type=str, help='data files')
    args = parser.parse_args()
    option = args.option
    files = args.files
    scatterer(files, option=option)


if __name__ == '__main__':
    main()


"""
ipythonで実行する例
ipython scatter.py {option} {file1} {file2}...
"""
