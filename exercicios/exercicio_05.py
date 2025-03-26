# Calcular a média final dadas as notas das 3 provas e produzir uma saída com a média e a situação
# do aluno de acordo com o seguinte critério: média >= 7, aprovado; média >=3 e média < 7,
# recuperação; média < 3, reprovado. Considerar também o número de faltas do aluno: se forem
# mais que sete faltas, o aluno estará automaticamente reprovado (o usuário deve fornecer o
# numero de faltas). Se o aluno se encontrar em recuperação, solicitar a nota da quarta prova e,
# após calcular a media final, informar se o aluno passou (media final >=5) ou não.

nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))
faltas = int(input("Digite a quantidade de faltas do aluno: "))

media = (nota1 + nota2 + nota3) / 3

if faltas > 7:
    print("Aluno reprovado por excesso de faltas.")

elif media >= 7:
    print("Aluno aprovado.")

elif media >3 and media < 7:
    print("Aluno de recuperação.")
    nota4 = float(input("Digite a nota da prova de recuperação: "))
    media_final = (media + nota4) / 2
    
    if media_final >= 5:
        print("Aluno aprovado na recuperação.")
    else:
        print("Aluno reprovado na recuperação.")

else:
    print("Aluno reprovado.")
    