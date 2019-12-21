import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


data = r'C:\Data\xampp\htdocs\dataData\Datamtcars.xlsx'
df = pd.read_excel (data)
df.head()

print ('Tabel mpg_level\n')

df.loc[(df['mpg'] < 20 ),'mpg_level'] = 'low'
df.loc[(df['mpg'] >= 20 )&(df['mpg'] <= 30 ),'mpg_level'] = 'medium'
df.loc[(df['mpg'] > 30 ),'mpg_level'] = 'hard'
print (df)

print ('Scatter Plot\n')
area = np.pi*3
plt.figure(1)
plt.scatter(x=df['wt'], y=df['mpg'], s=area, alpha=0.5)
plt.title('Scatter plot')
plt.xlabel('wt')
plt.ylabel('mpg')

print ('BarChart\n')
objects = df['Cars']
y_pos = np.arange(len(objects))
performance = df['mpg']
plt.figure(2)
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.xticks(rotation=90)
plt.ylabel('Milles/Gallon')
plt.title('Data dalam Barchart')
plt.show()
