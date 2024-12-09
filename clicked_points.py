#クリックした点の値を取得してファイルに保存


import os
import csv
import argparse
import numpy as np
import matplotlib.pyplot as plt


def readfile(filename):
    datalist = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            d = [float(val) for val in row[:-2]]
            datalist.append(d)
        datalist = np.array(datalist)
    return datalist

#クリックした点の値(横軸)を取得
#左クリックのみに反応
def onclick(event, savepath="./clicked.csv"):
    if event.inaxes is not None:
        if event.button == 1:
            xdata = int(event.xdata)
            with open(savepath, "a") as file:
                file.write(f"{xdata}\n")
            print(f"x is {xdata}")

def main():
    #datapath, chをコマンドラインから受け取る
    parser = argparse.ArgumentParser(description="Save clicked points")
    parser.add_argument("datapath", type=str, help="datafile")
    parser.add_argument('ch', nargs='+', type=int, help='selected channels, x and y axis')
    args = parser.parse_args()
    
    #プロットするデータを指定
    datafile = os.path.expanduser(args.datapath)
    data = readfile(datafile)
    xdata = data[:, args.ch[0]]
    ydata = data[:, args.ch[1]]

    #クリックされるごとにイベントを呼び出す
    fig, ax = plt.subplots()
    ax.plot(xdata, ydata)
    cid = fig.canvas.mpl_connect("button_press_event", onclick)
    plt.show()


if __name__ == "__main__":
    main()


"""
ipythonで実行する例
ipython clicked_points.py {datapath} {x} {y}
"""
