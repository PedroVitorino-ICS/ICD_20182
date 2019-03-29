# -*- coding: utf-8 -*-
import geopandas as gpd

geodf = gpd.read_file("ICD_20182/UFEBRASIL.shp")

geodf.plot()