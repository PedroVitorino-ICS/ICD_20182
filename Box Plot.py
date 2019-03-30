# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 00:41:09 2019

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

trace1 = go.Box(y = df.loc[df['sexo'] == "M", 'peso muito baixo'],
                name = 'Peso Muito Baixo por Sexo - Masculino',
                marker = {'color': 'blue'})
                         
trace2 = go.Box(y = df.loc[df['sexo'] == "F", 'peso muito baixo'],
                name = 'Peso Muito Baixo por Sexo - Feminino',
                marker = {'color': 'red'})
                          
trace3 = go.Box(y = df.loc[df['sexo'] == "M", 'peso baixo'],
                name = 'Peso Baixo por Sexo - Masculino',
                marker = {'color': 'blue'})
                          
trace4 = go.Box(y = df.loc[df['sexo'] == "F", 'peso baixo'],
                name = 'Peso Baixo por Sexo - Feminino',
                marker = {'color': 'red'})

trace5 = go.Box(y = df.loc[df['sexo'] == "M", 'peso adequado'],
                name = 'Peso Adequado por Sexo - Masculino',
                marker = {'color': 'blue'})
                          
trace6 = go.Box(y = df.loc[df['sexo'] == "F", 'peso adequado'],
                name = 'Peso Adequado por Sexo - Feminino',
                marker = {'color': 'red'})

trace7 = go.Box(y = df.loc[df['sexo'] == "M", 'peso elevado'],
                name = 'Peso Elevado por Sexo - Masculino',
                marker = {'color': 'blue'})
                          
trace8 = go.Box(y = df.loc[df['sexo'] == "F", 'peso elevado'],
                name = 'Peso Elevado por Sexo - Feminino',
                marker = {'color': 'red'})
                          
data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8]

layout = go.Layout(title = 'Dispersão de Peso por Sexo',
                   titlefont = {'family': 'Arial',
                                'size': 20,
                                'color': '#7f7f7f'},
                   #xaxis = {'title': 'Indentificador Peso'},
                   yaxis = {'title': 'N de Casos'},
                   paper_bgcolor = 'rgb(243, 243, 243)',
                   plot_bgcolor = 'rgb(243, 243, 243)')

fig = go.Figure(data = data, layout=layout)
url = py.plot(fig, filename='Box Plot')