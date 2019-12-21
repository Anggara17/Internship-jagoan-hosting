import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt
from matplotlib import rc

print ('\nimport data Data ke Python\n')
data = r'C:\Data\xampp\htdocs\dataData\Data.xlsx'
dataData = pd.read_excel (data)
dataData.head()
print(dataData)

print ('\nAnalisis Deskirptif Data Semua Data Data\n')
Data_inf = dataData['Data']
print(Data_inf)
JumlahData = len(Data_inf)
Mean = Data_inf.mean()
Median = Data_inf.median()
Modus = Data_inf.mode()
Min = min(Data_inf)
Max = max(Data_inf)
StandarDeviasi = statistics.stdev(Data_inf)

print('Jumlah Data = ', JumlahData)
print('Mean = ', Mean)
print('Median = ', Median)
print ('Modus = ')
print(Modus)
print('Nilai Standar Deviasi = ', StandarDeviasi)
print('Nilai Data Terkecil =', Min)
print('Nilai Data Terbesar =', Max)

print ('\nAnalisis Deskirptif )\n')
Data1 = dataData.iloc[0:8,[1]]
Data2 = dataData.iloc[8:20,[1]]
Data3 = dataData.iloc[20:32,[1]]
Data4 = dataData.iloc[32:44,[1]]
Data5 = dataData.iloc[44:56,[1]]
Data6 = dataData.iloc[56:68,[1]]
Data7 = dataData.iloc[68:80,[1]]
Data8 = dataData.iloc[80:92,[1]]
Data9 = dataData.iloc[92:104,[1]]
Data10 = dataData.iloc[104:116,[1]]


LData = [Data1, Data2,Data3, Data4, Data5, Data6, Data7, Data8,Data9,Data2010 ]
LMean =[]
LMin =[]
LMax =[]
for i in LData:

    JumlahDataDataPerTahun = len(i)
    MeanData = i.mean()
    MedianData = i.median()
    MinData = i.min()
    MaxData = i.max()
    StandarDeviasiData = i.std()
    LMean.append(MeanData)
    LMin.append(MinData)
    LMax.append(MaxData)
    print(i)
    print('Jumlah Data = ',JumlahDataDataPerTahun )
    print('Mean = ',MeanData )
    print('Median = ', MedianData )
    print('Min = ', MinData )
    print('Max = ', MaxData)
    print('Standar Deviasi = ', StandarDeviasiData)
    print ('\n')
    print ('')
    
print ('\n Grafik Rata-rata Data tiap tahun \n')
Tahun = ['2019','2018','2017','2016', '2015', '2014','2013', '2012', '2011', '2010']
plt.figure(1)
plt.figure(figsize=(6,8))
plt.plot(Tahun,ListMean, 'c-o')
plt.xticks(rotation=90)
plt.title('Grafik Rata - rata Data tiap tahun (2010-2019)')
plt.xlabel('Tahun')
plt.ylabel('Data') 

print ('\nGrafik Data (MIN) tiap tahun\n')
plt.figure(2)
plt.figure(figsize=(6,8))
plt.bar(Tahun,ListMin, color = "green")
plt.xticks(rotation=90)
plt.title('Grafik Data terkecil tiap tahun (2010-2019)')
plt.xlabel('Tahun') 
plt.ylabel('Data') 
plt.show()