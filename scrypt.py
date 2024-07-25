# Função que define os parâmetros
def teste(c):
    while True:
        if c == 1:
            t = float(input("Teste1 = "))
        elif c == 2:
            t = float(input("Teste2 = "))
        elif c == 3:
            t = float(input("Teste3 = "))
        else:
            continue

        if t < 0 or t > 20:
            print("Valor inválido. Digite novamente.")
        else:
            break
    return round(t, 2)

# Função que mostra o aproveitamento
def aproveitamento(media):
    if media >= 10:
        return "Aprovado"
    else:
        return "Reprovado"

# Função de transformação do nome
def nom():
    n1 = input('Nome: ')
    n1 = n1.strip(',.@#!`~/?\'\":;<>][}{\\=+-()*&^%$|1234567890')
    n1 = n1.strip()
    n1 = n1.title()
    return n1

# Função de criação de tabela
def imprimir_tabela(nomes_ordenados, t1s_ordenadas, t2s_ordenadas, t3s_ordenadas, medias_ordenadas, status_ordenados):
    print("\n| {:<50}| {:<10}| {:<10}| {:<10}| {:<12}| {:<16}|".format("Nome", "Teste 1", "Teste 2", "Teste 3", "Média", "Status"))
    for nome, teste1, teste2, teste3, media, status in zip(nomes_ordenados, t1s_ordenadas, t2s_ordenadas, t3s_ordenadas, medias_ordenadas, status_ordenados):
        print("| {:<50}| {:<10}| {:<10}| {:<10}| {:<12}| {:<16}|".format(nome, teste1, teste2, teste3, media, status))

# Função de ordenação
def fsort(nomes, t1s, t2s, t3s, medias, status_rap):
    nomes_ordenados = sorted(nomes)
    posicao_nomes = [nomes.index(nome) for nome in nomes_ordenados]
    
    t1s_ordenadas = [t1s[pos] for pos in posicao_nomes]
    t2s_ordenadas = [t2s[pos] for pos in posicao_nomes]
    t3s_ordenadas = [t3s[pos] for pos in posicao_nomes]
    medias_ordenadas = [medias[pos] for pos in posicao_nomes]
    status_ordenados = [status_rap[pos] for pos in posicao_nomes]
    
    imprimir_tabela(nomes_ordenados, t1s_ordenadas, t2s_ordenadas, t3s_ordenadas, medias_ordenadas, status_ordenados)

# Função principal
def principal():
    # Função que calcula a média
    def media(t1, t2, t3):
        from math import ceil, floor
        nota = [t1, t2, t3]
        media = sum(nota) / len(nota)
        decimal = media - round(media)
        if decimal >= 0.5:
            return ceil(media)
        else:
            return floor(media)
    
    # Criação de listas vazias:
    nomes = []
    testes1 = []
    testes2 = []
    testes3 = []
    medias = []
    status_rap = []
    
    # Mensagem de aviso
    print('=' * 70)
    print('‖{:<11} Para encerrar a inserção digite [fim] {:>19}'.format(' ', '‖'))
    print('‖{:<7} ⚠️ Atenção, essa ação encerrará antes do mínimo estimado! {:>4}'.format(' ', '‖'))
    print('=' * 70)
    
    # Iniciando o while:
    while True:
        n1 = nom()
        if n1.lower() == 'fim': break
        if n1 in nomes:
            print('Nome já existente. Por favor, insira outro nome.')
            continue

        t1 = teste(1)
        t2 = teste(2)
        t3 = teste(3)
        med = media(t1, t2, t3)
        status = aproveitamento(med)
        
        nomes.append(n1)
        testes1.append(t1)
        testes2.append(t2)
        testes3.append(t3)
        medias.append(med)
        status_rap.append(status)
        
        print()
        if len(nomes) >= 2:
            print('=' * 70)
            print("‖\t▮ Quantidade mínima de inserções atingida!")
            print("‖\t▮ Tens um total de 20 estudantes na tabela!")
            escolha = input('‖\t◧ Deseja colocar mais estudantes? [sim/nao]: ')
            if escolha.lower() == 'nao':
                break
            elif escolha.lower() == 'sim':
                print('=' * 70)
                print('‖{:<7}◧ Para encerrar a inserção digite: [fim] {:>20}'.format(' ', '‖'))
                print('=' * 70)
    
    # Chamada da função que faz a exibição da tabela
    fsort(nomes, testes1, testes2, testes3, medias, status_rap)

# Executando a função principal
principal()
