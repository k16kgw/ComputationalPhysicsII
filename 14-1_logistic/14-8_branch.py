# -*- coding: utf-8 -*-
"""
14-8_branch.pyプログラム
Landau, et al. 『計算物理学II』朝倉書店．14章p.343の演習
ロジスティック写像の分岐図を描画するシミュレーション
使い方 14-8_branch.py
"""

import numpy as np 
import matplotlib.pyplot as plt 
import japanize_matplotlib

N = 300     # N+200:経過させる世代数

# グラフ描画用変数
xlist = []
ylist = []

print('start')
for mu in np.arange(1, 4, 0.003):
    #print(mu)
    for x0 in np.arange(0.002, 1, 0.002):
        x = x0
        # 始めに200世代経過させる
        for i in range(1, 200):
            x = mu * x * (1-x)
        for i in range(1, N):
            x_before = x
            x = mu * x * (1-x)
            if x_before == x:
                break
        ylist.append(float(format(x, '.4f')))
        #ylist.append(x)
        xlist.append(mu)

print('グラフ描画開始')
fig = plt.figure(figsize=(15, 15))
plt.title('分岐図')
plt.scatter(xlist, ylist, s=0.3)
plt.xlabel('$\mu$')
plt.ylabel('$x_*$')
fig.savefig('14-1_logistic/branch_1-4.png', dpi=300)   # 画像の保存
plt.show()

print('グラフ描画終了')