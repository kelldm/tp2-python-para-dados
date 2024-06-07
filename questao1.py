def contar_nomes(lista_de_nomes): 
    contagem = {}
    for nome in lista_de_nomes:
        if nome in contagem:
            contagem[nome] += 1
        else:
            contagem[nome] = 1
    
    contagem_filtrada = {nome: qtd for nome, qtd in contagem.items() if qtd > 1}
    
    return contagem_filtrada

lista_de_nomes = ["Alice", "Bob", "Alice", "Carol", "Bob", "David", "Eve"]
resultado = contar_nomes(lista_de_nomes)
print(resultado)
