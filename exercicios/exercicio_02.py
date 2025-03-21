#Calcular a quantidade dinheiro gasto por um fumante. Dados: o número de anos que ele fuma, 
#o nº de cigarros fumados por dia e o preço de uma carteira com 20 cigarros.

anos = float(input("Digite a quantidade de anos que você fuma: "))
quant = int(input("Digite a quantidade de cigarros que você fuma por dia: "))
preco_maco = float(input("Digite o preço do maço de cigarro: "))

preco_unidade = preco_maco / 20
gasto_dia = preco_unidade * quant
gasto_total = gasto_dia * (anos * 365)

print(f"O valor total gasto durante o período de {anos} anos, foi de: R$ {gasto_total:.2f}")