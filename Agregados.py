# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 01:46:11 2019

@author: peuce
"""
import plotly 
import csv
import pandas as pd
import numpy as np
import plotly.offline as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='pedro.vitorino20',
                                  api_key='warhero23')

df = pd.read_csv('C:/Users/peuce/ICD_20182-xls_cleaning/DfUnic.csv')
df.head()

states_df = df.groupby(['ano', 'sexo', 'região'], as_index = False).sum()
states_df = states_df.drop('cod ibge', axis = 1)

new_df = states_df.loc[states_df['ano'] == 2008]

new_df = new_df.loc[new_df['região'] == 'NORTE']

new_df = new_df.drop("peso baixo", axis = 1)
new_df = new_df.drop("Unnamed: 0", axis = 1)
new_df = new_df.drop("sexo", axis = 1)
new_df = new_df.drop("peso adequado", axis = 1)
new_df = new_df.drop("peso elevado", axis = 1)
new_df = new_df.drop("total", axis = 1)
new_df = new_df.drop("cod uf", axis = 1)

data = go.Histogram(
        histofunc = "count",
        x = [new_df['ano']],
        y = [new_df['peso muito baixo']],
        name = "count")

#data = [trace]
fig = go.Figure(data = data)
url = py.plot(fig, filename='Histograma')

