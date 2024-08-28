#  Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []
#  Crie um loop para solicita os itens ao usuário:
for i in range(3):
#  Solicite o item e armazena na variável "item":
#  Adicione o item à lista "itens":
    itens.append(input())

# Exibe a lista de itens
print("Lista de Equipamentos:")
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")