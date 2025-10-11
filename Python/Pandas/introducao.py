import pandas as pd

# Criando um DataFrame manualmente
dados = [
    {"produto": 'Pizza', "valor": 30, "vendas": 300},
    {"produto": 'Cerveja', "valor": 10, "vendas": 320},
    {"produto": 'Brownie', "valor": 8, "vendas": 250},
]

df = pd.DataFrame(dados)

# Salvando o DataFrame em excel
df.to_excel("dataframe_pandas.xlsx", index=False)

# Lendo o arquivo excel
new_df = pd.read_excel("dataframe_pandas.xlsx")
print(new_df.head())