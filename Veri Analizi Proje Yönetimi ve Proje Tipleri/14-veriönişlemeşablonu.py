# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 00:10:35 2020

@author: ASUSGAMING
"""

#1. kütüphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2. Veri önişleme 

#2.1 Veri Yükleme
veriler = pd.read_csv('eksikveriler.csv')

#2.2 eksik veriler 
imputer= Imputer(missing_values='NaN', strategy = 'mean', axis=0 )    
Yas = veriler.iloc[:,1:4].values
#print(Yas)
imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
#print(Yas)

#encoder: Nominal ordinal(Kategorik)-> Numeric 
ulke = veriler.iloc[:,0:1].values #iloc= integer location 
#print(ulke)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
ulke[:,0] = le.fit_transform(ulke[:,0])
#print(ulke)

#ohe kolon başlıklarına etiketeri taşımak ve her etiketin altına 1,0 yazmak; oraya aitliğini göztermek 
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features='all')
ulke=ohe.fit_transform(ulke).toarray()
print(ulke)

#numpy dizilerin dataframe dönüşümü 
sonuc = pd.DataFrame(data = ulke, index = range(22), columns=['fr','tr','us'] )
print(sonuc)
sonuc2 =pd.DataFrame(data = Yas, index = range(22), columns = ['boy','kilo','yas'])
print(sonuc2)
cinsiyet = veriler.iloc[:,-1].values
print(cinsiyet)
sonuc3 = pd.DataFrame(data = cinsiyet , index=range(22), columns=['cinsiyet'])
print(sonuc3)
#concatenation 
s=pd.concat([sonuc,sonuc2],axis=1)
print(s)
s2= pd.concat([s,sonuc3],axis=1)
print(s2)

#eğitim ve test bölmesi 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(s, sonuc3, test_size = 0.33, random_state = 0)

#ölçekleme
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train =sc.fit_transform(x_train) 

















