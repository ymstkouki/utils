#step関数を作成


import random
import numpy as np


#各ステップの時間幅，値を指定
#[0, M]の範囲でランダムな値に
def step(time, repeat, M=1):
    steps = []
    for _ in range(repeat):
        #一様乱数を生成してM倍
        val = random.random()*M
        steps_ = [val]*time
        steps.extend(steps_)
    steps = np.array(steps)
    
    return steps
