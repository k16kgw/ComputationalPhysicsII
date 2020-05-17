# -*- coding: utf-8 -*-
"""
14-1_logistic.pyプログラム
Landau, et al. 『計算物理学II』朝倉書店．14章p.340の演習
（無次元化された）ロジスティック方程式のシミュレーション
解のカオス的挙動を調べる
使い方 14-1_chaos.py
"""

import numpy as np 
import matplotlib.pyplot as plt
import japanize_matplotlib          # 日本語表示に対応

N = 1000         # 世代数

# 初期設定
x0 = 0.75
mu = 3.95
eps = 2e-14

x0p = x0 * (1 + eps)
mup = mu * (1 - eps)
# 初期値の保存
x1 = x0
x2 = x0p
x3 = x0

# グラフ描画用変数
xlist = [0]
ylist1 = [x1]
ylist2 = [x2]
ylist3 = [x3]

for i in range(1, N):
    x1 = mu * x1 * (1 - x1)
    x2 = mu * x2 * (1 - x2)
    x3 = mup * x3 * (1 - x3)
    # 随時グラフ描画用変数に代入
    xlist.append(i)
    ylist1.append(x1)
    ylist2.append(x2)
    ylist3.append(x3)

# グラフの表示
fig = plt.figure()                  # グラフの描画先の準備
ax1 = plt.subplot(3, 1, 1)      # グラフを表示する領域の追加
plt.title('x0, μ')
ax2 = plt.subplot(3, 1, 2)
plt.title('x0(1+ε), μ')
ax3 = plt.subplot(3, 1, 3)
plt.title('x0, μ(1-ε)')
plt.subplots_adjust(top=0.8)

l1, l2, l3 = "x0, mu", "x0(1+eps), mu", "x0, mu(1-eps)"     # ラベル

ax1.plot(xlist, ylist1, label=l1)
ax2.plot(xlist, ylist2, label=l2)
ax3.plot(xlist, ylist3, label=l3)

#ax1.legend(loc='upper right')   # 凡例
#ax2.legend(loc='upper right')
#ax3.legend(loc='upper right')

plt.xlabel('世代数')
plt.ylabel('（無次元化された）個体数')

#fig.savefig("14-1_logistic/x0-mu.png")     # グラフをフォルダに画像として保存
plt.show()