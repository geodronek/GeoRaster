# OC-POL
DLA GEODANYCH:
- Wczytaj csv [done]
- Funkcja wyświetlacją dane dla wybranego powiatu - def() / gdf.columns()  
- Wykres dla każdego województwa (matplotlib)
- Mapa dla wybranego powiatu (apka)

# SatTiff
DLA RASTRÓW: 
Porównuje dwa rastry (GeoTIFF, Sentinel-2 JP2 itp.) tego samego obszaru i pokazuje różnice wizualne oraz podstawowe statystyki.

# Główne możliwości (MVP)
- Upload dwóch rastrów
- Automatyczne wyrównanie CRS i extentu (jeśli możliwe)
- Porównanie RGB → RGB
- Mapa absolutnych różnic (grayscale + kolorowana)
- Prosty binary change mask (próg użytkownika)
- Podstawowe indeksy spektralne (NDVI, NDWI) i ich różnice
- Interaktywny slider przed-po (leaflet)

# Technologie
- Django 5.x
- rasterio + rioxarray + numpy
- opencv-python-headless (do konturów i pseudo-kolor)
- leaflet.js + leaflet-image-overlay
- PostgreSQL + PostGIS (opcjonalnie)
- Celery + Redis (na dłuższe obliczenia)


