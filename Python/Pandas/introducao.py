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

# .head() serve para exibir apenas as 5 primeiras linhas do DataFrame
print(new_df.head())

# Selecionar Coluna
print(new_df['produto'])

# Selecionar várias colunas
print(new_df[['produto', 'valor']])

# Selecionar linha pelo índice
print(new_df.loc[0]) # Primeira linha