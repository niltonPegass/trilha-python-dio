carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

# saber qual o índice do elemento
# dentro de uma lista
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")