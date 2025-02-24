import pandas as pd
import matplotlib.pyplot as plt

path1 = '/home/nairaceorex/PycharmProjects/dataseries_rgaumsha/AofED_Datasets_Excel/EXRUK.xls'

df1 = pd.read_excel(path1, header=None)
Y = df1.iloc[:, 1]
X = df1.iloc[:, 0]

plt.plot(X, Y)
plt.show()
