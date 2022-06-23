mochila = {}

def valor_total(items, peso_maximo):
    return sum([x[2] for x in items]) if sum([x[1] for x in items]) <= peso_maximo else 0

def problema_mochila(lista_itens, peso_Max_Mochila):
    if not lista_itens:
        return ()
    if (lista_itens, peso_Max_Mochila) not in mochila:

        head = lista_itens[0]
        tail = lista_itens[1:]
        adiciona = (head,) + problema_mochila(tail, peso_Max_Mochila - head[1])
        nao_adiciona = problema_mochila(tail, peso_Max_Mochila)

        if valor_total(adiciona, peso_Max_Mochila) > valor_total(nao_adiciona, peso_Max_Mochila):
              resposta = adiciona
        else: resposta = nao_adiciona

        mochila[(lista_itens, peso_Max_Mochila)] = resposta
    return mochila[(lista_itens, peso_Max_Mochila)]

if __name__ == '__main__':

    peso_max_mochila = 15

    # itens = (lista_itens, peso (kg), valor(R$))
    itens = (
        ("caixa de caneta", 1, 35), ("caderno", 2, 20),
        ("caixa de lápis", 1, 40), ("rádio", 5, 160),
        ("nobreak", 10, 200), ("notebook", 5, 300),
        ("relogio", 2, 40), ("ferramenta", 12, 30),
        ("livro", 4, 50), ("agenda", 6, 25)
    )

    solucao = problema_mochila(itens, peso_max_mochila)

    print("Items na Mochila:\n")

    for item in solucao:
        print(item[0])

    print("\nValor: R$", valor_total(solucao, peso_max_mochila))
    print("Peso:", sum([x[1] for x in solucao]), 'KG')