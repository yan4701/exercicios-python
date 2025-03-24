# Que gere o preço de um carro ao consumidor e os valores pagos pelo imposto e pelo lucro do
# distribuidor, sabendo o custo de fábrica do carro e que são pagos: a) de imposto: 45% sobre o
# custo do carro; b) de lucro do distribuidor: 12% sobre o custo do carro.

# Solicita ao usuário que informe o custo de fábrica do veículo
custo_de_fabrica = float(input("Digite o valor do custo de fábrica do veículo: R$ "))

# Calcula o valor do imposto (45% sobre o custo de fábrica)
imposto = custo_de_fabrica * 0.45

# Calcula o lucro do distribuidor (12% sobre o custo de fábrica)
lucro_distribuidor = custo_de_fabrica * 0.12

# Calcula o valor final ao consumidor (soma do custo de fábrica, imposto e lucro do distribuidor)
valor_final = custo_de_fabrica + imposto + lucro_distribuidor

# Exibe um resumo dos custos e o valor final do veículo
print("\nResumo dos custos:")
print(f"- Custo de fábrica: R$ {custo_de_fabrica:.2f}")
print(f"- Valor do imposto: {imposto:.2f} ")
print(f"- Lucro do distribuidor: {lucro_distribuidor:.2f}")
print(f"- Valor final ao consumidor: R$ {valor_final:.2f}")