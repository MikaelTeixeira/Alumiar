import pandas as pd

# Caminho do CSV convertido do .tab
csv_file = r"C:\Users\mikae\Downloads\dataset-asteroides\earthapp_converted.csv"

with open(csv_file, 'r', encoding='latin-1') as f:
    for _ in range(10):
        print(f.readline())


# # Ler CSV
# df = pd.read_csv(csv_file)

# # Conferir as colunas disponíveis
# print("Colunas disponíveis:\n", df.columns)

# # ---------------------------------------------------
# # Ajustar o nome da coluna de distância mínima
# # (use o que aparecer no print acima)
# # ---------------------------------------------------
# col_dist = 'Min. (AU)'   # ajuste se o nome for diferente

# df[col_dist] = pd.to_numeric(df[col_dist], errors='coerce')

# df_clean = df.dropna(subset=[col_dist])


# top5 = df_clean.sort_values(by=col_dist, ascending=True).head(5)


# print("\nCinco asteroides mais próximos da Terra:")
# print(top5[['Asteroid', 'Nominal Date', col_dist, 'Vrel (km/s)']])
