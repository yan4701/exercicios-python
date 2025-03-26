# Calcular a média final dadas as notas das 3 provas e produzir uma saída com a média e a situação
# do aluno de acordo com o seguinte critério: média >= 7, aprovado; média >=3 e média < 7,
# recuperação; média < 3, reprovado. Considerar também o número de faltas do aluno: se forem
# mais que sete faltas, o aluno estará automaticamente reprovado (o usuário deve fornecer o
# numero de faltas). Se o aluno se encontrar em recuperação, solicitar a nota da quarta prova e,
# após calcular a media final, informar se o aluno passou (media final >=5) ou não.

# solicita as notas e faltas do aluno
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))
faltas = int(input("Digite a quantidade de faltas do aluno: "))

# calculo da media do aluno
media = (nota1 + nota2 + nota3) / 3

# verifica se o aluno excedeu o limite de faltas
if faltas > 7:
    print("Aluno reprovado por excesso de faltas.")

# se a media for maior que 7, aluno aprovado
elif media >= 7:
    print("Aluno aprovado.")
    
# verifica se o alino está em recuperação
elif media >3 and media < 7:
    print("Aluno de recuperação.")
    # solicita a nota de recuperação
    nota4 = float(input("Digite a nota da prova de recuperação: "))
    # calculo da media final após a prova de recuperação (nota anterior + nota da recuperação divido por 2)
    media_final = (media + nota4) / 2
    
    # verifica se o aluno passou após recuperação
    if media_final >= 5:
        print("Aluno aprovado na recuperação.")
    else:
        print("Aluno reprovado na recuperação.")

# se a média for menos que 3, aluno reprovado
else:
    print("Aluno reprovado.")
    