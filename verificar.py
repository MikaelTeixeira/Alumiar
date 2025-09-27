import pandas as pd

arquivo = r"C:\Users\mikae\Downloads\dataset-asteroides\earthapp_converted.csv"

# Ler arquivo tratando espaços como separador
df = pd.read_csv(
    arquivo,
    sep=r"\s+",
    skiprows=6,
    engine='python',
    on_bad_lines='skip'
)

# Criar coluna de nome completo do asteroide
df['Asteroid'] = df.iloc[:,0].astype(str) + " " + df.iloc[:,1].astype(str)

# Dar nomes úteis às principais colunas (ajuste os índices conforme seu print exato)
df = df.rename(columns={
    df.columns[2]: 'Date',
    df.columns[3]: 'Time',
    df.columns[4]: 'Uncertainty',
    df.columns[5]: 'LD',          # distância em unidades lunares
    df.columns[6]: 'AU',          # distância em unidades astronômicas
    df.columns[7]: 'MinAU',       # mínima distância AU
    df.columns[8]: 'Vrel',        # velocidade relativa (km/s)
    df.columns[12]: 'H'           # magnitude absoluta
})

# Converter para numérico as colunas que interessam
for col in ['LD','AU','MinAU','Vrel','H']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Remover linhas sem distância ou magnitude
df = df.dropna(subset=['AU','H'])

# Top 5 mais próximos
mais_proximos = df.sort_values(by='AU').head(5)

# Top 5 maiores (menor H = maior tamanho)
maiores = df.sort_values(by='H').head(5)

print("\n=== 5 ASTEROIDES MAIS PRÓXIMOS DA TERRA ===")
for _, row in mais_proximos.iterrows():
    print(f"Nome: {row['Asteroid']}")
    print(f"  Data: {row['Date']} {row['Time']}")
    print(f"  Distância (AU): {row['AU']}")
    print(f"  Distância (LD): {row['LD']}")
    print(f"  Velocidade relativa (km/s): {row['Vrel']}")
    print(f"  Magnitude H: {row['H']}")
    print("-"*50)

print("\n=== 5 MAIORES ASTEROIDES (por H) ===")
for _, row in maiores.iterrows():
    print(f"Nome: {row['Asteroid']}")
    print(f"  Data: {row['Date']} {row['Time']}")
    print(f"  Distância (AU): {row['AU']}")
    print(f"  Distância (LD): {row['LD']}")
    print(f"  Velocidade relativa (km/s): {row['Vrel']}")
    print(f"  Magnitude H: {row['H']}")
    print("-"*50)
