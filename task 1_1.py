import pandas as pd
import matplotlib.pyplot as plt

directory = '/home/nairaceorex/PycharmProjects/dataseries_rgaumsha/AofED_Datasets_Excel'
path1 = f'{directory}/EXRUK.xls'
path2 = f'{directory}/INCOME.xls'

df1 = pd.read_excel(path1, header=None)
df2 = pd.read_excel(path2, header=0)

Y = df1.iloc[:, 1]
X = df1.iloc[:, 0]

Y1=df2.iloc[:,1]
Y2=df2.iloc[:,2]
X1 = df2.iloc[:, 0]

fig, ax = plt.subplots()
ax.plot(X1, Y1)
ax.plot(X1, Y2)

#plt.plot(X, Y)
#plt.show()

income_growthRates = []
for i in range(1,len(Y2)):
    growthRate = 100 * (Y2[i]-Y[i-1])
    income_growthRates.append(growthRate)
plt.plot(X1[1:], income_growthRates)
plt.show()
