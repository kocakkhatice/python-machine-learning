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
veriler = pd.read_csv('veriler.csv')

#kod bölümü
boy = veriler[['boy']]
print(boy)
