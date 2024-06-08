import pandas as pd

df_january = pd.read_excel('vendas_janeiro.xlsx')
df_february = pd.read_excel('vendas_fevereiro.xlsx')

combined_df = pd.concat([df_january, df_february])

total_vendas = combined_df.groupby('Produto')['Vendas'].sum().reset_index()

total_vendas.to_excel('total_vendas.xlsx', index=False)
