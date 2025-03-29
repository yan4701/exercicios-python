# Para ler 3 números reais e verificar se o primeiro é maior que a soma dos outros dois.

# Para ler 3 números reais e verificar se o primeiro é maior que a soma dos outros dois.

def verifica_soma(n1, n2, n3):
    soma = n2 + n3
    print(f"A soma do segundo e terceiro número é: {soma:.2f}")  
    
    if n1 > soma:
        print(f"{n1:.2f} é maior que {soma:.2f}.")
    else:
        print(f"{n1:.2f} não é maior que {soma:.2f}.")

# Entrada dos números pelo usuário
n1 = float(input("Digite o primeiro número real: "))
n2 = float(input("Digite o segundo número real: "))
n3 = float(input("Digite o terceiro número real: "))

# Chamada da função 
verifica_soma(n1, n2, n3)

        