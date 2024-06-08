import pandas as pd

data = {
    'titulo': ['Inception', 'Toy Story', 'The Matrix', 'Interstellar'],
    'genero': ['Acao', 'Animacao', 'Ficcao Cientifica', 'Aventura'],
    'ano_de_lancamento': [2010, 1995, 1999, 2014]
}
df = pd.DataFrame(data)

df.to_json('filmes.json', orient='records', lines=True)

df_json = pd.read_json('filmes.json', orient='records', lines=True)

duracoes = [148, 81, 136, 169] 
df_json['duracao'] = duracoes

df_json.to_json('filmes_com_duracao.json', orient='records', lines=True)

print(df_json)
