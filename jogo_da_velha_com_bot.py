import random

# Inicializa o tabuleiro
tabuleiro = [
['   ', '   ', '   '],
['   ', '   ', '   '],
['   ', '   ', '   ']
]

def exibe_tabuleiro(tabuleiro):
    # Função que exibe o tabuleiro no console
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-'*11)

def movimento_humano(tabuleiro):
    # Função para capturar o movimento do jogador humano
    while True:
        try:
            linha = int(input('Escolha a linha (0, 1, 2): '))
            coluna = int(input('Escolha a coluna (0, 1, 2): '))
            if tabuleiro[linha][coluna] == '   ':
                return linha, coluna
            else:
                print('Esta casa está ocupada, tente outra!')
        except (ValueError, IndexError):
            print('Entrada inválida! Utilize apenas números entre 0 e 2.')

def verifica_vitoria(tabuleiro, jogador):
    # Verifica se o jogador atual venceu o jogo
    for linha in tabuleiro:
        if all(casa == jogador for casa in linha):
            return True
    for col in range(3):
        if all(tabuleiro[linha][col] == jogador for linha in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True
    return False

def verifica_empate(tabuleiro):
    # Verifica se todas as casas do tabuleiro estão preenchidas e ninguém venceu
    return all(tabuleiro[linha][col] != '   ' for linha in range(3) for col in range(3))

def movimento_bot_aleatorio(tabuleiro):
    # Função para o bot escolher um movimento aleatório
    movimentos_possiveis = [(linha, coluna) for linha in range(3) for coluna in range(3) if tabuleiro[linha][coluna] == '   ']
    return random.choice(movimentos_possiveis)

def movimento_bot_defensivo(tabuleiro):
    # Função para o bot impedir a vitória do jogador humano
    # Primeira prioridade: impedir vitória do humano
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == '   ':
                tabuleiro[linha][coluna] = ' X '  # Simula movimento humano
                if verifica_vitoria(tabuleiro, ' X '):
                    tabuleiro[linha][coluna] = '   '  # Reverte o movimento simulado
                    return linha, coluna  # Faz o movimento para bloquear
                tabuleiro[linha][coluna] = '   '  # Reverte o movimento simulado

    # Caso não haja movimento defensivo, faz um movimento aleatório
    return movimento_bot_aleatorio(tabuleiro)

# Jogador 1 é humano (X), jogador 2 é o bot (O)
player = ' X '

while True:
    print(f'Turno do Jogador {player}')

    exibe_tabuleiro(tabuleiro)

    if player == ' X ':
        x, y = movimento_humano(tabuleiro)
    else:
        # Alterna entre bot aleatório e bot defensivo para testes
        if random.random() < 0.5:
            x, y = movimento_bot_aleatorio(tabuleiro)
        else:
            x, y = movimento_bot_defensivo(tabuleiro)
        print(f'Bot jogou na posição ({x}, {y})')

    tabuleiro[x][y] = player

    if verifica_vitoria(tabuleiro, player):
        exibe_tabuleiro(tabuleiro)
        print(f'Jogador {player} venceu!')
        break

    if verifica_empate(tabuleiro):
        exibe_tabuleiro(tabuleiro)
        print('Empate!')
        break

    player = ' O ' if player == ' X ' else ' X '
