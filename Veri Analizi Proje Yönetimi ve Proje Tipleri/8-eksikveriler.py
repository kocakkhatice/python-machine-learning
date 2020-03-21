# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 23:18:02 2020

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