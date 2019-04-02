# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 12:45:08 2019

@author: peuce
"""

import plotly 
import csv
import pandas as pd
import numpy as np
import plotly.offline as py
import plotly.graph_objs as go

regionname = 'NORTE'

plotly.tools.set_credentials_file(username='pedro.vitorino20',
                                  api_key='warhero23')

df = pd.read_csv('C:/Users/peuce/ICD_20182-xls_cleaning/DfUnic.csv')
df.head()

states_df = df.groupby(['ano', 'sexo', 'região'], as_index = False).sum()
states_df = states_df.drop('cod ibge', axis = 1)

df_region = states_df

df_regionM = states_df[states_df['região']==regionname][states_df['sexo'] 
                        == 'M']

df_regionM.ano = pd.to_datetime(df_region.ano, format='%Y')

trace0 = go.Scatter(
                x=df_regionM.ano,
                y=df_regionM['peso muito baixo'],
                name = "Peso Muito Baixo",
                line = dict(color = 'red'),
                opacity = 0.8)

trace1 = go.Scatter(
                x=df_regionM.ano,
                y=df_regionM['peso baixo'],
                name = "Peso Baixo",
                line = dict(color = 'blue'),
                opacity = 0.8)
                
trace2 = go.Scatter(
                x=df_regionM.ano,
                y=df_regionM['peso adequado'],
                name = "Peso Adequado",
                line = dict(color = 'black'),
                opacity = 0.8)

trace3 = go.Scatter(
                x=df_regionM.ano,
                y=df_regionM['peso elevado'],
                name = "Peso Elevado",
                line = dict(color = 'pink'),
                opacity = 0.8)
    
df_region_F = states_df[states_df['região']==regionname][states_df['sexo'] 
                        == 'F']

df_region_F.ano = pd.to_datetime(df_region_F.ano, format='%Y')

trace4 = go.Scatter(
                x=df_region_F.ano,
                y=df_region_F['peso muito baixo'],
                name = "Peso Muito Baixo",
                line = dict(color = 'red'),
                opacity = 0.8,
                xaxis='x2',
                yaxis='y2')

trace5 = go.Scatter(
                x=df_region_F.ano,
                y=df_region_F['peso baixo'],
                name = "Peso Baixo",
                line = dict(color = 'blue'),
                opacity = 0.8,
                xaxis='x2',
                yaxis='y2')
                
trace6 = go.Scatter(
                x=df_region_F.ano,
                y=df_region_F['peso adequado'],
                name = "Peso Adequado",
                line = dict(color = 'black'),
                opacity = 0.8,
                xaxis='x2',
                yaxis='y2')

trace7 = go.Scatter(
                x=df_region_F.ano,
                y=df_region_F['peso elevado'],
                name = "Peso Elevado",
                line = dict(color = 'pink'),
                opacity = 0.8,
                xaxis='x2',
                yaxis='y2')

trace8 = go.Box(y = df_region.loc[df_region['sexo'] == "M", 'peso muito baixo'],
                name = 'Peso Muito Baixo-M',
                marker = {'color': 'blue'},
                xaxis='x3',
                yaxis='y3')
                         
trace9 = go.Box(y = df_region.loc[df_region['sexo'] == "F", 'peso muito baixo'],
                name = 'Peso Muito Baixo-F',
                marker = {'color': 'red'},
                xaxis='x3',
                yaxis='y3')
                          
trace10 = go.Box(y = df_region.loc[df_region['sexo'] == "M", 'peso baixo'],
                name = 'Peso Baixo-M',
                marker = {'color': 'blue'},
                xaxis='x3',
                yaxis='y3')
                          
trace11 = go.Box(y = df_region.loc[df_region['sexo'] == "F", 'peso baixo'],
                name = 'Peso Baixo-F',
                marker = {'color': 'red'},
                xaxis='x3',
                yaxis='y3')

trace12 = go.Box(y = df_region.loc[df_region['sexo'] == "M", 'peso adequado'],
                name = 'Peso Adequado-M',
                marker = {'color': 'blue'},
                xaxis='x3',
                yaxis='y3')
                          
trace13 = go.Box(y = df_region.loc[df_region['sexo'] == "F", 'peso adequado'],
                name = 'Peso Adequado-F',
                marker = {'color': 'red'},
                xaxis='x3',
                yaxis='y3')

trace14 = go.Box(y = df_region.loc[df_region['sexo'] == "M", 'peso elevado'],
                name = 'Peso Elevado-M',
                marker = {'color': 'blue'},
                xaxis='x3',
                yaxis='y3')
                          
trace15 = go.Box(y = df_region.loc[df_region['sexo'] == "F", 'peso elevado'],
                name = 'Peso Elevado-F',
                marker = {'color': 'red'},
                xaxis='x3',
                yaxis='y3')

layout = go.Layout(
        dict(title = "Região Por Peso " + regionname),
        xaxis=dict(
        title = "Masculino", 
        domain=[0, 0.45]
    ),
    yaxis=dict(
        domain=[0, 0.45]
    ),
     xaxis2=dict(
        title = "Feminino",
        domain=[0.55, 1]
    ),
    yaxis2=dict(
        domain=[0, 0.45],
        anchor='x2'
    ),
    xaxis3=dict(
        domain=[0, 1],
        anchor='y3'
    ),
    yaxis3=dict(
        domain=[0.55, 1]
    )
)
    
data = [trace0,trace1, trace2, trace3, trace4, trace5, trace6, trace7,
        trace8, trace9, trace10, trace11, trace12, trace13, trace14, trace15]

fig = dict(data=data, layout=layout)
url = py.plot(fig, filename = regionname)








