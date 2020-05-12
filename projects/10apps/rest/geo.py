import pandas as pd
from geopy.geocoders import ArcGIS

df = pd.read_csv('supermarkets.csv')

nom=ArcGIS()

df['Full_Address'] = df['Address'] + ', ' + df['City'] + ', ' + df['State']
df['Coordinates'] = df['Full_Address'].apply(nom.geocode)
df['Latitude'] = df['Coordinates'].apply(lambda x: x.latitude if x != None else None)
df['Longitude'] = df['Coordinates'].apply(lambda x: x.longitude if x != None else None)

print(df)
print(df.Full_Address)