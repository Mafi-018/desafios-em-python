notas = {}
continuar = True

while continuar:
    nota = float(input("Digite a nota: "))
    notas[len(notas) + 1] = nota

    opcao = input("Deseja adicionar mais notas? (S/N): ")
    if opcao.upper() == "N":
        continuar = False

media = sum(notas.values()) / len(notas)

print("Notas inseridas:")
for chave, valor in notas.items():
    print(f"Nota {chave}: {valor}")

print(f"Média das notas: {media}")
