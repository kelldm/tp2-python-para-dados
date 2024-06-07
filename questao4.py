import pandas as pd



file_path = "C:\\Users\\raquel.mata\\Desktop\\tp2 dacio\\bcdata.sgs.20716.csv"
df = pd.read_csv(file_path)
pd.DataFrame(df)

print("Número de linhas e colunas:", df.shape)
print("Tipos de dados:", df.dtypes)
print("Primeiras 5 linhas:\n", df.head())

print("Valores ausentes por coluna:\n", df.isnull().sum())

df = df.drop_duplicates()

df = df.fillna(method='ffill') 

output_file_path = "C:\\Users\\raquel.mata\\Desktop\\tp2 dacio\\bcdata.sgs.20716.modified.csv"
df.to_csv(output_file_path, index=False)


print("Arquivo modificado salvo em:", output_file_path)