# -*- coding: utf-8 -*-
"""
14-1_chaos.pyプログラム
Landau, et al. 『計算物理学II』朝倉書店．14章p.340の演習
（無次元化された）ロジスティック方程式のシミュレーション
解のカオス的挙動を調べる
使い方 14-1_chaos.py
"""

import numpy as np 
import matplotlib.pyplot as plt
import japanize_matplotlib          # 日本語表示に対応

N = 100         # 世代数

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

"""logistic方程式の計算"""
for i in range(1, N):
    x1 = mu * x1 * (1 - x1)
    x2 = mu * x2 * (1 - x2)
    x3 = mup * x3 * (1 - x3)
    # 随時グラフ描画用変数に代入
    xlist.append(i)
    ylist1.append(x1)
    ylist2.append(x2)
    ylist3.append(x3)

"""個別のグラフを並べて表示"""
# グラフ描画先の準備
fig1 = plt.figure()
# グラフを表示する領域の追加
ax1 = plt.subplot(3, 1, 1)          
ax2 = plt.subplot(3, 1, 2)
ax3 = plt.subplot(3, 1, 3)
# 各グラフタイトル
ax1.set_title('$x_0, \mu$')
ax2.set_title('$x_0(1+\epsilon), \mu$')
ax3.set_title('$x_0, \mu(1-\epsilon)$')
# 各グラフの設定
c1, c2, c3 = "blue", "red", "green"                     # プロットの色
l1, l2, l3 = "$x_0, \mu$", "$x_0(1+\epsilon), \mu$", "$x_0, \mu(1-\epsilon)$" # ラベル
ax1.plot(xlist, ylist1, color=c1, label=l1)
ax2.plot(xlist, ylist2, color=c2, label=l2)
ax3.plot(xlist, ylist3, color=c3, label=l3)
## 凡例
#ax1.legend(loc='upper right')
#ax2.legend(loc='upper right')
#ax3.legend(loc='upper right')
# 軸名
plt.xlabel('世代数')
plt.ylabel('（無次元化された）個体数')

fig1.suptitle('グラフを並べて表示', x=0.5, y=0.995)
fig1.tight_layout()       # レイアウト設定
fig1.savefig("14-1_logistic/chaos-parallel.png")     # グラフをフォルダに画像として保存
plt.show()      # グラフの表示

"""グラフを重ねて表示"""
fig2 = plt.figure()     # グラフ描画先の準備
ax = plt.subplot()      # グラフを表示する領域の追加

ax.set_title('グラフを重ねて表示')
ax.set_xlabel('世代数')
ax.set_ylabel('（無次元化された）個体数')

ax.plot(xlist, ylist1, color=c1, label=l1)
ax.plot(xlist, ylist2, color=c2, label=l2)
ax.plot(xlist, ylist3, color=c3, label=l3)
ax.legend(loc=0)    # 凡例
fig2.tight_layout() # レイアウトの設定
fig2.savefig('14-1_logistic/chaos-overlap.png')   # 画像の保存
plt.show()