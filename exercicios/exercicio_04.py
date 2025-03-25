# Ler dois números inteiros, x e y, e imprimir o quociente e o resto da divisão inteira entre eles,
# colocar o processamento em uma função.

def divisao_inteira (x, y): # funcão de querece dois números inteiros e retorna o quociente e o resto da divisão
    if y == 0:
        print("Erro: Divisão por zero não é permitida.")
        return
    quociente = x // y 
    resto = x % y 
    
    print(f"Quocitente: {quociente}")
    print(f"Resto: {resto}")

# entrada dos números pelo usuário
x = int(input("Digite o primeiro número inteiro (dividendo): "))
y = int(input("Digite o segundo número inteiro (divisor): "))

#chamada da função 
resultado = divisao_inteira(x, y)


