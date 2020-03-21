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