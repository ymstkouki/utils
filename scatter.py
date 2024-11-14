#ファイルから読み込んだデータを2次元上の点でプロット
#箱ひげ図などオプションで追加


import os
import csv

import numpy as np
import matplotlib.pyplot as plt

from readfile import *


#複数ファイルからデータを読み込み
#見やすいようにx軸の値にはノイズを付与
def scatter(files, xlabels=None):
    x = []

    #各ファイルからデータを読み込んでプロット
    for i, filename in enumerate(files):
        x = x.append(i)
        data = readfile(filename)
        length = len(data)
        noise = np.random.normal(0, 1, length)
        base = [i] * length + noise
        plt.scatter(base, data)
    
    #x軸のラベルが与えられていたら置き換え
    if xlabels != None:
        plt.xticks(x, xlabels)
    
    #グラフを表示
    plt.legend()
    plt.show()
        