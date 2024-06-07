def filmes_comuns(grupo1, grupo2):
    set_grupo1 = set(grupo1)
    set_grupo2 = set(grupo2)
    
    intersecao = set_grupo1.intersection(set_grupo2)
    
    lista_intersecao = list(intersecao)
    
    return lista_intersecao

grupo1 = ["Filme A", "Filme B", "Filme C", "Filme A"]
grupo2 = ["Filme D", "Filme B", "Filme E", "Filme B"]

sugestoes = filmes_comuns(grupo1, grupo2)
print("Sugestões de filmes comuns:", sugestoes)
