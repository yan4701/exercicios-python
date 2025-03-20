"1) Construa um programa para ler uma variável numérica N e imprimi-la somente se esta for maior que 100, caso contrário imprimi-la com o valor zero."

num = int(input("Entre com um número inteiro para conferir se este é maior que 100:"))

if num > 100:
    print(f"{num}")

else:
    print("0")