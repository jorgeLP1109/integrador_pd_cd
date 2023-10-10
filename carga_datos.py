import pandas as pd


data = {
    'Nombre': ['Jorge', 'Moises', 'Osiris', 'Lefry', 'Lurdes'],
    'is_dead': [1, 0, 1, 0, 0],
    'edad': [32, 45, 21, 29, 38]
}


print("\n///////////////////////////////////////////////////////////////\n")

df = pd.DataFrame(data)
print(df)

print("\n///////////////////////////////////////////////////////////////\n")


df_perecidos = df[df['is_dead'] == 1]
df_no_perecidos = df[df['is_dead'] == 0]


promedio_edades_perecidos = round(df_perecidos['edad'].mean(), 2)
promedio_edades_no_perecidos = round(df_no_perecidos['edad'].mean() , 2)


print("Promedio de edades de personas is dead:", promedio_edades_perecidos)
print("Promedio de edades de personas que no perecieron:", promedio_edades_no_perecidos)


print("\n///////////////////////////////////////////////////////////////\n")