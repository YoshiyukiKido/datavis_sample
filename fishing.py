import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = None
df_o = None

# 漁獲高の読み込み
for y in [2017, 2018, 2019, 2020, 2021, 2022]:
    for m in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        #if 2017 >= y or y >= 2019:
        #    break
        m_str = '0' + str(m) if m < 10 else str(m)
        filename = 'row_data/01_tukibetu_' + str(y) + '_' + m_str + '.xlsx'
        if not os.path.exists(filename):
            continue
        print(filename)
        df = pd.read_excel(filename, sheet_name=1)
        # 境のデータを抽出
        # 2017 - 2021-2
        if y < 2021 or (y == 2021 and m < 3):
            df_s = df.iloc[[3,46],[1,3,31,33,35,37,41,53,63,65,67]]
        # 2022
        elif y == 2022:
            df_s = df.iloc[[3,45],[1,3,33,35,37,39,43,55,63,65,67]]
        # 2021-3 -- 2021-12
        else:
            df_s = df.iloc[[3,45],[1,3,31,33,35,37,41,53,63,65,67]]
        # 魚の種類をカラム名に
        df_s = df_s.rename(columns=df_s.iloc[0])
        df_s = df_s.drop(index=df_s.index[[0]])
        if y == 2022:
            df_s.rename(columns={'くろまぐろ（生）':'まぐろ（生）'}, inplace=True)
        df_s['year_month'] = str(y) + '-' + m_str
        df_s = df_s.set_index('year_month')
        if df_o is None:
            df_o = df_s
        else:
            df_o = pd.concat([df_o, df_s], axis='index')
            #pass

print(df_o)
df_o['京都海面温'] = np.nan
df_o['京都上限値'] = np.nan
df_o['京都下限値'] = np.nan

# 京都気温データの読み込み
for y in [2017, 2018, 2019, 2020]:
    df = pd.read_csv('row_data/kyoto0-' + str(y) + '.csv', header=3)
    for m in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        m_str = '0' + str(m) if m < 10 else str(m)
        try:
            df_o.loc[str(y) + '-' + m_str, '京都海面温'] = df.iloc[:, m].mean()
            df_o.loc[str(y) + '-' + m_str, '京都上限値'] = df.iloc[:, m].max()
            df_o.loc[str(y) + '-' + m_str, '京都下限値'] = df.iloc[:, m].min()
        except:
            print(str(y) + '-' + m_str + ' not found')
''' 
df_o['兵庫海面温'] = np.nan
df_o['兵庫上限値'] = np.nan
df_o['兵庫下限値'] = np.nan

# 兵庫気温データの読み込み
for y in [2017, 2018, 2019, 2021]:
    df = pd.read_csv('row_data/hyogo4-' + str(y) + '.csv', header=3)
    for m in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        m_str = '0' + str(m) if m < 10 else str(m)
        try:
            df_o.loc[str(y) + '-' + m_str, '兵庫海面温'] = df.iloc[:, m].mean()
            df_o.loc[str(y) + '-' + m_str, '兵庫上限値'] = df.iloc[:, m].max()
            df_o.loc[str(y) + '-' + m_str, '兵庫下限値'] = df.iloc[:, m].min()
        except:
            print(str(y) + '-' + m_str + ' not found')
'''
# 解析
df_m = df_o.dropna(how='any')
df_m['まぐろ（生）'] = df_m['まぐろ（生）'].astype('float64')
df_m['まいわし'] = df_m['まいわし'].astype('float64')
df_m['うるめいわし'] = df_m['うるめいわし'].astype('float64')
df_m['かたくちいわし'] = df_m['かたくちいわし'].astype('float64')
df_m['まあじ'] = df_m['まあじ'].astype('float64')
df_m['さば類'] = df_m['さば類'].astype('float64')
df_m['するめいか（生）'] = df_m['するめいか（生）'].astype('float64')
df_m['ぶり類'] = df_m['ぶり類'].astype('float64')
df_m['かれい類（生）'] = df_m['かれい類（生）'].astype('float64')
df_m['まだい'] = df_m['まだい'].astype('float64')

sns.heatmap(df_m.corr())
plt.show()

a = df_m.plot.scatter(x='京都海面温', y='うるめいわし')
for k, v in df_m.iterrows():
    a.annotate(k, xy=(v[11], v[3]))
plt.show()

a = df_m.plot.scatter(x='京都海面温', y='かたくちいわし')
for k, v in df_m.iterrows():
    a.annotate(k, xy=(v[11], v[4]))
plt.show()

a = df_m.plot.scatter(x='京都海面温', y='さば類')
for k, v in df_m.iterrows():
    a.annotate(k, xy=(v[11], v[6]))
plt.show()

a = df_m.plot.scatter(x='京都海面温', y='まだい')
for k, v in df_m.iterrows():
    a.annotate(k, xy=(v[11], v[10]))
plt.show()
