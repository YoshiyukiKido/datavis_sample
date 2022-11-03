import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = None
df_o = None

df =  pd.read_excel('row_data/012-2.xls', sheet_name=0)
# 魚介だけ
df_s = df.iloc[[2,28,29], [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]]
df_s.iloc[0,0] = "種類"
df_s = df_s.rename(columns=df_s.iloc[0])
df_s = df_s.drop(index=df_s.index[[0]])
df_s = df_s.set_index('種類')
df_s.T.plot()
plt.ylim(0, 120)
plt.show()