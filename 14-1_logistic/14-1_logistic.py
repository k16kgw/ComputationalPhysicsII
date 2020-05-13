# -*- coding: utf-8 -*-
"""
14-1_logistic.pyプログラム
Landau, et al. 『計算物理学II』朝倉書店．14章p.338の演習
（無次元化された）ロジスティック方程式のシミュレーション
使い方 14-1_logistic.py
"""

import matplotlib.pyplot as plt
import japanize_matplotlib          # 日本語表示に対応

N = 100         # 世代数

# 初期設定
x = float(input("初期値x0を入力してください:"))
mu = float(input("増加率μの値を入力してください:"))
x0 = x      # 初期値を保存

# グラフ描画用変数
xlist = [0]
ylist = [x]

for i in range(1, N):
    x = mu * x * (1 - x)
    # 随時グラフ描画用変数に代入
    xlist.append(i)
    ylist.append(x)

#plt.rcParams["font.family"] = "IPAGothic"

# グラフの表示
fig = plt.figure()                  # グラフの描画先の準備
plt.title('初期値x0=%1.3f, 増加率μ=%1.3f' %(x0, mu))
plt.plot(xlist, ylist)
plt.xlabel('世代数')
plt.ylabel('（無次元化された）個体数')
fig.savefig("14-1_logistic/x0_%1.3f-mu_%1.3f.png" %(x0, mu))     # グラフを画像に保存
plt.show()