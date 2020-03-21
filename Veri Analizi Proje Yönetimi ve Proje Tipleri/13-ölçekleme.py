# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 00:10:35 2020

@author: ASUSGAMING
"""

#kütüphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#kodlar
#veri yükleme
veriler = pd.read_csv('eksikveriler.csv')

imputer= Imputer(missing_values='NaN', strategy = 'mean', axis=0 )    

Yas = veriler.iloc[:,1:4].values
print(Yas)
imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)

ulke = veriler.iloc[:,0:1].values
print(ulke)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
ulke[:,0] = le.fit_transform(ulke[:,0])
print(ulke)
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features='all')
ulke=ohe.fit_transform(ulke).toarray()
print(ulke)
print(list(range(22)))

sonuc = pd.DataFrame(data = ulke, index = range(22), columns=['fr','tr','us'] )
print(sonuc)

sonuc2 =pd.DataFrame(data = Yas, index = range(22), columns = ['boy','kilo','yas'])
print(sonuc2)

cinsiyet = veriler.iloc[:,-1].values
print(cinsiyet)

sonuc3 = pd.DataFrame(data = cinsiyet , index=range(22), columns=['cinsiyet'])
print(sonuc3)

s=pd.concat([sonuc,sonuc2],axis=1)
print(s)

s2= pd.concat([s,sonuc3],axis=1)
print(s2)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(s, sonuc3, test_size = 0.33, random_state = 0)
#random state: makinanın her durum için bir satır almasını sağlar

#ölçekleme: her kolonun katsayısı farklı etkileyecektir
#verileri aynı düzlemde tutmak için standardization ve normalisation kullanılır.
#boy normalleştirme: max= 193 min= 125 ilk satırdaki 130 için (130- 125)/193-125 = 0.07
#standartisation ortalamaya ne kadar yakın olduğunu +- olarak gösterir
#vs: n değerleri 0 1 aralığına indirger, s değerler üzerinden ilişkiler
#n nin sorunu outlier değerler işleri bozacaktır, örneğin kilonun 10000 oolması. s bu konuda biraz daha iyidir

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train =sc.fit_transform(x_train) 

















