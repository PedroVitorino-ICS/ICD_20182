# -*- coding: utf-8 -*-
import geopandas as gpd
import pandas as pd

geodf = gpd.read_file("ICD_20182/UFEBRASIL.shp")

geodf.head()
geodf.plot()

df = pd.read_csv('DfUnic.csv')
df.head()

states_df = df.groupby(['ano', 'sexo', 'cod uf', 'uf'])[["peso muito baixo", 
                      "peso baixo", "peso adequado", "peso elevado", 
                      "total"]].sum()

merged = geodf.set_index('NM_ESTADO').join(df.set_index('uf'))
merged.head()