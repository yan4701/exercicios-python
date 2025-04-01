#  Leia a velocidade máxima permitida em uma avenida e a velocidade com que o motorista estava
# dirigindo nela e calcule a multa que uma pessoa vai receber, sabendo que são pagos: a) 50 reais
# se o motorista estiver ultrapassar em até 10km/h a velocidade permitida (ex.: velocidade
# máxima: 50km/h; motorista a 60km/h ou a 56km/h); b) 100 reais, se o motorista ultrapassar de
# 11 a 30 km/h a velocidade permitida. c) 200 reais, se estiver acima de 31km/h da velocidade permitida.

# Programa para calcular multa com base no excesso de velocidade

# Entrada de dados
velocidade_maxima = int(input("Digite a velocidade máxima permitida na avenida (km/h): "))
velocidade_motorista = int(input("Digite a velocidade que o motorista estava dirigindo (km/h): "))

# Cálculo da diferença de velocidade
excesso = velocidade_motorista - velocidade_maxima

# Verificação das multas
if excesso <= 0:
    print("Motorista dentro do limite. Nenhuma multa aplicada.")
elif excesso <= 10:
    print("Multa de R$ 50,00 por excesso de até 10 km/h.")
elif excesso <= 30:
    print("Multa de R$ 100,00 por excesso entre 11 e 30 km/h.")
else:
    print("Multa de R$ 200,00 por excesso acima de 31 km/h.")
