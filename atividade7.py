import random

jogadores = ["Jogador 1", "Jogador 2", "Jogador 3", "Jogador 4"]
resultados = {}

for jogador in jogadores:
    resultado = random.randint(1, 6)
    resultados[jogador] = resultado

print("Resultados do jogo:")

for jogador, resultado in resultados.items():
    print(f"{jogador}: {resultado}")
