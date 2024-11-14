#ファイルからデータを読み出す
#冒頭のコメントは読み飛ばし，numpy配列で読み込む
#数値データのみで構成されたファイルを想定


import csv

import numpy as np


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
