# 研究で使用するために自作したプログラム

## readfile.py
filenameで指定されたファイルの中身を，numpyの配列として読み込む．

## plotter.py
指定されたチャンネルのグラフを描画する．
実行時にファイル名とチャンネルを受け取る．
チャンネルは複数指定可能．

## scatterer.py
散布図などを描画する．
(現時点では)オプションとして散布図，箱ひげ図，平均値を指定．

## step_fun.py
ステップ関数を作成する．
最大値Mを指定し，[0, M]の範囲の一様乱数を都度与える．
