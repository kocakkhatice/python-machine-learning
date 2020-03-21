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

from sklearn.preprocessing import Imputer
#axis satır veya sütun bazında hesap yapmak için 
imputer = Imputer(missing_values="NaN", strategy = 'mean', axis= 0)
Yas = veriler.iloc[:,1:4].values
print(Yas)
#imputer = imputer.fit_(Yas[:,1:4])
Yas[:,1:4 ]= imputer.fit_transform(Yas[:,1:4])
print(Yas)

ulke = veriler.iloc[:, 0:1].values
print(ulke)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
#işlemi yap ve sonucu içine yaz = fit_transform
ulke[:,0] = le.fit_transform(ulke[:, 0])
print(ulke)

from sklearn.preprocessing import OneHotEncoder 
ohe = OneHotEncoder(categorical_features = "all" )
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)
sonuc = pd.DataFrame(data = ulke, index=range(22), columns = ["fr", "tr", "us"])
print(sonuc)
sonuc2 = pd.DataFrame(data = Yas, index= range(22), columns=["boy","kilo","yas"] )
print(sonuc2)
cinsiyet = veriler.iloc[:, -1:].values
print(cinsiyet)
sonuc3 = pd.DataFrame(data = cinsiyet, index = range(22), columns = ['cinsiyet'])
s = pd.concat([sonuc, sonuc2, sonuc3], axis = 1)
print(s)