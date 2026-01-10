import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

miasto = "Częstochowa"

path_file = 'C:/Users/kamil/OneDrive/Desktop/Aplikacje/python_2/withJula/GeoRaster/all_schrony(XY)_csv.csv'
gdf = gpd.read_file(path_file, encoding="utf-8")

gdf.loc[gdf["Powiat"] == "Częstochowa", ["ObjectID", "Powiat", "Rodzaj_obi"]]

liczba_schronien = len(gdf.loc[gdf["Powiat"] == "Częstochowa", ["ObjectID", "Powiat", "Rodzaj_obi"]])
print(f'Liczba schronów w powiecie {miasto} to: {liczba_schronien}')
# 1453
